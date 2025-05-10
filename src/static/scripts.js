// Mode toggling with server sync
const modes = ['Line Follower', 'Autonomous Vehicle', 'Manual'];
let currentModeIndex = 2;
const currentModeSpan = document.getElementById('current-mode');
const modeToggleHeader = document.getElementById('mode-toggle');

function sendModeToServer(mode) {
  fetch('/set-mode', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ mode })
  }).then(response => {
    if (!response.ok) {
      console.error('Failed to set mode:', mode);
    } else {
      console.log('Mode sent to server:', mode);
    }
  }).catch(err => console.error('Error sending mode:', err));
}

modeToggleHeader.addEventListener('click', () => {
  currentModeIndex = (currentModeIndex + 1) % modes.length;
  const newMode = modes[currentModeIndex];
  currentModeSpan.textContent = newMode;
  sendModeToServer(newMode);
});

// Joystick setup
const joystick = nipplejs.create({
  zone: document.getElementById('joystick-container'),
  mode: 'static',
  position: { left: '50%', top: '50%' },
  color: 'white',
  size: 150,
  multitouch: true,
  restJoystick: true,
});

const endpointMap = {
  forward: '/forward',
  backward: '/backward',
  left: '/left',
  right: '/right',
  'top-left': '/top-left',
  'top-right': '/top-right',
  'bottom-left': '/bottom-left',
  'bottom-right': '/bottom-right',
  stop: '/stop'
};

let lastSent = null;

function sendJoystickDirection(direction) {
  if (!direction || direction === lastSent) return;
  lastSent = direction;

  const endpoint = endpointMap[direction];
  if (!endpoint) return;

  fetch(endpoint, {
    method: 'POST',
  }).then(response => {
    if (!response.ok) {
      console.error(`Failed to send direction: ${direction}`);
    } else {
      console.log(`Sent: ${direction}`);
    }
  }).catch(console.error);
}

function resetLastDirection() {
  lastSent = null;
}

joystick.on('move', (evt, data) => {
  if (!data || !data.angle) return;
  const angle = data.angle.degree;
  let direction = null;

  if (angle >= 337.5 || angle < 22.5) direction = 'right'; 
  else if (angle < 67.5) direction = 'top-right';
  else if (angle < 112.5) direction = 'forward'; 
  else if (angle < 157.5) direction = 'top-left';
  else if (angle < 202.5) direction = 'left';
  else if (angle < 247.5) direction = 'bottom-left'; 
  else if (angle < 292.5) direction = 'backward';
  else direction = 'bottom-right';

  sendJoystickDirection(direction);
});

joystick.on('end', () => {
  fetch('/stop', { method: 'POST' });
  resetLastDirection();
});

// Buttons
function handleTurnButton(btnSelector, directionEndpoint) {
  const button = document.querySelector(btnSelector);

  button.addEventListener('mousedown', () => {
    fetch(directionEndpoint, { method: 'POST' });
  });

  button.addEventListener('mouseup', () => {
    fetch('/stop', { method: 'POST' });
  });

  button.addEventListener('touchstart', () => {
    fetch(directionEndpoint, { method: 'POST' });
  });

  button.addEventListener('touchend', () => {
    fetch('/stop', { method: 'POST' });
  });
}

// Apply to turn buttons
handleTurnButton('.turn-left', '/turn-left');
handleTurnButton('.turn-right', '/turn-right');

document.querySelector('.shutdown').addEventListener('click', () => {
  if (confirm("Are you sure you want to shut down the electronic components of the robot?")) {
    fetch('/shutdown', {
      method: 'POST'
    }).then(response => {
      if (response.ok) {
        console.log('Shutdown request sent.');
      } else {
        console.error('Shutdown failed.');
      }
    }).catch(console.error);
  }
});

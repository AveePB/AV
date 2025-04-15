class VirtualJoystick {
    constructor() {
        this.joystick = document.getElementById('joystick');
        this.container = document.getElementById('joystick-container');
        this.statusElement = document.getElementById('status');
        this.turnLeftBtn = document.getElementById('turnLeft');
        this.turnRightBtn = document.getElementById('turnRight');
        
        this.isDragging = false;
        this.touchId = null;
        this.activeTurnButton = null;
        this.lastDirection = null;
        this.apiBaseUrl = window.location.origin; // Use current server as API base
        
        this.containerRect = null;
        this.containerRadius = 0;
        this.thumbRadius = 0;
        this.maxDistance = 0;
        this.centerX = 0;
        this.centerY = 0;
        
        this.init();
    }

    init() {
        this.calculateDimensions();
        this.setupEventListeners();
        this.updateStatus('Ready');
    }

    calculateDimensions() {
        this.containerRect = this.container.getBoundingClientRect();
        this.thumbRadius = this.joystick.offsetWidth / 2;
        this.containerRadius = this.containerRect.width / 2;
        this.maxDistance = this.containerRadius - this.thumbRadius;
        this.centerX = this.containerRect.left + this.containerRadius;
        this.centerY = this.containerRect.top + this.containerRadius;
    }

    setupEventListeners() {
        // Mouse events
        this.joystick.addEventListener('mousedown', (e) => {
            this.startDrag(e);
            e.preventDefault();
        });

        document.addEventListener('mousemove', (e) => {
            this.drag(e);
        });

        document.addEventListener('mouseup', () => {
            this.endDrag();
        });

        // Touch events
        this.joystick.addEventListener('touchstart', (e) => {
            if (!this.touchId && e.changedTouches.length > 0) {
                this.touchId = e.changedTouches[0].identifier;
                this.startDrag(e.changedTouches[0]);
                e.preventDefault();
            }
        }, { passive: false });

        document.addEventListener('touchmove', (e) => {
            if (this.touchId !== null) {
                for (let touch of e.changedTouches) {
                    if (touch.identifier === this.touchId) {
                        this.drag(touch);
                        e.preventDefault();
                        break;
                    }
                }
            }
        }, { passive: false });

        document.addEventListener('touchend', (e) => {
            for (let touch of e.changedTouches) {
                if (touch.identifier === this.touchId) {
                    this.touchId = null;
                    this.endDrag();
                    e.preventDefault();
                    break;
                }
            }
        }, { passive: false });

        document.addEventListener('touchcancel', (e) => {
            if (this.touchId !== null) {
                this.touchId = null;
                this.endDrag();
                e.preventDefault();
            }
        }, { passive: false });

        // Turn buttons
        const handleTurnStart = (direction, e) => {
            this.activeTurnButton = direction;
            this.sendCommand(`/turn-${direction.toLowerCase()}`, 'POST');
            e.preventDefault();
        };

        const handleTurnEnd = (e) => {
            if (this.activeTurnButton) {
                this.sendCommand('/stop', 'POST');
                this.activeTurnButton = null;
            }
        };

        this.turnLeftBtn.addEventListener('mousedown', (e) => handleTurnStart('left', e));
        this.turnLeftBtn.addEventListener('touchstart', (e) => handleTurnStart('left', e));
        
        this.turnRightBtn.addEventListener('mousedown', (e) => handleTurnStart('right', e));
        this.turnRightBtn.addEventListener('touchstart', (e) => handleTurnStart('right', e));
        
        document.addEventListener('mouseup', handleTurnEnd);
        document.addEventListener('touchend', handleTurnEnd);

        // Window resize
        window.addEventListener('resize', () => {
            this.calculateDimensions();
        });
    }

    async sendCommand(endpoint, method = 'POST') {
        try {
            const response = await fetch(`${this.apiBaseUrl}${endpoint}`, {
                method: method,
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            this.updateStatus(`Command sent: ${endpoint}`);
        } catch (error) {
            console.error('Error sending command:', error);
            this.updateStatus(`Error: ${error.message}`);
        }
    }

    updateStatus(message) {
        this.statusElement.textContent = `Status: ${message}`;
    }

    startDrag(e) {
        this.isDragging = true;
        this.joystick.style.transition = 'none';
        this.joystick.classList.add('active');
        this.calculateDimensions();
        this.drag(e);
    }

    drag(e) {
        if (!this.isDragging) return;

        const clientX = e.clientX ?? e.touches?.[0]?.clientX ?? e.changedTouches?.[0]?.clientX;
        const clientY = e.clientY ?? e.touches?.[0]?.clientY ?? e.changedTouches?.[0]?.clientY;
        
        if (clientX === undefined || clientY === undefined) return;

        let x = clientX - this.centerX;
        let y = clientY - this.centerY;
        
        const distance = Math.sqrt(x * x + y * y);
        const angle = Math.atan2(y, x) * (180 / Math.PI); // Convert to degrees
        
        if (distance > this.maxDistance) {
            const ratio = this.maxDistance / distance;
            x *= ratio;
            y *= ratio;
            this.joystick.classList.add('at-boundary');
        } else {
            this.joystick.classList.remove('at-boundary');
        }
        
        this.joystick.style.transform = `translate(${x}px, ${y}px)`;
        
        // Determine direction based on angle and distance
        const normalizedDistance = distance / this.maxDistance;
        let direction = this.getDirection(angle, normalizedDistance);
        
        if (direction !== this.lastDirection) {
            this.lastDirection = direction;
            this.sendCommand(`/${direction}`, 'POST');
        }
    }

    getDirection(angle, distance) {
        if (distance < 0.3) return 'stop';
        
        // Convert angle to positive value (0-360)
        angle = (angle + 360) % 360;
        
        if (angle >= 337.5 || angle < 22.5) return 'right';
        if (angle >= 22.5 && angle < 67.5) return 'bottom-right';
        if (angle >= 67.5 && angle < 112.5) return 'backward';
        if (angle >= 112.5 && angle < 157.5) return 'bottom-left';
        if (angle >= 157.5 && angle < 202.5) return 'left';
        if (angle >= 202.5 && angle < 247.5) return 'top-left';
        if (angle >= 247.5 && angle < 292.5) return 'forward';
        if (angle >= 292.5 && angle < 337.5) return 'top-right';
        
        return 'stop';
    }

    endDrag() {
        if (!this.isDragging) return;
        
        this.isDragging = false;
        this.touchId = null;
        this.joystick.style.transition = 'transform 0.3s ease-out';
        this.joystick.style.transform = 'translate(-50%, -50%)';
        this.joystick.classList.remove('active', 'at-boundary');
        
        if (this.lastDirection !== 'stop') {
            this.lastDirection = 'stop';
            this.sendCommand('/stop', 'POST');
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new VirtualJoystick();
});
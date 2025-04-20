class VirtualJoystick {
    constructor() {
        // UI Elements
        this.joystick = document.getElementById('joystick');
        this.container = document.getElementById('joystick-container');
        this.statusElement = document.getElementById('status');
        this.turnLeftBtn = document.getElementById('turnLeft');
        this.turnRightBtn = document.getElementById('turnRight');
        this.modeToggle = document.getElementById('modeToggle');
        this.videoStream = document.getElementById('videoStream');
        
        // State variables
        this.isDragging = false;
        this.touchId = null;
        this.activeTurnButton = null;
        this.lastDirection = null;
        this.currentMode = 'manual';
        this.apiBaseUrl = window.location.origin;
        
        // Geometry properties
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
        this.updateStatus('System Ready');
        this.updateModeDisplay();
        this.setupVideoStream();
    }

    setupVideoStream() {
        // Handle video stream errors
        this.videoStream.onerror = () => {
            this.updateStatus('Video feed disconnected');
            // Attempt to reconnect every 5 seconds
            setTimeout(() => {
                this.videoStream.src = `${this.apiBaseUrl}/camera?${Date.now()}`;
            }, 5000);
        };
        
        // Refresh stream periodically to prevent freezing
        setInterval(() => {
            this.videoStream.src = `${this.apiBaseUrl}/camera?${Date.now()}`;
        }, 30000); // Refresh every 30 seconds
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
        // Mode toggle
        this.modeToggle.addEventListener('click', () => this.toggleMode());

        // Mouse events
        this.joystick.addEventListener('mousedown', (e) => {
            if (this.currentMode === 'manual') {
                this.startDrag(e);
                e.preventDefault();
            }
        });

        document.addEventListener('mousemove', (e) => {
            if (this.isDragging) this.drag(e);
        });

        document.addEventListener('mouseup', () => {
            if (this.isDragging) this.endDrag();
        });

        // Touch events
        this.joystick.addEventListener('touchstart', (e) => {
            if (this.currentMode === 'manual' && !this.touchId) {
                this.touchId = e.changedTouches[0].identifier;
                this.startDrag(e.changedTouches[0]);
                e.preventDefault();
            }
        }, { passive: false });

        document.addEventListener('touchmove', (e) => {
            if (!this.touchId) return;
            for (let touch of e.changedTouches) {
                if (touch.identifier === this.touchId) {
                    this.drag(touch);
                    e.preventDefault();
                    break;
                }
            }
        }, { passive: false });

        document.addEventListener('touchend', (e) => {
            for (let touch of e.changedTouches) {
                if (touch.identifier === this.touchId) {
                    this.endDrag();
                    this.touchId = null;
                    e.preventDefault();
                    break;
                }
            }
        }, { passive: false });

        // Turn buttons
        const handleTurnStart = (direction, e) => {
            if (this.currentMode === 'manual') {
                this.activeTurnButton = direction;
                this.sendCommand(`/turn-${direction.toLowerCase()}`);
                e.preventDefault();
            }
        };

        const handleTurnEnd = () => {
            if (this.activeTurnButton) {
                this.sendCommand('/stop');
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

    toggleMode() {
        this.currentMode = this.currentMode === 'manual' ? 'autonomous' : 'manual';
        this.updateModeDisplay();
        const endpoint = this.currentMode === 'manual' ? '/manual-mode' : '/autonomous-mode';
        this.sendCommand(endpoint);
    }

    updateModeDisplay() {
        if (this.currentMode === 'manual') {
            this.modeToggle.textContent = 'Manual Mode';
            this.modeToggle.classList.replace('autonomous', 'manual');
            this.enableControls(true);
            this.updateStatus('Manual Control Active');
        } else {
            this.modeToggle.textContent = 'Autonomous Mode';
            this.modeToggle.classList.replace('manual', 'autonomous');
            this.enableControls(false);
            this.updateStatus('Autonomous Mode Active');
            this.sendCommand('/stop');
        }
    }

    enableControls(enabled) {
        const opacity = enabled ? '1' : '0.6';
        this.joystick.style.opacity = opacity;
        this.turnLeftBtn.disabled = !enabled;
        this.turnRightBtn.disabled = !enabled;
        
        if (!enabled) {
            if (this.isDragging) this.endDrag();
            if (this.activeTurnButton) {
                this.sendCommand('/stop');
                this.activeTurnButton = null;
            }
        }
    }

    async sendCommand(endpoint) {
        try {
            const timestamp = Date.now();
            const response = await fetch(`${this.apiBaseUrl}${endpoint}?_=${timestamp}`, {
                method: 'POST',
                headers: { 'Accept': 'application/json' }
            });
            
            if (!response.ok) throw new Error(`HTTP error ${response.status}`);
            
            const responseText = await response.text();
            this.updateStatus(responseText || `Command sent: ${endpoint}`);
            
            try {
                return JSON.parse(responseText);
            } catch {
                return responseText;
            }
        } catch (error) {
            console.error('Command error:', error);
            this.updateStatus(`Error: ${error.message}`);
            throw error;
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
        if (!this.isDragging || this.currentMode !== 'manual') return;

        const clientX = e.clientX ?? e.touches?.[0]?.clientX;
        const clientY = e.clientY ?? e.touches?.[0]?.clientY;
        if (!clientX || !clientY) return;

        let x = clientX - this.centerX;
        let y = clientY - this.centerY;
        
        const distance = Math.sqrt(x * x + y * y);
        const angle = Math.atan2(y, x) * (180 / Math.PI);
        
        if (distance > this.maxDistance) {
            const ratio = this.maxDistance / distance;
            x *= ratio;
            y *= ratio;
            this.joystick.classList.add('at-boundary');
        } else {
            this.joystick.classList.remove('at-boundary');
        }
        
        this.joystick.style.transform = `translate(${x}px, ${y}px)`;
        
        const direction = this.getDirection(angle, distance / this.maxDistance);
        if (direction !== this.lastDirection) {
            this.lastDirection = direction;
            this.sendCommand(`/${direction}`);
        }
    }

    getDirection(angle, distance) {
        if (distance < 0.3) return 'stop';
        angle = (angle + 360) % 360;
        
        /*
        if (angle >= 337.5 || angle < 22.5) return 'right';
        if (angle >= 22.5 && angle < 67.5) return 'bottom-right';
        if (angle >= 67.5 && angle < 112.5) return 'backward';
        if (angle >= 112.5 && angle < 157.5) return 'bottom-left';
        if (angle >= 157.5 && angle < 202.5) return 'left';
        if (angle >= 202.5 && angle < 247.5) return 'top-left';
        if (angle >= 247.5 && angle < 292.5) return 'forward';
        if (angle >= 292.5 && angle < 337.5) return 'top-right';
        */

        const directions = [
            [337.5, 22.5, 'right'],
            [22.5, 67.5, 'bottom-right'],
            [67.5, 112.5, 'backward'],
            [112.5, 157.5, 'bottom-left'],
            [157.5, 202.5, 'left'],
            [202.5, 247.5, 'top-left'],
            [247.5, 292.5, 'forward'],
            [292.5, 337.5, 'top-right']
        ];
        
        for (const [min, max, dir] of directions) {
            if (angle >= min && angle < max) return dir;
        }
        return 'stop';
    }

    endDrag() {
        if (!this.isDragging) return;
        
        this.isDragging = false;
        this.joystick.style.transition = 'transform 0.3s ease-out';
        this.joystick.style.transform = 'translate(-50%, -50%)';
        this.joystick.classList.remove('active', 'at-boundary');
        
        if (this.lastDirection !== 'stop') {
            this.lastDirection = 'stop';
            this.sendCommand('/stop');
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new VirtualJoystick();
});
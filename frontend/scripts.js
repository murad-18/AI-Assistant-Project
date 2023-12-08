class Debugger {
    static log(message) {
        try {
            console.log(message);
        } catch (exception) {
            return;
        }
    }
}

function windowLoadHandler() {
    canvasApp();
}

function canvasSupport() {
    return Modernizr.canvas;
}

function canvasApp() {
    if (!canvasSupport()) {
        return;
    }

    const theCanvas = document.getElementById("canvasOne");
    const context = theCanvas.getContext("2d");

    let displayWidth;
    let displayHeight;

    let timer;
    let wait;

    let count;
    let numToAddEachFrame;
    let particlelist;
    let recycleBin;

    let particleAlpha;
    let r, g, b;

    let flen;

    let projCenterX;
    let projCenterY; // Fix typo
    let zMax;

    let turnAngle;
    let turnSpeed;

    let sphereCenterX, sphereCenterY, sphereCenterZ; // Fix typos
    let particleRad;

    let zeroAlphaDepth;
    let randAccelX, randAccelY, randAccelZ; // Fix typos

    let gravity;
    let rgbString; // Declare rgbString
    let p;
    let i;
    let theta, phi;

    init();

    function init() {
        wait = 1;
        count = wait - 1;
        numToAddEachFrame = 8;
        r = 0;
        g = 72;
        b = 255;
        rgbString = "rgba(" + r + "," + g + "," + b + ",";
        particleAlpha = 1;
        displayWidth = theCanvas.clientWidth;
        displayHeight = theCanvas.clientHeight;
        flen = 320;
        projCenterX = displayWidth / 2;
        projCenterY = displayHeight / 2; // Fix typo
        zMax = flen - 2;
        particlelist = {};
        recycleBin = {};
        randAccelX = 0.1;
        randAccelY = 0.1; // Fix typo
        gravity = 0;
        particleRad = 1.8;
        sphereCenterX = 0;
        sphereCenterY = 0; // Fix typo
        sphereCenterZ = -3 * particleRad; // Fix typo
        zeroAlphaDepth = -750;
        turnSpeed = (2 * Math.PI) / 1200;
        turnAngle = 0;
        timer = setInterval(update, 10);
    }

    function update() {
        onTimer();

        turnAngle = (turnAngle + turnSpeed) % (2 * Math.PI);
        let sinAngle = Math.sin(turnAngle);
        let cosAngle = Math.cos(turnAngle);

        // Background fill
        context.fillStyle = "#000000";
        context.fillRect(0, 0, displayWidth, displayHeight);

        // Update and draw particles
        let p = particlelist.first;

        while (p != null) {
            let nextParticle = p.next;
            p.age++;

            if (p.age > p.stuckTime) {
                p.velx += p.accelX + randAccelX;
                p.vely += p.accelY + randAccelY * (Math.random() * 2 - 1);
                p.velz += p.accelZ + randAccelZ * (Math.random() * 2 - 1);

                p.x += p.velx;
                p.y += p.vely;
                p.z += p.velz;
            }

            p = nextParticle;
        }

        p = particlelist.first;

        while (p != null) {
            let nextParticle = p.next;

            let rotX = cosAngle * p.x + sinAngle * (p.z - sphereCenterZ);
            let rotZ = -sinAngle * p.x + cosAngle * (p.z - sphereCenterZ);

            let m = particleRad * flen / (flen - rotZ + sphereCenterZ);

            p.projX = rotX * m + projCenterX;
            p.projY = p.y * m + projCenterY;

            if (p.age < p.attack + p.hold + p.decay) {
                if (p.age < p.attack) {
                    p.alpha = (p.holdValue - p.initValue) / p.attack * p.age + p.initValue;
                } else if (p.age < p.attack + p.hold) {
                    p.alpha = p.holdValue;
                } else if (p.age < p.attack + p.hold + p.decay) {
                    p.alpha = (p.lastValue - p.holdValue) / p.decay * (p.age - p.attack - p.hold) + p.holdValue;
                }
            } else {
                p.dead = true;
            }

            let outsideTest;

            if (p.projX > displayWidth || p.projX < 0 || p.projY < 0 || p.projY > displayHeight || rotZ > zMax) {
                outsideTest = true;
            } else {
                outsideTest = false;
            }

            if (outsideTest || p.dead) {
                recycle(p);
            } else {
                let depthAlphaFactor = 1 - rotZ / zeroAlphaDepth;
                depthAlphaFactor = depthAlphaFactor > 1 ? 1 : (depthAlphaFactor < 0 ? 0 : depthAlphaFactor);

                context.fillStyle = rgbString + depthAlphaFactor * p.alpha + ")";
                context.beginPath();
                context.arc(p.projX, p.projY, m * particleRad, 0, 2 * Math.PI, false);
                context.closePath();
                context.fill();
            }

            p = nextParticle;
        }
    }

    function onTimer() {
        count++;

        if (count >= wait) {
            count = 0;

            for (i = 0; i < numToAddEachFrame; i++) {
                theta = Math.random() * 2 * Math.PI;
                phi = Math.acos(Math.random() * 2 - 1);
                let x0 = particleRad * Math.sin(phi) * Math.cos(theta);
                let y0 = particleRad * Math.sin(phi) * Math.sin(theta);
                let z0 = particleRad * Math.cos(phi);
                p = addParticle(x0, sphereCenterY + y0, sphereCenterZ + z0, 0.002 * x0, 0.002 * y0, 0.002 * z0);
                p.attack = 50;
                p.hold = 50;
                p.decay = 100;
                p.initValue = 0;
                p.holdValue = particleAlpha;
                p.lastValue = 0;
                p.stuckTime = 90 + Math.random() * 20;
                p.accelX = 0;
                p.accelY = gravity;
            }
        }

        p.accelZ = 0;
    }

    function addParticle(x0, y0, z0, vx0, vy0, vz0) {
        let newParticle;

        if (recycleBin.first != null) {
            newParticle = recycleBin.first;

            if (newParticle.next != null) {
                recycleBin.first = newParticle.next;
                newParticle.next.prev = null;
            } else {
                recycleBin.first = null;
            }
        } else {
            newParticle = {};
        }

        if (particlelist.first == null) {
            particlelist.first = newParticle;
            newParticle.prev = null;
            newParticle.next = null;
        } else {
            newParticle.next = particlelist.first;
            particlelist.first.prev = newParticle;
            particlelist.first = newParticle;
            newParticle.prev = null;
        }

        newParticle.x = x0;
        newParticle.y = y0;
        newParticle.z = z0;
        newParticle.velx = vx0;
        newParticle.vely = vy0;
        newParticle.velz = vz0;
        newParticle.age = 0;
        newParticle.dead = false;

        return newParticle;
    }

    function recycle(p) {
        if (particlelist.first == p) {
            if (p.next != null) {
                p.next.prev = null;
                particlelist.first = p.next;
            } else {
                particlelist.first = null;
            }
        } else {
            if (p.next == null) {
                p.prev.next = null;
            } else {
                p.prev.next = p.next;
                p.next.prev = p.prev;
            }
        }

        if (recycleBin.first == null) {
            recycleBin.first = p;
            p.prev = null;
            p.next = null;
        } else {
            p.next = recycleBin.first;
            recycleBin.first.prev = p;
            recycleBin.first = p;
            p.prev = null;
        }
    }

    $(function () {
        $("#slider-range").slider({
            range: false,
            min: 20,
            max: 500,
            value: 280,
            slide: function (event, ui) {
                console.log(ui.value);
                particleRad = ui.value;
            }
        });
    });

    $(function () {
        $("#slider-test").slider({
            range: false,
            min: 1.0,
            max: 2.0,
            value: 1,
            step: 0.01,
            slide: function (event, ui) {
                radius_sp = ui.value;
            }
        });
    });
}

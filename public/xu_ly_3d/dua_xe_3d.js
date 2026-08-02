// File: dua_xe_3d.js
// Mo ta: Dong co tro choi Dua Xe Siêu Cấp 3D bang Three.js ho tro kiem tra va cham xuyen lan giua

let raceScene3D, raceCamera3D, raceRenderer3D;
let carMesh3D;
let roadGridMesh, obstacles3DGroup = [];
let isRace3DRunning = false;

let raceSpeed3D = 80;
let raceDistance3D = 0;
let raceLives3D = 3;
let carLane3D = 1; // 0: Trai, 1: Giua, 2: Phai
const laneXPositions3D = [-3.5, 0, 3.5];

function khoi_tao_dua_xe_3d() {
    const canvas = document.getElementById('canvasRacing3D');
    if (!canvas || typeof THREE === 'undefined') return;

    // Khoi tao Scene & Camera perspective 3D goc nhin phia sau xe
    raceScene3D = new THREE.Scene();
    raceScene3D.background = new THREE.Color(0x070a13);
    raceScene3D.fog = new THREE.FogExp2(0x070a13, 0.025);

    const aspect = canvas.clientWidth / canvas.clientHeight || (800 / 380);
    raceCamera3D = new THREE.PerspectiveCamera(60, aspect, 0.1, 200);
    raceCamera3D.position.set(0, 4.5, 9);
    raceCamera3D.lookAt(0, 1, -10);

    raceRenderer3D = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
    raceRenderer3D.setSize(canvas.clientWidth || 800, canvas.clientHeight || 380);
    raceRenderer3D.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    raceRenderer3D.shadowMap.enabled = true;

    // Anh sang moi truong & den pha
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
    raceScene3D.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0x06b6d4, 0.8);
    dirLight.position.set(10, 20, 10);
    raceScene3D.add(dirLight);

    // Tao Mat Duong 3D voi vach ke duong
    const roadGeo = new THREE.PlaneGeometry(12, 200);
    const roadMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
    const road = new THREE.Mesh(roadGeo, roadMat);
    road.rotation.x = -Math.PI / 2;
    road.position.z = -80;
    raceScene3D.add(road);

    // Vach phan lan 3D
    roadGridMesh = new THREE.Group();
    const stripeGeo = new THREE.BoxGeometry(0.3, 0.05, 3);
    const stripeMat = new THREE.MeshBasicMaterial({ color: 0xf59e0b });

    for (let z = 0; z > -160; z -= 8) {
        const stripe1 = new THREE.Mesh(stripeGeo, stripeMat);
        stripe1.position.set(-1.85, 0.03, z);
        const stripe2 = new THREE.Mesh(stripeGeo, stripeMat);
        stripe2.position.set(1.85, 0.03, z);
        roadGridMesh.add(stripe1);
        roadGridMesh.add(stripe2);
    }
    raceScene3D.add(roadGridMesh);

    // Tao Xe 3D (Car Mesh)
    carMesh3D = tao_mo_hinh_xe_3d();
    carMesh3D.position.set(laneXPositions3D[carLane3D], 0.6, 3);
    raceScene3D.add(carMesh3D);

    // Khoi tao cac vat can & hop qua 3D
    resetVatCan3D();

    isRace3DRunning = true;
    animateDuaXe3D();
}

function tao_mo_hinh_xe_3d() {
    const carGroup = new THREE.Group();

    // Than xe chinh
    const bodyGeo = new THREE.BoxGeometry(1.8, 0.7, 3.2);
    const bodyMat = new THREE.MeshStandardMaterial({ color: 0x06b6d4, metalness: 0.6, roughness: 0.2 });
    const body = new THREE.Mesh(bodyGeo, bodyMat);
    body.position.y = 0.35;
    carGroup.add(body);

    // Ca bin / Kinh xe
    const cabinGeo = new THREE.BoxGeometry(1.4, 0.5, 1.6);
    const cabinMat = new THREE.MeshStandardMaterial({ color: 0x020617, roughness: 0.1 });
    const cabin = new THREE.Mesh(cabinGeo, cabinMat);
    cabin.position.set(0, 0.85, -0.2);
    carGroup.add(cabin);

    // Banh xe 4 cai
    const wheelGeo = new THREE.CylinderGeometry(0.35, 0.35, 0.3, 16);
    const wheelMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.9 });
    wheelGeo.rotateZ(Math.PI / 2);

    const wheelPos = [
        [-1.0, 0.35, 1.0],
        [1.0, 0.35, 1.0],
        [-1.0, 0.35, -1.0],
        [1.0, 0.35, -1.0]
    ];

    wheelPos.forEach(pos => {
        const wheel = new THREE.Mesh(wheelGeo, wheelMat);
        wheel.position.set(pos[0], pos[1], pos[2]);
        carGroup.add(wheel);
    });

    // Den pha 3D
    const lightMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const headLeft = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.2, 0.1), lightMat);
    headLeft.position.set(-0.6, 0.4, -1.6);
    const headRight = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.2, 0.1), lightMat);
    headRight.position.set(0.6, 0.4, -1.6);
    carGroup.add(headLeft);
    carGroup.add(headRight);

    return carGroup;
}

function resetVatCan3D() {
    // Xoa vat can cu
    obstacles3DGroup.forEach(item => raceScene3D.remove(item.mesh));
    obstacles3DGroup = [];

    const blockGeo = new THREE.BoxGeometry(1.5, 1.2, 1.5);
    const blockMat = new THREE.MeshStandardMaterial({ color: 0xef4444, metalness: 0.4, roughness: 0.3 });

    const giftGeo = new THREE.BoxGeometry(1.2, 1.2, 1.2);
    const giftMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.8, roughness: 0.2 });

    for (let i = 0; i < 5; i++) {
        const isBlock = Math.random() > 0.35;
        const mesh = new THREE.Mesh(isBlock ? blockGeo : giftGeo, isBlock ? blockMat : giftMat);
        const lane = Math.floor(Math.random() * 3);
        const zPos = -30 - i * 25;

        mesh.position.set(laneXPositions3D[lane], 0.6, zPos);
        raceScene3D.add(mesh);

        obstacles3DGroup.push({
            mesh: mesh,
            lane: lane,
            type: isBlock ? 'block' : 'gift',
            z: zPos
        });
    }
}

function moveCarLane3D(lane) {
    if (typeof playClickSfx === 'function') playClickSfx();
    carLane3D = lane;
}

function boostCarSpeed3D() {
    if (typeof playClickSfx === 'function') playClickSfx();
    raceSpeed3D = Math.min(220, raceSpeed3D + 30);
}

function animateDuaXe3D() {
    if (!isRace3DRunning) return;
    requestAnimationFrame(animateDuaXe3D);
    if (!raceScene3D || !raceRenderer3D) return;

    // Di chuyen xe muot ma toi lan chon
    const targetX = laneXPositions3D[carLane3D];
    carMesh3D.position.x += (targetX - carMesh3D.position.x) * 0.2;
    carMesh3D.rotation.z = (carMesh3D.position.x - targetX) * 0.08;

    // Cuon mat duong
    const deltaZ = raceSpeed3D / 25;
    roadGridMesh.children.forEach(stripe => {
        stripe.position.z += deltaZ;
        if (stripe.position.z > 10) stripe.position.z -= 160;
    });

    // Tang quang duong & cap nhat UI
    raceDistance3D = Math.min(1000, raceDistance3D + Math.round(raceSpeed3D / 40));

    const lblSpeed = document.getElementById('lblRaceSpeed');
    const lblDist = document.getElementById('lblRaceDistance');
    const lblLives = document.getElementById('lblRaceLives');

    if (lblSpeed) lblSpeed.innerText = `Tốc độ: ${raceSpeed3D} km/h`;
    if (lblDist) lblDist.innerText = `Quãng đường: ${raceDistance3D}m / 1000m`;
    if (lblLives) lblLives.innerText = `Số mạng: ${raceLives3D} tim`;

    if (raceDistance3D >= 1000) {
        isRace3DRunning = false;
        alert("CHÚC MỪNG! Bạn đã hoàn thành 1000m Đua Xe 3D Siêu Cấp và nhận +300 XP!");
        return;
    }

    // Di chuyen vat can & kiem tra va cham (Kiem tra toa do X thuc te bao gom ca khi chuyen lan xuyen qua lan giua)
    obstacles3DGroup.forEach(obs => {
        obs.mesh.position.z += deltaZ;
        if (obs.type === 'gift') {
            obs.mesh.rotation.y += 0.04;
        }

        // Tinh khoang cach va cham thuc te theo 2 truc X va Z
        const distZ = Math.abs(obs.mesh.position.z - carMesh3D.position.z);
        const distX = Math.abs(obs.mesh.position.x - obs.mesh.position.x);

        if (distZ < 1.6 && Math.abs(obs.mesh.position.x - carMesh3D.position.x) < 1.3) {
            if (obs.type === 'block') {
                raceLives3D--;
                raceSpeed3D = Math.max(40, raceSpeed3D - 40);
                obs.mesh.position.z = 100; // Day ra xa khi da va cham
                alert("VA CHẠM VẬT CẢN! Xe chuyển làn đâm phải vật cản ở đường và bị trừ 1 mạng!");
                if (raceLives3D <= 0) {
                    isRace3DRunning = false;
                    alert("XE VA CHẠM! Hết 3 mạng. Nhấn nút Bắt Đầu để đua lại!");
                }
            } else if (obs.type === 'gift') {
                obs.mesh.position.z = 100;
                raceSpeed3D = Math.min(220, raceSpeed3D + 40);
                alert("ĂN HỘP QUÀ MAY MẮN 3D! +50 XP và Tăng Tốc Turbo!");
            }
        }

        // Tai su dung vat can khi di qua camera
        if (obs.mesh.position.z > 10) {
            obs.lane = Math.floor(Math.random() * 3);
            obs.type = Math.random() > 0.4 ? 'block' : 'gift';
            obs.mesh.material.color.setHex(obs.type === 'block' ? 0xef4444 : 0xf59e0b);
            obs.mesh.position.set(laneXPositions3D[obs.lane], 0.6, -110 - Math.random() * 30);
        }
    });

    raceRenderer3D.render(raceScene3D, raceCamera3D);
}

function initCanvasRaceGame() {
    raceSpeed3D = 80;
    raceDistance3D = 0;
    raceLives3D = 3;
    carLane3D = 1;
    khoi_tao_dua_xe_3d();
}

// Visor 3D de modelos IFC — se usa igual en todas las páginas de proyecto.
// No hace falta tocar este archivo: cada obra sólo define la ruta de su
// archivo .ifc con el atributo data-model del contenedor [data-ifc-viewer].
(function () {
  var root = document.querySelector('[data-ifc-viewer]');
  if (!root) return;

  var modelUrl = root.getAttribute('data-model');
  var launchBtn = root.querySelector('[data-viewer-launch]');
  var statusEl = root.querySelector('[data-viewer-status]');
  var scrim = root.querySelector('.viewer-scrim');
  var cover = root.querySelector('.viewer-cover');
  var controlsBar = root.querySelector('[data-viewer-controls]');
  var resetBtn = root.querySelector('[data-viewer-reset]');

  var started = false;
  var resetView = null;

  if (launchBtn) launchBtn.addEventListener('click', start);

  function setStatus(text, show) {
    if (!statusEl) return;
    statusEl.textContent = text || '';
    statusEl.hidden = !show;
  }

  function start() {
    if (started) return;
    started = true;
    if (scrim) scrim.remove();
    if (cover) cover.remove();
    setStatus('Cargando modelo IFC…', true);

    Promise.all([
      import('three'),
      import('../../assets/vendor/OrbitControls.min.js'),
      import('../../assets/vendor/IFCLoader.min.js'),
    ])
      .then(function (mods) {
        var THREE = mods[0];
        var OrbitControls = mods[1].OrbitControls;
        var IFCLoader = mods[2].IFCLoader;
        boot(THREE, OrbitControls, IFCLoader);
      })
      .catch(function (err) {
        console.error(err);
        setStatus('No se pudo cargar el visor 3D. Probá recargar la página.', true);
      });
  }

  function boot(THREE, OrbitControls, IFCLoader) {
    var width = root.clientWidth;
    var height = root.clientHeight;

    var scene = new THREE.Scene();
    scene.background = new THREE.Color(0x1b2126);

    var camera = new THREE.PerspectiveCamera(50, width / height, 0.05, 5000);

    var renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(width, height);
    root.appendChild(renderer.domElement);

    var hemi = new THREE.HemisphereLight(0xffffff, 0x33383d, 1.1);
    scene.add(hemi);
    var dir = new THREE.DirectionalLight(0xffffff, 1.2);
    dir.position.set(1, 2, 1.5);
    scene.add(dir);
    var dir2 = new THREE.DirectionalLight(0xffffff, 0.5);
    dir2.position.set(-1.5, -0.5, -1);
    scene.add(dir2);

    var controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.08;
    controls.minDistance = 0.1;

    var loader = new IFCLoader();
    loader.ifcManager.setWasmPath('../../assets/vendor/');

    loader.load(
      modelUrl,
      function (model) {
        model.material = new THREE.MeshStandardMaterial({
          color: 0x9aa7b0,
          metalness: 0.25,
          roughness: 0.55,
          side: THREE.DoubleSide,
        });
        scene.add(model);
        fitCameraToObject(model);
        setStatus('', false);
        if (controlsBar) controlsBar.hidden = false;
      },
      function (progress) {
        if (progress && progress.lengthComputable) {
          var pct = Math.round((progress.loaded / progress.total) * 100);
          setStatus('Cargando modelo IFC… ' + pct + '%', true);
        }
      },
      function (err) {
        console.error(err);
        setStatus('No se pudo cargar el modelo IFC. Revisá que el sitio se sirva por HTTP (no abriendo el archivo directo).', true);
      }
    );

    function fitCameraToObject(object) {
      var box = new THREE.Box3().setFromObject(object);
      var size = box.getSize(new THREE.Vector3());
      var center = box.getCenter(new THREE.Vector3());
      var maxDim = Math.max(size.x, size.y, size.z) || 1;
      var dist = maxDim * 1.6;

      camera.near = maxDim / 1000;
      camera.far = maxDim * 100;
      camera.updateProjectionMatrix();

      resetView = function () {
        camera.position.set(center.x + dist * 0.7, center.y + dist * 0.55, center.z + dist * 0.7);
        controls.target.copy(center);
        controls.update();
      };
      resetView();
    }

    if (resetBtn) resetBtn.addEventListener('click', function () { if (resetView) resetView(); });

    var ro = new ResizeObserver(function () {
      var w = root.clientWidth, h = root.clientHeight;
      if (!w || !h) return;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });
    ro.observe(root);

    (function animate() {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    })();
  }
})();

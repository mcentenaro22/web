// Lógica de la home: arma las tarjetas de proyectos desde data/proyectos.json
// y maneja el envío del formulario de contacto. No hace falta tocar este archivo
// para agregar una obra nueva — para eso está data/proyectos.json.
(function () {
  var grid = document.querySelector('[data-project-grid]');
  if (grid) {
    fetch('data/proyectos.json', { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(function (proyectos) {
        if (!Array.isArray(proyectos) || !proyectos.length) {
          grid.innerHTML = '<p class="projects-empty">Todavía no hay obras cargadas en data/proyectos.json.</p>';
          return;
        }
        grid.innerHTML = proyectos.map(renderCard).join('');
      })
      .catch(function (err) {
        console.error('No se pudo cargar data/proyectos.json', err);
        grid.innerHTML = '<p class="projects-empty">No se pudieron cargar los proyectos. Si estás mirando el sitio en tu compu, abrilo con un servidor local (no hagas doble clic en el archivo) — ver GUIA.md.</p>';
      });
  }

  function renderCard(p) {
    var meta = (p.meta || []).map(function (m) { return '<b>' + esc(m) + '</b>'; }).join('');
    return (
      '<a class="project-card" href="proyectos/' + esc(p.slug) + '/">' +
        '<span class="arrow">Ver obra ↗</span>' +
        '<div class="thumb"><img src="' + esc(p.imagen) + '" alt="' + esc(p.titulo) + '" loading="lazy"></div>' +
        '<div class="info">' +
          '<span class="tag">' + esc(p.categoria || '') + '</span>' +
          '<h3>' + esc(p.titulo) + '</h3>' +
          '<p>' + esc(p.resumen || '') + '</p>' +
          '<div class="meta">' + meta + '</div>' +
        '</div>' +
      '</a>'
    );
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // ---- formulario de contacto (FormSubmit, sin backend propio) ----
  var form = document.querySelector('[data-contact-form]');
  if (!form) return;
  var status = form.querySelector('[data-form-status]');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (form.querySelector('.hp').value) return; // honeypot anti-spam
    status.textContent = 'Enviando…';
    status.className = 'form-status';
    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' },
    })
      .then(function (r) {
        if (!r.ok) throw new Error('status ' + r.status);
        status.textContent = '¡Gracias! Recibí tu mensaje y te voy a responder a la brevedad.';
        status.className = 'form-status ok';
        form.reset();
      })
      .catch(function () {
        status.textContent = 'No se pudo enviar desde el formulario. Escribime directo a mcentenaro2@gmail.com o por WhatsApp.';
        status.className = 'form-status err';
      });
  });
})();

// Minimal interactivity: smooth scroll for anchor links
document.addEventListener('click', (e) => {
  const a = e.target.closest('a');
  if (!a || !a.getAttribute) return;
  const href = a.getAttribute('href');
  if (href && href.startsWith('#')) {
    const el = document.querySelector(href);
    if (el) {
      e.preventDefault();
      el.scrollIntoView({behavior:'smooth',block:'start'});
    }
  }
});

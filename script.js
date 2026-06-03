// Minimal interactivity: smooth scroll for anchor links
const copyButton = document.getElementById('share-profile-btn');
const copyMessage = document.getElementById('share-message');

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

if (copyButton) {
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      copyMessage.textContent = 'Profile link copied! Paste it to friends.';
    } catch (err) {
      copyMessage.textContent = 'Copy failed. Please share the current page URL manually.';
    }
  });
}

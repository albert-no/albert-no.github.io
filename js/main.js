document.addEventListener('DOMContentLoaded', function () {
  const items = document.querySelectorAll('.fade-item');

  if (items.length) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    items.forEach(item => observer.observe(item));
  }

  const newsList = document.querySelector('.news-list');
  const newsToggle = document.querySelector('.news-toggle');

  if (newsList && newsToggle) {
    newsToggle.addEventListener('click', () => {
      const expanded = newsList.classList.toggle('expanded');
      newsToggle.textContent = expanded ? 'Hide earlier updates' : 'Show earlier updates';
      newsToggle.setAttribute('aria-expanded', expanded);
    });
  }
});

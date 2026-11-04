const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.08 });

document.querySelectorAll('.gallery-flow figure, .machine-card, .principles p, .project-row').forEach((el) => {
  el.classList.add('reveal');
  observer.observe(el);
});

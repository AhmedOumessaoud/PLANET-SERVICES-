'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() { navigation.classList.remove('open'); menuButton.setAttribute('aria-expanded', 'false'); menuButton.setAttribute('aria-label', 'فتح القائمة'); }
menuButton.addEventListener('click', () => { const opened = navigation.classList.toggle('open'); menuButton.setAttribute('aria-expanded', String(opened)); menuButton.setAttribute('aria-label', opened ? 'إغلاق القائمة' : 'فتح القائمة'); });
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('click', event => { if (!event.target.closest('.nav-wrap')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && navigation.classList.contains('open')) { closeMenu(); menuButton.focus(); } });
window.matchMedia('(min-width: 761px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
if ('IntersectionObserver' in window) {
 document.documentElement.classList.add('js');
 const revealObserver = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); revealObserver.unobserve(entry.target); } }), { threshold: 0.08 });
 document.querySelectorAll('.reveal').forEach(element => revealObserver.observe(element));
 const sections = [...navigation.querySelectorAll('a')].map(link => document.querySelector(link.hash));
 const activeObserver = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) navigation.querySelectorAll('a').forEach(link => { const active = link.hash === '#' + entry.target.id; link.classList.toggle('active', active); if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); }); }), { rootMargin: '-15% 0px -55% 0px' });
 sections.forEach(section => activeObserver.observe(section));
}
const lightbox = document.querySelector('.lightbox');
let previousFocus;
document.querySelectorAll('[data-image]').forEach(button => button.addEventListener('click', () => { previousFocus = button; lightbox.querySelector('img').src = button.dataset.image; lightbox.querySelector('img').alt = button.dataset.caption; lightbox.querySelector('p').textContent = button.dataset.caption; lightbox.showModal(); document.body.style.overflow = 'hidden'; }));
document.querySelector('.lightbox-close').addEventListener('click', () => lightbox.close());
lightbox.addEventListener('click', event => { if (event.target === lightbox) { const rect = lightbox.getBoundingClientRect(); if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) lightbox.close(); } });
lightbox.addEventListener('close', () => { document.body.style.overflow = ''; previousFocus?.focus(); });
const backTop = document.querySelector('.back-top');
window.addEventListener('scroll', () => { backTop.hidden = window.scrollY < 600; }, { passive: true });
backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' }));
document.querySelector('#year').textContent = new Date().getFullYear();

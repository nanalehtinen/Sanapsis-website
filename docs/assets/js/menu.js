// Opens and closes the main menu on small screens.
document.addEventListener('DOMContentLoaded', function () {
  var button = document.querySelector('.menu-toggle');
  var nav = document.getElementById('main-nav');
  if (!button || !nav) return;
  button.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    button.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
});

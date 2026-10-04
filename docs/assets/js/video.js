// Shows a still image first; the Vimeo player loads only when the visitor taps it.
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.video-poster[data-vimeo]').forEach(function (button) {
    button.addEventListener('click', function () {
      var frame = document.createElement('div');
      frame.className = 'video-frame';
      var iframe = document.createElement('iframe');
      iframe.src = 'https://player.vimeo.com/video/' + button.dataset.vimeo + '?autoplay=1&dnt=1';
      iframe.title = button.getAttribute('aria-label');
      iframe.allow = 'autoplay; fullscreen; picture-in-picture';
      iframe.allowFullscreen = true;
      frame.appendChild(iframe);
      button.replaceWith(frame);
    });
  });
});

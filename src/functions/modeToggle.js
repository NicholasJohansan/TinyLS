import $ from 'jquery';

// Elements
const html = $('html');
const toggleButton = $('#mode-toggle-invisible-button');
const darkIcon = $('#dark-mode-icon');
const lightIcon = $('#light-mode-icon');

const setMode = (isDarkMode) => {
  html.attr('data-theme', isDarkMode ? 'dark' : 'light');
  if (isDarkMode) {
    darkIcon.removeClass('hidden');
    lightIcon.addClass('hidden');
  } else {
    darkIcon.addClass('hidden');
    lightIcon.removeClass('hidden');
  }
};

let isDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
setMode(isDarkMode);
toggleButton.on('click', () => {
  isDarkMode = !isDarkMode;
  setMode(isDarkMode);
});

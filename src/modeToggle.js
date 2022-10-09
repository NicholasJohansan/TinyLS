import $ from 'jquery';

const setMode = (isDarkMode) => {
  $('html').attr('data-theme', isDarkMode ? 'dark' : 'light');
  if (isDarkMode) {
    $('#dark-mode-icon').removeClass('hidden');
    $('#light-mode-icon').addClass('hidden');
  } else {
    $('#dark-mode-icon').addClass('hidden');
    $('#light-mode-icon').removeClass('hidden');
  }
};

export const bindModeToggle = () => {
  let isDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
  setMode(isDarkMode);
  $('#mode-toggle-invisible-button').on('click', () => {
    isDarkMode = !isDarkMode;
    setMode(isDarkMode);
  });
}
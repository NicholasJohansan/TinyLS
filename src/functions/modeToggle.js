import $ from 'jquery';
import { settings } from '../store';
import { runAsync } from '../utils';

// Elements
const html = $('html');
const toggleButton = $('#mode-toggle-invisible-button');
const darkIcon = $('#dark-mode-icon');
const lightIcon = $('#light-mode-icon');

const setMode = (isDarkMode) => {
  settings.set('mode', isDarkMode ? 'dark' : 'light');
  html.attr('data-theme', isDarkMode ? 'dark' : 'light');
  if (isDarkMode) {
    darkIcon.removeClass('hidden');
    lightIcon.addClass('hidden');
  } else {
    darkIcon.addClass('hidden');
    lightIcon.removeClass('hidden');
  }
};

runAsync(async () => {
  let savedMode = await settings.get('mode');
  let isDarkMode = savedMode ? savedMode == 'dark' : window.matchMedia('(prefers-color-scheme: dark)').matches;
  setMode(isDarkMode);
  toggleButton.on('click', () => {
    isDarkMode = !isDarkMode;
    setMode(isDarkMode);
  });
});

import $ from "jquery";
import mainHtml from './html/main.html?raw';
import titlebarHtml from './html/titlebar.html?raw';
import modeToggleHtml from './html/modeToggle.html?raw';
import urlBoxHtml from './html/urlBox.html?raw';
import.meta.globEager('./styles/*.css'); // import all css files

$('#titlebar').html(titlebarHtml);
$('#app').html(mainHtml);
$('#mode-toggle').html(modeToggleHtml);
$('#url-box').html(urlBoxHtml);

import { bindTitlebarEvents } from './titlebar';
import { bindModeToggle } from './modeToggle';
import { bindUrlBox } from './urlBox';
bindTitlebarEvents();
bindModeToggle();
bindUrlBox();

import api from './api';

let feedbackTimeout = null;

$('form').on('submit', async (e) => {
  e.preventDefault();
  if (feedbackTimeout) {
    clearTimeout(feedbackTimeout);
  }

  const link = $('#long-url-input').val();
  const alias = $('#alias-url-input').val();

  var message;
  if (link && alias) {
    const response = await api.shortenLink(link, alias);
    if (response.success) {
      message = 'Success!';
    } else {
      message = response.message;
    }
  } else {
    if (!link) message = 'Error: missing url to shorten.';
    else if (!alias) message = 'Error: missing alias.';
  }

  $('#feedback-message').text(message);
  $('#feedback-message').removeClass('hidden');
  feedbackTimeout = setTimeout(() => {
    $('#feedback-message').addClass('hidden');
  }, 3000);
});
import $ from 'jquery';
import api from '../api';

// Elements
const form = $('form');
const feedback = $('#feedback-message');
const aliasUrlInput = $('#alias-url-input');
const longUrlInput = $('#long-url-input');

let feedbackTimeout = null;
form.on('submit', async (e) => {
  e.preventDefault();
  if (feedbackTimeout) {
    clearTimeout(feedbackTimeout);
  }

  const link = longUrlInput.val();
  const alias = aliasUrlInput.val();

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

  feedback.text(message);
  feedback.removeClass('hidden');
  feedbackTimeout = setTimeout(() => {
    feedback.addClass('hidden');
  }, 3000);
});
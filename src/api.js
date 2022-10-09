
export const shortenLink = async (link, alias) => {
  const response = await fetch(`https://api.allorigins.win/get?url=${encodeURIComponent(`https://tinyurl.com/create.php?alias=${alias}&url=${link}`)}`);
  const text = await response.text();
  if (text.includes('TinyURL can\'t be created, please try again below:')) {
    var message;
    if (text.includes('Invalid URL')) {
      message = 'Invalid URL format.';
    } else if (text.includes('Alias is not available')) {
      message = `tinyurl.com/${alias} is taken.`;
    } else if (text.includes('The Alias must be at least 5 characters')) {
      message = 'Alias must be at least 5 characters.';
    } else if (text.includes('Too many custom aliases for this URL')) {
      message = 'URL has too many shortened links.'
    } else {
      message = 'Unknown error.';
    }
    return {
      success: false,
      message: `Error: ${message}`
    }
  }
  return {
    success: true
  }
};

export default {
  shortenLink
}
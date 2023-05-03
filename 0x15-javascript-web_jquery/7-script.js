// Fetches the character name
// from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const charDiv = $('div#character')

const starWarsChar = (url) => {
  $.get(url, (data, textStatus) => {
    if (textStatus === 'success')
      charDiv.text(data.name);
  })
};

starWarsChar(url);

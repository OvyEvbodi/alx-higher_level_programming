// Fetches the character name
// from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const charDiv = $('div#character')

starWarsChar = (url) => {
  $.get(url, (data) => {
    charDiv.text(data.name);
  })
};

starWarsChar(url);

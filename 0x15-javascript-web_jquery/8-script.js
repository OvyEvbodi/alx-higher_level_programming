// Fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const ulList = $('ul#list_movies');
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

const listTitle = (movie) => {
  let listItem = $('<li></>').text(movie.title);
  listItem.appendTo(ulList);
};
const starWarsMovies = (url) => {
  $.get(url, (data, textStatus) => {
    if (textStatus === 'success')
      data.results.map(listTitle)
  })
};

starWarsMovies(url);

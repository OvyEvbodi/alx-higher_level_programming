// Fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const ulList = $('ul#list_movies');
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

listTitle = (movie) => {
  let listItem = $('<li></>').text(movie.title);
  listItem.appendTo(ulList);
};
starWarsMovies = (url) => {
  $.get(url, (data) => {
    data.results.map(listTitle)
    console.log(data);
  })
};

starWarsMovies(url);

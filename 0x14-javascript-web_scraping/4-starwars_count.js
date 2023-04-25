#!/usr/bin/node
// Print the number of movies where character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const idx in films) {
      const character = films[idx].characters;
      for (const charIndex in character) {
        if (character[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error: ' + response.statusCode);
  }
});

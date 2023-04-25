#!/usr/bin/node
// Print the number of movies where character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2] + "18";

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else 
});
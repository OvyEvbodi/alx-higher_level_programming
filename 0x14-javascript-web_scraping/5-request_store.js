#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf-8');
  }
});

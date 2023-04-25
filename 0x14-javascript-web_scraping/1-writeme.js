#!/usr/bin/node
// Writes a string to a file

const file = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(file, string, 'utf8', (error) => {
    if (error) {
        console.log(error);
    }
});

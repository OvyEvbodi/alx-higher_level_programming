#!/usr/bin/node
// Reads and prints the contents of a file

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (data, error) => {
    if (data) {
        console.log(data);
    } else {
        console.log(error);
    }
});

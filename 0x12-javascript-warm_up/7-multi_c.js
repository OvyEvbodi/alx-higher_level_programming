#!/usr/bin/node
// prints x times “C is fun”

const times = process.argv[2];
if (!isNaN(parseInt(times))) console.log('Missing number of occurrences');
else {
  while (times) {
    console.log('C is fun');
    times--;
  }
}

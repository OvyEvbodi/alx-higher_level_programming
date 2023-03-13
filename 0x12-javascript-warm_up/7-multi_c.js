#!/usr/bin/node
// prints x times “C is fun”

const times = parseInt(process.argv[2]);
if (isNaN(times)) console.log('Missing number of occurrences');
else {
  while (times) {
    console.log('C is fun');
    times--;
  }
}

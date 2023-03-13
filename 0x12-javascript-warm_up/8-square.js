#!/usr/bin/node
// prints a square

let times = parseInt(process.argv[2]);
const n = times;

if (isNaN(times)) {
  console.log('Missing size');
} else {
  while (times) {
    let msg = '';
    for (let i = 0; i < n; i++) {
      msg += 'X';
    }
    console.log(msg);
    times--;
  }
}

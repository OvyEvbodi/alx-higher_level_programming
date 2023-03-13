#!/usr/bin/node
// searches the second biggest integer in the list of arguments

if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  let max = process.argv[2];
  let secMax = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      secMax = max;
      max = process.argv[i];
    }
  }
}

console.log(secMax);

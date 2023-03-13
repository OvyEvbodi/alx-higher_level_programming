#!/usr/bin/node
// computes and prints a factorial

function doFactorial(n) {
  if (n === 1 || isNaN(n)) {
    return (1);
  }
  return (n * doFactorial(n - 1));
}

console.log(doFactorial(parseInt(process.argv[2])));

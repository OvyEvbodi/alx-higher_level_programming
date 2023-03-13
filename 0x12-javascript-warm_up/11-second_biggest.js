#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const getSecondMax = (arr) => {
  let max = arr[2];
  let secMax = arr[2];
  
  if ((arr.length === 2) || (arr.length === 3)) {
    return (0);
  } else {
    for (let i = 3; i < arr.length; i++) {
      if (arr[i] > max) {
        secMax = max;
        max = arr[i];
      }
    }
    return (secMax);
  }
}

console.log(getSecondMax(process.argv));

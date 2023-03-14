#!/usr/bin/node
// Returns the reversed version of a list

exports.esrever = function (list) {
  let newList = [];
  let index = list.length - 1;
  while (index >= 0) {
    newList.push(list[index]);
    index--;
  }
  return (newList);
};

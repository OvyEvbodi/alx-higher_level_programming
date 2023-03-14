#!/usr/bin/node
// Imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence

const dict = require('./101-data').dict;
const newDict = {};

  for (key in dict) {
    if (newDict[dict[key]] === undefined) {
      newDict[dict[key]] = [];
    }
    newDict[dict[key]].push(key);
  }

  console.log(newDict);

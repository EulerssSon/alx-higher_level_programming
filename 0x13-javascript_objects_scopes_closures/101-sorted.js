#!/usr/bin/node
const mDict = require('./101-data').dict;
const occDict = {};
for (const key in mDict) {
  const value = mDict[key];
  if (occDict[value] === undefined) {
    occDict[value] = [];
  }
  occDict[value].push(key);
}
console.log(occDict);

#!/usr/bin/node
const m_dict = require('./101-data').dict;
const occDict = {};
for (key in m_dict) {
  const value = m_dict[key];
  if (occDict[value] === undefined) {
    occDict[value] = [];
  }
  occDict[value].push(key);
}
console.log(occDict);

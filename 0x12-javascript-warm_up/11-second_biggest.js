#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log('0');
} else {
  const numbers = argv.slice(2).map(Number);
  const second = numbers.sort(function(a, b) { return b - a; })[1];
  console.log(second);
}

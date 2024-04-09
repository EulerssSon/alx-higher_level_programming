#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number);
  numbers.sort();
  console.log(numbers[numbers.length - 2]);
}

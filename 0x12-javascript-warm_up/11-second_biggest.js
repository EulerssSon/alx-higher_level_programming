#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number);
  numbers.sort();
  const uniqueNumbers = [...new Set(numbers)];
  console.log(uniqueNumbers[uniqueNumbers.length - 2]);
}

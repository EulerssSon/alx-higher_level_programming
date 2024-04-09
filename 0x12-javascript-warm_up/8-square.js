#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 3 || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let character = 'X';
    for (let j = 0; j < parseInt(argv[2]) - 1; j++) {
      character += 'X';
    }
    console.log(character);
  }
}

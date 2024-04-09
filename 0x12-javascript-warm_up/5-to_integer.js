#!/usr/bin/node
const { argv } = require('node:process');
let firstArg;
if (argv.length <= 2) {
  console.log('Not a number');
} else if (argv.length > 2) {
  firstArg = argv[2];
  if (isNaN(firstArg)) {
    console.log('Not a number');
  } else {
    intFirstArg = parseInt(firstArg);
    console.log(`My number: ${intFirstArg}`);
  }
}

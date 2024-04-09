#!/usr/bin/node
const { argv } = require('node:process');
let firstArg;
let secondArg;
if (argv.length > 2) {
  firstArg = argv[2];
}
if (argv.length > 3) {
  secondArg = argv[3];
}
console.log(`${firstArg} is ${secondArg}`);

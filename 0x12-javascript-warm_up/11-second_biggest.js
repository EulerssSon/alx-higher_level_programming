#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  argv.shift();
  argv.shift();
  argv.sort();
  console.log(argv[argv.length - 2]);
}

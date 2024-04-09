#!/usr/bin/node
const { argv, exit } = require('node:process');
argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
    exit();
  }
});
console.log('No argument');

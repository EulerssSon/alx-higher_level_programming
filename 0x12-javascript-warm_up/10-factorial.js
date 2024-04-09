#!/usr/bin/node
const { argv } = require('node:process');
function fact (factorial) {
  if (isNaN(factorial) || factorial <= 0) {
    return 1;
  }
  return factorial * fact(factorial - 1);
}
console.log(fact(parseInt(argv[2])));

#!/usr/bin/node
const { argv } = require('node:process');
function fact (factorial) {
  if (isNaN(factorial)) {
    return 1;
  }
  for (let i = factorial - 1; i >= 1; i--) {
    factorial *= i;
  }
  return factorial;
}
console.log(fact(parseInt(argv[2])));

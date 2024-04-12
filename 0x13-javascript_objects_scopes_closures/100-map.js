#!/usr/bin/node
const my_list = require('./100-data.js').list;
const new_list = my_list.map(Number);
for (let i = 0; i < new_list.length; ++i) {
  new_list[i] *= i
}
console.log(my_list);
console.log(new_list);

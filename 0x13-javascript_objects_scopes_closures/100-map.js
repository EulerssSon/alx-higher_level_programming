#!/usr/bin/node
const my_list = require('./100-data.js').list;
const new_list = my_list.map(Number);
cost new_list = my_list.map((num) => (num * 2));
console.log(my_list);
console.log(new_list);

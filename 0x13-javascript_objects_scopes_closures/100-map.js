#!/usr/bin/node
let my_list = require('./100-data.js').list;
const new_list = [];
for (let i = 0; i < my_list.length; ++i) {
  new_list.push(my_list[i]* i);
}
console.log(my_list);
console.log(new_list);

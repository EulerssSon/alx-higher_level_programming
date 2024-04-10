#!/usr/bin/node
exports.logMe = function (item) {
  this.count = this.count || 0;
  console.log(`${this.count}: ${item}`);
  this.count++;
};

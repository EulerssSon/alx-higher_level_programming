#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c) {
      Rectangle.char = c;
    }
    this.print();
  }
}

module.exports = Square;

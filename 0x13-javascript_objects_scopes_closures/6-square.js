#!/usr/bin/node

const originalSquare = require('./5-square');

class Square extends originalSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let pattern = '';
      for (let j = 0; j < this.width; j++) {
        pattern += c;
      }
      console.log(pattern);
    }
  }
}

module.exports = Square;

#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let pattern = '';
      for (let j = 0; j < this.width; j++) {
        pattern += 'x';
      }
      console.log(pattern);
    }
  }
};

module.exports = Rectangle;

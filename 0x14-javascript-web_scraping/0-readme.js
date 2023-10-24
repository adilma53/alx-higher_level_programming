#!/usr/bin/node

const fs = require('fs');

const fileToWriteTO = process.argv[2];

fs.readFile(fileToWriteTO, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

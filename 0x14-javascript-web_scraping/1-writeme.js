#!/usr/bin/node

const fs = require('fs');

const fileToWriteTO = process.argv[2];
const stringTowrite = process.argv[3];

fs.readFile(fileToWriteTO, stringTowrite, (err) => {
  if (err) {
    console.error(err);
  }
});

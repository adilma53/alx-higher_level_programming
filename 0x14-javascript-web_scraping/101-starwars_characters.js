#!/usr/bin/node

const request = require('request');
const print = (characters, i) => {
  request(characters[i], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        print(characters, i + 1);
      }
    }
  });
};

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, resp, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    print(characters, 0);
  }
});

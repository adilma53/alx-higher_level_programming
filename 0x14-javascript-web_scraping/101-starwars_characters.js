#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, resp, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach((element) => {
      request(element, function (err, response, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});

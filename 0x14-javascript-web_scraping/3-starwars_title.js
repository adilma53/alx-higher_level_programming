#!/usr/bin/node
const request = require('request');

const baseUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(baseUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const parsedBody = JSON.parse(body);
    console.log(parsedBody.title);
  }
});

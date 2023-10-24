#!/usr/bin/node
const request = require('request');

const baseUrl = process.argv[2];

request(baseUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

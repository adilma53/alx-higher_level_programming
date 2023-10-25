#!/usr/bin/node

const request = require('request');
const baseUrl = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request.get(baseUrl, (error, body) => {
  if (error) {
    console.log(error);
  }
  const parsedBody = JSON.parse(body);
  const characters = parsedBody.characters;
  for (const character of characters) {
    request.get(character, (error, body) => {
      if (error) {
        console.log(error);
      }
      const parsedBodyCharacters = JSON.parse(body);
      console.log(parsedBodyCharacters.name);
    });
  }
});

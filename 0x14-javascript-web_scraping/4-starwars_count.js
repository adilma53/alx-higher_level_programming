#!/usr/bin/node
const request = require('request');

const baseUrl = process.argv[2];

function moviesWithCharacter (results, characterId) {
  let showCount = 0;

  const url = 'https://swapi-api.alx-tools.com/api/people/';
  results.forEach((show) => {
    if (show.characters.includes(`${url}${characterId}/`)) {
      showCount++;
    }
  });

  return showCount;
}

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const parsedBody = JSON.parse(body);
    const results = parsedBody.results;

    const count = moviesWithCharacter(results, 18);

    console.log(count);
  }
});

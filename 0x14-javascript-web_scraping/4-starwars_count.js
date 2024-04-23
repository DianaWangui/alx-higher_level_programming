#!/usr/bin/node
const request = require('request');
const urlApi = process.argv[2];
request.get(urlApi, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(response.body).results;
    const characterId = '18';
    let count = 0;
    films.forEach((film) => {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
        }
      });
      console.log(count);
  }
});

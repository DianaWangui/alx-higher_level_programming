#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const urlApi = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request.get(urlApi, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});

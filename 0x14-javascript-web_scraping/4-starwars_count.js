#!/usr/bin/node
const request = require('request');
const urlApi = process.argv[2];
request.get(urlApi, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(response.body).characters.length);
  }
});

#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, response.body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

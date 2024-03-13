#!/usr/bin/node
const fs = require('fs').promises;
const { argv } = require('process');
const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];
async function concatTwoFiles () {
  try {
    const data1 = await fs.readFile(fileA);
    const data2 = await fs.readFile(fileB);
    fs.writeFile(fileC, data1 + data2);
  } catch (err) {
    console.log(err);
  }
}
concatTwoFiles();

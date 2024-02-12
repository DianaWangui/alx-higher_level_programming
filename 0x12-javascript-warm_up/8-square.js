#!/usr/bin/node
const size = parseInt(process.argv[2]);
const row = 'X'.repeat(size);
let i;
if (!isNaN(size)) {
  for (i = 0; i < size; i++) {
    row;
    console.log(row);
  }
} else {
  console.log('Missing size');
}

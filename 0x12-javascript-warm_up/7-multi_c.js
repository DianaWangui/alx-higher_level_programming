#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (!arg) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}

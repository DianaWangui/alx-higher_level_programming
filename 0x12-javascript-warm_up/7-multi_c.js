#!/usr/bin/node
let i;
const numOfArgument = parseInt(process.argv[2]);
if (!isNaN(numOfArgument)) {
  for (i = 0; i < numOfArgument; i++) {
    console.log('Cis fun');
  }
} else {
  console.log('Missing number of occurrences');
}

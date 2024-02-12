#!/usr/bin/node
const argNumber = process.argv.length - 2;
if (argNumber === 0) {
  console.log('No argument');
} else if (argNumber === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

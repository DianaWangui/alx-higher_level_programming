#!/usr/bin/node
let i;
let count = 0;
for (i = 0; i < process.argv.length; i++) {
  count++;
}
if (count < 3) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

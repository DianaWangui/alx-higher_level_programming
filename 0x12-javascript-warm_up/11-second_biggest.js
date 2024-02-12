#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(Number).filter(num => !isNaN(num));
numbers.sort((a, b) => b - a);
const length = numbers.length;
if (length === 0 || length === 1) {
  console.log(0);
} else {
  console.log(numbers[1]);
}

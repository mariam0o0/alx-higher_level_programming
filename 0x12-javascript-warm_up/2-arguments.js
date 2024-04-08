#!/usr/bin/node
// script that prints a message depending of the no.of arguments

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

#!/usr/bin/node
// script that searches the second biggest integer in a list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arglist = process.argv.sort();
  console.log(arglist.reverse()[1]);
}

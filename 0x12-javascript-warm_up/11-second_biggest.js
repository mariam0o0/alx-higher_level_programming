#!/usr/bin/node
// script that searches the second biggest integer in a list of arguments

const argl = process.argv;
if (argl.length <= 3) {
  console.log(0);
} else {
  console.log(argl.sort((x, y) => y - x).slice(3)[0]);
}

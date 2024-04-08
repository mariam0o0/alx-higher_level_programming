#!/usr/bin/node
// script that computes and prints a factorial

function get_factorial (num) {
  if ((isNaN(num)) || (num === 1)) {
    return 1;
  } else {
    return num *get_factorial(num - 1);
  }
}
console.log(get_factorial(parseInt(process.argv[2])));

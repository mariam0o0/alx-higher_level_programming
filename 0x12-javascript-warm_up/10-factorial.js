#!/usr/bin/node
// script that computes and prints a factorial

function Factorial (num) {
  if ((isNaN(num)) || (num === 1)) {
    return 1;
  } else {
    return num * Factorial(num - 1);
  }
}

console.log(Factorial(parseInt(process.argv[2])));

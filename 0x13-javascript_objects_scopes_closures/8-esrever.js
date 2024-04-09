#!/usr/bin/node
exports.esrever = function (list) {
  if (list === undefined) return [];
  let rev = [];
  for (let len = list.length - 1; len >= 0; len--) {
    rev.push(list[len]);
  }
  return rev;
};

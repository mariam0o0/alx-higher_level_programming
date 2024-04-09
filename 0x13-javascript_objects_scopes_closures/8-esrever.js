#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (esreved, current) {
    esreved.push(current);
    return esreved;
  }, []);
};

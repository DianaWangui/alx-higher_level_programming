#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (const ele of list) {
    rev.unshift(ele);
  }
  return rev;
};

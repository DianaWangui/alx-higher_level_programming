#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  if (x > 0) {
    theFunction();
    exports.callMeMoby(x - 1, theFunction);
  }
};

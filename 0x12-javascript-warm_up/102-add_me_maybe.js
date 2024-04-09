#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  number += 1;
  return theFunction(number);
}

module.exports = { addMeMaybe };

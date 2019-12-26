
function whatIsInAName(collection, source) {
  var matches = collection.filter(function(v) {
    var propNames = Object.keys(source);
    var hasAll = true;
    propNames.forEach(function(propName) {
      if (v[propName] != source[propName]) {
        hasAll = false;
        }
      });
    return hasAll;
  });
  return matches;
}

console.log(whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" }));

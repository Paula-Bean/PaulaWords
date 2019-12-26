var m = new Map();
m.set(1, "black");
m.set(2, "red");
m.set("colors", 2);
m.set({x:1}, 3);

m.forEach(function (item, key) {
    console.log(item.toString());
});

console.log(m.get(2));

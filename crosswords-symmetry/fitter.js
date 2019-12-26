
// TODO: comes from outer scope.
var rows=8, cols=8;

// Initial configuration (empty grid, nothing placed yet).
var cfg = {}
cfg.usedwords = new Set();
cfg.placedwords = [];
cfg.cells = [];

for (var r=0; r<rows; r++) {
    var row = [];
    for (var c=0; c<cols; c++)
        row.push(".");
    cfg.cells.push(row);
    }


function placeword(cfg, w, r, c, direction) { // place a word, unconditionally
    cfg.usedwords.add(w);
    cfg.placedwords.push([w, r, c, direction]);
    var dx = 1, dy = 0; // horizontal
    if (direction == "v") {
        dx = 0; // vertical
        dy = 1;
        }
    [...w].forEach((letter) => {
            cfg.cells[r][c] = letter;
            c += dx;
            r += dy;
    });
    }

console.log(cfg);
placeword(cfg, "HELLO", 4, 1, "h");
placeword(cfg, "POOH", 1, 1, "v");
console.log(cfg);

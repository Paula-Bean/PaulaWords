
function is_outside_grid(r, c) {
    if (r < 0 || r >= rows)
        return true;
    if (c < 0 || c >= cols)
        return true;
    return false;
    }


function is_blocked_cell(r, c) {
    var id = `#${r}-${c}`;
    return $(id).hasClass("black");
    }


function is_valid_letter_cell(r, c) {
    if (is_outside_grid(r, c))
        return false;
    return !is_blocked_cell(r, c);
    }


function is_vertical_startcell(r, c) {
    // cell itself should be valid for a letter
    if (!is_valid_letter_cell(r, c))
        return false;
    // cell above it should be invalid for a letter
    if (is_valid_letter_cell(r - 1, c))
        return false;
    // cell below should be valid for a letter
    if (!is_valid_letter_cell(r + 1, c))
        return false;
    return true;
    }


function is_horizontal_startcell(r, c) {
    // cell itself should be valid for a letter
    if (!is_valid_letter_cell(r, c))
        return false;
    // cell left of it should be invalid for a letter
    if (is_valid_letter_cell(r, c - 1))
        return false;
    // cell right of it should be valid for a letter
    if (!is_valid_letter_cell(r, c + 1))
        return false;
    return true;
    }


function is_start_cell(r, c) {
    return is_vertical_startcell(r, c) || is_horizontal_startcell(r, c);
    }


function vertical_wordlen(r, c) {
    var len = 0;
    while (is_valid_letter_cell(r, c)) {
         len += 1;
         r += 1;
        }
    return len;
    }


function horizontal_wordlen(r, c) {
    var len = 0;
    while (is_valid_letter_cell(r, c)) {
        len += 1;
        c += 1;
        }
    return len;
    }



function determinelights()
{
    // Assign numbers to cells which can be a start of a light (either horizontal or vertical)
    lightstarts = new Map(); // Mapping from [r, c] => assigned number
    nr = 1;
    for (var r=0; r<rows; r++)
        for (var c=0; c<cols; c++)
            if (is_start_cell(r, c)) {
                lightstarts.set([r,c], nr);
                nr += 1;
                }
    // Build list of lights.
    lights = [];
    for (var r=0; r<rows; r++)
        for (var c=0; c<cols; c++) {
            if (is_vertical_startcell(r, c))
                lights.push(["v", r, c, vertical_wordlen(r, c)]);
            if (is_horizontal_startcell(r, c))
                lights.push(["h", r, c, horizontal_wordlen(r, c)]);
            }
    }

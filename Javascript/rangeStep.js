var range = function (start, stop, step) {
    var result = []
    for (var count = start; count < stop; count += step)
        result.push(count);
    return result
};

var lista = range(1, 20, 2);

console.log(lista);

console.log("lista è " + typeof (lista))


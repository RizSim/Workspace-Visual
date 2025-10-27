var range =function(start,stop,step){
    var result = []
    for (var count =start;count<stop;count+=step)
    result.push(count);
    return result
};

var lista =range(12,50,3)
console.log(lista);
console.log("range è "+typeof(range))

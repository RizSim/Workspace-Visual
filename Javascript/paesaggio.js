var paesaggio =function (){
    var result ="";
    var pianura =function(size){
        for(var count =0;count<size;count++)
        result +="_";
    };
    var montagna =function(size){
        result +="/";
        for (var count =0;count<size;count++)
        result +="'";
        result+="\\";
    };
    pianura(3);
    montagna(4);
    pianura(6);
    montagna(1);
    pianura(2);
    return result;
};

console.log(paesaggio());
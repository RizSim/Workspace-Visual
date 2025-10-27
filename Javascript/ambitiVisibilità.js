var x = "fuori";
var f1 = function () {
    var x = "dentro f1";//Qui definiamo var x solo dentro f1
};
f1();
console.log($"Stampa[x]");//Qui stamperà la variabile
var f2 = function () {
    x = "dentro f2";//Qui definiamo la x
};
f2();
console.log(x);

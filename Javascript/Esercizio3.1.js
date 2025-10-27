
let riga = ""
for (let number = 0; number <= 8; number = number + 1) {
    if (number % 2 == 0) {
        for (
            let number = 0; number <= 8; number = number + 1) { riga = riga + " *" }
    }
    else {
        for (
            let number = 0; number <= 8; number = number + 1) { riga = riga + "* " }
    }
    riga = riga + "\n"
}
console.log(riga)





let righe=""
  for (let number = 0;number<=8;number =number+1)
    {if (number %2 == 0){
      for (
        let number = 0;number<=8;number =number+1){ righe =righe+" *"}
    }
    else {
      for (
        let number = 0;number<=8;number =number+1){ righe =righe+"* "}
      }
    righe =righe+"\n"
    }
console.log(righe)

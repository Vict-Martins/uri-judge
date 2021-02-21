let intervalo = (num1, num2) => {
    let inicio = 0
    let fim = 0
    let impares = []
    if(num1 > num2){
        fim = num1
        inicio = num2
    }
    else{
        fim = num2
        inicio = num1
    }
    for(let i = 0; i < fim; i++){
        if(i%2==1){
            impares[i] = i
        }
    }
    return `${impares}`
}

console.log(intervalo(0, 100))
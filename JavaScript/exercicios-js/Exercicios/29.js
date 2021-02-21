let intervalo = vetor =>{
    let dentro = 0
    let fora = 0
for (i in vetor){
    if(vetor[i] >= 10 && vetor[i] <= 20){
        dentro++
    }
    else{
        fora++
    }
}
return [dentro, fora]
}

let num = [1, 2, 3, 10, 15, 20]
console.log(intervalo(num))
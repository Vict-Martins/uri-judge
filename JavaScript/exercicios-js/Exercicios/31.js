let negativos = vetor =>{
    let contador = 0
    for(i in vetor){
        if(vetor[i] < 0){
            contador++
        }
    }
    return contador
}
let num = [1, -1, 2, -2]
console.log(negativos(num))
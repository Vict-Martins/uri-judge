let maxMin = vetor =>{
    let maximo = Math.max(...vetor)
    let minimo = Math.min(...vetor)
    return [maximo, minimo]
}

var num = [1, 2, 3, 4, 5]
console.log(maxMin(num))
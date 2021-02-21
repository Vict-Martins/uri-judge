let arrayMult = (vetor, numero) => {
    let resultado = []
    vetor.forEach(element => {
        resultado.push(element * numero)
    });
    return resultado
}

let numv = [2, 4, 6, 8]
let numm = 5

console.log(arrayMult(numv, numm))
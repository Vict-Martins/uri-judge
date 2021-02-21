let vetores = (vetorInteiro, vetorString, vetorFloat) => {
    let resultado = []
    resultado = resultado.concat(vetorInteiro)
    resultado = resultado.concat(vetorString)
    resultado = resultado.concat(vetorFloat)
    return resultado
}
let vetorInt = [1, 2, 3, 4, 5]
let vetorString = ['a', 'b', 'c', 'd', 'f']
let vetorFloat = [1.5, 2.6, 7.8]

console.log(vetores(vetorInt, vetorString, vetorFloat))


// Função sem retorno
function imprimirSoma(a, b){
    console.log(a + b)
}

imprimirSoma(2, 3)
imprimirSoma(2)
imprimirSoma(2, 10, 3, 4, 5, 6, 7)
imprimirSoma()

// funcao com retorno

function soma(a = 1, b = 0){ // definir valor padrão, quando o valor não é definido na chamada da função
    return a + b
}
console.log(soma(2))
console.log(soma())
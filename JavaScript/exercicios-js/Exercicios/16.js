let calculadora = (numero1, sinal, numero2) =>{
    let resultado
    switch (sinal){
        case '+':
            resultado = numero1 + numero2
            return resultado
        case '-':
            resultado = numero1 - numero2
            return resultado
        case '/':
            resultado = numero1 / numero2
            return resultado
        case '*':
            resultado = numero1 * numero2
            return resultado
        default:
            return 'Operação inválida'
    }
}
console.log(calculadora(2, '+', 2))
console.log(calculadora(2, '-', 2))
console.log(calculadora(2, '/', 2))
console.log(calculadora(2, '*', 3))
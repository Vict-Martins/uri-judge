let qNotas = (valor) => {
    let n100 = valor/100
    n100 = Math.floor(n100)
    let prox = (valor%100)
   
    let n50 = prox/50
    n50 = Math.floor(n50)
    prox = (valor%50)

    let n10 = prox/10
    n10 = Math.floor(n10)
    prox = (valor%10)
    
    let n5 = prox/5
    n5 = Math.floor(n5)
    prox = (valor%5)

    let n1 = prox/1
    n1 = Math.floor(n1)
    prox = (valor%1)

    return `${n100} notas de 100\n${n50} notas de 50\n${n10} notas de 10\n${n5} notas de 5\n${n1} notas de 1\n`
}
console.log(qNotas(1179))
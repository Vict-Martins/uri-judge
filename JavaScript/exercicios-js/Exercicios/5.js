function tratamento(valor){ 
    reais = `R$ ${valor.toFixed(2).replace(".",",")}`
    return reais
}
console.log(tratamento(0.1 + 0.2))
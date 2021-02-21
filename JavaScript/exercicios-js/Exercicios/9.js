function notasEscola(nota){
    let correcao = arredondar(nota)
    if(correcao >= 40){
        return `Aprovado: ${correcao}`
    }
    else{
        return `Reprovado: ${correcao}`
    }
}

function arredondar(nota){
    if(nota >= 38 && nota % 5 > 2){
        nota = nota + (5 - ( nota % 5))
    }
    return nota
}

console.log(notasEscola(38))
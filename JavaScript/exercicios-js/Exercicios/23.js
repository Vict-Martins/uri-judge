let avaliacao = (codigo, nota1, nota2, nota3) => {
    let media = ((nota1 * 4) + (nota2 * 3) + (nota3 * 3))/(4 + 3 + 3)
    if(media >= 5){
        return `${codigo}, ${nota1}, ${nota2}, ${nota3}, ${media} Aprovado`
    }
    else if(media <= 5){
        return `Código: ${codigo}\n, Nota 1: ${nota1}\n, Nota 2: ${nota2}\n, Nota 3: ${nota3}\n, ${media} Reprovado`
    }
}
console.log(avaliacao(01, 5, 5, 5))
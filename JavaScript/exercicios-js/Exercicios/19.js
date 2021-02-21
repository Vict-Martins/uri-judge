let lanchonet = (codigo, quantidade) =>{
    switch (codigo){
        case 100:
            return `${quantidade} Cachorro(s) Quente(s): ${3*quantidade} R$`
        case 200:
            return `${quantidade} Hamburguer Simples: ${4*quantidade} R$`

        case 300:
            return `${quantidade} cheeseburguer: ${5.50*quantidade} R$`
        
        case 400:
            return `${quantidade} Bauru: ${7.50*quantidade} R$`

        case 500:
            return `${quantidade} Refrigerante: ${3.50*quantidade} R$`
        
        case 600:
            return `${quantidade} suco: ${2.80*quantidade} R$`
        }
}
console.log(lanchonet(100, 2))
console.log(lanchonet(200, 2))
console.log(lanchonet(300, 2))
console.log(lanchonet(400, 2))
console.log(lanchonet(500, 2))
console.log(lanchonet(600, 2))
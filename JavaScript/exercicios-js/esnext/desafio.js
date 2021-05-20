const fs = require('fs')
const path = require('path')

function letArquivo(caminho) {
    return new Promise(resolve => {
        fs.readFile(caminho, function(_, conteudo){
            resolve(conteudo.toString())
        })
        console.log('depois de ler')
    })
}

const caminho = path.join(__dirname, 'dados.txt')

letArquivo(caminho)
    .then(conteudo => conteudo.split('\n'))
    .then(linhas => console.log(linha[1]))

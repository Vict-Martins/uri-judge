const retornarObjeto = objeto => {
    return Object.entries(objeto)
}

const objetoParaArray = ({
    nome: "Maria",
    profissao: "Desenvolvedora de software"
})

console.log(retornarObjeto(objetoParaArray))


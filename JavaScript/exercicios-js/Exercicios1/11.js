const removerPropriedade = (objeto, retirar) => {
    const aux = Object.assign({}, objeto)
    delete objeto[retirar]
    return objeto
}

console.log(removerPropriedade({a: 1, b: 2}, "a"))
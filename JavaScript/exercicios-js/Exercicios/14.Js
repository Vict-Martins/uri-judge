let tipoFruta = fruta =>{

    switch (fruta){
        case 'maça':
            return 'Não vendemos essa fruta aqui'
            break
        case 'kiwi':
            return 'Estamos com escassez de kiwis'
            break
        case 'melancia':
            return 'Aqui estar, são 3 reais o quilo'
            break
        default:
            return 'Inválido'
            break;
    }
}

console.log(tipoFruta('flores'))
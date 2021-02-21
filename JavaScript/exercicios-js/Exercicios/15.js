let comprarCarros = modelo =>{
    switch (modelo) {
        case 'hatch':
            return 'Compra efetuada com sucesso'
            break
        case 'sedan':
            return 'Tem certeza que não prefere este modelo'
            break
        case 'motocicletas':
            return 'Tem certeza que não prefere este modelo'
            break
        case 'caminhonetes':
            return 'Compra efetuada com sucesso'
            break;
        default:
            return 'Não trabalhamos com esse modelo'
            break;
    }
}

console.log(comprarCarros('hatch'))
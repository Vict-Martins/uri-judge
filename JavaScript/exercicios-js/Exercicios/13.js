
let qualquer = a => {
switch (a){
    case 1:
        return 'Inválido'
        break;
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
        return 'Válido'
        break;
    case 7:
        return 'Inválido'
        break;
    default:
        return 'Inválido'
        break;
}
}

console.log(qualquer(1))
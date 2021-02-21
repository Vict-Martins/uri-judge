let aumento = (salario, plano) => {
    switch (plano){
        case 'A':
            return (salario*1.10).toFixed(2)
        case 'B':
            return (salario*1.15).toFixed(2)
        case 'C':
            return (salario*1.20).toFixed(2)
        default:
            return 'operacao invalida'
    }
}
console.log(aumento(100, 'A'))
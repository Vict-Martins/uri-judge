let iptu = (mes, valor) => {
    let atraso = mes - 1
    let montante = (valor*((1+0.05)**atraso)).toFixed(2)
    return montante
}
console.log(iptu(4,100))

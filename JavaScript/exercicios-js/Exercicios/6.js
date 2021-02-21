function jSimples(ci, juros, tempo){
    return (ci + ((ci*juros)*tempo))
}

let juSimples = (ci, juros, tempo) => ci + ((ci*juros)*tempo)
let juComposto = (ci, juros, tempo) => ci*((1+juros)**tempo)

console.log(juSimples(2000, 0.1, 10))
console.log(juComposto(2000, 0.1, 10).toFixed(2))

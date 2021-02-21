let pa = (n, a1, r) => {
    let elementPa = []
    elementPa[0] = 0
    let soma = 0
    for(let i = 1; i <= n; i++){
        elementPa[i] = a1+r+elementPa[i-1]
        soma += elementPa[i]
    }
    return [elementPa, soma]
}
let pg = (n, a1, r) => {
    let elementPg = []
    elementPg[0] = 1 
    let somaPg = 0
    for(let i = 1; i <= n; i++){
        elementPg[i] = (r*elementPg[i-1])
        somaPg += elementPg[i]
    }
    return [elementPg, somaPg]
}
console.log(pa(10, 0, 2))
console.log(pg(10, 1, 2))
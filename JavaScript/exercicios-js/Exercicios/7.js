let baskara = (a, b, c) => {
    raizes= []
    delta = (b**2)-(4*a*c)
    if(delta < 0){
        return 'Delta é negativo'
    }
    x1 = (-b + Math.sqrt(delta))/2*a
    x2 = (-b - Math.sqrt(delta))/2*a
    raizes.push(x1)
    raizes.push(x2)
    return raizes
}
console.log(baskara(1, 3, 2))
console.log(baskara(3, 1, 2))

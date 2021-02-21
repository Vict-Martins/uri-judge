function tipoTriangulo(a, b, c){
    if(a + b < c || a + c < b || b + c < a){
        return 'Não forma triangulo'
    }
    else if(a == b && b == c ){
        return 'Equilátero'
    }
    else if(a == b || b == c || a == c){
        return 'Isósceles'
    }
    else{
        return 'Escaleno'
    }
}
console.log(tipoTriangulo(1, 1, 10))
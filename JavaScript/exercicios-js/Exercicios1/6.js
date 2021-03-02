const intervalo = (numero, minimo, maximo, Boolean = false) => {
    if( numero > minimo && numero < maximo){
        return true
    } 
    else if(numero >= minimo && numero <= maximo && Boolean == true){
        return true
    }
    else{
        return false
    }
}
console.log(intervalo(8, 9, 100, true))
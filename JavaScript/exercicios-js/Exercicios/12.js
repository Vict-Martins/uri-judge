let fatorial = valor =>{
    let total
    
    if(valor == 1){
        return 1
    }
    else{
        total = valor * fatorial(valor - 1)
    }
    return total
}

console.log(fatorial(6))
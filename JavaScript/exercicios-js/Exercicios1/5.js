const inversor = num => {
    if (typeof num == 'boolean'){
        return !num
    }
    else if(typeof num == 'number'){
        return -num
    }
    else{
        return `booleano ou números esperado, mas o parâmetro é do tipo string`
    }
}

console.log(inversor(true))
console.log(inversor(6))
console.log(inversor('qwe'))
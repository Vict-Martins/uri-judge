const totalSalário = (horas, valorHora) => `Salário igual a R$ ${horas*valorHora}`

console.log(totalSalário(10, 10))

const mesesDoAno = num => {    
    let meses = [ 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return meses[--num]
} 
console.log(mesesDoAno(1))
let num1 = 1
let num2 = 2

num1++
console.log(num1)
--num1
console.log(num1)

console.log(++num1 === num2--) // a forma prefixada fez o incremento antes da comparacao
console.log(num1 === num2)
const escola = 'Cod3r'

console.log(escola.charAt(4)) // retorna o valor do indice 4
console.log(escola.charAt(5))
console.log(escola.charCodeAt(3)) // retorna o valor da tabela asc
console.log(escola.indexOf('3'))
console.log(escola.substring(1)) // retorna as string a partir do indice 1
console.log(escola.substring(0, 3)) // retorna a cadeia de caracteres no intervalo de 0 a 3
console.log('escola'.concat(escola).concat('!'))
console.log('escola' + (escola) + ('!')) // concatenando variáveis
console.log(escola.replace(3, 'e'))
console.log(escola.replace(/\d/, 'e'))
console.log(escola.replace(/\w/g,'e')) // todos os caracteres são transformados na letra e
console.log('Ana,Maria,Pedro'.split(',')) // array


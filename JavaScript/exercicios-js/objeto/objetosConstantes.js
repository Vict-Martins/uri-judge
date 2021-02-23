// pessoa -> 123 -> {...}
const pessoa = { nome: 'joao'}
pessoa.nome = 'Pedro'
console.log(pessoa.nome)

// pessoa <- 456 -> {...}
// pessoa = { nome: 'Ana' }

Object.freeze(pessoa) // nao consegue mecher no objeto

pessoa.end = 'Rua sem nome'
delete.pessoa.nome


console.log(pessoa.nome)
console.log(pessoa)

const pessoaConstante = Object.freeze({ nome: 'Maria'})
pessoaConstante.nome = 'Jonas'
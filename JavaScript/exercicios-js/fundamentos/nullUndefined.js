let valor
console.log(valor) //undefined

valor = null // Nenhum valor, e não aponta para um endereço de memoria
console.log(valor) //null,  zerar um valor que aponta para algo
// c0onsole.log(valor.toString())// erro

const produto = {}
console.log(produto.preco)
console.log(produto)
produto.preco = 3.50

console.log(produto)

console.log(!!produto.preco)
console.log(produto)
delete produto.preco
console.log(produto)

produto.preco = null

console.log(!!produto.preco)
console.log(produto)
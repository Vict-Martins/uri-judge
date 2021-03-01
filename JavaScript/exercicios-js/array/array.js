console.log(typeof Array, typeof new Array, typeof[])

let aprovados = new Array('Bia', 'Carlos', 'Ana')
console.log(aprovados)

aprovados = ['Bia', 'Carlos', 'Ana']
console.log(aprovados[0])
console.log(aprovados[1])
console.log(aprovados[2])
console.log(aprovados[3])

aprovados[3] = 'Paulo'
aprovados.push('Abia')
console.log(aprovados.length)

aprovados[9] = 'Rhafael'
console.log(aprovados.length)
console.log(aprovados[8] === undefined)


console.log(aprovados)
aprovados.sort() // reordena o array
console.log(aprovados)  

delete aprovados[1]
console.log(aprovados[1])
console.log(aprovados[2])

aprovados = ['bia', 'carlos', 'ana']
aprovados.splice(1, 1, 'elemento1', 'elemento2') // exclui elementos a partir do indice 1.
console.log(aprovados)
const pilotos = ['Vettel', 'Alonso', 'Raikkonen', 'Massa']
pilotos.pop()
console.log(pilotos)

pilotos.push('Verstappen')
console.log(pilotos)

pilotos.shift() // remove o primeiro elemento da lista
console.log(pilotos)

pilotos.unshift('Hamilton')// adiciona o elemento na primeira posicao índice 0 
console.log(pilotos)

// splice pode adicionar e remover elementos

pilotos.splice(2, 0, 'bosttas', 'Massa')
console.log(pilotos)

// remover

pilotos.splice(3, 1)

const algunsPilotos = pilotos.slice(2) // copia o array a parti do índice
console.log(algunsPilotos)

const algunsPilotos2 = pilotos.slice(1, 4) // o indice 1 entra, porém o 4 não
console.log(algunsPilotos2)
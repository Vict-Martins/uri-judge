// não aceita repetição/não indexada
const times = new Set()
times.add('vasco')
times.add('São Paulo').add('palmeiras').add('corinthians')
times.add('flamengo')
times.add('vasco')

console.log(times)
console.log(times.size)
console.log(times.has('vasco'))
console.log(times.has('vasco'))
times.delete('flamengo')
console.log(times.has('flamengo'))

const nomes = ['raquel', 'lucas', 'Julia', 'lucas']
const nomesSet = new Set(nomes)
console.log(nomesSet)
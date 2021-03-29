// sem promisse...
const url = `http://files.cod3r.com.br/curso-js/turma${letra}.json`

const getTurma = (letra, callback) => {
   
    return new Promises((resolve, reject) => {
        http.get(url, res =>{

            res.on('data', dados => {
                resultado += dados
            })
    
            res.on('end', () => {
                try{
                    resolve(JSON.parse(resultado))
                } catch(e){
                    reject(e)
                }
            })
        })
    })
    
}

let nomes = []

getTurma('A').then(alunos => {
    nomes = nomes.concat(alunos.map(a => `A: ${a.nome}`))
    getTurma('B').then(alunos => {
        nomes = nomes.concat(alunos.map(a => `B: ${a.nome}`))
        getTurma('C').then(alunos => {
            nomes = nomes.concat(alunos.map(a => ` C: ${c.nome}`))
            console.log(nomes)
        })
    })
})
    
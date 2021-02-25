class Lancamento {
    constructor(nome = 'Generico', valor = 0){
        this.nome
        this.valor = valor
    }
}

class cicloFinanceiro {
    constructor(mes, ano){
        this.mes = mes
        this.ano = ano
        this.Lancamento =[]
    }
    addLancamento(...Lancamento){
        Lancamento.forEach(l => this.Lancamento.push(l))
    }
    sumario(){
        let valorConsolidado = 0
        this.Lancamento.forEach(l => {
            valorConsolidado += l.valor
        })
        return valorConsolidado
    }
}

const salario = new Lancamento('Salario', 45000)
const contaDeluz = new Lancamento('Luz', -220)

const contas = new cicloFinanceiro(6, 2018)
contas.addLancamento(salario, contaDeLuz)
console.log(contas.sumario())
function tratarErroElancar(erro){
   // throw new Error('...')
   // throw true
   // throw 'mensagem'
   throw {
       nome: erro.name,
       msg: erro.message,
       date: new Date
   }
}

function imprimirNomeGritando(obj){
    try{
        console.log(obj.nome.toUpperCase() + '!!!')
    } catch (e){
        tratarErroElancar(e)
    } finally{
        console.log('final')
    }
}

const obj = { nome: 'Roberto'}
imprimirNomeGritando(obj)
var express = require('express');
var router = express.Router();
var dbConn = require('../db/db.js');
// ROTA para página principal com consulta de extensao
router.get('/', function(req, res, next) {
dbConn.query('SELECT * FROM contrata ORDER BY id desc',function(err, queryExtensao) {
if(err) {
req.flash('error', err);
// preparar dados para página em views/extensao/index.ejs
} else {
// preparar dados para página em views/extensao/index.ejs
res.render('extensao',{dataExtensao: queryExtensao});
}
});
});
// EDITAR AQUI PARA INSERIR MÉTODOS PARA insert, uptdate e delete
//------------------------------------------------------------------------------------------------
// mostra página editar (inserir dados)
router.get('/adicionar', function(req, res, next) {
    // render to editar.ejs, variáveis para get response do servidor
    res.render('extensao/inserir.ejs', {
        FK_Pessoa: '', 
        FK_Cadastra: '', 
        nota_avaliacao: '',
        discricao_avaliacao: '', 
        data_avaliacao: '', 
        data_contrato: '', 
        valor_mensal: '', 
        status: '', 
        validade: ''
       
    })
    })

    // Insere extensao, valores vindo de name dos input no body do html
    router.post('/adicionar', function(req, res, next) { //adicionar é o caminho indicado na pag. html
    let FK_Pessoa = req.body.FK_Pessoa;
    let FK_Cadastra = req.body.FK_Cadastra;
    let nota_avaliacao = req.body.nota_avaliacao;
    let discricao_avaliacao = req.body.discricao_avaliacao;
    let data_avaliacao = req.body.data_avaliacao;
    let data_contrato = req.body.data_contrato;
    let valor_mensal = req.body.valor_mensal;
    let status = req.body.status;
    let validade = req.body.validade;
   
    let errors = false;
    // definição de insereDados
   if(!errors) {
    var insereDados = {
    FK_Pessoa: FK_Pessoa,
    FK_Cadastra: FK_Cadastra,
    nota_avaliacao: nota_avaliacao, 
    discricao_avaliacao: discricao_avaliacao, 
    data_avaliacao: data_avaliacao, 
    data_contrato: data_contrato, 
    valor_mensal: valor_mensal, 
    status: status, 
    validade: validade
   
    }

    dbConn.query('INSERT INTO contrata SET ?', insereDados, function(err, result) {
    if (err) { req.flash('error', err)
    // render para inserir.ejs com os mesmos dados
    res.render('extensao/inserir.ejs', {
    FK_Pessoa: insereDados.FK_Pessoa, 
    FK_Cadastra: insereDados.FK_Cadastra,
    nota_avaliacao: insereDados.nota_avaliacao,
    discricao_avaliacao: insereDados.discricao_avaliacao,
    data_avaliacao: insereDados.data_avaliacao,
    data_contrato: insereDados.data_contrato,
    valor_mensal: insereDados.valor_mensal,
    status: insereDados.status,
    validade: insereDados.validade
    
    })
    } else {
    req.flash('success', 'Inserido com sucesso');
    res.redirect('/extensao');
    }
    })
    }
    });

//-------------------------------------------------------------------------------------------------------

// ROTA PARA EDITAR REGISTRO
router.get('/atualizar/(:id)', function(req, res, next) {
    let id = req.params.id; //recebe id da página editar.ejs
    dbConn.query('SELECT * FROM contrata WHERE id = ' + id,
    function(err, queryEditar, fields) {
    if (queryEditar.length <= 0) { //se query retornou vazia
    req.flash('error', 'Não encontrado extensao com id = ' + id)
    res.redirect('/extensao')
    } else {
    // render para editar.ejs com dados do livro da query rows
    res.render('extensao/editar.ejs', {
    title: 'Edita extensao', 
    id: queryEditar[0].id,
    FK_Pessoa: queryEditar[0].FK_Pessoa,
    FK_Cadastra: queryEditar[0].FK_Cadastra, 
    nota_avaliacao: queryEditar[0].nota_avaliacao,
    discricao_avaliacao: queryEditar[0].discricao_avaliacao,
    data_avaliacao: queryEditar[0].data_avaliacao,
    data_contrato: queryEditar[0].data_contrato,
    valor_mensal: queryEditar[0].valor_mensal,
    status: queryEditar[0].status,
    validade: queryEditar[0].validade
    })
    }
    })
    })
    
    // rota (post) para atualizar livros
    router.post('/atualizar/:id', function(req, res, next) {
    let id = req.params.id;
    let FK_Pessoa = req.body.FK_Pessoa;
    let FK_Cadastra = req.body.FK_Cadastra;
    let nota_avaliacao = req.body.nota_avaliacao;
    let discricao_avaliacao = req.body.discricao_avaliacao;
    let data_avaliacao = req.body.data_avaliacao;
    let data_contrato = req.body.data_contrato;
    let valor_mensal = req.body.valor_mensal;
    let status = req.body.status;
    let validade = req.body.validade;
    let errors = false;
    if( !errors ) {
    var editaDados = {
    FK_Pessoa: FK_Pessoa,
    FK_Cadastra: FK_Cadastra,
    nota_avaliacao: nota_avaliacao,
    discricao_avaliacao: discricao_avaliacao,
    data_avaliacao: data_avaliacao,
    data_contrato: data_contrato,
    valor_mensal: valor_mensal,
    status: status,
    validade: validade
    }
    // update query
dbConn.query('UPDATE contrata SET ? WHERE id = ' + id,
editaDados, function(err, result) {
if (err) {
req.flash('error', err)
// render para editar.ejs com os mesmos dados
res.render('extensao/editar.ejs', {
id: req.params.id,
FK_Pessoa: editaDados.FK_Pessoa, 
FK_Cadastra: editaDados.FK_Cadastra, 
nota_avaliacao: editaDados.nota_avaliacao, 
discricao_avaliacao: editaDados.discricao_avaliacao, 
data_avaliacao: editaDados.data_avaliacao, 
data_contrato: editaDados.data_contrato, 
valor_mensal: editaDados.valor_mensal, 
status: editaDados.status, 
validade: editaDados.validade
})
} else {
req.flash('success', 'extensao atualizado com sucesso');
res.redirect('/extensao');
}
})
}
})
//-------------------------------------------------------------------------------------
// DELETAR LIVRO
router.get('/delete/(:id)', function(req, res, next) {
    let id = req.params.id;
    dbConn.query('DELETE FROM contrata WHERE id = ' + id, function(err, result) {
    if (err) {
    req.flash('error', err)
    res.redirect('/extensao') // redirecionar para página principal
    } else {
    req.flash('success', 'extensao deletado...! ID = ' + id)
    res.redirect('/extensao')
    }
    })
    })
module.exports = router

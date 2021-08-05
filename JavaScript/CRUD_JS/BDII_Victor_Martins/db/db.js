var mysql = require('mysql');
var connection = mysql.createConnection({
	host:'localhost',
	user:'root',
	password:'123456',
	database:'credito'
});
connection.connect(function(error){
	if(!!error) {
		console.log(error);
	} else {
		console.log('Servidor conectado, acesse no browse http://localhost:3000/extensao');
	}
});
module.exports = connection;
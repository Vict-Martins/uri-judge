const prod1 = {}
prod1.nome = 'Celular Ultra Mega'
prod1.preco = 4998.90
prod1['Desconto legal'] = 0.40
console.log(prod1)

const prod2 = {
    nome: 'Camisa Polo',
    preco: 79.90,
    obj:{
        blabla:1,
        obj: 'Camisa de manga'
    }
}

// '{"nome": "Camisa Polo", "preco": 79.90}' Formato json


console.log(prod2)

// Objetos em JavaScript o variável e passada por referência na memoria
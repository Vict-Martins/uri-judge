let comparaComThis = function (param){
    console.log(this === param)
}

comparaComThis(global)

const obj = {}
comparaComThis = comparaComThis.bind(obj)
comparaComThis(global)
comparaComThis(obj)

let comparaComThisArrom = param => console.log(this === param)
comparaComThis(global)
comparaComThis(module.exports)

comparaComThisArrom = comparaComThisArrom.bind(obj)
comparaComThisArrom(obj)
comparaComThisArrom(module.exports)
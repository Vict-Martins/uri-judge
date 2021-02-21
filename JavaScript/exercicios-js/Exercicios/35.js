let combina = (vetorIni, vetorAdd) =>{
    for (i in vetorAdd){
        console.log(vetorAdd[i])
        vetorIni.push(vetorAdd[i])
    }
    return vetorIni
}

let vet1 = [1, 2, 3, 4, 5]
let vet2 = [6, 7, 8, 9, 10]

console.log(combina(vet1, vet2))
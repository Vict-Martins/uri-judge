Pjogos = " 20, 30, 40, 50, 60, 70, 80, 90, 0"

function analise (Pjogos) { 
    let Pojogos = Pjogos.split(", ")
    let melhorP = 0
    let piorJogo = 1
    let quantidade = 0
    let PiorPontuacao = 0

    for(let i = 1; i < Pjogos.length; i++){
        if(Pojogos[i] > melhorP){
            melhorP = Pojogos[i]
            quantidade++
        }
        else if(Pojogos[i] < piorJogo){
            piorJogo = Pojogos[i]
            PiorPontuacao = i+1
        }
    }
return [quantidade, PiorPontuacao]
}

console.log(analise(Pjogos))
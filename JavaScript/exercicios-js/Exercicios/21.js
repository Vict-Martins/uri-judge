let planoSaude = idade =>{
    let valorPagar = 100
    if(idade < 10 && idade > 0){
        valorPagar += 80
    }
    else if(idade < 30 && idade > 10){
        valorPagar += 50
    }
    else if(idade < 60 && idade > 30){
        valorPagar += 95
    }
    else if(idade > 60){
        valorPagar += 130
    }
    else{
        return 'Idade inválida'
    }
return valorPagar
}

console.log(planoSaude(90))
let comparaString = (string1, string2) => {
    let maior 
    let menor
    if(string1.length > string2.length){
        maior = string1.length
        menor = string2.length
    }
    else{
        maior = string2.length
        menor = string1.length
    } 
    
    let gatilho = Boolean
    for(let i = 0; i < maior;i++){
        for(let y = 0; y < menor;y++){
            if(string2.includes(string1[i])){
                gatilho = true
            }
            else{
                return false
            }
        }
    }
return gatilho
}
let s = [1, 2, 3, 4, 's']
let s1 = [3, 2, 1, 4, 's']
console.log(comparaString(s, s1))
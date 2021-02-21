let media = vetor =>{
    let mediaTotal = 0
    for(i in vetor){
        mediaTotal += vetor[i]
    }
    return mediaTotal/vetor.length
}
let num = [10, -1, 2, -2]
console.log(media(num))
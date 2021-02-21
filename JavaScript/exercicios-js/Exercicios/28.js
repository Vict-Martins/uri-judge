let imparPar = vetor =>{
    let par = 0
    let impar = 0
   
 for (i in vetor){
     if(vetor[i]%2 == 0){
         par++
     }
     else{
         impar++
     }
 }
 return [par, impar]
}

let num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(imparPar(num))
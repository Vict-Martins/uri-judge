{
    {
        {
            { 
                var sera = 'Será?' // var é visto universalmente, dentro e fora do scopo.
            }
        }
    }
}
console.log(sera)

function teste(){
    var local = 123 // var só é visivel dentro da função
}
teste()
console.log(local)
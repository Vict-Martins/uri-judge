inicio = gets.to_i
final = gets.to_i
soma = 0

if inicio > final
    aux = final
    final = inicio
    inicio = aux
end

inicio.upto(final) do

    if inicio%13 != 0 
        soma += inicio
    end

inicio += 1
end

puts soma
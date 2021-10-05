inicio = gets.to_i
fim = gets.to_i
soma = 0

if inicio > fim
    aux = inicio
    inicio = fim
    fim = aux
end

inicio += 1
fim -= 1

inicio.upto(fim) do
    if  inicio % 5 == 2 || inicio % 5 == 3
        puts inicio
    end
inicio += 1
end


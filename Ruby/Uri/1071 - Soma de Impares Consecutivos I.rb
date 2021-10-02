a = gets.chomp.to_i
b = gets.chomp.to_i
maior = a
menor = b

if (menor > maior)
    aux = maior
    maior = menor
    menor = aux
end

aux = menor + 1
soma = 0

while aux < maior
    if aux % 2 != 0
        soma += aux
    end
aux += 1
end

puts soma
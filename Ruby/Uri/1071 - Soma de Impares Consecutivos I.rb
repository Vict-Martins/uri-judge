a = gets.chomp.to_i
b = gets.chomp.to_i
aux = 0

if (b > a)
    aux = a
    a = b
    b = aux
end

aux = a + 1
soma = 0

while aux < b
    if aux % 2 != 0
        soma += aux
        #puts soma
         
    end
aux += 1
end

puts aux
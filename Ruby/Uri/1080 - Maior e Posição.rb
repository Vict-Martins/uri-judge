cont = 0
maior = 0
index = 0

while cont < 100
    
    entrada = gets.to_i
    if entrada > maior
        maior = entrada
        index = cont + 1
    end
cont += 1    
end

puts maior
puts index
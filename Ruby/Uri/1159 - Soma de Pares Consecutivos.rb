cont = 0
soma = 0
num = 0
while true
    soma = 0
    cont = 0
    entrada = gets.to_i
    if entrada == 0
        break
    end
    while cont < 5
        if entrada % 2 == 0
            soma += entrada
            cont += 1
        end
    entrada += 1
    end
    puts soma
end
entrada = gets.to_i
cont = 0
soma = 0


for a in 1..entrada
    x = gets.strip.split(' ')
    comeco, quant = x
    comeco = comeco.to_i
    quant = quant.to_i
    
    while cont < quant
        if comeco % 2 == 1
            soma += comeco
            cont += 1
        end
    comeco += 1
    end
    puts soma
    soma = 0
    cont = 0
end
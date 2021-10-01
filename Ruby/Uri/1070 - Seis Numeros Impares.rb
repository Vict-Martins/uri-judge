entrada = gets.chomp.to_i
contador = 0

while contador < 6

    if(entrada%2 == 1)
        puts entrada
        contador += 1
    end
    if contador == 6
        break
    end
entrada += 1
end
entrada = gets.to_i
contador = 0

entrada.times do |num|

    entrada_info = gets.strip.split(' ')
    populacao1, populacao2, taxa1, taxa2 = entrada_info
    populacao1 = populacao1.to_i
    populacao2 = populacao2.to_i

    taxa1 = taxa1.to_f
    taxa2 = taxa2.to_f
    taxa1 = taxa1 / 100
    taxa2 = taxa2 / 100

    while populacao2 >= populacao1

        populacao1 += (populacao1 * taxa1).to_i
    
        populacao2 += (populacao2 * taxa2).to_i
        
        contador += 1

        break if contador > 100

    end
    if contador > 100
        puts "Mais de 1 seculo."
    else
        puts "#{contador.to_i} anos."
    end
    contador = 0

end
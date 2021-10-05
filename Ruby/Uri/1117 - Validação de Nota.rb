cont = 0
soma = 0
while cont != 2 
    
    entrada = gets.chomp.to_f
    
    if entrada >= 0 && entrada <= 10
        soma += entrada
        cont += 1
    else
        puts "nota invalida"
    end

end
soma = soma/cont
puts "media = #{'%.2f'% soma}" 
Entrada = gets.to_f
if Entrada >= 0 && Entrada <= 25
    puts "Intervalo [0,25]"
elsif Entrada > 25 && Entrada <= 50
    puts "Intervalo (25,50]"
elsif Entrada > 75 && Entrada <=100
    puts "Intervalo (75,100]"
else   
    puts "Fora de intervalo"
end
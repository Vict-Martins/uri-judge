entrada = gets.to_f
vet = []

100.times do |x|

    vet << entrada
    puts "N[#{x}] = #{'%.4f'% vet[x]}"
    entrada = entrada / 2

    
end

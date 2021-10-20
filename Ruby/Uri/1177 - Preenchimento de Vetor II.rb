entrada = gets.to_i

vet = []
i = 0

while i < 1000
    
        vet <<  i%entrada
        puts "N[#{i}] = #{vet[i]}"
        i += 1

end

vet = []

for a in 1..10

    entrada = gets.to_i
    if entrada > 0
        vet << entrada
    else
        vet << 1
    end
    puts "X[#{a-1}] = #{vet[a-1]}"
    
end


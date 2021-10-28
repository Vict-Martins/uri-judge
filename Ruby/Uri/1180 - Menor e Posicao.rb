entrada = gets.strip.to_i

converte_i = lambda { |numero| numero.to_i}

vetor = gets.split(' ').collect!(&converte_i)
vetor = vetor[0..entrada-1]

minimo = Float::INFINITY
index_minimo = -1

vetor.each_with_index do |item, index|

    if item < minimo
    
        minimo = item
        index_minimo = index

    end

end

puts "Menor valor: #{minimo}"
puts "Posicao: #{index_minimo}"
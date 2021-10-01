pares = 0
impares = 0
positivos = 0
negativos = 0

5.times do |entrada|
    entrada = gets.chomp.to_i
    if entrada % 2 == 0
        pares += 1
    else
        impares += 1
    end

    if entrada > 0
        positivos += 1
    elsif entrada < 0
        negativos += 1
    end
end
puts "#{pares} valor(es) par(es)"
puts "#{impares} valor(es) impar(es)"
puts "#{positivos} valor(es) positivo(s)"
puts "#{negativos} valor(es) negativo(s)"
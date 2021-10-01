i = 0
soma = 0

6.times do |entrada|
    entrada = gets.strip.to_f
    if entrada > 0
        soma += entrada
        i += 1
    end
end

soma /= i

puts "#{i} valores positivos\n#{'%.1f' % soma}"


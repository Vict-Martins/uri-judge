x = x.to_f
soma = 0

while true

    entrada = gets.to_f
    if entrada < 0
        break
    end
    soma += entrada
    x += 1

end

soma /=x

puts "#{'%.2f'% soma}"
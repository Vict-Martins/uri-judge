coluna = gets.to_i
char = gets.strip
soma = 0
matriz = [12][12]
for x in 0..11
    for y in 0..11
    matriz = gets.to_f
    soma = soma + matriz if y == coluna
    end
end

puts char == 'S' ? "#{'%.1f' %soma}" : "#{'%.1f' %(soma/12)}"
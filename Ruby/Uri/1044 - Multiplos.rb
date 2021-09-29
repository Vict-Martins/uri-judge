entrada = gets.strip.split(' ')
a, b = entrada

a = a.to_i
b = b.to_i

if b % a == 0 || a % b == 0
    puts "Sao Multiplos"
else
    puts "Nao sao Multiplos"
end
entrada = gets.strip.split(' ')

a ,b = entrada

a = a.to_i
b = b.to_i

temp = 0



c_1 = a == b
c_2 = a > b
c_3 = a < b

if  c_2
    puts "O JOGO DUROU #{24 - (a - b)} HORA(S)"
elsif c_3
    puts "O JOGO DUROU #{b - a} HORA(S)"
else
    puts "O JOGO DUROU 24 HORA(S)"
end

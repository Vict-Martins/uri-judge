entrada = gets.strip.split(' ')
h1, m1, h2, m2 = entrada

h1 = h1.to_i
m1 = m1.to_i
h2 = h2.to_i
m2 = m2.to_i

dif = ((h2 * 60)+ m2) - ((h1 * 60) + m1)
if(dif <= 0)
    dif += 24 * 60
end

puts "O JOGO DUROU #{dif/60} HORA(S) E #{dif%60} MINUTO(S)"

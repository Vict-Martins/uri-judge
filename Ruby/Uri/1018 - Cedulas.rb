ENTRADA = gets.to_i
A = ENTRADA/100
A1 = ENTRADA%100
B = A1/50
B1 = A1%50
C = B1/20
C1 = B1%20
D = C1/10
D1 = C1%10
E = D1/5
E1 = D1%5
F = E1/2
F1 = E1%2
G = F1

puts "#{ENTRADA}"
puts "#{A} nota(s) de R$ 100,00"
puts "#{B} nota(s) de R$ 50,00"
puts "#{C} nota(s) de R$ 20,00"
puts "#{D} nota(s) de R$ 10,00"
puts "#{E} nota(s) de R$ 5,00"
puts "#{F} nota(s) de R$ 2,00"
puts "#{G} nota(s) de R$ 1,00"
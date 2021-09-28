Entrada = gets.to_f
resto = Entrada*1000

c_100 = resto/100000
resto %= 100000
c_50 = resto/50000
resto %= 50000
c_20 = resto/20000
resto %= 20000
c_10 = resto/10000
resto %= 10000
c_5 = resto/5000
resto %= 5000
c_2 = resto/2000
resto %= 2000
c_1 = resto/1000
resto %= 1000
m_50 = resto/500
resto %= 500
m_25 = resto/250
resto %= 250
m_10 = resto/100
resto %= 100
m_5 = resto/50
resto %= 50
m_1 = resto/10

puts  "NOTAS:"
puts  "#{c_100.to_i} nota(s) de R$ 100.00"
puts  "#{c_50.to_i} nota(s) de R$ 50.00"
puts  "#{c_20.to_i} nota(s) de R$ 20.00"
puts  "#{c_10.to_i} nota(s) de R$ 10.00"
puts  "#{c_5.to_i} nota(s) de R$ 5.00"
puts  "#{c_2.to_i} nota(s) de R$ 2.00"
puts  "MOEDAS:"
puts  "#{c_1.to_i} moeda(s) de R$ 1.00"
puts  "#{m_50.to_i} moeda(s) de R$ 0.50"
puts  "#{m_25.to_i} moeda(s) de R$ 0.25"
puts  "#{m_10.to_i} moeda(s) de R$ 0.10"
puts  "#{m_5.to_i} moeda(s) de R$ 0.05"
puts  "#{m_1.to_i} moeda(s) de R$ 0.01"
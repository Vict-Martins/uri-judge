ENTRADA = gets.to_i
A = ENTRADA/365
A1 = ENTRADA%365
B = A1/30
B1 = A1%30
C = B1
puts "#{A} ano(s)\n#{B} mes(es)\n#{C} dia(s)"

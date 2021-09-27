X1 = gets.split(' ')
X2 = gets.split(' ')

DISTANCIA = Math.sqrt((X2[0].to_f - X1[0].to_f )**2 + (X2[1].to_f - X1[1].to_f)**2)
puts "#{'%.4f'%DISTANCIA}"
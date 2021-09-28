Entrada = gets.split(' ')
A = Entrada[0].to_f
B = Entrada[1].to_f
C = Entrada[2].to_f
Delta = (B ** 2) - (4 * A * C)

if(Delta < 0 or A <= 0 )
    puts "Impossivel calcular"
else
    R1 = (-B + Math.sqrt(Delta)) / (2*A)
    R2 = (-B - Math.sqrt(Delta)) / (2*A)
    puts "R1 = #{'%.5f'%R1}\nR2 = #{'%.5f'%R2}"
end
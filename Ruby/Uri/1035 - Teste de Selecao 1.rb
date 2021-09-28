Entrada = gets.split(' ')
A = Entrada[0].to_i
B = Entrada[1].to_i
C = Entrada[2].to_i
D = Entrada[3].to_i

if((B > C && D > A ) && (C + D) > (A + B) && (C  > 0 &&  D.to_i > 0) && A%2==0)
    puts "Valores aceitos"
else
    puts "Valores nao aceitos"
end
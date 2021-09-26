A = gets.split(' ')
B = gets.split(' ')
C = A[1].to_i * A[2].to_f + B[1].to_i * B[2].to_f
puts "VALOR A PAGAR: R$ #{'%.2f' % C}"
A = gets.split(' ')
TRIANGULO = A[0].to_f * A[2].to_f/2
CIRCULO = 3.14159 * A[2].to_f ** 2 
TRAPEZIO = (A[0].to_f + A[1].to_f) * A[2].to_f/2
QUADRADO = A[1].to_f ** 2
RETANGULO = A[0].to_f * A[1].to_f
puts "TRIANGULO: #{'%.3f' % TRIANGULO}"
puts "CIRCULO: #{'%.3f' % CIRCULO}"
puts "TRAPEZIO: #{'%.3f' % TRAPEZIO}"
puts "QUADRADO: #{'%.3f' % QUADRADO}"
puts "RETANGULO: #{'%.3f' % RETANGULO}"
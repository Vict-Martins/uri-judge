nome = gets.chomp #gets requer entrada do teclado | chomp ignora a ultima tecla(normalmente é o enter que pula a linha)
idade = gets.chomp.to_i #to_i seta a variável para o tipo int

puts "Olá, Victor?"
puts "victor#{idade} #{nome}"
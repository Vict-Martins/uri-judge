entrada = gets.chomp.to_i
a = 0
b = 0
c = 0
media = 0
entrada.times do |x|
    x =  gets.split(' ')
    a = x[0].to_f
    b = x[1].to_f
    c = x[2].to_f
    media = ((a * 2) + (b * 3) + (c * 5)) / 10
    puts "#{'%.1f'% media}"
end
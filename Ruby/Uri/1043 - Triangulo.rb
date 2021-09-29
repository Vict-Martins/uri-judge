entrada = gets.strip.split(' ')

a, b, c  = entrada

a = a.to_f
b = b.to_f
c = c.to_f

c_1 = (b - c).abs < a && a < (b + c)
c_2 = (a - c).abs < b && b < (a + c)
c_3 = (a - b).abs < c && c < (a + b)

if c_1 || c_2 || c_3
    perimetro = a + b + c
    puts "Perimetro = #{'%.1f'% perimetro}"
else
    area = (a + b) * c / 2.0
    puts "Area = #{'%.1f'% area}"
end
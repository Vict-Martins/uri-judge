entrada = gets.strip.split(' ')

a, b, c = entrada

a = a.to_f
b = b.to_f
c = c.to_f

temp = 0

if a < b
    temp = a
    a = b
    b = temp
end
if b < c
    temp = b
    b = c
    c = temp
end
if a < b
    temp = a
    a = b
    b = temp
end

naoForma = a >= b + c
retangulo = a**2 == b**2 + c**2
obtusangulo = a**2 > b**2 + c**2
acutangulo = a**2 < b**2 + c**2
equilatero = a == b && b == c
isosceles = a == b || b == c || a == c 

if naoForma
    puts "NAO FORMA TRIANGULO"

else

    if retangulo
        puts "TRIANGULO RETANGULO"
    end

    if obtusangulo
        puts "TRIANGULO OBTUSANGULO"
    end

    if acutangulo
        puts "TRIANGULO ACUTANGULO"
    end

    if equilatero
        puts "TRIANGULO EQUILATERO"
    elsif isosceles 
        puts "TRIANGULO ISOSCELES"
    end

end

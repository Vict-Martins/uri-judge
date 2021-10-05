a = 1
b = 1

while a != 0 || b != 0
    
    entrada = gets.strip.split(' ')
    
    a = entrada[0].to_i
    b = entrada[1].to_i

    if a == 0 || b == 0
        break
    elsif a > 0 && b > 0
        puts "primeiro"
    elsif a > 0 && b < 0
        puts "quarto"
    elsif a < 0 && b < 0
        puts "terceiro"
    else
        puts "segundo"
    end
end
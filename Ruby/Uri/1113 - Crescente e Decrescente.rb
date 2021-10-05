flag = 0
while flag == 0 
    
    x = gets.strip.split(' ')
    a = x[0].to_i
    b = x[1].to_i

    if a == b
        break
    elsif a > b
        puts "Decrescente"
    else
        puts "Crescente"
    end
end
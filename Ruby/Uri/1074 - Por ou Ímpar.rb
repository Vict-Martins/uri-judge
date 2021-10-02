entrada = gets.chomp.to_i

entrada.times do |x|
    x = gets.chomp.to_i
    if x == 0
        puts "NULL"
    elsif x > 0
        if x % 2 == 0
            puts "EVEN POSITIVE"
        else
            puts "ODD POSITIVE"
        end
    else
        if x % 2 == 0
            puts "EVEN NEGATIVE"
        else
            puts "ODD NEGATIVE"
        end
    end
end
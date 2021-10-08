alcool = 0
gasolina = 0
diesel = 0

while true
    
    x = gets.to_i
    
    while x > 4
        x = gets.to_i
    end

    if x == 1
        alcool += 1
    elsif x == 2
        gasolina += 1
    elsif x == 3
        diesel += 1
    elsif x == 4
        break
    end

end

puts "MUITO OBRIGADO"
puts "Alcool: #{alcool}"
puts "Gasolina: #{gasolina}"
puts "Diesel: #{diesel}"

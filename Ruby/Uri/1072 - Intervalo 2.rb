entrada = gets.chomp.to_i
c_1 = 0
c_2 = 0

entrada.times do |x|
    x = gets.chomp.to_i
    if x >= 10 && x <= 20
        c_1 += 1
    else
        c_2 += 1
    end
end

puts "#{c_1} in\n#{c_2} out"
a = 0
i = 0
6.times do
    a = gets.to_f
    if a >= 0
        i = i + 1
    end
end
puts "#{i} valores positivos"
entrada = gets.chomp.to_i
i = 1
10000.times do |x|
    if i % entrada == 2
        puts i
    end
i += 1
end
entrada = gets.chomp.to_i
i = 1
while i <= entrada
    if i % 2 == 0
        puts "#{i}^2 = #{i*i}"
    end
i += 1    
end
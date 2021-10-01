par = 0

5.times do |entrada| 
    entrada = gets.to_i
    if entrada %2 == 0
        par += 1
    end
end

puts "#{par} valores pares"
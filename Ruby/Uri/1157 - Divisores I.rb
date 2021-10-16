entrada = gets.to_i

for a in 1..entrada
    if entrada%a == 0 || entrada%a == entrada
        puts a
    end
end
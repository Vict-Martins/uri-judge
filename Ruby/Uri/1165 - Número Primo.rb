entrada = gets.to_i
contador = 0



entrada.times do |num|

    num = gets.to_i

    for a in 1..num

        if num % a == 0
            contador += 1
        end

    end

    if contador == 2
        puts "#{num} eh primo"
    else
        puts "#{num} nao eh primo"
    end
    
    contador = 0

end
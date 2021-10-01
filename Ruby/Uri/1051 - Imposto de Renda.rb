entrada = gets.to_f
aux = 0

if entrada <= 2000.0
    puts "Isento"
end

if entrada > 2000.00
    if(entrada <= 3000)
        aux += (entrada - 2000) * 0.08
        puts "R$ #{'%.2f'%aux}"
    else
        aux += (1000 * 0.08)
    end
    
end

if entrada > 3000.00
    if(entrada <= 4500)
        aux += (entrada - 3000) * 0.18
        puts "R$ #{'%.2f'%aux}"
    else
        aux += (1500 * 0.18)
    end
end

if entrada > 4500
    aux += (entrada - 4500) * 0.28
    puts "R$ #{'%.2f'%aux}"
end
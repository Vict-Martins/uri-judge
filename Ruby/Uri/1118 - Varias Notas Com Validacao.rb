repetir = 0

while repetir != 2
    repetir = 0
    c_1 = 0
    media = 0.0

    while c_1 < 2

        entrada = gets.strip.to_f

        if entrada >= 0.0 && entrada <= 10
            media += entrada
            c_1 += 1
        else
            puts "nota invalida"
        end
end

media /= 2

puts "media = %.2f" % media

    while repetir != 1 && repetir != 2
        puts "novo calculo (1-sim 2-nao)"
        repetir = gets.strip.to_i
    end
end

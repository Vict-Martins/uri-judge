entrada = gets.split(' ')
c_1 = entrada[0].to_f
c_2 = entrada[1].to_f

if c_1 == 0 && c_2 == 0
    puts "Origem\n"
elsif c_1 == 0
    puts "Eixo Y\n"
elsif c_2 == 0
    puts "Eixo X\n"
elsif c_1 > 0 && c_2 > 0
    puts "Q1\n"
elsif c_1 < 0 && c_2 > 0
    puts "Q2\n"
elsif c_1 < 0 && c_2 < 0
    puts "Q3\n"
elsif c_1 > 0 && c_2 < 0
    puts "Q4\n"
end
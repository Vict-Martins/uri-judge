entrada = gets.to_i
perfeito = 0
n = 1

entrada.times do |num|

    entrada1 = gets.to_i

    while entrada1 > perfeito

        perfeito = (2 ** ( n - 1 )) * (( 2 ** n ) - 1)
        
        if entrada1 == 1
            puts "#{entrada1} nao eh perfeito"
        elsif perfeito == entrada1
            puts "#{entrada1} eh perfeito"
        elsif perfeito > entrada1
            puts "#{entrada1} nao eh perfeito"
        end

        n += 1 
    
    end
    
    n = 1
    perfeito = 0

end
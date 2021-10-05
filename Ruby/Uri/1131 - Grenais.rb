flag = 1
grenais = 0
inter = 0
gremio = 0
empates = 0

while flag != 2
    
    entrada = gets.strip.split(' ')
    
    a = entrada[0].to_i
    b = entrada[1].to_i

    if a == b
        empates += 1
    elsif a > b
        inter += 1
    else
        gremio += 1
    end

    grenais += 1

    puts "Novo grenal (1-sim 2-nao)"
    
    flag = gets.to_i
    
    if flag == 2
        break
    end

end

puts "#{grenais} grenais"
puts "Inter:#{inter}"
puts "Gremio:#{gremio}"
puts "Empates:#{empates}"
if inter > gremio
    puts "Inter venceu mais"
elsif gremio > inter
    puts "Gremio venceu mais"
else
    puts "Nao houve vencendor"
end
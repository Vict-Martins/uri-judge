vet = []

for a in 0..19
    vet << gets.to_i
end

aux = 0

for i in 1..10
    aux = vet[i-1]
    vet[i-1] = vet[vet.length-i]
    vet[vet.length-i] = aux
end


for x in 0..19
    puts "N[#{x}] = #{vet[x]}"
end
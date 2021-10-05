i = gets.chomp.to_i

i.times do |x|
    x = gets.strip.split(' ')
    maior = x[0].to_i
    menor = x[1].to_i

    if (menor > maior)
        aux = maior
        maior = menor
        menor = aux
    end

    aux = menor + 1
    soma = 0

    while aux < maior
        if aux % 2 != 0
            soma += aux
        end
    aux += 1
    end

    puts soma
end
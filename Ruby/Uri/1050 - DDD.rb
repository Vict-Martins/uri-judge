entrada = gets.to_i
hash = {'Brasilia': 61, 'Salvador': 71, 'Sao Paulo': 11, 'Rio de Janeiro': 21, 'Juiz de Fora': 32, 'Campinas': 19, 'Vitoria': 27, 'Belo Horizonte': 31}

if hash.has_value?(entrada)
    hash.each {|x,y|
        if y == entrada
            puts "#{x}"
        end
    }
else
    puts "DDD nao cadastrado"
end
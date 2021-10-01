entrada = gets.to_i
hash = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

if hash.has_value?(entrada)
    hash.each {|x,y|
        if y == entrada
            puts "#{x}"
        end
    }
end
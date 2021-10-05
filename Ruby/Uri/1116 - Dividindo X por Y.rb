entradas = gets.to_i

entradas.times do |x|
    x = gets.strip.split(' ')
    a = x[0].to_f
    b = x[1].to_f

    if b == 0
        puts "divisao impossivel"
    elsif a == 0
        puts "#{'%.1f'% a}"
    else
        puts "#{a/b}"
    end
end
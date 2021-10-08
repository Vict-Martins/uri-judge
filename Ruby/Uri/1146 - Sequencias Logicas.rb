
while true

    entrada = gets.to_i
    if entrada == 0
        break
    end
    for a in 1..entrada
        if a == entrada
            print "#{a}\n"
        else
            print "#{a} "
        end
        a += 1
    end     
  
end
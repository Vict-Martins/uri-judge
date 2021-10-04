i = 1
j = 7
c_1 = 1

for a in 0..14 do

    puts "I=#{i} J=#{j}"
    
    if c_1 == 3
        c_1 = 0
        i += 2
        j = 8
    end
c_1 += 1
j -= 1
end
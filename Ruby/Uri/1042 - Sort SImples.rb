entrada = gets.split(' ')
v_1 = entrada[0].to_i
v_2 = entrada[1].to_i
v_3 = entrada[2].to_i
temp = 0

if v_1 > v_2
    temp = v_1
    v_1 = v_2
    v_2 = temp
end
if v_2 > v_3
    temp = v_2
    v_2 = v_3
    v_3 = temp
end
if v_1 > v_2
    temp = v_1
    v_1 = v_2
    v_2 = temp
end
puts v_1
puts v_2
puts v_3
puts ""
puts entrada



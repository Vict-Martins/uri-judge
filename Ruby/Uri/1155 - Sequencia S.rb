s = s.to_f

1.upto(100) do |num|
    
    s += 1 / (1.0 * num)

end

puts "#{'%.2f'%s}"
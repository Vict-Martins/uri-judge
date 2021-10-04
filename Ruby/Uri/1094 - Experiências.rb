entrada = gets.to_i
coelhos = 0
ratos = 0
sapos = 0
total = 0

entrada.times do |x|
    x = gets.strip.split(' ')
    aux = x[0].to_i
    if x[1] == 'C'
        coelhos += aux
        total += aux
    elsif x[1] == 'R'
        ratos += aux
        total += aux
    else
        sapos += aux
        total += aux
    end
end

per_c = (coelhos.to_f/total.to_f)*100.0
per_r = (ratos.to_f/total.to_f)*100.0
per_s = (sapos.to_f/total.to_f)*100.0

puts "Total: #{total} cobaias"
puts "Total de coelhos: #{coelhos}"
puts "Total de ratos: #{ratos}"
puts "Total de sapos: #{sapos}"
puts "Percentual de coelhos: #{'%.2f'% per_c} %"
puts "Percentual de ratos: #{'%.2f'% per_r} %"
puts "Percentual de sapos: #{'%.2f'% per_s} %"
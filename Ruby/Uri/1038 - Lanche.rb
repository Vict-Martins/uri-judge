Entrada = gets.split(' ')
Item = Entrada[0].to_f
Quantidade = Entrada[1].to_f

case Item
when 1
    puts "Total: R$ #{'%.2f'%(4.00*Quantidade)}"
when 2
    puts "Total: R$ #{'%.2f'%(4.50*Quantidade)}"
when 3
    puts "Total: R$ #{'%.2f'%(5.00*Quantidade)}"
when 4
    puts "Total: R$ #{'%.2f'%(2.00*Quantidade)}"
when 5
    puts "Total: R$ #{'%.2f'%(1.50*Quantidade)}"
end
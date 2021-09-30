e = gets.to_f

c_1 = e >= 0 && e <= 400.00
c_2 = e > 400.00 && e <= 800.00
c_3 = e > 800 && e <= 1200.00
c_4 = e > 1200 && e <= 2000.00
c_5 = e > 2000
diferrence = 0
aux = 0

case c_1 || c_2 || c_3 || c_4 || c_5
    when c_1
        aux = e
        e *= 1.15
        aux = e - aux
        puts "Novo salario: #{'%.2f'% e}\nReajuste ganho: #{'%.2f'% aux}\nEm percentual: 15 %"
    when c_2
        aux = e
        e *= 1.12
        aux = e - aux
        puts "Novo salario: #{'%.2f'% e}\nReajuste ganho: #{'%.2f'% aux}\nEm percentual: 12 %"
    when c_3
        aux = e
        e *= 1.10
        aux = e - aux
        puts "Novo salario: #{'%.2f'% e}\nReajuste ganho: #{'%.2f'% aux}\nEm percentual: 10 %"
    when c_4
        aux = e
        e *= 1.07
        aux = e - aux
        puts "Novo salario: #{'%.2f'% e}\nReajuste ganho: #{'%.2f'% aux}\nEm percentual: 7 %"
    when c_5
        aux = e
        e *= 1.04
        aux = e - aux
        puts "Novo salario: #{'%.2f'% e}\nReajuste ganho: #{'%.2f'% aux}\nEm percentual: 4 %"
    end
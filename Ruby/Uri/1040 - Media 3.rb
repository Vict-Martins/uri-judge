entrada =  gets.split(' ')
a = entrada[0].to_f
b = entrada[1].to_f
c = entrada[2].to_f
d = entrada[3].to_f

media = ((a * 2) + (b * 3) + (c * 4) + d) / 10.0

if media >= 7.0
    puts "Media: #{'%.1f' % media}\nAluno aprovado."
elsif media < 5.0
    puts "Media: #{'%.1f' % media}\nAluno reprovado."
elsif media >= 5.0
    puts "Media: #{'%.1f'% media}\nAluno em exame."
    exame = gets.to_f
    puts "Nota do exame: #{'%.1f'% exame}"
    media = (exame + media) / 2
    puts media > 5 ? "Aluno aprovado.\nMedia final: #{'%.1f' % media}": "Aluno reprovado.\nMedia final: #{'%.1f' % media}"
end
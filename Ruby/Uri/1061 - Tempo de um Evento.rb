entrada = gets.strip.split(" ")
tempo_incial = gets.strip.split(' : ')

dia_incial = entrada[1]
horas_inicial, minutos_inicial, segundos_inicial = tempo_incial

entrada = gets.strip.split(' ')
tempo_final = gets.strip.split(' : ')

dia_final = entrada[1]
horas_final, minutos_final, segundos_final = tempo_final

dia_incial = dia_incial.to_i
horas_inicial = horas_inicial.to_i
minutos_inicial = minutos_inicial.to_i
segundos_inicial = segundos_inicial.to_i

dia_final = dia_final.to_i
horas_final = horas_final.to_i
minutos_final = minutos_final.to_i
segundos_final = segundos_final.to_i

contagem_total = (dia_final*86400 + horas_final*3600 + minutos_final*60 + segundos_final) - (dia_incial*86400 + horas_inicial*3600 + minutos_inicial*60 + segundos_inicial);
contagem_dia = contagem_total/86400
contagem_hora = (contagem_total%86400)/3600
contagem_minutos = ((contagem_total%86400)%3600/60)
contagem_segundos = (((contagem_total%86400)%3600)%60)

puts "#{contagem_dia} dia(s)\n#{contagem_hora} hora(s)\n#{contagem_minutos} minuto(s)\n#{contagem_segundos} segundo(s)"
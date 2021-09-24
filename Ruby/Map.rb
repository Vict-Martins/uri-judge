nomes = ["victor", "jose", "gonçalves", "martins"]

#percore a lista e copia o conteúdo
nomes_completos = nomes.map do |nome_completo|
    nome_completo + gets.chomp
end

puts nomes_completos
hash = {nome: "victor", idade: 35} #cria hash e atribue duas chaves
hash[:altura] = 1.73 # adiciona a chave altura a hash
hash.delete(:altura) # deleta a chave autura da hash
puts hash.has_value?("victor")
puts hash.has_value?(:nome)
puts hash.keys # retorna as chaves do hash
puts hash.values # retorna os valores do hash
puts hash.size # retorna o tamanho do hash
#puts hash.clear # limpa a hash
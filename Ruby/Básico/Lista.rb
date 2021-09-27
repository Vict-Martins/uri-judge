lista = []
lista.push("Victor", "José")
lista << "Gonçalves"#insere na lista
lista.insert(0,"viktor")#insere no indice 0 & "empurrando o anteior para o próximo valor"
lista[0] = "Vitor"#substitui o indice 0
lista.delete("Vitor")
puts lista.length#contagem de elementos da lista
puts lista.sort#organiza em ordem alfabética
puts lista.sort.first#retorna o primeiro nome da lista
puts lista.sort.last#retorna o ultimo nome da lista
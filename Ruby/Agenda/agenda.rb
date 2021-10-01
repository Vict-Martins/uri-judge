#instancia de variável
@agenda = [
    {nome: 'Diego', telefone: '9999'},
    {nome: 'Fulano', telefone: '8888'}
]

def todosContatos
    @agenda.each do |contato|
        puts "#{contato[:nome]} - #{contato[:telefone]}"
    end
    puts "-----------------------------------------"
end

def adicionarContato
    print "Nome: "
    nome = gets.chomp
    print "Nome: "
    telefone = gets.chomp

    @agenda << {nome: nome, telefone: telefone}
end

def verContato
    print "Qual nome você deseja: "
    nome = gets.chomp
    @agenda.each do |contato|
        if contato[:nome].downcase.include?(nome.downcase)
            puts "#{contato[:nome]} #{contato[:telefone]}"
        end
        puts "-----------------------------------------"
    end
end

def editaContato
    print "Qual nome deseja editar: "
    nome = gets.chomp

    @agenda.each do |contato|
        if contato[:nome].downcase == nome.downcase
            print "Nome para editar: "
            nome_salvo = contato[:nome]
            contato[:nome] = gets.chomp
            #A string está vazia
            contato[:nome] = contato[:nome].empty? ? nome_salvo : contato[:nome]
            
            print "telefone para editar: "
            telefone_salvo = contato[:telefone]
            contato[:telefone] = gets.chomp
            #A string está vazia ?
            contato[:telefone] = contato[:telefone].empty? ? telefone_salvo : contato[:telefone]
        end
    end
end

def removerContato
    print "Qual nome deseja remover: "
    nome = gets.chomp
    
    @agenda.each do |contato|
        if contato[:nome].downcase ==  nome.downcase
            indice = @agenda.index(contato)
            @agenda.delete_at(indice)
        end
    end
end

loop do

puts "1. Contatos\n2. Adiciona Contato\n3. Ver Contato\n4. Editar contato\n5. Remover Contato\n0. Sair"
   
    codigo = gets.to_i

    case
    when codigo == 0
        puts "Desconect"
        break
    when codigo == 1
        todosContatos
    when codigo == 2
        adicionarContato
    when codigo == 3
        verContato
    when codigo == 4
        editaContato
    when codigo == 5
        removerContato
    end
end
par = []
impar = []

def print_vetor(titulo, vetor)
    vetor.each_with_index do |item, index|
        puts "#{titulo}[#{index}] = #{item}"
    end
    vetor.clear
end

15.times do 
    number = gets.strip.to_i

    impar = print_vetor('impar', impar) if impar.size == 5
    par = print_vetor('par', par) if par.size == 5

    number % 2 == 0 ? par.push(number) : impar.push(number)
end

print_vetor('impar', impar)
print_vetor('par', par)
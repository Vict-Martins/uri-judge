nomes = ["joão", "maria", "josé", "mateus"]
dict = {nome: "victor", idade: 35, altura: 1.73}

nome = "victor"
nomes.each do |i|
    puts i
end

dict.each do |i,y|
    puts "#{i}: #{y}"
end
puts nome
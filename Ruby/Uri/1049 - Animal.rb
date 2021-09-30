a = gets.strip
b = gets.strip
c = gets.strip

case a
when "vertebrado"

    case b

    when "ave"

        case c

        when "carnivoro"
            puts "aguia"
        
        when "onivoro"
            puts "pomba"

        end

    when "mamifero"

        case c

        when "onivoro"
            puts "homem"
        
        when "herbivoro"
            puts "vaca"
        
        end
        
    end


when "invertebrado"

    case b

    when "inseto"

        case c

        when "hematofago"
            puts "pulga"
        
        when "herbivoro"
            puts "lagarta"

        end

    when "anelideo"

        case c

        when "hematofago"
            puts "sanguessuga"
        
        when "onivoro"
            puts "minhoca"
        
        end
        
    end

end


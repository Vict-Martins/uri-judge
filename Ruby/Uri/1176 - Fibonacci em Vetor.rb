entrada = gets.to_i



def fibonacci(a)
    
    fibo = [0 , 1]
    for x in 0..a-1
    
        fibo[x+2] = fibo[x+1] + fibo[x] 
        
    end

    puts "Fib(#{a}) = #{fibo[a]}"
    
end



entrada.times do |x|

    x = gets.to_i
    result = fibonacci(x)

end

import java.util.Scanner;

public class URI_1002 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        double raio = date.nextDouble();    
        double n = 3.14159;
        double area = n*Math.pow(raio, 2);
        System.out.printf("A=%.4f\n", area);
    }
            
}
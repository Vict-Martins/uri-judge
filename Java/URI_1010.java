import java.util.Scanner;

public class URI_1010 {

    public static void main(String[] args) {

        Scanner date = new Scanner(System.in);
        int code = date.nextInt();
        int quant = date.nextInt();
        double value = date.nextDouble();
        int code1 = date.nextInt();
        int quant1 = date.nextInt();
        double value1= date.nextDouble();
        double result = (quant*value)+(quant1*value1);
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", result );
        
    }
    
}
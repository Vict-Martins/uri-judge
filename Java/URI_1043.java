import java.util.Scanner;

public class URI_1043 {
    

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        Double A, B, C;
        A = date.nextDouble();
        B = date.nextDouble();
        C = date.nextDouble();
        if(A+B>C && A+C>B && B+C>A) {

            System.out.printf( "Perimetro = %.1f\n", (A+B+C) );

        }else {

            System.out.printf( "Area = %.1f\n", (((A+B)*C)/2 ));

        }

    }

}

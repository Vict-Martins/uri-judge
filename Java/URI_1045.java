import java.util.Scanner;

public class URI_1045 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        double A, B, C;
        A = date.nextDouble();
        B = date.nextDouble();
        C = date.nextDouble();
        if(A>=B+C||B>=A+C||C>=A+B){
            System.out.println("NAO FORMA TRIANGULO");
        }
        else if( (C*C) == (A*A)+(B*B) ){
            System.out.println("TRIANGULO RETANGULO");
        }
        else if( (C*C) < (B*B)+(A*A) ){ 
            System.out.println("TRIANGULO ACUTANGULO");
            if(A==B && A==C && B==C){
                System.out.println("TRIANGULO ISOSCELES");
            }
            else if(A==B && A==C){
                System.out.println("TRIANGULO EQUILATERO");
            }
        }
        else if( (C*C) > (B*B)+(A*A) ){
            System.out.println("TRIANGULO OBTUSANGULO");
            if(A==B || A==C || B==C){
                System.out.println("TRIANGULO ISOSCELES");
            }
        }
        if(A==B && A==C && B==C){
            System.out.println("TRIANGULO ISOSCELES");
        }
        else if(A==B && A==C){
            System.out.println("TRIANGULO EQUILATERO");
        }

    }

}
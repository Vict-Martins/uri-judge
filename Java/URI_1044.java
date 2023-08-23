import java.util.Scanner;

public class URI_1044 {
    
    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        Double A, B;
        A = date.nextDouble();
        B = date.nextDouble();
        if(B%A == 0) {
            System.out.println("Sao Multiplos");
        }
        else if(A%B == 0) {
            System.out.println("Sao Multiplos");
        }else{
            System.out.println("Nao sao Multiplos");
        }
    }
}
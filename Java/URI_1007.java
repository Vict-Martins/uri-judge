import java.util.Scanner;

public class URI_1007 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int A = date.nextInt();
        int B = date.nextInt();
        int C = date.nextInt();
        int D = date.nextInt();
        int DIFERENCA = A*B-C*D;
        System.out.println("DIFERENCA = "+DIFERENCA);
    }
    
}

import java.util.Scanner;

public class URI_1046 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int A, B;
        A = date.nextInt();
        B = date.nextInt();
        if(A == B) {
            System.out.println("O JOGO DUROU 24 HORA(S)");
        }else if(B>A){
            System.out.println("O JOGO DUROU " + (B-A) + " HORA(S)");
        }else{
            System.out.println("O JOGO DUROU " + ((24-A)+B) + " HORA(S)");
        }
        
    }
    
}

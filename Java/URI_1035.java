import java.util.Scanner;

public class URI_1035 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int A, B, C, D;
        A = date.nextInt();
        B = date.nextInt();
        C = date.nextInt();
        D = date.nextInt();
        if((B>C&&D>A)&&((C+D)>(A+B))&&(C>0)&&(D>0)&&(A%2==0)){
            System.out.println("Valores aceitos");
        }else{
            System.out.println("Valores nao aceitos");
        }
    }
}

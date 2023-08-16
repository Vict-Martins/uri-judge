import java.util.Scanner;

public class URI_1013 {

        public static void main(String[] args) { 
            Scanner date = new Scanner(System.in);
            int A, B, C, maiorAB;
            A = date.nextInt();
            B = date.nextInt();
            C = date.nextInt();
            maiorAB = (A+B+Math.abs(A-B))/2;
            String mensagem = maiorAB > C ? maiorAB + " eh o maior" : C + " eh o maior";
            System.out.println(mensagem);
            
        }

}

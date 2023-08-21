import java.util.Scanner;

public class URI_1018 {

    public static void main (String[] args) {
        Scanner date = new Scanner(System.in);
        int ent = date.nextInt();
        int n100, n50, n20, n10, n5, n2, n1, aux;
        aux = ent;
        n100 = ent/100;
        ent = ent%100;
        n50 = ent/50;
        ent = ent%50;
        n20 = ent/20;
        ent = ent%20;
        n10 = ent/10;
        ent = ent%10;
        n5 = ent/5;
        ent = ent%5;
        n2 = ent/2;
        ent = ent%2;
        n1 = ent/1;
        ent = ent%1;
        System.out.println(aux);
        System.out.println(n100 + " nota(s) de R$ 100,00");
        System.out.println(n50 + " nota(s) de R$ 50,00");
        System.out.println(n20 + " nota(s) de R$ 20,00");
        System.out.println(n10 + " nota(s) de R$ 10,00");
        System.out.println(n5 + " nota(s) de R$ 5,00");
        System.out.println(n2 + " nota(s) de R$ 2,00");
        System.out.println(n1 + " nota(s) de R$ 1,00");
    }
    
}

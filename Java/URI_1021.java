import java.util.Scanner;

public class URI_1021 {

    public static void main(String[] args) {
        
        Scanner date = new Scanner(System.in);
        double value = date.nextDouble();
        value = value*10000;
        value =  (int)value;
        int n100, n50, n20, n10, n5, n2, m100, m50, m25, m10, m5, m1, aux;
        n100 = (int) (value/1000000);
        aux = (int) (value%1000000);
        n50 = aux/500000;
        aux = aux%500000;
        n20 = aux/200000;
        aux = aux%200000;
        n10 = aux/100000;
        aux = aux%100000;
        n5 = aux/50000;
        aux = aux%50000;
        n2 = aux/20000;
        aux = aux%20000;
        m100 = aux/10000;
        aux = aux%10000;    
        m50 = aux/5000;
        aux = aux%5000;
        m25 = aux/2500;
        aux = aux%2500;
        m10 = aux/1000;
        aux = aux%1000;
        m5 = aux/500;
        aux = aux%500;
        m1 = aux/100;
        aux = aux%100;
        System.out.println("NOTAS:");
        System.out.printf(n100 + " nota(s) de R$ 100.00\n");
        System.out.printf(n50 + " nota(s) de R$ 50.00\n");
        System.out.printf(n20 + " nota(s) de R$ 20.00\n");
        System.out.printf(n10 + " nota(s) de R$ 10.00\n");
        System.out.printf(n5 + " nota(s) de R$ 5.00\n");
        System.out.printf(n2 + " nota(s) de R$ 2.00\n");
        System.out.println("MOEDAS:");  
        System.out.printf(m100 + " moeda(s) de R$ 1.00\n");
        System.out.printf(m50 + " moeda(s) de R$ 0.50\n");
        System.out.printf(m25 + " moeda(s) de R$ 0.25\n");
        System.out.printf(m10 + " moeda(s) de R$ 0.10\n");
        System.out.printf(m5 + " moeda(s) de R$ 0.05\n");
        System.out.printf(m1 + " moeda(s) de R$ 0.01\n");
        }
    }
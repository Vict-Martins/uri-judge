import java.util.Scanner;

public class URI_1020 {

    public static void main(String[] args) {

        Scanner date = new Scanner(System.in);
        int dia, mes, ano, aux;
        aux = date.nextInt();
        ano = aux/365;
        aux = aux%365;
        mes = aux/30;
        aux = aux%30;
        dia = aux;
        System.out.println(ano+ " ano(s)");
        System.out.println(mes+ " mes(es)");
        System.out.println(dia+ " dia(s)");

    }
    
}

import java.util.Scanner;

public class URI_1041 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        double p1, p2;
        p1 = date.nextDouble();
        p2 = date.nextDouble();
        if(p1>0&&p2>0) {
            System.out.println("Q1");
        }
        else if(p1<0&&p2>0) {
            System.out.println("Q2");
        }
        else if(p1<0&&p2<0) {
            System.out.println("Q3");
        }else if(p1>0&&p2<0) {
            System.out.println("Q4");
        }else if(p1==0&&p2!=0){
            System.out.println("Eixo X");
        }else if(p1!=0&&p2==0){
            System.out.println("Eixo Y");
        }
        else {
            System.out.println("Origem");
        }
    }

}
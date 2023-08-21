import java.util.Scanner;

public class URI_1036 {

public static void main(String[] args) {
    Scanner date = new Scanner(System.in);
    double A, B, C, delta, x1, x2;
    A = date.nextDouble();
    B = date.nextDouble();
    C = date.nextDouble();
    delta = 0;
    delta = (Math.pow(B, 2))-4*A*C;
    if(delta>0&&A>0){
        x1=(-B+Math.sqrt(delta))/(2*A);
        x2=(-B-Math.sqrt(delta))/(2*A);
        System.out.printf("R1 = %.5f\n", x1);
        System.out.printf("R2 = %.5f\n", x2);
    }else{
        System.out.println("Impossivel calcular");
    }
}
}

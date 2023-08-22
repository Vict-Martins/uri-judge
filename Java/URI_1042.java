import java.util.Arrays;
import java.util.Scanner;

public class URI_1042 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int A, B, C;
        A = date.nextInt();
        B = date.nextInt();
        C = date.nextInt();
        int[] array = {A, B, C};
        Arrays.sort(array);
        int menor, medio, maior;
        menor = array[0];
        medio = array[1];
        maior = array[2];
        System.out.println(menor);
        System.out.println(medio);
        System.out.println(maior);
        System.out.println();
        System.out.println(A);
        System.out.println(B);
        System.out.println(C);

    }

}

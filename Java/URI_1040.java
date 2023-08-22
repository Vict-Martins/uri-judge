import java.text.DecimalFormat;
import java.util.Scanner;

public class URI_1040 {
    
    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        Double n1, n2, n3, n4, nf, md;
        n1 = date.nextDouble();
        n2 = date.nextDouble();
        n3 = date.nextDouble();
        n4 = date.nextDouble();
        md = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10;
        if(md >= 7.0) {
            System.out.printf("Media: %.1f\n",md);
            System.out.println("Aluno aprovado.");
        }else if(md < 5) {
            DecimalFormat df = new DecimalFormat("#.0");
            System.out.println("Media: " + df.format(md));
            System.out.println("Aluno reprovado.");
        }
        else if(md >= 5 && md <= 7.0) {
            nf = date.nextDouble();
            System.out.printf("Media: %.1f\n",md);
            System.out.println("Aluno em exame.");
            System.out.printf("Nota do exame: %.1f\n", nf);
            if(nf >= 5) {
                System.out.println("Aluno aprovado.");
                System.out.printf("Media final: %.1f\n", (md+nf)/2);
            }else if(nf < 5) {
                System.out.println("Aluno reprovado.");
                System.out.printf("Media final: %.1f\n", (md+nf)/2);
            }
            
        }

    }

}
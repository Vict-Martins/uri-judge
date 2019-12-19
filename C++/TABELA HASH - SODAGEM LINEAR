/*TABELA HASH SONDAGEM LINEAR-
HASH TABLE LINEAR SURVEY
GIT HUB*/


#include <stdio.h>
#include <stdlib.h>
#define max 100000

int insere(int vetor[],int valor, int tamanho){
    int i,colide = 0;
    for(i = 0; i<tamanho;i++){
        if(vetor[(valor%tamanho+i)%tamanho] == -1){
            vetor[(valor%tamanho+i)%tamanho] = valor;
            colide = i;
            break;
        }
    }
    return colide;
}
int mostrar(int vetor[],int tamanho){
    int i;
    printf("A TABELA \n----------------------------\n");
    for(i = 0; i < tamanho; i++){
        printf("[%d] = %d\n",i,vetor[i]);
    }
    printf("\n----------------------------\n");
}
int iniciar(int vetor[],int tamanho){
    int i;
    for(i = 0; i < tamanho;i++){
        vetor[i] = -1;
    }
}
int remover(int vetor[], int valor,int tamanho){
    int i;
    for(i = 0; i < tamanho;i++){
        if(vetor[(valor%tamanho+i)%tamanho] == valor){
            vetor[(valor%tamanho+i)%tamanho] = -1;
        }
        else if((vetor[(valor%tamanho+i)%tamanho] != valor) && i == tamanho-1){
            system("clear");
            printf("\n\n-----ELEMENTO NAO EXISTE!!!-----\n\n");
            break;
        }
    }
}

main(){

int vet[max], tam, cont, vinsere, ncolide;



printf("Digite o tamanho da tabela, considerando valores inteiros positivos: \n");
scanf("%d",&tam);
iniciar(vet,tam);
system("clear");

printf("Olá,\nDigite 1 para inserir\nDigite 2 para remover\nDigite 3 para mostrar tabela\nDigite 0 para sair\n-->");
scanf("%d",&cont);


do{
        switch(cont)
        {
            case 1:
                printf("\n\nDigite o valor a ser inserido:\n\n");
                scanf("%d",&vinsere);
                system("clear");
                ncolide += insere(vet, vinsere, tam);
                mostrar(vet,tam);
                printf("Numero de colisoes: %d\n",ncolide);
                printf("----------------------------\n");
                printf("Olá,\nDigite 1 para inserir\nDigite 2 para remover\nDigite 3 para mostrar tabela\nDigite 0 para sair\n-->");
                scanf("%d",&cont);
                break;
            case 2:
                printf("\n\nDigite o valor a ser removido:\n\n");
                scanf("%d",&vinsere);
                remover(vet, vinsere, tam);
                mostrar(vet,tam);
                printf("Olá,\nDigite 1 para inserir\nDigite 2 para remover\nDigite 3 para mostrar tabela\nDigite 0 para sair\n-->");
                scanf("%d",&cont);
                break;
            case 3:
                printf("\n\nMostrar Tabela:\n\n");
                system("clear");
                mostrar(vet,tam);
                printf("Olá,\nDigite 1 para inserir\nDigite 2 para remover\nDigite 3 para mostrar tabela\nDigite 0 para sair\n-->");
                scanf("%d",&cont);
                break;
            case 0:
                printf("\n\n----EXIT----\n\n");
                break;
            default:
                printf("Valor inválido, digite novamente:\n");
                system("pause");
                system("clear");
                printf("Olá,\nDigite 1 para inserir\nDigite 2 para remover\nDigite 3 para mostrar tabela\nDigite 0 para sair\n-->");
                scanf("%d",&cont);
        }
}while(cont != 0);


    
}


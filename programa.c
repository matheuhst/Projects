# include <stdio.h>
# include <locale.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
    char nome[100];
    float salario;
    printf("Qual seu nome? ");
    scanf("%s", &nome);
    printf("Quanto voc� ganha? ");
    scanf("%f", &salario);

    if (salario <= 1520){
        printf("%s tem depress�o.", nome);
    } else if ((salario > 1520) && (salario <= 3500)){
        printf("%s tenta se virar com o que d�, pra sobreviver", nome);
    } else{
        printf("%s consegue ser feliz em meio a tanto caos.", nome);
    }
}

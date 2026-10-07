#include <stdio.h>

int main() {
    float numero1, numero2, suma;

    // Solicitar los dos números al usuario
    printf("Ingrese el primer numero: ");
    scanf("%f", &numero1);

    printf("Ingrese el segundo numero: ");
    scanf("%f", &numero2);

    // Realizar la suma
    suma = numero1 + numero2;

    // Mostrar el resultado (con un máximo de 2 decimales)
    printf("La suma es: %.2f\n", suma);

    return 0;
}

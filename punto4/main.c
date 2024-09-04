#include <stdio.h>
#include <time.h>

int main() {
    long long int suma = 0;
    long long int N = 100000000; 


    clock_t inicio = clock();

    for (long long int i = 1; i <= N; i++) {
        suma += i;
    }

    clock_t fin = clock();
    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("Suma en C: %lld\n", suma);
    printf("Tiempo de ejecución en C: %f segundos\n", tiempo);

    return 0;
}

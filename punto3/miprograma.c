#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s <archivo> <palabra_clave>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("No se pudo abrir el archivo %s\n", argv[1]);
        return 1;
    }

    char *palabra_clave = argv[2];
    char linea[1024];
    int contador = 0;

    while (fgets(linea, sizeof(linea), file)) {
        char *posicion = linea;

        while ((posicion = strstr(posicion, palabra_clave)) != NULL) {
            contador++;
            posicion += strlen(palabra_clave);
        }
    }

    fclose(file);
    
    printf("'%s' se repite %d veces en el texto.\n", palabra_clave, contador);
    return 0;
}

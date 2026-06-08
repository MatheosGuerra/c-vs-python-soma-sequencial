#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Lê o pico de memória (VmPeak) do processo atual em KB
long get_memory_kb() {
    FILE *f = fopen("/proc/self/status", "r");
    char line[128];
    long mem = 0;
    while (fgets(line, sizeof(line), f)) {
        if (sscanf(line, "VmRSS: %ld kB", &mem) == 1) break;
    }
    fclose(f);
    return mem;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Uso: ./soma <N>\n");
        return 1;
    }

    long long n = atoll(argv[1]);

    // Medição de tempo
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // Soma sequencial de 0 até N-1
    long long resultado = 0;
    for (long long i = 0; i < n; i++) {
        resultado += i;
    }

    clock_gettime(CLOCK_MONOTONIC, &end);

    double tempo = (end.tv_sec - start.tv_sec) +
                   (end.tv_nsec - start.tv_nsec) / 1e9;

    long mem_kb = get_memory_kb();
    double mem_mb = mem_kb / 1024.0;

    printf("%.6f %.3f\n", tempo, mem_mb);

    return 0;
}

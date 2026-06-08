import sys
import time
import resource

def soma_sequencial(n):
    resultado = sum(range(n))
    return resultado

if __name__ == "__main__":
    n = int(sys.argv[1])

    start = time.perf_counter()
    resultado = soma_sequencial(n)
    end = time.perf_counter()

    tempo = end - start
    mem_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    mem_mb = mem_kb / 1024.0

    print(f"{tempo:.6f} {mem_mb:.3f}")

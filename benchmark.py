#!/usr/bin/env python3
import subprocess
import statistics
import json

TAMANHOS = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
REPETICOES = 11 

resultados = {"C": {}, "Python": {}}

print("=" * 60)
print("BENCHMARK: Soma Sequencial — C vs Python")
print("Protocolo: 11 execuções por ponto, descarte do warm-up")
print("=" * 60)

for n in TAMANHOS:
    tempos_c, mems_c = [], []
    tempos_py, mems_py = [], []

    for i in range(REPETICOES):
        r = subprocess.run(["./soma", str(n)], capture_output=True, text=True)
        t, m = map(float, r.stdout.strip().split())
        if i > 0:  # descarta warm-up (i=0)
            tempos_c.append(t)
            mems_c.append(m)

        r = subprocess.run(["python3", "soma.py", str(n)], capture_output=True, text=True)
        t, m = map(float, r.stdout.strip().split())
        if i > 0:
            tempos_py.append(t)
            mems_py.append(m)

    tc = statistics.mean(tempos_c)
    tp = statistics.mean(tempos_py)
    dp_c = statistics.stdev(tempos_c)
    dp_py = statistics.stdev(tempos_py)
    mc = statistics.mean(mems_c)
    mp = statistics.mean(mems_py)
    razao = tp / tc if tc > 0 else float('inf')

    resultados["C"][str(n)] = {
        "tempo_medio": tc,
        "tempo_desvio": dp_c,
        "memoria_media": mc
    }
    resultados["Python"][str(n)] = {
        "tempo_medio": tp,
        "tempo_desvio": dp_py,
        "memoria_media": mp
    }

    print(f"\nn = {n:>12,}")
    print(f"  C      → tempo: {tc:.6f} ± {dp_c:.6f}s | mem: {mc:.1f} MB")
    print(f"  Python → tempo: {tp:.6f} ± {dp_py:.6f}s | mem: {mp:.1f} MB")
    print(f"  Python é {razao:.1f}x mais lento que C")

with open("resultados.json", "w") as f:
    json.dump(resultados, f, indent=2)

print("\n" + "=" * 60)
print("Resultados salvos em resultados.json")
print("=" * 60)

#!/usr/bin/env python3
import subprocess
import statistics
import json

TAMANHOS = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
REPETICOES = 5

resultados = {"C": {}, "Python": {}}

print("=" * 60)
print("BENCHMARK: Soma Sequencial — C vs Python")
print("=" * 60)

for n in TAMANHOS:
    tempos_c, mems_c = [], []
    tempos_py, mems_py = [], []

    for _ in range(REPETICOES):
        r = subprocess.run(["./soma", str(n)], capture_output=True, text=True)
        t, m = map(float, r.stdout.strip().split())
        tempos_c.append(t)
        mems_c.append(m)

        r = subprocess.run(["python3", "soma.py", str(n)], capture_output=True, text=True)
        t, m = map(float, r.stdout.strip().split())
        tempos_py.append(t)
        mems_py.append(m)

    tc = statistics.mean(tempos_c)
    tp = statistics.mean(tempos_py)
    mc = statistics.mean(mems_c)
    mp = statistics.mean(mems_py)

    resultados["C"][str(n)] = {
        "tempo_medio": tc,
        "tempo_desvio": statistics.stdev(tempos_c),
        "memoria_media": mc
    }
    resultados["Python"][str(n)] = {
        "tempo_medio": tp,
        "tempo_desvio": statistics.stdev(tempos_py),
        "memoria_media": mp
    }

    razao = tp / tc if tc > 0 else float('inf')
    print(f"\nn = {n:>12,}")
    print(f"  C      → tempo: {tc:.6f}s | mem: {mc:.1f} MB")
    print(f"  Python → tempo: {tp:.6f}s | mem: {mp:.1f} MB")
    print(f"  Python é {razao:.1f}x mais lento que C")

with open("resultados.json", "w") as f:
    json.dump(resultados, f, indent=2)

print("\n" + "=" * 60)
print("Resultados salvos em resultados.json")
print("=" * 60)

# Análise Comparativa de Desempenho entre C e Python na Execução de Soma Sequencial

Repositório do artigo científico submetido ao **SSCAD-WIC 2026** (Workshop de Iniciação Científica — XXVII Simpósio em Sistemas Computacionais de Alto Desempenho).

## Autores

- Matheos de Oliveira Guerra — matheos.guerra@cesar.school
- Eduardo Roma Cavalcanti de Albuquerque — erca@cesar.school
- Bernardo Carneiro Heuer Guimarães — bchg@cesar.school

**Instituição:** CESAR School — Recife, PE, Brasil

## Resumo

Este trabalho apresenta uma comparação empírica de desempenho entre as linguagens C e Python na execução de soma sequencial, utilizando o idioma nativo de cada linguagem: `sum(range(n))` em Python e laço `for` explícito em C. Foram medidos tempo de execução e uso de memória para valores de N entre 10.000 e 100.000.000 em um ambiente virtualizado (KVM) com processador Intel Xeon a 2,20 GHz, com 10 repetições por configuração após descarte de warm-up.

**Resultado principal:** C é aproximadamente **5,4x mais rápido** e usa **7,8x menos memória** que Python.

## Ambiente Experimental

- **Processador:** Intel Xeon @ 2,20 GHz (KVM)
- **Sistema Operacional:** Ubuntu 24.04.4 LTS
- **Compilador C:** GCC 13.3.0 (flag `-O0`)
- **Python:** CPython 3.12.3

## Estrutura do Repositório

```
.
├── soma.c              # Implementação da soma sequencial em C
├── soma.py             # Implementação da soma sequencial em Python
├── benchmark.py        # Script de benchmark (10 repetições + warm-up)
├── resultados.json     # Dados coletados nos experimentos
└── comparacao_c_vs_python.png  # Gráfico comparativo
```

## Como Reproduzir os Experimentos

**Compilar o código C:**
```bash
gcc -O0 -o soma soma.c
```

**Rodar o benchmark:**
```bash
python3 benchmark.py
```

Os resultados serão salvos em `resultados.json`.

## Resultados

| N | C (s) | Python (s) | Razão (Py/C) |
|---|---|---|---|
| 10.000 | 0,000025 ± 0,000002 | 0,000136 ± 0,000014 | 5,3x |
| 100.000 | 0,000387 ± 0,000276 | 0,002249 ± 0,000941 | 5,8x |
| 1.000.000 | 0,002615 ± 0,000089 | 0,014438 ± 0,000832 | 5,5x |
| 10.000.000 | 0,025910 ± 0,000206 | 0,137712 ± 0,003237 | 5,3x |
| 100.000.000 | 0,256632 ± 0,003122 | 1,373432 ± 0,035074 | 5,4x |

> **Nota metodológica:** cada linguagem foi avaliada usando seu idioma nativo. O `sum(range(n))` do Python executa internamente em C (builtin otimizado do CPython), enquanto o código C usa laço explícito com `-O0`. Essa assimetria é discutida como ameaça à validade no artigo.

## Evento

**SSCAD-WIC 2026** — Workshop de Iniciação Científica
XXVII Simpósio em Sistemas Computacionais de Alto Desempenho
3 a 5 de novembro de 2026 — Natal, RN, Brasil
https://sscad2026.imd.ufrn.br

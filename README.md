# Análise Comparativa de Desempenho entre C e Python na Execução de Soma Sequencial

Repositório do artigo científico submetido ao **SSCAD-WIC 2026** (Workshop de Iniciação Científica - XXVII Simpósio em Sistemas Computacionais de Alto Desempenho).

## Autores

- Matheos de Oliveira Guerra - matheos.guerra@cesar.school
- Eduardo Roma Cavalcanti de Albuquerque - erca@cesar.school
- Bernardo Carneiro Heuer Guimarães - bchg@cesar.school

**Instituição:** CESAR School - Recife, PE, Brasil

## Resumo

Este trabalho apresenta uma comparação empírica de desempenho entre as linguagens C e Python na execução de soma sequencial (soma dos inteiros de 0 a N). Foram medidos tempo de execução e uso de memória para valores de N entre 10.000 e 100.000.000 em um ambiente virtualizado (KVM) com processador Intel Xeon a 2,20 GHz.

**Resultado principal:** C é aproximadamente **4,6x mais rápido** e usa **7,7x menos memória** que Python.

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
├── benchmark.py        # Script de benchmark (roda os experimentos)
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

Os resultados serão salvos em `resultados.json` e o gráfico gerado automaticamente.

## Resultados

| N | Tempo C (s) | Tempo Python (s) | Razão (Py/C) |
|---|---|---|---|
| 10.000 | 0,000025 | 0,000141 | 5,5x |
| 100.000 | 0,000267 | 0,001265 | 4,7x |
| 1.000.000 | 0,002769 | 0,012765 | 4,6x |
| 10.000.000 | 0,028745 | 0,124838 | 4,3x |
| 100.000.000 | 0,270826 | 1,253129 | 4,6x |

## Evento

**SSCAD-WIC 2026** - Workshop de Iniciação Científica  
XXVII Simpósio em Sistemas Computacionais de Alto Desempenho  
3 a 5 de novembro de 2026 - Natal, RN, Brasil  
https://sscad2026.imd.ufrn.br

# Perceptron — Treinamento (Atividade)

Este README resume o treinamento registrado em `log_treinamento.txt`. 

---

## Resultados

```

===== CICLO 1 =====
x=[1, 0, 0], y=0 | h=0.00, y_func=0, erro=0, novos pesos=[0.0, 0.0, 0.0]
x=[1, 0, 1], y=0 | h=0.00, y_func=0, erro=0, novos pesos=[0.0, 0.0, 0.0]
x=[1, 1, 0], y=1 | h=0.00, y_func=0, erro=1, novos pesos=[0.1, 0.1, 0.0]
x=[1, 1, 1], y=1 | h=0.20, y_func=1, erro=0, novos pesos=[0.1, 0.1, 0.0]

===== CICLO 2 =====
x=[1, 0, 0], y=0 | h=0.10, y_func=1, erro=-1, novos pesos=[0.0, 0.1, 0.0]
x=[1, 0, 1], y=0 | h=0.00, y_func=0, erro=0, novos pesos=[0.0, 0.1, 0.0]
x=[1, 1, 0], y=1 | h=0.10, y_func=1, erro=0, novos pesos=[0.0, 0.1, 0.0]
x=[1, 1, 1], y=1 | h=0.10, y_func=1, erro=0, novos pesos=[0.0, 0.1, 0.0]

```

---

## Resumo do problema.

- Conjunto de treinamento (X, y):
  - x=[1, 0, 0], y=0
  - x=[1, 0, 1], y=0
  - x=[1, 1, 0], y=1
  - x=[1, 1, 1], y=1


- Inicialização dos pesos: `[0.0, 0.0, 0.0]` (bias + 2 pesos)
- Taxa de aprendizado: `alpha = 0.1` (conforme detalhes do log)
- Número de ciclos executados: 2 (CICLO 1 e CICLO 2)
- Resultados iguais aos calculados na sala de aula.

---
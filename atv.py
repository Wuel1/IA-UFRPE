def predicao(x, w):
    h = sum(w[i] * x[i] for i in range(len(x)))
    y_func = 1 if h > 0 else 0
    return h, y_func


def atualiza_peso(x, y_verdadeiro, w, alpha):
    h, y_func = predicao(x, w)
    erro = y_verdadeiro - y_func

    for i in range(len(w)):
        w[i] = w[i] + alpha * erro * x[i]

    return w, h, y_func, erro


def treinar():
    dados = [
        ([1, 0, 0], 0),  # Joãozinho
        ([1, 0, 1], 0),  # Zequinho
        ([1, 1, 0], 1),  # Zezinho
        ([1, 1, 1], 1),  # Luizinho
    ]

    w = [0.0, 0.0, 0.0]
    alpha = 0.1

    logs = []

    for ciclo in range(2):
        print(f"\n===== CICLO {ciclo+1} =====")
        logs.append(f"\n===== CICLO {ciclo+1} =====")

        for x, y in dados:
            w, h, y_func, erro = atualiza_peso(x, y, w, alpha)

            linha = (
                f"x={x}, y={y} | h={h:.2f}, y_func={y_func}, "
                f"erro={erro}, novos pesos={w}"
            )
            print(linha)
            logs.append(linha)

    with open("log_treinamento.txt", "w") as f:
        f.write("\n".join(logs))

    print("\nPesos finais:", w)


if __name__ == "__main__":
    treinar()
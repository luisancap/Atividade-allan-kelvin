estoque_padrao = {}
estoque_atual = []

def alimentar_estoque_padrao():
    i = 1
    while True:
        entrada = input(f"{i} - ").split()
        if len(entrada) != 2 or entrada[0] == "0":
            break

        fruta, quantidade = entrada
        quantidade = int(quantidade)
        estoque_padrao[fruta] = {"quantidade": quantidade}
        i += 1

def alimentar_estoque_atual():
    frutas_nulas = []
    for fruta, _ in estoque_padrao.items():
        quantidade_atual = int(input(f"{fruta}: \n"))
        estoque_atual.append({fruta: quantidade_atual})
        if quantidade_atual == 0:
            frutas_nulas.append(fruta)
    if not frutas_nulas:
        return "NENHUMA"

    return frutas_nulas

def calculo():
    i = 1

    for fruta, dados in estoque_padrao.items():
        quantidade_padrao = dados["quantidade"]
        quantidade_atual = 0

        for item in estoque_atual:
            if fruta in item:
                quantidade_atual = item[fruta]
                break

        if quantidade_atual < quantidade_padrao:
            quantidade_faltante = quantidade_padrao - quantidade_atual
            print(f"{i} – {fruta}: {quantidade_faltante}")
            i += 1
def main():
    print("===== MENU ESTOQUE ARMAZÉM ====\n\n")
    print("ENTRE COM O ESTOQUE PADRAO:\n")
    print("FRUTA/QUANT:")

    alimentar_estoque_padrao()

    print("====== ESTADO DO ESTOQUE ATUAL ===\n\n")
    print("Estoque atual: \n")

    frutas_nulas = alimentar_estoque_atual()

    print("====== RESULTADO ====\n\n")
    print("QUANTIDADE PARA COMPRAR\n")

    calculo()

    print(f"FRUTAS SEM ESTOQUE - {frutas_nulas}")

main()

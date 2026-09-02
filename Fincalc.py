def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros

def calcular_aposentadoria(patrimonio_atual: float, aporte_mensal: float, anos: int, taxa_anual: float) -> float:
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses): 
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo

if __name__ == "___main__":
    print("Iniciando o sistema FinCalc ... ")
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R${patrimonio:.2f}")
def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros

def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante

if __name__ == "__main__":
    print("Iniciando o sistema FinCalc ... ")
    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante:.2f}")
    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}")

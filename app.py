aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência em watts (W): "))
horas_dia = float(input("Digite quantas horas por dia ele é usado: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

print("\nResultado:")
print("Aparelho:", aparelho)
print("Consumo estimado:", consumo_mensal, "kWh/mês")
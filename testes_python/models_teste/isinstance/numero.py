def processar_numero(valor):
    if isinstance(valor, (int, float)):  # Tupla de tipos
        return valor * 2
    else:
        raise TypeError("Esperado número")

print(processar_numero(5))      # 10
print(processar_numero(5.5))    # 11.0
processar_numero("5")         # TypeError
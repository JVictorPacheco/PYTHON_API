class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = 0 # inicial sempre em 0
        self._historico = []
        
        
        
        if saldo_inicial > 0:
            self.depositar(saldo_inicial)
            
            
    @property
    def saldo(self):
        """Retorna o saldo atual (somente leitura)"""
        return self._saldo
    
    
    @property
    def historico(self):
        """Retorna cópia do histórico (não pode ser modificado diretamente)"""
        return self.historico.copy()
    
    
    def depositar(self, valor):
       if valor <= 0:
            raise ValueError("Valor deve ser positivo")
       self._saldo += valor
       self._historico.append(f"Depósito: +R${valor:.2f}")
       
       
       
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= valor
        self._historico.append(f"Saque: -R${valor:.2f}")

        
        
        
# Uso
conta = ContaBancaria("João", 1000)
print(conta.saldo)       # 1000.0 (getter)

# conta.saldo = 5000     # ❌ Erro! Não tem setter
conta.depositar(500)     # ✅ Forma correta
print(conta.saldo)       # 1500.0

# conta.historico.append("hack")  # ❌ Não funciona (é uma cópia)
print(conta._historico)   # Lista do histórico
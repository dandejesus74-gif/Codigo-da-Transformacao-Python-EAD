import unittest

# Classe Calculadora
class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

# Classe de Testes Automatizados para a Calculadora
class TesteCalculadora(unittest.TestCase):
    
    def setUp(self):
        # Instancia a calculadora antes de cada teste
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

if __name__ == "__main__":
    print("Executando Passo 2: Testes da Classe Calculadora")
    unittest.main()
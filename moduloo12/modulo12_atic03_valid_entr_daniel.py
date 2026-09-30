import unittest

class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

class TesteEntradasInvalidas(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero(self):
        # Verifica se o código lança um ValueError ao tentar dividir por zero
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == "__main__":
    print("Executando Passo 3: Validação de Entradas Inválidas (Exceções)")
    unittest.main()
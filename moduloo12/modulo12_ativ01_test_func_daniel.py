import unittest

# Função a ser testada
def somar(a, b):
    return a + b

# Classe de Testes Automatizados
class TesteSoma(unittest.TestCase):
    
    def test_soma_positivos(self):
        resultado = somar(2, 3)
        self.assertEqual(resultado, 5)

    def test_soma_negativos(self):
        resultado = somar(-1, -1)
        self.assertEqual(resultado, -2)

if __name__ == "__main__":
    print("Executando Passo 1: Teste de Soma")
    unittest.main()
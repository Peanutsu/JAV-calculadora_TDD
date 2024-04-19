import unittest
from calculator import Calculator

class Test_calculator(unittest.TestCase, Calculator):
    
    def setUp(self):
        self.calculadora = Calculator()
        
    def test_soma(self):
        self.assertEqual(self.soma(2, 8), 10)
        
    def test_divisao_inteira(self):
        self.assertEqual(self.divisao(10,5,2),2)
    
    def test_divisao_float(self):
        self.assertEqual(self.divisao(1.2,0.1,2),12)
    
    def test_divisao_inteira_sem_precisao(self):
       self.assertEqual(self.divisao(10,5),2)
       
    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.divisao(10,0)
    
        
    
    # testes para o método raiz_quadrada (RQ)
    def teste_rq(self):
        self.assertEqual(self.raiz_quadrada(9), 3)
    
    def test_rqZero(self):
        self.assertEqual(self.raiz_quadrada(0), 0)

    def test_rqValorGrande(self):
        self.assertEqual(self.raiz_quadrada(10000), 100)
    
    def test_rqErrorNegativo(self):
        self.assertRaises(ValueError, self.raiz_quadrada, -9)

    def test_rqErrorString(self):
        self.assertRaises(ValueError, self.raiz_quadrada, "9a")

    # testes para o método fatorial
    def test_fatorial(self):
        self.assertEqual(self.fatorial(5), 120)

    def test_fatorialZero(self):
        self.assertEqual(self.fatorial(0), 1)

    def test_fatorialErrorNegativo(self):
        self.assertRaises(ValueError, self.fatorial, -5)

    def test_fatorialErrorString(self):
        self.assertRaises(ValueError, self.fatorial, "5a")

    # testes para o método resto_divisao
    def test_restoZero(self):
        self.assertEqual(self.resto_divisao(10, 2), 0)

    def test_restoDivisao(self):
        self.assertEqual(self.resto_divisao(10, 3), 1)
    
    def test_restoErrorZero(self):
        self.assertRaises(ZeroDivisionError, self.resto_divisao, 10, 0)

    def test_restoErrorStringA(self):
        self.assertRaises(ValueError, self.resto_divisao, "a", 10)

    def test_restoErrorStringB(self):
        self.assertRaises(ValueError, self.resto_divisao, 10, "b")

    def test_restoErrorStringAB(self):
        self.assertRaises(ValueError, self.resto_divisao, "a", "b")

if __name__ == '__main__':
    unittest.main()
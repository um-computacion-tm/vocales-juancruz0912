import unittest

def contar_vocales(string):
    
    vocales = ('a', 'e', 'i', 'o', 'u')
    acento = {'á': 'a','é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', }
    resultado = {}

    string = string.replace('á', 'a')
    string = string.replace(' ','')
    string = string.lower()

    for i in string:
        if i in acento.keys():
            string = string.replace(i, acento[i])

    for letra in string:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado

class TestContarVocales(unittest.TestCase):
    
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {}) 
    
    def test_contar_a(self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado, {'a':1})
    
    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a':2})

    def test_contar_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual(resultado, {'e':2})

    def test_contar_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a':1, 'e':1})
    
    def test_contar_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a':3, 'o':1})
    
    def test_contar_espacio(self):
        resultado = contar_vocales('ab eceda  rio')
        self.assertEqual(resultado, {'a':2, 'e':2, 'i': 1, 'o':1})

    def test_contar_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual(resultado, {'a':1, 'e':1, 'i': 1, 'o':1, 'u': 1})

    def test_contar_acento(self):
        resultado = contar_vocales('día')
        self.assertEqual(resultado, {'a':1,'i': 1})


unittest.main()

#while(True):
#   palabra = input('Ingrese palabra: ')
#   print(contar_vocales(palabra))
from sympy import * 
from latex2sympy2 import latex2sympy
from sympy import init_printing
init_printing() 
class LatexFormulaHandler:
    formula = ""
    t, l = symbols("t, l")
    def setFormula(self, formula):
        self.formula = formula
    def getIntegral(self):
        return latex(latex2sympy(self.formula).doit())
    


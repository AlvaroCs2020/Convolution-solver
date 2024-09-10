
import os
from openai import OpenAI
import asyncio
from openai import AsyncOpenAI
from SimpyTest import LatexFormulaHandler

class GptHandler:
    def_convolution = " \int_{0}^{t} x(T) \cdot y(t-T) \, dT "
    #default / rampa y escalon unitario!!!
    x = "t" 
    y = "1"
    question = ""
    
    def __init__(self):
      self.client = OpenAI( #Al tener el key aca se puede usar este proyecto sin usar una propia, aunque lo pago yo!!!
        api_key=""
        )
    def setFunctions(self, f1, f2):
       self.x = f1
       self.y = f2
    def setQuestion(self, f1, f2):
        return  """ Dada la definicion de convolucion {convolve} y las funciones, 
                            h1(t) = {x} e h2(t) = {y} en funcion del parametro t
                            necesito que reemplaces estas dos funciones que te di en latex en la formula de convolucion
                            y que me devuelvas el codigo latex de la integral de convolucion a resolver
                            No le agregues nada raro, hace el reemplazo que te estoy pidiendo
                            Y, si podes, encargate de que la integral sea facil de computar NO ARRIESGUES PONER ALGO INCORRECTO
                            repondeme, exclusivamente, el latex resultante sin ninguna igualdad. SOLO LA INTEGRAL A RESOLVER
                            """.format(convolve = self.def_convolution, x = f1, y = f2)
    
    def getResponse(self,f1, f2):
        question = self.setQuestion(f1,f2)
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-4",
        )
        split_ret = chat_completion.choices[0].message.content.split(r'\int_', 1)
        #print(question)
        return "\int_" + split_ret[1]
    
        
#gptHandler = GptHandler()
#
#response = gptHandler.getResponse()
#
#print(response)


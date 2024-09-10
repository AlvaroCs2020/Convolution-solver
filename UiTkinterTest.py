import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from GptApiTest import GptHandler
from SimpyTest import LatexFormulaHandler
#Objetos globales para el proceso de las convoluciones

h1 = "1"
h2 = "t"

gptHandler = GptHandler()

integralHandler = LatexFormulaHandler()

# Función para renderizar LaTeX en una figura
def render_latex(formula):
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, f"${formula}$", fontsize=20, ha='center', va='center')
    ax.set_axis_off()
    return fig

def render_latex_doble(formula1, formula2):
    fig, ax = plt.subplots()
    # Renderizar la primera fórmula
    ax.text(0.5, 0.6, f"${formula1}$", fontsize=20, ha='center', va='center')
    # Renderizar la segunda fórmula
    ax.text(0.5, 0.4, f"${formula2}$", fontsize=20, ha='center', va='center')
    ax.set_axis_off()
    return fig
# Función para actualizar el gráfico en una sección específica
def actualizar_formula1(entry, canvas):
    global h1
    formula = entry.get()  # Obtener la fórmula del input field
    fig = render_latex(formula)
    h1 = formula
    # Limpiar el canvas anterior y dibujar el nuevo gráfico
    canvas.figure = fig
    canvas.draw()

def actualizar_formula2(entry, canvas):
    global h2
    formula = entry.get()  # Obtener la fórmula del input field
    fig = render_latex(formula)
    h2 = formula
    # Limpiar el canvas anterior y dibujar el nuevo gráfico
    canvas.figure = fig
    canvas.draw()

def calcular_convolucion( canvas):
    
    gptHandler.setFunctions(h1,h2)
    formulaIntegral = gptHandler.getResponse(h1,h2) # de aca saco la integral a resolver
    print(h2)
    integralHandler.setFormula(formulaIntegral)
    formulaConvolution = integralHandler.getIntegral()

    fig = render_latex_doble(formulaIntegral, formulaConvolution)
    # Limpiar el canvas anterior y dibujar el nuevo gráfico
    canvas.figure = fig
    canvas.draw()

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Renderizador LaTeX en Tres Secciones")

# Crear un Frame para organizar cada tercio
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

# Empaquetar los Frames en la ventana principal
frame1.pack(side="left", fill="both", expand=True)
frame2.pack(side="left", fill="both", expand=True)
frame3.pack(side="left", fill="both", expand=True)

# Función auxiliar para crear un "tercio" con su campo de entrada, botón y canvas
def crear_seccion1(frame, formula_inicial):
    # Campo de entrada para la fórmula LaTeX
    entry = tk.Entry(frame, width=30)
    entry.pack(pady=10)

    # Botón para actualizar la fórmula
    button = tk.Button(frame, text="Actualizar f1", command=lambda: actualizar_formula1(entry, canvas))
    button.pack(pady=10)

    # Crear una figura inicial vacía
    fig = render_latex(formula_inicial)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    return entry, canvas
def crear_seccion2(frame, formula_inicial):
    # Campo de entrada para la fórmula LaTeX
    entry = tk.Entry(frame, width=30)
    entry.pack(pady=10)

    # Botón para actualizar la fórmula
    button = tk.Button(frame, text="Actualizar f2", command=lambda: actualizar_formula2(entry, canvas))
    button.pack(pady=10)

    # Crear una figura inicial vacía
    fig = render_latex(formula_inicial)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    return entry, canvas

def crear_seccion3(frame, formula_inicial):

    # Botón para actualizar la fórmula
    button = tk.Button(frame, text="Calcular convolucion", command=lambda: calcular_convolucion( canvas))
    button.pack(pady=10)

    # Crear una figura inicial vacía
    fig = render_latex(formula_inicial)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    return canvas

# Crear secciones en cada tercio
crear_seccion1(frame1, h1)
crear_seccion2(frame2, h2)
crear_seccion3(frame3, "f1 * f2")

# Iniciar el bucle principal de la ventana
root.mainloop()

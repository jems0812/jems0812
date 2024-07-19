import turtle
import time
import subprocess  # Para ejecutar comandos del sistema
import os

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#7F1734")  # Color vinotinto

# Configuración de la tortuga
t = turtle.Turtle()
t.speed(0)  # Velocidad máxima de la tortuga
t.hideturtle()  # Ocultar la tortuga

# Directorio donde se guardarán los fotogramas
frame_dir = os.path.join(os.path.dirname(__file__), 'frames/')

# Crear directorio si no existe
try:
    os.makedirs(frame_dir, exist_ok=True)
    print(f"Directorio {frame_dir} creado correctamente.")
except OSError as e:
    print(f"Error al crear el directorio {frame_dir}: {e}")
    exit()

# Contador de fotogramas
frame_count = 0

# Función para capturar un fotograma
def capture_frame():
    global frame_count
    canvas = screen.getcanvas()
    canvas.postscript(file=f"{frame_dir}frame_{frame_count}.ps", colormode='color')
    frame_count += 1

# Función para escribir texto con una tortuga
def escribir_texto_animado(t, texto, color, x, y):
    t.penup()
    t.goto(-screen.window_width() // 2, y)  # Comienza desde el lado izquierdo de la pantalla
    t.pendown()
    t.color(color)
    t.showturtle()
    
    # Moverse a la posición final con efecto de animación
    while t.xcor() < x:
        t.setx(t.xcor() + 10)
        time.sleep(0.02)
        capture_frame()  # Capturar cada fotograma
    
    t.write(texto, align="center", font=("Arial", 24, "bold"))
    t.hideturtle()
    t.penup()
    capture_frame()  # Capturar el fotograma final

# Función para dibujar una estrella
def dibujar_estrella(t, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()
    t.penup()
    capture_frame()  # Capturar el fotograma final de la estrella

# Función para escribir el autor en el pie de página
def escribir_autor(t, texto, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.write(texto, align="center", font=("Arial", 12, "normal"))
    t.penup()
    capture_frame()  # Capturar el fotograma final

# Coordenadas para los textos
coordenadas_texto = [
    ("Mano", "yellow", 0, 60),
    ("tengo", "blue", 0, 0),
    ("FE", "red", 0, -60)
]

# Coordenadas para las estrellas
coordenadas_estrellas = [
    (-90, 150),
    (-60, 170),
    (-30, 180),
    (0, 185),
    (30, 180),
    (60, 170),
    (90, 150),
    (120, 120)
]

# Escribir los textos con animación
for texto, color, x, y in coordenadas_texto:
    escribir_texto_animado(t, texto, color, x, y)
    time.sleep(0.5)  # Espera de 0.5 segundos entre cada palabra

# Dibujar las estrellas
for x, y in coordenadas_estrellas:
    dibujar_estrella(t, "white", x, y)

# Escribir el autor en el pie de página
escribir_autor(t, "Autor: J Montes", "white", 0, -screen.window_height() // 2 + 20)

# Convertir los archivos .ps a .png
try:
    subprocess.run(["mogrify", "-format", "png", f"{frame_dir}*.ps"])
except Exception as e:
    print(f"Error al convertir archivos PS a PNG: {e}")
    exit()

# Combinar las imágenes PNG en un GIF animado usando ImageMagick
try:
    subprocess.run(["convert", "-delay", "50", "-loop", "0", f"{frame_dir}frame_*.png", "animacion.gif"])
except Exception as e:
    print(f"Error al crear el GIF animado: {e}")
    exit()

# Mantener la ventana abierta
screen.mainloop()

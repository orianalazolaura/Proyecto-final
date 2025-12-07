# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC4.py
#  your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.
# Creamos la lista de páginas

paginas = ['🐇Temática', '🐇Personalidad', '🐇Diario de un genio incomprendido']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona aquí para empezar el viaje a este mundo de la filosofía romanticista', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == '🐇Temática':

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Corazones Desbordados: La Rebeldía Emocional del Siglo XIX</h1>", unsafe_allow_html=True)

  # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # En la primera columna colocamos la imagen de perfil
    col1.image("imagen del romanticismo.jpg", caption='arte', width=300)

texto = """
El Romanticismo no fue solo un movimiento artístico y literario que floreció en Europa a finales del siglo XVIII y principios del XIX, sino también una profunda corriente filosófica y cultural que surgió como una reacción directa y a menudo vehemente contra el racionalismo estricto de la Ilustración. Mientras que la Ilustración había exaltado la razón, la objetividad y el análisis científico como el camino principal hacia el conocimiento y el progreso, el Romanticismo se centró en la primacía de la emoción, la subjetividad, la intuición y el sentimiento. Fue una reivindicación del individuo, del mundo interior y de todo aquello que la razón pura no podía abarcar. Tres temas centrales de esta época fueron la naturaleza y el sentimiento, el yo y la subjetividad y lo irracional y lo trascendente. En primer lugar, la naturaleza dejó de ser vista como una simple máquina que podía ser analizada (como la veía la ciencia), para convertirse en un ser vivo, dinámico y, a menudo, indomable. Los románticos buscaron una conexión mística con ella, viéndola como un reflejo del espíritu humano y un escape de la industrialización y la artificialidad de la vida urbana. En segundo lugar, el yo y la subjetividad puso un énfasis radical en la experiencia personal y el genio individual. El filósofo o artista romántico era visto como un héroe, un ser dotado de una visión única capaz de acceder a verdades más profundas que las que ofrecía la lógica. En tercer lugar, lo irracional y lo trascendente exploró activamente lo oscuro, lo misterioso, lo sublime y lo infinito. Fenómenos como los sueños, el folclore, lo sobrenatural y la historia medieval (en contraste con la antigüedad clásica preferida por la Ilustración) se convirtieron en temas de gran interés, buscando la verdad en el corazón de lo irracional y lo desconocido.
"""

elif  pagina_seleccionada == '🐇Personalidad':

# SISTEMA DE DIAGNÓSTICO DE PERSONALIDAD (Versión Narrativa)

# Este programa conduce al usuario por una serie de preguntas diseñadas para explorar los cimientos emocionales, racionales y simbólicos de su personalidad. Cada respuesta aporta matices a un retrato final, casi como si el código pintara un óleo psicológico del individuo.

# Diccionario para almacenar las respuestas del usuario.
respuestas = {}

# ------------------------------------------------------------
# FUNCIONES DE APOYO
# ------------------------------------------------------------

def preguntar(categoria, pregunta):
    """
    Esta función formula una pregunta y guarda la respuesta.
    
    Cada pregunta representa una puerta hacia un aspecto
    profundo de la personalidad del usuario. No buscamos
    respuestas correctas, sino huellas emocionales que permitan
    perfilar su inclinación natural.
    """
    print(f"\n[{categoria}]")
    print(pregunta)
    respuesta = input("Tu respuesta: ")
    respuestas[pregunta] = respuesta


def interpretar_resultado(respuestas):
    """
    Esta función analiza la esencia emocional de las respuestas
    del usuario. No usa estadística matemática; más bien evalúa
    la atmósfera y las palabras clave que revelan la tendencia
    del alma del usuario.

    El resultado final se expresa como una descripción literaria,
    casi como si un narrador omnisciente revelara el tipo de
    espíritu que habita en la persona que responde.
    """
    
    texto = " ".join(respuestas.values()).lower()

    # Patrones simples: se buscan señales emocionales.
    razon = any(p in texto for p in ["analizo", "pienso", "lógica", "razón", "calma"])
    impulso = any(p in texto for p in ["pasión", "impulso", "corazón", "emocional", "sentimiento"])
    melancolia = any(p in texto for p in ["tristeza", "nostalgia", "melancolía", "recuerdo"])
    oscuridad = any(p in texto for p in ["ruinas", "abandonado", "misterio", "noche", "oscuridad"])
    libertad = any(p in texto for p in ["libertad", "viaje", "desapego", "mundos", "explorar"])
    
    # --------------------------------------------------------
    # PERFILACIÓN FINAL (NARRATIVA)
    # --------------------------------------------------------

    if impulso and libertad:
        resultado = """
        ✦ **Genio Apasionado 𖤐 Viajero Eterno**
        
        Eres una fuerza en movimiento. Tu personalidad vibra con intensidad,
        como un fuego que no se deja domesticar. Sigues el impulso, pero no
        para perderte: lo haces para expandirte. El mundo es demasiado pequeño
        para tu espíritu errante. Donde otros ven límites, tú ves horizontes
        que reclaman ser explorados.
        """

    elif razon and melancolia:
        resultado = """
        ✦ **Melancólico Reflexivo 𖤐 Idealista Nostálgico**
        
        Tu alma parece recordar cosas que nunca has vivido. Caminas con una
        mezcla de serenidad racional y un trasfondo suave de nostalgia.
        Analizas, comprendes, observas… pero dentro de ti hay una música
        antigua que te hace contemplar lo que pudo ser, lo que fue y lo que
        aún podría existir en un mundo más bello.
        """

    elif oscuridad and impulso:
        resultado = """
        ✦ **Explorador de la Oscuridad 𖤐 Genio Apasionado**
        
        Posees un magnetismo extraño: te atrae aquello que otros evitan.
        No buscas lo macabro, sino la verdad profunda escondida en la sombra.
        Tus emociones son intensas, tus pasiones profundas. Ves belleza en la
        decadencia, poesía en lo roto y significado en lo que la sociedad
        decide olvidar.
        """

    elif libertad and razon:
        resultado = """
        ✦ **Viajero Eterno 𖤐 Observador Analítico**
        
        Eres como un viento que piensa. Tienes la mente de un filósofo y la
        libertad de un nómada. No te atan las estructuras sociales, pero
        tampoco te gobiernan los impulsos. Eres aire en movimiento: ligero,
        perceptivo y difícil de encasillar.
        """

    else:
        resultado = """
        ✦ **Alma Indefinida en Transición**
        
        Tu personalidad no se deja atrapar por una sola categoría. Eres un
        territorio en movimiento, un proceso en constante cambio. Quizás
        el mundo todavía no tiene un nombre para lo que eres, porque aún
        estás creándote, reinventándote, expandiéndote.
        """

    return resultado


# ------------------------------------------------------------
# LISTA DE PREGUNTAS  
# (Organizadas por dimensiones conceptuales del Romanticismo)
# ------------------------------------------------------------

# I. Razón, Sentimiento e Impulso
preguntar("Razón / Sentimiento / Impulso",
          "En una situación de conflicto, ¿qué guía tu primer paso?")
preguntar("Razón / Sentimiento / Impulso",
          "¿Cómo abordas tus proyectos creativos o tus pasiones?")
preguntar("Razón / Sentimiento / Impulso",
          "¿Qué valoras más en el arte?")

# II. Individualidad y Sociedad
preguntar("Individualidad y Sociedad",
          "¿Cómo te sientes respecto a las normas sociales?")
preguntar("Individualidad y Sociedad",
          "¿Qué te resulta más difícil de soportar?")
preguntar("Individualidad y Sociedad",
          "En tu vida ideal, ¿cómo te ves?")

# III. Naturaleza y Lo Urbano
preguntar("Naturaleza vs Lo Urbano",
          "¿Qué tipo de paisaje te atrae más profundamente?")
preguntar("Naturaleza vs Lo Urbano",
          "Cuando experimentas algo grandioso, ¿cómo reaccionas?")
preguntar("Naturaleza vs Lo Urbano",
          "¿Qué piensas del progreso tecnológico y la vida moderna?")

# IV. Pasado y Misterio
preguntar("Pasado y Misterio",
          "¿Qué época histórica te fascina más y por qué?")
preguntar("Pasado y Misterio",
          "¿Qué frase te describe mejor?")
preguntar("Pasado y Misterio",
          "¿Qué buscas al explorar lugares abandonados o misteriosos?")

# ------------------------------------------------------------
# RESULTADO FINAL
# ------------------------------------------------------------
print("\n──────────────────────────────────────")
print("✨ RESULTADO DE TU PERSONALIDAD ✨")
print("──────────────────────────────────────")
print(interpretar_resultado(respuestas))

else pagina_seleccionada == '🐇Diario de un genio incomprendido':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>¿Cómo te sientes el día de hoy?</h1>", unsafe_allow_html=True)

# EL DIARIO DEL GENIO INCOMPRENDIDO – ESTÉTICA VAPORWAVE
# ------------------------------------------------------------
# Este programa convierte tres respuestas del usuario en un fragmento de prosa dramática con estética vaporwave.
# ------------------------------------------------------------
# Diccionario donde se guardarán las respuestas
diario = {}

# ------------------------------------------------------------
# Función para preguntar al usuario y guardar la respuesta
# ------------------------------------------------------------
def preguntar_diario(etiqueta, texto):
    print(f"\n🌸 [{etiqueta}] 🌸")
    print(texto)
    respuesta = input("✎ Tu respuesta: ")
    diario[etiqueta] = respuesta

# ------------------------------------------------------------
# Función que genera la entrada de diario con estética vaporwave
# ------------------------------------------------------------
def generar_diario_vaporwave(d):
    sentimiento = d["Sentimiento Actual"]
    deseo = d["Deseo Profundo"]
    clima = d["Metáfora Climática"]

entrada = f"""
┌───────────────────────────────┐
│ 🌴  EL DIARIO DEL GENIO INCOMPRENDIDO  🌴 │
└───────────────────────────────┘

💭 Hoy me siento: {sentimiento} 🌸
No sé si este estado es un glitch en mi matrix interior o un
destello de claridad en la neón-tormenta de mi alma.

✨ Mi deseo más profundo ahora: {deseo} ✨
Sé que es inalcanzable, pero su resplandor rosa y cyan
ilumina cada rincón de mi existencia vaporwave.

🌧️ El clima hoy es: {clima} 🌈
Cada nube, cada pixel en el cielo refleja mi aura
retro-futurista. Todo vibra en 80s pastel y synthwave.

💾 Nadie necesita comprenderlo. Basta con que exista.
                                              — Tu Alma Romántica 🌸✨
"""
    return entrada

# ------------------------------------------------------------
# PREGUNTAS AL USUARIO
# ------------------------------------------------------------
preguntar_diario("Sentimiento Actual",
                 "¿Cómo te sientes en este momento? (Palabra o frase breve)")

preguntar_diario("Deseo Profundo",
                 "¿Cuál es tu anhelo o deseo más profundo AHORA?")

preguntar_diario("Metáfora Climática",
                 "Si el clima de hoy fuera una metáfora de tu alma, ¿qué palabra usarías?")

# ------------------------------------------------------------
# RESULTADO FINAL
# ------------------------------------------------------------
print("\n──────────────────────────────────────")
print("✨ TU ENTRADA DE DIARIO VAPORWAVE ✨")
print("──────────────────────────────────────\n")
print(generar_diario_vaporwave(diario))

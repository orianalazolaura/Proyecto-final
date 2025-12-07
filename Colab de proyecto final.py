# Proyecto Streamlit – Filosofía Romanticista (Vaporwave Estético)
import streamlit as st

# ------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ------------------------------------------------------------
st.set_page_config(
    page_title="Filosofía Romanticista 🌸",
    page_icon="🌸",
    layout="centered"
)

# ------------------------------------------------------------
# MENÚ DE NAVEGACIÓN
# ------------------------------------------------------------
paginas = ['🐇Temática', '🐇Personalidad', '🐇Diario de un genio incomprendido']
pagina_seleccionada = st.sidebar.selectbox(
    'Selecciona tu viaje al mundo de la filosofía romanticista',
    paginas
)

# ------------------------------------------------------------
# PÁGINA 1 – TEMÁTICA
# ------------------------------------------------------------
if pagina_seleccionada == '🐇Temática':
    st.markdown(
        "<h1 style='text-align: center; color:#FF77FF;'>💖 Corazones Desbordados 💖</h1>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2])
    col1.image("imagen del romanticismo.jpg", caption='Arte Romántico', width=300)

    texto = """
    <p style='color:#FF99FF; font-size:16px;'>
    El Romanticismo no fue solo un movimiento artístico y literario que floreció en Europa a finales del siglo XVIII y principios del XIX, sino también una profunda corriente filosófica y cultural que surgió como una reacción directa y a menudo vehemente contra el racionalismo estricto de la Ilustración. Mientras que la Ilustración había exaltado la razón, la objetividad y el análisis científico como el camino principal hacia el conocimiento y el progreso, el Romanticismo se centró en la primacía de la emoción, la subjetividad, la intuición y el sentimiento. Fue una reivindicación del individuo, del mundo interior y de todo aquello que la razón pura no podía abarcar. Tres temas centrales de esta época fueron la naturaleza y el sentimiento, el yo y la subjetividad y lo irracional y lo trascendente. En primer lugar, la naturaleza dejó de ser vista como una simple máquina que podía ser analizada (como la veía la ciencia), para convertirse en un ser vivo, dinámico y, a menudo, indomable. Los románticos buscaron una conexión mística con ella, viéndola como un reflejo del espíritu humano y un escape de la industrialización y la artificialidad de la vida urbana. En segundo lugar, el yo y la subjetividad puso un énfasis radical en la experiencia personal y el genio individual. El filósofo o artista romántico era visto como un héroe, un ser dotado de una visión única capaz de acceder a verdades más profundas que las que ofrecía la lógica. En tercer lugar, lo irracional y lo trascendente exploró activamente lo oscuro, lo misterioso, lo sublime y lo infinito. Fenómenos como los sueños, el folclore, lo sobrenatural y la historia medieval (en contraste con la antigüedad clásica preferida por la Ilustración) se convirtieron en temas de gran interés, buscando la verdad en el corazón de lo irracional y lo desconocido.
    </p>
    """
    col2.markdown(texto, unsafe_allow_html=True)

# ------------------------------------------------------------
# PÁGINA 2 – PERSONALIDAD
# ------------------------------------------------------------
elif pagina_seleccionada == '🐇Personalidad':
    st.markdown(
        "<h1 style='text-align: center; color:#FF66CC;'>✨ Descubre tu Alma Romántica ✨</h1>",
        unsafe_allow_html=True
    )

    respuestas = {}
    st.markdown("<h3 style='color:#FF99FF;'>I. Razón, Sentimiento e Impulso</h3>", unsafe_allow_html=True)
    respuestas["conflicto"] = st.text_input("💭 En un conflicto, ¿qué guía tu primer paso?")
    respuestas["proyectos"] = st.text_input("🎨 ¿Cómo abordas tus proyectos creativos o pasiones?")
    respuestas["arte"] = st.text_input("🖌️ ¿Qué valoras más en el arte?")

    st.markdown("<h3 style='color:#FF99FF;'>II. Individualidad y Sociedad</h3>", unsafe_allow_html=True)
    respuestas["normas"] = st.text_input("📜 ¿Cómo te sientes respecto a las normas sociales?")
    respuestas["difícil"] = st.text_input("⚡ ¿Qué te resulta más difícil de soportar?")
    respuestas["vida_ideal"] = st.text_input("🌈 En tu vida ideal, ¿cómo te ves?")

    st.markdown("<h3 style='color:#FF99FF;'>III. Naturaleza y Lo Urbano</h3>", unsafe_allow_html=True)
    respuestas["paisaje"] = st.text_input("🌳 ¿Qué tipo de paisaje te atrae más profundamente?")
    respuestas["grandioso"] = st.text_input("🌌 Cuando algo grandioso ocurre, ¿cómo reaccionas?")
    respuestas["tecnologia"] = st.text_input("💻 ¿Qué piensas del progreso tecnológico y la vida moderna?")

    st.markdown("<h3 style='color:#FF99FF;'>IV. Pasado y Misterio</h3>", unsafe_allow_html=True)
    respuestas["epoca"] = st.text_input("⏳ ¿Qué época histórica te fascina más y por qué?")
    respuestas["frase"] = st.text_input("💬 ¿Qué frase te describe mejor?")
    respuestas["explorar"] = st.text_input("🏰 ¿Qué buscas al explorar lugares abandonados o misteriosos?")

    def interpretar_resultado(respuestas):
        texto = " ".join(respuestas.values()).lower()
        razon = any(p in texto for p in ["analizo", "pienso", "lógica", "razón", "calma"])
        impulso = any(p in texto for p in ["pasión", "impulso", "corazón", "emocional", "sentimiento"])
        melancolia = any(p in texto for p in ["tristeza", "nostalgia", "melancolía", "recuerdo"])
        oscuridad = any(p in texto for p in ["ruinas", "abandonado", "misterio", "noche", "oscuridad"])
        libertad = any(p in texto for p in ["libertad", "viaje", "desapego", "mundos", "explorar"])

        if impulso and libertad:
            return "💖 **Genio Apasionado 𖤐 Viajero Eterno**\nTu espíritu vibra intensamente y busca horizontes infinitos."
        elif razon and melancolia:
            return "🌸 **Melancólico Reflexivo 𖤐 Idealista Nostálgico**\nAnalizas la vida mientras sientes un eco de nostalgia profunda."
        elif oscuridad and impulso:
            return "🌑 **Explorador de la Oscuridad 𖤐 Genio Apasionado**\nEncuentras poesía y significado en lo que otros ignoran."
        elif libertad and razon:
            return "🌬️ **Viajero Eterno 𖤐 Observador Analítico**\nLigero, perceptivo y difícil de encasillar."
        else:
            return "✨ **Alma Indefinida en Transición**\nEres un territorio en constante expansión, único e irrepetible."

    if st.button("💫 Ver mi personalidad"):
        st.markdown("### Resultado Final")
        st.markdown(f"<p style='color:#FF77FF;'>{interpretar_resultado(respuestas)}</p>", unsafe_allow_html=True)

# ------------------------------------------------------------
# PÁGINA 3 – DIARIO VAPORWAVE
# ------------------------------------------------------------
elif pagina_seleccionada == '🐇Diario de un genio incomprendido':
    st.markdown(
        "<h1 style='text-align: center; color:#FF66CC;'>🌴 Diario del Genio Incomprendido 🌴</h1>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        sentimiento = st.text_input("💭 ¿Cómo te sientes en este momento?")
        deseo = st.text_input("✨ ¿Cuál es tu deseo más profundo AHORA?")
        clima = st.text_input("🌧️ Si el clima de hoy fuera una metáfora de tu alma, ¿qué palabra usarías?")

    with col2:
        st.markdown(
            "<div style='background-color:#FFCCFF; padding:15px; border-radius:15px;'>"
            "<h3 style='color:#FF77FF;'>✨ Tu Diario Vaporwave ✨</h3>"
            "</div>", unsafe_allow_html=True
        )

    def generar_diario_vaporwave(sentimiento, deseo, clima):
        return f"""
    entrada = """
🌴*EL DIARIO DEL GENIO INCOMPRENDIDO* 🌴
💭 Hoy me siento: {sentimiento} 🌸
No sé si es un glitch en mi matrix interior o un destello de claridad en la neón-tormenta.

✨ Deseo más profundo: {deseo} ✨
Su resplandor rosa y cyan ilumina cada rincón de mi existencia vaporwave.

🌧️ Clima del alma: {clima} 🌈
Cada nube refleja mi aura retro-futurista, vibrando en la década de los ochenta, pastel y synthwave.

💾 Nadie necesita comprenderlo. Basta con que exista.
                                              — *Tu Alma Romántica* 🌸✨
"""
st.text(entrada)
    if st.button("🌟 Generar Diario"):
        st.markdown(f"<pre style='color:#FF77FF;'>{generar_diario_vaporwave(sentimiento, deseo, clima)}</pre>", unsafe_allow_html=True)
"""




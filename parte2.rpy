
label dia_3:

    yuki "Otro día... Mis pensamientos están más nublados que nunca. Hoy no sé qué hacer con mi vida."

    menu:
        "Ir al parque a despejarme":
            yuki "Intento ir al parque para tomar un poco de aire fresco, pero todo me parece distante."
            $ puntos -= 3  # Mejorar ligeramente la salud mental, pero la desconexión sigue
            yuki "Sigo sintiéndome distante, pero al menos veo algo diferente al estar afuera."

        "Ver una película en casa":
            yuki "Me pongo a ver una película. Tal vez me distraiga un rato."
            $ puntos += 3  # Aumenta la depresión al seguir eligiendo distracciones sin resolver el problema real
            yuki "Al final, la película solo me hace sentir más solo. Como si estuviera en un mundo ajeno."

        "Intentar escribir mis pensamientos":
            yuki "Decido escribir sobre lo que siento. Tal vez pueda entenderme mejor."
            $ puntos -= 1  # Ligeramente positivo al reflexionar sobre su situación
            yuki "Escribir me ayuda a ver las cosas desde otro ángulo, aunque sigue siendo difícil."

    yuki "La noche llega y, aunque intenté distraerme, sigo atrapado en mis pensamientos."

    jump dia_4

# =============================================================================================================================================

# **Cuarto día de vacaciones**
label dia_4:

    yuki "Hoy no quiero hacer nada, pero siento que necesito hacer algo, aunque no sé qué."

    menu:
        "Salir con Yato al cine":
            yuki "Yato me invita al cine, aunque no tengo muchas ganas de salir, decido ir."
            $ puntos -= 5  # Disminuye la depresión al interactuar con amigos
            yuki "Al final, la salida fue más divertida de lo que esperaba. No puedo negar que me alegra pasar tiempo con mis amigos."

        "Jugar videojuegos otra vez":
            yuki "Vuelvo a jugar videojuegos para evitar mis pensamientos. No sé qué más hacer."
            $ puntos += 5  # Aumenta la depresión, ya que las distracciones no ayudan
            yuki "El juego me hace olvidar un rato, pero cuando termina, el vacío regresa."

        "Llamar a Aki para hablar":
            yuki "Llamo a Aki, y esta vez ella me responde. Aunque al principio no sé qué decir, la conversación me hace sentir un poco mejor."
            $ puntos -= 3  # Mejora la salud mental por conectar con un amigo
            yuki "Hablar con Aki me da algo de consuelo. Quizás no todo está perdido."

    yuki "Parece que las cosas están mejorando un poco... Tal vez haya algo de esperanza."

    jump dia_5

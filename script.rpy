
label before_main_menu:
    play music "audio/title.wav"
    return

# Definir la variable de puntos (depresion)
default puntos = 40

# Definir los personajes
define yuki = Character("Yuki", color="#A0A0A0")
define hana = Character("Hana", color="#FF66CC")
define ren = Character("Ren", color="#33CCFF")

# Definimos el estilo para los puntos
define style_puntos_text = "default"
screen depresion_counter():

    # Mostrar el texto con el estilo definido
    text "Puntos: [puntos]" xalign 0.0 yalign 0.0 style "puntos_text"

# ============================================================================================================================================

label start:
    # Muestra la pantalla de puntos (depresion) en todo momento
    show screen depresion_counter

    # Musica feliz en bucle
    play music "audio/ambiente-feliz.wav"

    # Introduccion
    scene bg school
    show yuki-1
    yuki "Hoy es el ultimo dia antes de las vacaciones. Me siento extraño..."
    yuki "No estoy seguro si quiero que lleguen."
    hide yuki-1
    show hana-1
    hana "¡Vas a disfrutar mucho las vacaciones, Yuki! ¡No seas tan negativo!"
    "Para ti es facil decirlo..."
    hide hana-1
    show ren-1
    ren "Sí, tienes que aprovechar para descansar un poco. Ya sé que eres un poco flojo..."
    ren "Pero este es el momento perfecto para relajarte."
    "No es eso..."
    "No estoy seguro si quiero estar solo todo este tiempo..."
    hide ren-1
    show yuki-1
    yuki "Lo sé... pero algo me dice que no va a ser tan divertido."
    yuki "Mis padres estarán trabajando todo el día, y yo me quedaré solo practicamente todas las vacaciones."
    yuki "No sé si estoy listo para eso..."
    hide yuki-1
    show hana-1
    hana "No te preocupes, Yuki. Siempre podemos reunirnos para salir los 3."
    hide hana-1
    show ren-1
    ren "Sí, podemos hacer algo divertido otro dia. No te preocupes tanto por eso."
    hide ren-1
    show yuki-1
    yuki "..."

    menu:
        "Si, claro...":
            $ puntos += 5
            play sound "audio/points-base.wav"
            hide yuki-1
            show hana-1
            hana "¿Qué pasa con esos animos?"
            hana "No lo hagas sonar como la ultima vez. ¡Aun tenemos muuuchos dias!"
            hide hana-1
            show ren-1
            ren "Sí, no te preocupes. Siempre podemos salir a hacer algo divertido."
            hide ren-1
            show yuki-1
            yuki "Lo sé..."
            "Pero no puedo evitarlo. No sé si quiero estar solo todo este tiempo."
            "No lo sé..."
            hide yuki-1
            show ren-1
            ren "¿Por qué no te quedas un rato más?"
            ren "Podemos hablar o hacer algo divertido juntos, como siempre."
            hide ren-1
            show hana-1
            hana "¡Sí! ¡Podemos hacer algo divertido ahora mismo!"
            hide hana-1
            show yuki-1
            yuki "No sé..."
            yuki "No tengo energia para hacer nada..."

        "¿Por qué no seguimos divirtiendonos ahora?":
            $ puntos -= 5
            play sound "audio/points-feliz.wav"
            hide yuki-1
            show hana-1
            hana "¡Eso es! ¡Vamos a divertirnos antes de que termine el día!"
            hana "¡Esa es la actitud, Yuki!"
            hide hana-1
            show yuki-1
            yuki "Claro. Podemos hacer algo divertido juntos."
            yuki "Después de todo, ya estamos libres."
            hide yuki-1
            show ren-1
            ren "Perdón por arruinarles el ambiente, pero yo no puedo."
            ren "Tengo que irme a ayudar a los del club."
            hide ren-1
            show hana-1
            hana "Ya veo... que lastima."
            hide hana-1
            show yuki-1
            yuki "Si..."

        "Tengo prisa, me voy a casa.":
            $ puntos += 10
            play sound "audio/points-triste.wav"
            hide yuki-1
            show hana-1
            hana "¿Ehhh?"
            hana "¿Por qué tan rápido?"
            hide hana-1
            show ren-1
            ren "¿Qué pasa, Yuki?"
            ren "¿No quieres quedarte un rato más?"
            hide ren-1
            show yuki-1
            yuki "No tengo ganas de hacer nada... estoy muy cansado."


    hide yuki-1
    show ren-1
    ren "Bueno, yo me voy a ayudar a los del club."
    ren "Nos vemos luego, Hana, Yuki."
    hide ren-1
    show hana-1
    hana "¡Nos vemos, Ren!"
    hide hana-1
    show yuki-1
    yuki "Adios."
    "Ren se iria a ayudar a los del club dejandome solo con Hana..."
    yuki "..."
    hide yuki-1
    show hana-1
    hana "¿Yuki?"
    hana "¿Estás bien?"
    hide hana-1
    show yuki-1
    yuki "Si, claro."
    yuki "Solo estoy un poco cansado."
    hide yuki-1
    "Solo estoy cansado..."
    "Cansado..."
    "..."
    play sound "audio/thing-4.wav"
    "Cansado de todo..."

    # Aumenta los puntos (Tristeza) por la despedida??? y reproduce un sonidito
    $ puntos += 20
    play sound "audio/points-triste.wav"

# ============================================================================================================================================

    # Salta a "parte1"
    jump dia_1

# =============================================================================================================================================

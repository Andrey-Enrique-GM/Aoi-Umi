
label dia_5:

    yuki "Hoy no me siento tan mal, pero tampoco tan bien. ¿Qué debo hacer?"

    menu:
        "Salir a caminar nuevamente":
            yuki "Salgo a caminar, pero esta vez me siento más ligero. Tal vez esté aprendiendo a lidiar con esto."
            $ puntos -= 4  # Mejora la salud mental por hacer una actividad positiva
            yuki "Caminar me da algo de paz. No está todo resuelto, pero por lo menos estoy un poco mejor."

        "Ignorar todo y quedarme en casa":
            yuki "Hoy no tengo fuerzas para hacer nada. Decido quedarme en casa todo el día."
            $ puntos += 6  # Aumenta la depresión por evitar enfrentar los problemas
            yuki "El día se pasa lentamente, y la sensación de vacío crece cada vez más."

        "Escribir en mi diario":
            yuki "Decido escribir sobre lo que siento. Aunque no cambie mucho, me ayuda a ordenar mis pensamientos."
            $ puntos -= 2  # Ligeramente positivo por la reflexión
            yuki "Escribir me da un poco de claridad. Tal vez pueda entenderme mejor si sigo así."

    yuki "Aunque hoy fue un día sin muchas sorpresas, algo en mí ha cambiado."

    jump dia_6

# =============================================================================================================================================

# **Sexto día de vacaciones (Final)**
label dia_6:

    yuki "Último día de vacaciones. No sé si estoy mejor o peor."

    menu:
        "Salir con Aki y Yato al parque":
            yuki "Decido salir al parque con Aki y Yato. Este tiempo juntos me hace sentir que las cosas pueden mejorar."
            $ puntos -= 8  # Gran mejora, ya que la compañía de amigos lo ayuda
            yuki "Puedo sonreír por primera vez en mucho tiempo. Tal vez no todo está perdido."

        "Pasar el día solo":
            yuki "Decido quedarme en casa. Hoy no quiero salir, ni ver a nadie."
            $ puntos += 8  # Empeora la depresión al seguir aislándose
            yuki "La soledad se siente más pesada que nunca. Me siento atrapado."

# =============================================================================================================================================

# Se calcula que final se consiguio
    if puntos > 100:
        jump final_muy_malo
    elif puntos >= 80:
        jump final_triste
    elif puntos <= 30:
        jump final_positivo
    else:
        jump final_neutro

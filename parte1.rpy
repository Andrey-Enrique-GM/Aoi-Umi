
label dia_1:
    scene bg home
    show yuki-1
    yuki "Llegué a casa. Estoy solo... de nuevo."

    # Eleccion que influye en los puntos
    menu:
        "Jugar videojuegos":
            $ puntos -= 5  # Disminuye un poco los puntos
            play sound "audio/points-feliz.wav"
            yuki "Puedo jugar videojuegos para olvidar un poco."

        "Escuchar música":
            $ puntos -= 3  # Disminuye algo los puntos
            play sound "audio/points-base.wav"
            yuki "Escucharé música, tal vez me ayude a sentirme mejor."

        "No hacer nada":
            $ puntos += 10  # Aumenta los puntos
            play sound "audio/points-triste.wav"
            yuki "No tengo ganas de hacer nada... Solo me quedaré aquí."

    # Reajustar los puntos para que estén entre 0 y 100
    $ puntos = max(0, min(puntos, 100))

    yuki "El día termina, pero no me siento mejor."

    jump dia_2

# =============================================================================================================================================

label dia_2:
    # Segundo día con otra elección
    scene bg home
    yuki "Otro día más en casa, sin nadie para hablar..."
    
    menu:
        "Salir a caminar":
            yuki "Voy a salir a caminar para despejarme."
            $ puntos -= 5  # Disminuye los puntos

        "Llamar a Hana":
            yuki "Tal vez debería llamar a Hana, podría ayudarme."
            $ puntos -= 3  # Disminuye un poco

        "No hacer nada":
            yuki "Me quedo aquí... No sé qué hacer."
            $ puntos += 7  # Aumenta los puntos

    $ puntos = max(0, min(puntos, 100))  # Asegurarse de que esté en el rango correcto

    yuki "Este día ha sido igual que el anterior..."

    jump dia_3



# Definir la variable de puntos (depresión)
default puntos = 50

# Definir los personajes
define yuki = Character("Yuki", color="#A0A0A0")
define hana = Character("Hana", color="#FF66CC")
define ren = Character("Ren", color="#33CCFF")

# Fondo y música
image bg school = "school.jpg"
image bg home = "home.jpg"



# Definir la pantalla del contador con delineado azul claro
# Definir un estilo para el texto
# Definir un estilo para el texto
# Definimos el estilo para los puntos
# Definir el estilo directamente con define
define style_puntos_text = "default"
 
# Luego en la pantalla, puedes modificar las propiedades del estilo como se muestra:
screen depresion_counter():

    # Mostrar el texto con el estilo definido
    text "Puntos: [puntos]" xalign 0.0 yalign 0.0 style "puntos_text"





label start:
    # Muestra la pantalla de depresión en todo momento
    show screen depresion_counter

    # Introducción
    scene bg school
    yuki "Hoy es el último día antes de las vacaciones. Me siento extraño... no estoy seguro si quiero que lleguen."
    hana "¡Vas a disfrutar mucho las vacaciones, Yuki! ¡No seas tan negativo!" 
    ren "Sí, tienes que aprovechar para descansar un poco. Ya sé que eres un poco flojo, pero este es el momento perfecto para relajarte."
    yuki "Lo sé... pero algo me dice que no va a ser tan divertido. Mis padres estarán trabajando todo el día, y yo me quedaré solo."

    yuki "Las vacaciones comenzarán, pero algo no se siente bien."

    # Aumenta los puntos
    $ puntos += 10

    jump dia_1

label dia_1:
    scene bg home
    yuki "Llegué a casa. Estoy solo... de nuevo."

    # Elección que influye en los puntos
    menu:
        "Jugar videojuegos":
            yuki "Puedo jugar videojuegos para olvidar un poco."
            $ puntos -= 5  # Disminuye un poco los puntos

        "Escuchar música":
            yuki "Escucharé música, tal vez me ayude a sentirme mejor."
            $ puntos -= 3  # Disminuye algo los puntos

        "No hacer nada":
            yuki "No tengo ganas de hacer nada... Solo me quedaré aquí."
            $ puntos += 10  # Aumenta los puntos

    # Reajustar los puntos para que estén entre 0 y 100
    $ puntos = max(0, min(puntos, 100))

    yuki "El día termina, pero no me siento mejor."

    jump dia_2

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

# **Tercer día de vacaciones**
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

# **Quinto día de vacaciones**
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

    if puntos >= 80:
        jump final_triste
    elif puntos <= 30:
        jump final_positivo
    else:
        jump final_neutro

# **Final triste**
label final_triste:
    yuki "Las vacaciones han sido un reflejo de todo lo que siento... Estoy más solo que nunca, y no sé si puedo seguir adelante."
    return

# **Final positivo**
label final_positivo:
    yuki "Aunque aún me siento triste a veces, he aprendido a dar pequeños pasos. Mis amigos me apoyaron, y sé que no estoy solo."
    return

# **Final neutro**
label final_neutro:
    yuki "No estoy mejor ni peor. Las vacaciones fueron difíciles, pero al menos ahora sé que debo seguir adelante, paso a paso."
    return

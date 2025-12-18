# Saludar
saludar = "Hola, bon dia!!"
print(saludar)

# Preguntar el nom
nom = input("Jo em dic Fisibot i seré el teu chatbot encarregat de resoldre problemes físics. Com et dius? ")

# Separant per espai
nom = nom.split(" ")
nom = nom[-1]  
print("Perfecte " + nom + ", encantat de conèixer-te" + 3*"!")

# Primera pregunta: Problema o teoria
preferencia = input("Prefereixes que et resolgui un problema o que t'expliqui teoria? ").lower()

# Entén respostes obertes
if "teoria" in preferencia:
    print("\nMini teoria de física:")
    print("La física és la ciència que estudia la naturalesa i les lleis que governen l'univers.")
    print("Analitza conceptes com moviment, energia, força, matèria i interaccions.")
    print("Permet comprendre com funcionen els objectes i fenòmens del món real.\n")

elif "problema" in preferencia:
    tema = input("Sobre quin tema de física podríem parlar? (per exemple: velocitat o energia, força) ").lower()

    # Opcions per escollir el tema del que vols parlar
    if "velocitat" in tema:
        print("\nEt posaré un exercici bàsic per practicar el càlcul de la velocitat.")
        print("Un cotxe recorre 120 km en 2 hores.")
        print("Quina és la seva velocitat mitjana?")
        print("Recorda la fórmula: v = d / t")
        velocitat = 120 / 2
        print(f"Resposta: {velocitat} km/h\n")

    elif "energia" in tema:
        print("\nEt posaré un exercici senzill d'energia potencial.")
        print("Un objecte de 2 kg es troba a una alçada de 5 metres. Calcula la seva energia potencial gravitatòria.")
        print("Recorda la fórmula: Ep = m * g * h")
        m = 2
        g = 9.8
        h = 5
        Ep = m * g * h
        print(f"Resposta: {Ep} J (joules)\n")

    elif "força" in tema or "forca" in tema:
        print("\nEt posaré un exercici per aplicar la segona llei de Newton.")
        print("Un objecte de 3 kg s'accelera a 4 m/s². Quina força s'hi aplica?")
        print("Recorda la fórmula: F = m * a")
        m = 3
        a = 4
        F = m * a
        print(f"Resposta: {F} N (newtons)\n")

    else:
        print("\nTema no reconegut. Podem parlar d’altres temes més endavant.\n")

else:
    print("\nNo he entès la teva resposta, però seguirem amb la resta de preguntes.\n")

# Repte físic 
repte = input("Vols que et faci un repte físic? ").lower()

if "si" in repte or "sí" in repte:
    print("\nRepte de velocitat: Un cotxe recorre 180 km en 3 hores. Quina és la seva velocitat mitjana?")
    resposta_usuari = input("Resposta (en km/h): ")
    resposta_usuari = resposta_usuari.replace("km/h", "").replace(" ", "")
    resposta_usuari = float(resposta_usuari)
    resposta_correcta = 180 / 3  # 60 km/h

    if resposta_usuari == resposta_correcta:
        print("Molt bé!")
    else:
        print("Incorrecte.")
else:
    print("\nCap problema! Seguim endavant.\n")

# Preguntes de física
print("\nPots fer-me 3 preguntes de física, i intentaré respondre-les.")

for i in range(1, 4):
    pregunta = input(f"\nPregunta {i}: ").lower()

    if "adeu" in pregunta:
        print("\nGràcies per parlar amb mi, " + nom + "!")
        print("Fins aviat, " + nom + "! Que tinguis un bon dia! ☀️")
        exit()

    if "velocitat" in pregunta:
        print("La fórmula de la velocitat és v = d / t.")
    elif "gravetat" in pregunta:
        print("El valor de la gravetat a la Terra és 9,81 m/s².")
    elif "força" in pregunta or "forca" in pregunta:
        print("La unitat de mesura de la força és el newton.")
    else:
        print("No en tinc ni idea d’això... pots fer-me una altra?")

# Si no diu adeu durant les preguntes, li preguntem si vol continuar
while True:
    missatge = input("\nVols dir-me alguna cosa més? ").lower()

    # Si diu "adeu" o "no", acomiadament
    if "adeu" in missatge or "no" in missatge:
        print("\nGràcies per parlar amb mi, " + nom + "!")
        print("Fins aviat, " + nom + "! Que tinguis un bon dia! ☀️")
        break

import random as r
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Se usa cuando se quiere referir en forma sarcastica a algo",
            "POV": "Se usa para mostrar perspectivas graciosas o especificas",
            "SIMP": "Alguien que exagera en su admiración por otra persona, a menudo romántica",
            "F": "Usado para 'respetos' en situaciones tristes (referencia al juego Call of Duty)",
            "GG": "significa good game, se usa para decir que algo estuvo bien a veces de manera ironica",
            "AFK": "significa away from keyboard , se usa para expresar que alguien no esta presente",
    
            }
print(meme_dict.keys())

word = input("Escribe una palabra que no entiendas o escribe sorprendeme : ").upper()

if word in meme_dict.keys():
    print("El significado es:", meme_dict[word])
elif word == "SORPRENDEME":
    wordr = r.choice(list(meme_dict.keys()))
    print("La palabra es:", wordr, "y el significado es:", meme_dict[wordr])
else:
    print("Esta palabra aún no se ha agregado al diccionario")

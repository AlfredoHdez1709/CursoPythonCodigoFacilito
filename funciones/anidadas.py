def comenzar_play_list(lista):
    def reproducir():
        nonlocal lista
        lista = [1,2,3]
        for val in lista:
            print(val)
        
    reproducir()
    print(lista)
lista = ["track1", "track2", "track3", "track4"]

comenzar_play_list(lista)


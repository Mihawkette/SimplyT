import download_module


if __name__ == "__main__":
    lista_modalita = ["0: Scarica Audio", "1: Scarica video",
                      "2: Cambia cartella di destinazione", "3: scarica audio multipli"]
    for mode in lista_modalita:
        print(mode)

    while True:
        numero_mode = int(input("Inserisci il numero della modalità da utilizzare: \n"))
        if numero_mode in range(0,4): break
        else: print("Il numero inserito non va bene, riprova.\n")

    if numero_mode == 0:
        url = input("Inserisci l'url da scaricare: \n")
        download_module.download_audio(url)

    if numero_mode == 3:
        print("Inserisci gli url dei video da scaricare, separati da un invio;"
              " \nQuando desideri procedere al download immetti 'ok'")
        url = ""
        listadownload = []
        while url != "ok":
            url = input()
            listadownload += [url]
        download_module.download_multiplo(listadownload)



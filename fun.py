import pafy


print("NOTA: LO SCRIPT PER ADESSO SCARICA IL VIDEO SELEZIONATO IN FORMATO AUDIO NELLA CARTELLA IN CUI VIENE AVVIATO")
url = input("Inserisci l'url da scaricare: \n")
video = pafy.new(url)
print()

bestaudio = video.getbestaudio()
bestaudio.download()


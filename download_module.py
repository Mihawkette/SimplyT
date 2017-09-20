import pafy

def simple_download(url):
    video = pafy.new(url)
    audiolist = video.audiostreams
    index = 0
    audio_to_dl = audiolist[index]
    audioformat = audio_to_dl.extension
    try:
        audio_to_dl.download()
    except OSError:
        audio_to_dl.download(filepath="InvalidTitle." + audioformat)
def download_audio(url):
    video = pafy.new(url)
    audiolist = video.audiostreams
    index = 0
    for audio in audiolist:
        print(str(index) + ": " + str(audio)[6:])
        index += 1

    audio_to_dl_index = int(input("Seleziona il numero della traccia desiderata: \n"))
    audio_to_dl = audiolist[audio_to_dl_index]
    audioformat = audio_to_dl.extension
    try:
        audio_to_dl.download()
    except OSError:
        audio_to_dl.download(filepath="InvalidTitle." + audioformat)


def download_multiplo(lista_download):
    lista_download = lista_download[:len(lista_download)-1]
    invalid_counter = 0
    for video in lista_download:
        video = pafy.new(video)
        audio_to_dl = video.getbestaudio(preftype="m4a")
        try:
            audio_to_dl.download()
        except OSError:
            invalid_counter += 1
            filename = "multi_InvalidTitle({}).{}".format(invalid_counter,video.getbestaudio().extension)
            audio_to_dl.download(filepath=filename)
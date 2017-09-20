# SimplyT
Python practice youtube downloader with a (limited) GUI version and a console version

design.py contains the gui elements, made with PyQt5

download_module.py does most of the work, contains functions to download videos in a number of ways:
  simple_download allows the gui version to download -one- video in m4a format, no questions asked, for simplicity.
  
  download_audio allows to download a video and choose the file extension among available ones
  
  download_multiplo allows to download multiple videos from inputs, but defaults to m4a files
  
main.py runs the terminal version of the program
interface_main.pyw runs the simplistic gui version

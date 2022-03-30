# Random parameters generator
Rnorm="$1"
S="$2"
n="$3"

# run flashcrowd
python3 /vagrant/loadGen/flashcrowd.py -f $Rnorm,$S,$n -l http://192.168.50.50/videos/playlist.xspf

<<USO
usage: flashcrowd.py [-h] [-V] [-v] [-f Rnorm,S,n] -l PLAYLIST

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -v, --verbose         set verbosity level [default: None]
  -f Rnorm,S,n, --flashcrowd Rnorm,S,n
                        set the flashcrowd behavior, that varies with Rnorm
                        (normal load), S (shock_level) and n (constant used in
                        rampdown)
  -l PLAYLIST, --playlist PLAYLIST
                        Set the playlist for the clients
USO

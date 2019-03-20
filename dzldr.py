import time
import deezloader
import os

def print_quality():
    str = "\tQuality:\n"
    str += "(1) flac\n"
    str += "(2) mp3 (320 CBR)\n"
    str += "(3) mp3 (256 CBR)\n"
    str += "(4) mp3 (128 CBR)\n"
    print(str)

def print_menu():
    str = "\tOptions:\n"
    str += "(1) Download\n"
    str += "(2) Modify parameters\n"
    str += "(3) Exit\n"
    print(str)

def print_parameters():
    str = "\tChange Parameters: \n"
    str += "(1) Donwload Quality \n"
    str += "(2) Skip Existing Downloads\n"
    str += "(3) Revert To Worse Quality If Current One Is Unavailable\n"
    str += "(4) Back\n"
    print(str)

def deezer_spotify(url):
    """Finds if the url is from Spotify or Deezer and adds an offset for the funtion call"""
    if "spotify" in url:
        return 3
    return 0

def track_album_playlist(url):
    """ Finds out if a given Deezer/Spotify link is from an album, track or playlist"""
    url = url.split("/")
    for el in url:
        if el in ["album", "track", "playlist"]:
            return el
    raise ValueError("Invalid link!")

def set_default_options(dl):
    """ Set default download options"""
    return [dl.download_trackdee, dl.download_albumdee, dl.download_playlistdee,
            dl.download_trackspo, dl.download_albumspo, dl.download_playlistspo], \
           "FLAC", True, True

def download(option):
    """ Donwloads song/album/playlist after a given link"""
    global chec
    global qualit
    global recursiv
    map = {"track": 0,
           "album": 1,
           "playlist": 2}

    url = input("link: ")
    try:
       option = option[deezer_spotify(url) + map[track_album_playlist(url)]]
       option(url, output = "download location", check = chec, quality = qualit, recursive = recursiv)
       time.sleep(1.5)
    except:
       print("Invalid link!")
       time.sleep(1)
       return

def exit_app(options):
    """ Closes the app"""
    print("Bye!")
    exit()

def set_quality():
    """ Modifies the quality parameter"""
    global qualit
    os.system('clear')
    print("\ncurrent quality is ", qualit)
    print_quality()
    commands = {"1": "FLAC",
                "flac": "FLAC",
                "2": "MP3_320",
                "mp3": "MP3_320",
                "3": "MP3_256",
                "4": "MP3_128"}
    cmnd = input("> ")
    if cmnd in commands:
        qualit = commands[cmnd]
    else:
        print("Invalid Command!")
        time.sleep(0.4)

def set_check():
    """ Modifies the check parameter"""
    global chec
    os.system('clear')
    print("\ncurrent setting is ", chec)
    print("Set True / False")
    cmnd = input("> ")
    if cmnd == "True":
        chec = True
    elif cmnd == "False":
        chec = False
    else:
        print("Invalid Command!")
        time.sleep(0.4)

def set_recursive():
    """ Modifies the recursive parameter"""
    global recursiv
    os.system('clear')
    print("\ncurrent setting is ", recursiv)
    print("Set True / False")
    cmnd = input("> ")
    if cmnd == "True":
        recursiv = True
    elif cmnd == "False":
        recursiv = False
    else:
        print("Invalid Command!")
        time.sleep(0.4)

def modify_parameters(options):
    """ Modifies all the parameters of the download function"""
    while True:
        os.system('clear')
        print_parameters()
        commands = {"1": set_quality,
                   "2": set_check,
                   "3": set_recursive}

        cmnd = input("> ")
        if cmnd == "4":
            break
        elif cmnd in commands:
            commands[cmnd]()
        else:
            print("Invalid Command!")
            time.sleep(0.4)

qualit, chec, recursiv = 0,0,0

if __name__ == "__main__":
    menu = {"1": download,
            "2": modify_parameters,
            "3": exit_app}

    dl = deezloader.Login("email", "password", "token")
    option, qualit, chec, recursiv = set_default_options(dl)
    while True:
        os.system('clear')
        print_menu()
        cmnd = input("> ")
        if cmnd in menu:
            menu[cmnd](option)
        else:
            print("Invalid Command!")
            time.sleep(0.4)

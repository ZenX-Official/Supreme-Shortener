#!/usr/bin/python3
#  ZENZED OFFICIAL
#  [+]  Youtube  :  http://bit.ly/ZenXYoutube     [+]
#  [+]  Facebook :  https://bit.ly/ZenXFbPage     [+]
#  [+]  Website  :  https://bit.ly/ZenXWebsite    [+]
#  [+]  github   :  https://bit.ly/ZenXGithub     [+]
#  [+]  E-mail   :  zenzedofficial@gmail.com      [+]
import os
import time
import pyshorteners
from time import sleep


os.system('clear')

def Main():
    print("\033[0;31m         ██████  █    ██  ██▓███   ██▀███  ▓█████  ███▄ ▄███▓▓█████")
    print("       ▒██    ▒  ██  ▓██▒▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▓█   ▀ ")
    print("       ░ ▓██▄   ▓██  ▒██░▓██░ ██▓▒▓██ ░▄█ ▒▒███   ▓██    ▓██░▒███   ")
    print("         ▒   ██▒▓▓█  ░██░▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒▓█  ▄ ")
    print("       ▒██████▒▒▒▒█████▓ ▒██▒ ░  ░░██▓ ▒██▒░▒████▒▒██▒   ░██▒░▒████▒")
    print("       ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░░ ▒░ ░")
    print("       ░ ░▒  ░ ░░░▒░ ░ ░ ░▒ ░       ░▒ ░ ▒░ ░ ░  ░░  ░      ░ ░ ░  ░")
    print("       ░  ░  ░   ░░░ ░ ░ ░░         ░░   ░    ░   ░      ░      ░   ")
    print("             ░     ░                 ░        ░  ░       ░      ░  ░\n")
    print("  ██████  ██░ ██  ▒█████   ██▀███  ▄▄▄█████▓▓█████  ███▄    █ ▓█████  ██▀███  ")
    print("▒██    ▒ ▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒")
    print("░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒")
    print("  ▒   ██▒░▓█ ░██ ▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ")
    print("▒██████▒▒░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒")
    print("▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░")
    print("░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░    ░     ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░")
    print("░  ░  ░   ░  ░░ ░░ ░ ░ ▒    ░░   ░   ░         ░      ░   ░ ░    ░     ░░   ░ ")
    print("      ░   ░  ░  ░    ░ ░     ░                 ░  ░         ░    ░  ░   ░     \033[0m\r\n")
    print("      \033[1;30m[Generate Your Own Convincing Links/URL For Social Engineering]")
    print("      \033[1;30m[Good Luck At Yout Victim :]     Coded By: ZenX Official [1.0v]")

    print("\n\033[1;36m[01]  Google                 [02]  Pinterest")
    print("[03]  Youtube                [04]  Facebook")
    print("[05]  Instagram              [06]  000Webhost")
    print("[07]  Github                 [08]  Messenger")
    print("[09]  Twitter                [10]  Personalized")
    print("\n[00]  Exit")
    Selector()

def Selector():
    select = int(input("\n\033[1;33;40mSupreme-Shortener []=> "))
    if select == 1:
        EnlaceGoogle()
    elif select == 2:
        EnlacePinterest()
    elif select == 3:
        EnlaceYoutube()
    elif select == 4:
        EnlaceFacebook()
    elif select == 5:
        EnlaceInstagram()
    elif select == 6:
        EnlaceWebhost()
    elif select == 7:
        EnlaceGithub()
    elif select == 8:
        EnlaceMessenger()
    elif select == 9:
        EnlaceTwitter()
    elif select == 10:
        EnlacePersonalized()
    elif select == 00:
        os.system('clear')
        print("Exiting Tool")
        sleep(1)
        os.system('clear')
        print("Exiting Tool .")
        sleep(1)
        os.system('clear')
        print("Exiting Tool . .")
        sleep(1)
        os.system('clear')
        print("Exiting Tool . . .")
        sleep(1)
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print("Please Select a Valid option...")
        sleep(1)
        os.system('clear')
        Main()

def EnlaceGoogle():
    os.system('clear')
    print("[SELECTED] : [GOOGLE]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something Like: this-is-an-amazing-content-you-should-see")
    Postlink = str(input("\nPost LINK: "))
    os.system('clear')
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.google.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceYoutube():
    os.system('clear')
    print("[SELECTED] : [YOUTUBE]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-video-your-should-watch")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.youtube.com-video-{Postlink}@{Withouthttp}")
    Other()

def EnlaceInstagram():
    os.system('clear')
    print("[SELECTED] : [INSTAGRAM]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-photo-your-should-see")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.instagram.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceFacebook():
    os.system('clear')
    print("[SELECTED] : [FACEBOOK]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-post-your-should-see")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.facebook.com-profile-{Postlink}@{Withouthttp}")
    Other()

def EnlaceGithub():
    os.system('clear')
    print("[SELECTED] : [GITHUB]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-post-your-should-see")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.github.com-{Postlink}@{Withouthttp}")
    Other()

def EnlacePinterest():
    os.system('clear')
    print("[SELECTED] : [PINTEREST]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-post-your-should-see")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.pinterest.ph-{Postlink}@{Withouthttp}")
    Other()

def EnlaceTwitter():
    os.system('clear')
    print("[SELECTED] : [TWITTER]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-post-your-should-see")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://twitter.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceMessenger():
    os.system('clear')
    print("[SELECTED] : [MESSENGER]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-post-your-should-see")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.messenger.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceWebhost():
    os.system('clear')
    print("[SELECTED] : [000WEBHOST]")
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-post-your-should-see")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\n[NEW!] [GENERATED] [LINK] : https://www.000webhost.com-{Postlink}@{Withouthttp}")
    Other()

def EnlacePersonalized():
    os.system('clear')
    print("[SELECTED] : [PERSONALIZED]")
    Domain = str(input("e.g [https.www.] Domain [.com] \n Input Domain:"))
    OriginalLink = str(input("\nOriginal URL: "))
    print("\nInput something that: this-is-an-amazing-content-your-should-watch")
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener(api_key='9b27c732524d2d395bb98486c41d1d6078ea6447')
    EndLink = Shortener.bitly.short(OriginalLink)
    Withouthttp = EndLink[8:]
    os.system('clear')
    print(f"\033[1;32;40m\nYour Link is: https://www.{Domain}.com-{Postlink}@{Withouthttp}")
    Other()

def Other():
    print("\033[93m\nDo you want to generate another link?")
    print("[01] Yes \n[02] No ")
    select=int(input("\nSelect an Option: "))
    if select == 1:
        sleep(1)
        os.system('clear')
        Main()
    else:
        os.system('clear')
        print("Exiting Tool")
        sleep(1)
        os.system('clear')
        print("Exiting Tool .")
        sleep(1)
        os.system('clear')
        print("Exiting Tool . .")
        sleep(1)
        os.system('clear')
        print("Exiting Tool . . .")
        sleep(1)
        os.system('clear')
        exit()

#SYSCALL
Main()

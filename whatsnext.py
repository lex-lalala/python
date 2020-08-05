#!/bin/python3
import sys
def banner():                 # some cool banners
	print("*" * 50)
def genre():                  # choose a genre
    print("CHOOSE A GENRE")   
    print("-" * 50)
    print("1.action")
    print("2.adventure")
    print("3.horror")
    print("4.romance")
def start():           
	print("\n")
	print(":" * 60)
	while True:
                cmd = input('\nDo you want to go back or quit, enter "q" to quit, "c" to continue: ') # go back or exit
                print("\n")
                if cmd == 'c':
                     import whatsnext.py
                elif cmd == 'q':
                      print("\nThank You for using this program, have a nice and chilling day :p") # credits hahaha
                      print("\nMade by lexlalala")
                      break            
value = input("tv shows OR movies: ")  #enter a category
if value == "movies":  #category: movies                   
         banner()
         genre()
         genre = input("GENRE: ")
         if genre ==  "action":
         	banner()
         	print("The Old Guard")
         	start()
         elif genre == "adventure":
         	banner()
         	print("Double World")
         	start()
         elif genre == "horror":
         	banner()
         	print("The Rental")
         	start()
         elif genre == "romance":
         	banner()
         	print(" Dil Bechara")
         	start()
         else:
             print("\ncouldn't determine the input...sorry")
             start()
elif value == "tv shows":  #category:tv shows
         print("*" * 50)
         genre()
         genre = input("GENRE: ")
         if genre ==  "action":
         	banner()
         	print("Game Of thrones")
         	start()
         elif genre == "adventure":
         	banner()
         	print("The Chilling Adventures Of Sabrina")
         	start()
         elif genre == "horror":
         	banner()
         	print("The Walking Dead")
         	start()
         elif genre == "romance":
         	banner()
         	print("The Vampire Diaries")
         	start()
         else:
            print("\ncouldn't determine the input...sorry")
            start()

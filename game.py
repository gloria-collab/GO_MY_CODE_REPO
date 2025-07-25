def main(): # putting the codes into procedures, this my main code

    import random  
    word_list = ["goal", "mine", "hole", "long", "land","told", "boat", "dull", "word", "runs",
    "call", "bank", "dogs", "hang", "mail", "pole", "sail","time", "good",'wale', 'play']
    com_choice =random.choice(word_list)
    tries= 3
    num_guess = 0
    display = "_" * len(com_choice)
    n = 0
    point= 3
    print("WELCOME GAMER")
    user_input= input("what your name gamer? ").capitalize()
    print("hi, {}, would you like to play my guessing game :) :) ".format(user_input)) # the {} is used as a representation of the users input
    print(" NOTE: READ THE INSTRUCTIONS BELOW.")
    print("use the alphabets below to play the game {}. ".format(user_input))
    print("abcdefghijklmnopqrstuvwxyz")
    print("You get 3 point for this game, when you get the words incorrectly you lose 1 point")
    S_G= input("PRESS ENTER TO START GAME")
    print("GAME START")
    game_over = False
    print(com_choice)


    while not game_over:
        print(display)
        print("guess the word :) :) ")
        print("YOU HAVE" + " " + str (tries) + " "  +"TRIES" +  " " + "REMAINING" )
        print(str(point) + " " + "POINTS" + " " + "ALLOCATED")
        guess = input("INPUT LETTER: ").lower()
    
        if guess in com_choice:
            while com_choice.find(guess, n) != -1:
                num_guess = com_choice.find(guess, n)
                n = com_choice.find(guess, n) #n represent the location of the letter guessed correctly in the word
                display = display[:n] + guess + display[n + 1:]
                
                n += 1
                print("correct")
                point = point + 1
                print("YOU GET AN EXTRA 1 POINT")

                   
        else:
            print("incorrect")
            tries -=1
            point -=1
        if tries == 0:
                print("YOUR ATTEMPT HAS BEEN USED UP")
                print("GAME OVER")
                break
            
        if point == 0:
                print("YOU LOST ALL YOUR POINT")
                break

                        
        if com_choice == display:
            print("CONGRATULATIONS YOU GOT IT")
            print("WHAT A MAGA WIN")
            print(" :) :) :) :) :) :) :)")
            print("THE WORD WAS" + " " + (com_choice).capitalize() )
            play_again = input("WOULD YOU LIKE TO PLAY AGAIN {}. ENTER YES/NO: ".format(user_input)).lower()
            g= "yes"
            h= "no"
            if play_again == h:
                    print(" BYE :) :) :) :)")
                    print("TILL ANOTHER TRY {} ".format(user_input))
                    break
            else:
                print("RESTARTING GAME, {} ".format(user_input).capitalize)
             # this reruns the game to the beginning
                main()
                game_over= True
main()
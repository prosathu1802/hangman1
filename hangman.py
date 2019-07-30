def hangman(word):
        wrong = 0
            stages = ["",
                                  "_________        ",
                                                "|                ",
                                                              "|        |       ",
                                                                            "|        0       ",
                                                                                          "|      / | |     ",
                                                                                                        "|       / |      ",
                                                                                                                      "|                "
                                                                                                                                    ]
                remaining_letter= list(word)
                    win = False
                        board = ["_"] * len(word)
                            print("Welcome to Hangman")

                                while wrong< len(stages)-1:
                                            print("\n")
                                                    char = input("Guess a letter")
                                                            if char in remaining_letter:
                                                                            character_Index = remaining_letter.index(char)
                                                                                        board[character_Index] = char
                                                                                                    remaining_letter[character_Index]='$'
                                                                                                            else:
                                                                                                                            wrong +=1
                                                                                                                                    print((" ".join(board)))
                                                                                                                                            c = wrong + 1
                                                                                                                                                    print("\n".join(stages[0:c]))
                                                                                                                                                            if "_" not in board:
                                                                                                                                                                            print("\n")
                                                                                                                                                                                        print("You Win!")
                                                                                                                                                                                                    print(" ".join(board))
                                                                                                                                                                                                                win = True
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                            if not win:
                                                                                                                                                                                                                                        print("\n".join(stages[0:wrong]))
                                                                                                                                                                                                                                                print("You lose! It was {}.".format(word))
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                            hangman("Hello")

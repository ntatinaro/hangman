#https://github.com/ntatinaro/hangman/blob/main/hangman.py


def stage(n):
    stage6= """
          _____      
               |     
               O     
              /|\    
              / \    """

    stage5 = """
              _____      
                   |     
                   O     
                  /|\    
                  /      """

    stage4 = """
              _____      
                   |     
                   O     
                  /|\    
                         """

    stage3 = """
                  _____      
                       |     
                       O     
                      /|     
                             """

    stage2 = """
                  _____      
                       |     
                       O     
                      /      
                             """

    stage1 = """
                  _____      
                       |     
                       O     
                             
                             """

    stage0 = """
                      _____      
                           |     
                                 

                                 """

    if n == 6:
        print(stage6)
    elif n == 5:
        print(stage5)
    elif n == 4:
        print(stage4)
    elif n == 3:
        print(stage3)
    elif n == 2:
        print(stage2)
    elif n == 1:
        print(stage1)
    else:
        print(stage0)

def hangaman(word):
    wrong = 0
    wordlist = []
    for w in word:
        wordlist.append(w)
    board = []
    for w in word:
        board.append("_")
    stage(0)
    while wrong < 6:
        print(board)
        if board != wordlist:
            t = input("Guess a letter")
            if t not in wordlist:
                wrong += 1
                print("incorrect")
                stage(wrong)
            else:
                i = 0
                while i < len(wordlist):
                    if t == wordlist[i]:
                        board[i]=t
                    i+=1
        else:
            print("You Win!")
            break




hangaman("hello world")

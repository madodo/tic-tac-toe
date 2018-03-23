gameover = False

spot1 = '_'
spot2 = '_'
spot3 = '_'
spot4 = '_'
spot5 = '_'
spot6 = '_'
spot7 = '_'
spot8 = '_'
spot9 = '_'

def winornot():
    if spot5 == 'x' and spot2 == 'x' and spot8 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True
    elif spot5 == 'x' and spot4 == 'x' and spot6 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True
    elif spot5 == 'x' and spot3 == 'x' and spot7 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True
    elif spot5 == 'x' and spot1 == 'x' and spot9 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True
    elif spot1 == 'x' and spot4 == 'x' and spot7 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True
    elif spot3 == 'x' and spot6 == 'x' and spot9 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True
    elif spot1 == 'x' and spot2 == 'x' and spot3 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True
    elif spot7 == 'x' and spot8 == 'x' and spot9 == 'x':
        print('x win')
        print(' ')
        print(' ')
        gameover = True

    if spot5 == 'o' and spot2 == 'o' and spot8 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True
    elif spot5 == 'o' and spot4 == 'o' and spot6 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True
    elif spot5 == 'o' and spot3 == 'o' and spot7 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True
    elif spot5 == 'o' and spot1 == 'o' and spot9 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True
    elif spot1 == 'o' and spot4 == 'o' and spot7 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True
    elif spot3 == 'o' and spot6 == 'o' and spot9 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True
    elif spot1 == 'o' and spot2 == 'o' and spot3 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True
    elif spot7 == 'o' and spot8 == 'o' and spot9 == 'o':
        print('o win')
        print(' ')
        print(' ')
        gameover = True



def xchoose():
    global spot1
    global spot2
    global spot3
    global spot4
    global spot5
    global spot6
    global spot7
    global spot8
    global spot9
    x = input('x what spot')
    if x == '1':
        spot1 = 'x'
    elif x == '2':
        spot2 = 'x'
    elif x == '3':
        spot3 = 'x'
    elif x == '4':
        spot4 = 'x'
    elif x == '5':
        spot5 = 'x'
    elif x == '6':
        spot6 = 'x'
    elif x == '7':
        spot7 = 'x'
    elif x == '8':
        spot8 = 'x'
    elif x == '9':
        spot9 = 'x'
    print("{}|{}|{}".format(spot1, spot2, spot3))
    print("{}|{}|{}".format(spot4, spot5, spot6))
    print("{}|{}|{}".format(spot7, spot8, spot9))

    winornot()
#-------------------------------------------------------------------------------------#

def ochoose():
    o = input('o what spot')
    global spot1
    global spot2
    global spot3
    global spot4
    global spot5
    global spot6
    global spot7
    global spot8
    global spot9
    if o == '1':
        spot1 = "o"
    elif o == '2':
        spot2 = 'o'
    elif o == '3':
        spot3 = 'o'
    elif o == '4':
        spot4 = 'o'
    elif o == '5':
        spot5 = 'o'
    elif o == '6':
        spot6 = 'o'
    elif o == '7':
        spot7 = 'o'
    elif o == '8':
        spot8 = 'o'
    elif o == '9':
        spot9 = 'o'
    print("{}|{}|{}".format(spot1, spot2, spot3))
    print("{}|{}|{}".format(spot4, spot5, spot6))
    print("{}|{}|{}".format(spot7, spot8, spot9))

    winornot()

##asdfghjkl

while gameover == False:
    xchoose()
    ochoose()

if gameover == True:
    print('game over. reload to play again.')
#eeeeeee




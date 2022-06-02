import random
p = 'paper'
s = 'stone'
sci = 'scissor'
i = 0
while 10 >= i:
    print('enter any one', '[', p, s, sci, ']')
    i = i+1
    a = [s, p, sci]
    comp = random.choice(a)

    play = input()
    if comp == play:
        print('draw')
        print('computer entered',comp,'\nused chances',i,'/10')
    elif s == comp:
        if play == sci:
            print('loss')
            print('computer entered',comp,'\nused chances',i,'/10')
        elif play == p:
            print('win')
            print('computer entered',comp,'\nused chances',i,'/10')
        else:
            print('please enter valid input','used chance',i)
    elif p == comp:
        if play == sci:
            print('win')
            print('computer entered',comp,'\nused chances',i,'/10')
        elif play == s:
            print('loss')
            print('computer entered',comp,'\nused chances',i,'/10')
        else:
            print('please enter vali input','used chance',i,'/10')
    elif sci == comp:
        if play == p:
            print('loss')
            print('computer entered',comp,'\nused chances',i)
        elif play == s:
            print('win')
            print('computer entered',comp,'used chances',i)
        else:
            print('please enter vali input','used chance',i)
    else:
        print('please enter vali input','used chance',i)


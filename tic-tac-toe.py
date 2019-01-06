name1=input("enter  player1 name")
name2=input("enter player2 name")
tt_board={'tl':'','tm':'','tr':'',
         'ml':'','mm':'','mr':'',
         'll':'','lm':'','lr':''}
def tttboard(t_board):
    print(tt_board['tl'],'|',tt_board['tm'],'|',tt_board['tr'])
    print('tl|tm|tr')
    print('--+--+--')
    print(tt_board['ml'],'|',tt_board['mm'],'|',tt_board['mr'])
    print('ml|mm|mr')
    print('--+--+--')
    print(tt_board['ll'],'|',tt_board['lm'],'|',tt_board['lr'])
    print('ll|lm|lr')


while name1 and name2:
    tttboard(tt_board)
    break
def turnon():
    for i in range (9):
        #print(name1,'take your turn 0 or X ')
        #print('set your positions like tl-tm-tr or ml-mm-mr or ll-lm-lr ')
        print(name1,'take your turn 0 or X ')
        turn1=input()
        print('set your positions like tl-tm-tr or ml-mm-mr or ll-lm-lr ')
        position1=input()
        while turn1==True:
            print(turn1)
            """if tt_board['tl']==turn1 and tt_board['tm']==turn1 and tt_board['tr']==turn1:
                print(name1,'Bravo you win')"""
            if tt_board['tl']== tt_board['ml'] or tt_board['tl']==tt_board['ll'] or tt_board['ml']==tt_board['ll']:
                print(name1,'Bravo you win')
            """elif tt_board['tl']==turn1 and tt_board['mm']==turn1 and tt_board['lr']==turn1:
                print(name1,'Bravo you win')
            elif tt_board['tr']==turn1 and tt_board['mm']==turn1 and tt_board['ll']==turn1:
                print(name1,'Bravo you win')
            elif tt_board['tr']==turn1 and tt_board['mr']==turn1 and tt_board['lr']==turn1:
                print(name1,'Bravo you win')
            elif tt_board['ll']==turn1 and tt_board['lm']==turn1 and tt_board['lr']==turn1:
                print(name1,'Bravo you win')
            elif tt_board['lm']==turn1 and tt_board['mm']==turn1 and tt_board['rm']==turn1:
                print(name1,'Bravo you win')
            elif tt_board['ll']==turn1 and tt_board['lm']==turn1 and tt_board['lr']==turn1:
                print(name1,'Bravo you win')
            elif tt_board['tm']==turn1 and tt_board['mm']==turn1 and tt_board['lm']==turn1:
                print(name1,'Bravo you win')"""
            break
            print(name2,'Unfortunaely you loose the game')
            exit()
        
        while tt_board[position1]=='':       
            if turn1=='0' and position1=='tl':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='tm':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='tr':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='ml':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='mm':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='mr':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='ll':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='lm':
                tt_board[position1]='0'
            elif turn1=='0' and position1=='lr':
                tt_board[position1]='0'
            else:
                tt_board[position1]='X'

            tttboard(tt_board)
            break   
        print(name2,'take your turn 0 or X ')
        turn2=input()
        print('set your positions like tl-tm-tr or ml-mm-mr or ll-lm-lr ')
        position2=input()
        
        while tt_board[position2]=='':
            if turn2=='0' and position2=='tl':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='tm':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='tr':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='ml':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='mm':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='mr':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='ll':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='lm':
                tt_board[position2]='0'
            elif turn2=='0' and position2=='lr':
                tt_board[position2]='0'
            else:
                tt_board[position2]='X'

            tttboard(tt_board)
            break
        """
        while  turn2:
            if tt_board['tl']==tt_board['tm']==tt_board['tr']:
                print(name2,'Bravo you win')
            elif tt_board['tl']==tt_board['ml']==tt_board['ll']:
                print(name2,'Bravo you win')
            elif tt_board['tl']==tt_board['mm']==tt_board['lr']:
                print(name2,'Bravo you win')
            elif tt_board['tr']==tt_board['mm']==tt_board['ll']:
                print(name2,'Bravo you win')
            elif tt_board['tr']==tt_board['mr']==tt_board['lr']:
                print(name2,'Bravo you win')
            elif tt_board['ll']==tt_board['lm']==tt_board['lr']:
                print(name2,'Bravo you win')
            elif tt_board['lm']==tt_board['mm']==tt_board['rm']:
                print(name2,'Bravo you win')
            elif tt_board['ll']==tt_board['lm']==tt_board['lr']:
                print(name2,'Bravo you win')
            elif tt_board['tm']==tt_board['mm']==tt_board['lm']:
                print(name2,'Bravo you win')
            else:
                print('Unfortunately you loose the game')
            break
            exit()
            """
turnon()

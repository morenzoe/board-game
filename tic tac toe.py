# import module
import random
# set up matrix board
board = ['(   )', '(   )', '(   )', '(   )', '(   )', '(   )', '(   )', '(   )', '(   )']
# set up matrix tutorial board
tutorial_board = ['( 1 )', '( 2 )', '( 3 )', '( 4 )', '( 5 )', '( 6 )', '( 7 )', '( 8 )', '( 9 )']

# fungsi tanya nama
def nama(symbol):
    while True:
        player = input('Pemain ' + symbol + ', masukkan namamu: ')
        if player == '':
            print('Nama tidak boleh kosong')
            continue
        else:
            break
    return player

# pembukaan game
print('\nTic-Tac-Toe Munyi v2.0\n')
player_O = nama('O')
player_X = nama('X')

# set up exceptions
class Error(Exception):
    pass
class too_small(Error):
    pass
class too_high(Error):
    pass
class used(Error):
    pass

#set up fungsi dan input posisi
def mark(player, symbol):
    # awal giliran
    print('\nGiliran ' + player + ',')
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])



    # set up loop check value
    while True:
        try:
            posisi = input(player + ' mau taruh ' + symbol + ' dimana? ')
            if int(posisi) < 1:
                raise too_small
            elif int(posisi) > 9:
                raise too_high
            if board[int(posisi) - 1] == '( O )' or board[int(posisi) - 1] == '( X )':
                raise used
            break
        except too_small:
            print('\nInput kamu kurang dari 1, coba lagi')
        except too_high:
            print('\nInput kamu lebih dari 9, coba lagi')
        except used:
            print('\nTidak bisa, sudah ada isinya.')
        except ValueError:
            print('\nInput kamu bukan bilangan bulat, coba lagi ')
            continue
    board[int(posisi) - 1] = '( ' + symbol + ' )'
    check(symbol)

# set up fungsi check
menang = False
def check(symbol):
    turun1 = board[0] == '( ' + symbol + ' )' and board[3] == '( ' + symbol + ' )' and board[6] == '( ' + symbol + ' )'
    turun2 = board[1] == '( ' + symbol + ' )' and board[4] == '( ' + symbol + ' )' and board[7] == '( ' + symbol + ' )'
    turun3 = board[2] == '( ' + symbol + ' )' and board[5] == '( ' + symbol + ' )' and board[8] == '( ' + symbol + ' )'
    serong1 = board[0] == '( ' + symbol + ' )' and board[4] == '( ' + symbol + ' )' and board[8] == '( ' + symbol + ' )'
    serong2 = board[2] == '( ' + symbol + ' )' and board[4] == '( ' + symbol + ' )' and board[6] == '( ' + symbol + ' )'
    global menang
    menang = board[0:3] == ['( ' + symbol + ' )', '( ' + symbol + ' )', '( ' + symbol + ' )'] or \
              board[3:6] == ['( ' + symbol + ' )', '( ' + symbol + ' )', '( ' + symbol + ' )'] or \
              board[6:9] == ['( ' + symbol + ' )', '( ' + symbol + ' )', '( ' + symbol + ' )'] or \
              turun1 == True or \
              turun2 == True or \
              serong1 == True or \
              serong2 == True

# set up fungsi tutorial
def tutorial():
    while True:
        tutor = input('Mau baca tutorial dulu? [ya/tidak] ')
        if tutor == 'ya' or tutor == 'tidak':
            while True:
                if tutor == 'ya':
                    print('\n\
                    Tic-Tac-Toe Munyi v1.0 adalah permainan Tic-Tac-Toe original 3x3.\n\
                    Permainan ini selesai ketika ada salah satu pemain yang berhasil menyusun 3 simbolnya dalam\n\
                    satu garis horizontal, vertikal, atau diagonal.\n\
                    Kamu hanya perlu menuliskan angka yang mewakili posisi yang kamu inginkan,\n\
                    tapi hanya angka yang posisinya masih kosong ya.\n\n\
                    Angka yang mewakili posisi tersebut adalah sebagai berikut:')
                    print(tutorial_board[0:3])
                    print(tutorial_board[3:6])
                    print(tutorial_board[6:9])
                    tutor = input('\nMau baca tutorial lagi? [ya/tidak] ')
                    continue
                elif tutor == 'tidak':
                    break
                else:
                    print('\nMaksudnya? Ketik ya atau tidak.')
                    tutor = input('Mau baca tutorial lagi? [ya/tidak] ')
                    continue
            break
        else:
            print('\nMaksudnya? Ketik ya atau tidak.')
            continue

# tutorial game
tutorial()

# set up fungsi main
def main():
    global board
    global menang
    turn = 1
    giliran = random.randint(0,1)
    while menang == False and turn != 10:
        if giliran%2 == 1:
            mark(player_O, 'O')
            giliran = giliran + 1
            turn += 1

        elif giliran%2 == 0:
            mark(player_X, 'X')
            giliran = giliran + 1
            turn += 1

    # kondisi board akhir
    print('\n')
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

    # pengumuman seri
    if menang == True :
        # pengumuman pemenang
        if giliran%2 == 0:
            print('\nPemenangnya adalah ' + player_O)
        elif giliran%2 == 1:
            print('\nPemenangnya adalah ' + player_X)

    # main lagi
    while True:
        ulang = input(player_O + ' dan ' + player_X + ' mau main lagi? [ya/tidak] ')
        if ulang == 'ya' or ulang == 'tidak':
            if ulang == 'ya':
                board = ['(   )', '(   )', '(   )', '(   )', '(   )', '(   )', '(   )', '(   )', '(   )']
                menang = False
                main()
            elif ulang == 'tidak':
                print('\nTerima kasih ' + player_O + ' dan ' + player_X + '. Nanti main lagi ya!')
                break
        else:
            print('\nMaksudnya? Ketik ya atau tidak.')
            continue

# mulai game
print('\nOke, ayo kita mulai!')
main()
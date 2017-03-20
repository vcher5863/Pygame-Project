from gamelib import *

game = Game(970,540,"Practice222")

bk = Image("image\\sky2.jpg",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)
    
bird= Animation("image\\pet22.png",22,game,1200/5,1570/5,4)


while not game.over:
    game.processInput()
    bk.draw()
    bird.draw()




    game.update(60)
game.quit()
            

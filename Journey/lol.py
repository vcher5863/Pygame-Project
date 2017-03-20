from gamelib import *

game= Game(698,393,"Journey To Paradise")

bk= Image("images\\sky3.jpg",game)
bk.resizeTo(game.width, game.height)

game.setBackground(bk)

bk.draw()
game.drawText("Journey To Paradise",400,300)
game.update(1)
game.drawText("Press [SPACE] to play",600,200)
game.update(1)
game.wait(K_SPACE)

player= Image("images\\up.png",game)

birds=[]

for times in range(3):
    birds.append( Animation("images\\bird2.png",15,game,918/15,506/15,5))

for b in birds:
    b.resizeBy(-80)
    x= randint(100,700)
    y= randint(100,500)
    b.setSpeeed(3,180)
    b.moveTo(x,y)

planes=[]

for times in range(3):
    planes.append( Image("images\\plane.png",game))

for p in planes:
    p.resizeBy(-80)
    x= randint(100,700)
    y= randint(100,500)
    p.moveTo(x,y)

fuel1=[]

for times in range(3):
    fuel1.append( Image("images\\fuel1.png",game))

for f in fuel1:
    f.resizeBy(-80)
    x= randint(100,700)
    y= randint(100,500)
    f.moveTo(x,y)
    
while not game.over:
    game.processInput()
    player.draw()
    b.draw()

    if keys.Pressed[K_LEFT]:
        player.x-=5

    if keys.Pressed[K_RIGHT]:
        player.x+=5

    if keys.Pressed[K_UP]:
        player.y-=5

    if keys.Pressed[K_DOWN]:
        player.y+=5

    if player.colldiedWith(b):
        player.health-=5

    if player.collidedWith(p):
        game.over=True
        




game.update(60)
game.quit()

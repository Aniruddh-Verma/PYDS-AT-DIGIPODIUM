import pgzrun
WIDTH = 1200
HEIGHT =600

scr = 0

def gamescr(title,bgcolor='gray',info="Play The Game"):
      screen.fill(bgcolor)
      screen.draw.text(title,center = (WIDTH//2,HEIGHT//2),fontsize=100,color='white',align ='center')
      screen.draw.text(info,center = (WIDTH//2,HEIGHT//2+100),fontsize=50,color='white',align ='center')


def draw():
      if scr==0:
            gamescr('Amazing Game','black','press space to start')
            
      if scr == 1:
            gamescr(bgcolor='green',title='game is running')
            
      if scr == 2:
            gamescr('Game Over',info='press enter to restart')
            
      #screen.fill("white")
      #screen.blit("bg1",(0,0))
      pass
def update():
      global scr 
      if keyboard.SPACE and scr == 0:
            scr = 1
      elif keyboard.ESCAPE and scr == 1:
           scr = 2
      elif keyboard.RETURN and scr == 2:
            scr = 0
      print(scr)

pgzrun.go()
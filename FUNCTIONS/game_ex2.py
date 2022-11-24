import pgzrun


HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center = (WIDTH//2,HEIGHT//2))

title = "IRON-MAN GAME"

def draw():
      screen.fill('white')
      screen.draw.text(title,center=(WIDTH//2,30),fontsize = 60,
          color = 'black', align = 'center', shadow=(.2,1),scolor = "red")
      #screen.draw.text(title,(10,10),fontsize = 30,color = 'black') 
      p.draw()
def p_move():
      '''function to move player'''
      if keyboard.left or keyboard.A:
            p.x -= 3
            p.angle = 10
      elif keyboard.right or keyboard.D:
            p.x +=3
            p.angle = -10
      elif keyboard.up or keyboard.W:
            p.y -=3
      elif keyboard.down or keyboard.S:
            p.y +=3
      else:
            p.angle = 0
      pass
def handle_boundary():
      if p.x > WIDTH:
            p.x = 0
      elif p.x < 0:
            p.x = WIDTH
      elif p.y > HEIGHT:
            p.y = 0
      elif p.y < 0:
            p.y = HEIGHT

      pass

def update():
      p_move()    #function Call 
      handle_boundary()   # Function Call
      print(p.x,p.y)

pgzrun.go()
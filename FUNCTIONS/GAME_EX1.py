import pgzrun

HEIGHT = 300
WIDTH = 800

p = Actor('ironman',(100,100))   ## 100 , 100 is the cordinates of the screen 
c = Actor('cookie_img')

def draw():
      #screen.clear()
      screen.fill('white')
      p.draw()
      c.draw()


pgzrun.go()
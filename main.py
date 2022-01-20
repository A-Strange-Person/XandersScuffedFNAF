# This project has been licenced under GPLv3 with permission of the original author.

import cmu_graphics
from cmu_graphics import *
import random as r
dice = r.randint(1,3)



#####           MENUS
menu = Rect(0,0,400,400,fill='darkSlateGray')
menu.menu = 'start'
menu.gameStarted = False
menu.active = True
menu.option = 1
menu.night = 1

startButton = Label('Start',40,320,size=40,fill='yellow',align='left')

quitButton = Label('Quit',40,360,size=40,fill='darkGray',align='left')

startMenu = Group(startButton,quitButton,
    Label('Five Nights',360,60,size=60,fill='white',align='right'),
    Label("at Freddy's",360,120,size=60,fill='white',align='right'),
    Label('Scuffed Edition',360,180,size=30,fill='darkGray',align='right')
    )
    
    
    
night1 = Label('Night 1',32,80,size=30,fill='yellow',align='left')
night2 = Label('Night 2',32,120,size=30,fill='darkGray',align='left')
night3 = Label('Night 3',32,160,size=30,fill='darkGray',align='left')
night4 = Label('Night 4',32,200,size=30,fill='darkGray',align='left')
night5 = Label('Night 5',32,240,size=30,fill='darkGray',align='left')
night6 = Label('Night 6',32,280,size=30,fill='darkGray',align='left')
night7 = Label('Night 7',32,320,size=30,fill='darkGray',align='left')


menuFreddy = Circle(180,80,25,fill='sienna')
menuBonnie = Circle(180,160,25,fill='slateBlue')
menuChica  = Circle(180,240,25,fill='goldenrod')
menuFoxy   = Circle(180,320,25,fill='fireBrick')

startLevels = Label("Starting levels",260,40,fill='white')
am4Levels = Label("4AM Levels",340,40,fill='white')

start1 = Label(0,260,80,fill='white',size=40)
start2 = Label(0,260,160,fill='white',size=40)
start3 = Label(0,260,240,fill='white',size=40)
start4 = Label(0,260,320,fill='white',size=40)

am41 = Label(0,340,80,fill='white',size=40)
am42 = Label(3,340,160,fill='white',size=40)
am43 = Label(2,340,240,fill='white',size=40)
am44 = Label(2,340,320,fill='white',size=40)

selectMenu = Group(night1,night2,night3,night4,night5,night6,night7,menuFreddy,menuBonnie,menuChica,menuFoxy,startLevels,am4Levels,
    start1,start2,start3,start4,am41,am42,am43,am44
    )
selectMenu.visible = False

customFreddy = Circle(75,80 ,30,fill='sienna'   ,border='yellow'  ,borderWidth=5)
customBonnie = Circle(75,160,30,fill='slateBlue',border='darkGray',borderWidth=5)
customChica  = Circle(75,240,30,fill='goldenrod',border='darkGray',borderWidth=5)
customFoxy   = Circle(75,320,30,fill='fireBrick',border='darkGray',borderWidth=5)

freddyCustomAI = Label(0,180,80,fill='white',size=40)
bonnieCustomAI = Label(0,180,160,fill='white',size=40)
chicaCustomAI = Label(0,180,240,fill='white',size=40)
foxyCustomAI = Label(0,180,320,fill='white',size=40)

customMenu = Group(customFreddy,customBonnie,customChica,customFoxy,freddyCustomAI,bonnieCustomAI,chicaCustomAI,foxyCustomAI,
    Label('Press enter',300,260,size=20,fill='white'),
    Label('to start.',300,280,size=20,fill='white'),
    )
customMenu.visible=False



#####   Controls

def onKeyPress(key):
    
    
    
    
    #   Tells if a menu is active
    if menu.active == True:
        
        #   Tells if the menu is start
        if menu.menu == 'start':
            
            #   Tells if it's up or down for menu control
            if key == 'down' and menu.option == 1:
                startButton.fill='darkGray'
                quitButton.fill='yellow'
                menu.option += 1
                
            elif key == 'up' and menu.option == 2:
                startButton.fill ='yellow'
                quitButton.fill='darkGray'
                menu.option -= 1
            
            #   Tells if it's enter for menu control
            elif key == 'enter':
                
                if menu.option == 1:
                    startMenu.visible = False
                    menu.menu = 'select'
                    menu.option = 1
                    startButton.fill='yellow'
                    quitButton.fill='darkGray'
                    menu.active = True
                    selectMenu.visible = True
                    
                    
                elif menu.option == 2: app.stop()
            
            #   Tells if it's escape for menu control
            elif key == 'escape': app.stop()
                
        #   Tells if the menu is select
        elif menu.menu == 'select':
            
            #   Tells if it's up or down for menu control
            if menu.option == 1:
                if key == 'up': 
                    night1.fill='darkGray'
                    night7.fill='yellow'
                    menu.option = 7
                elif key == 'down':
                    night1.fill='darkGray'
                    night2.fill='yellow'
                    menu.option += 1
            elif menu.option == 2:
                if key == 'up': 
                    night2.fill='darkGray'
                    night1.fill='yellow'
                    menu.option -=1
                elif key == 'down':
                    night2.fill='darkGray'
                    night3.fill='yellow'
                    menu.option += 1        
            elif menu.option == 3:
                if key == 'up': 
                    night3.fill='darkGray'
                    night2.fill='yellow'
                    menu.option -=1
                elif key == 'down':
                    night3.fill='darkGray'
                    night4.fill='yellow'
                    menu.option += 1     
            elif menu.option == 4:
                if key == 'up': 
                    night4.fill='darkGray'
                    night3.fill='yellow'
                    menu.option -=1
                elif key == 'down':
                    night4.fill='darkGray'
                    night5.fill='yellow'
                    menu.option += 1     
            elif menu.option == 5:
                if key == 'up': 
                    night5.fill='darkGray'
                    night4.fill='yellow'
                    menu.option -=1
                elif key == 'down':
                    night5.fill='darkGray'
                    night6.fill='yellow'
                    menu.option += 1     
            elif menu.option == 6:
                if key == 'up': 
                    night6.fill='darkGray'
                    night5.fill='yellow'
                    menu.option -=1
                elif key == 'down':
                    night6.fill='darkGray'
                    night7.fill='yellow'
                    menu.option += 1     
            elif menu.option == 7:
                if key == 'up': 
                    night7.fill='darkGray'
                    night6.fill='yellow'
                    menu.option -=1
                elif key == 'down':
                    night7.fill='darkGray'
                    night1.fill='yellow'
                    menu.option = 1
            
            if night1.fill=='yellow':
                start1.value=0
                start2.value=0
                start3.value=0
                start4.value=0
                am41.value=0
                am42.value=3
                am43.value=2
                am44.value=2
                menu.night = 1
            elif night2.fill=='yellow':
                start1.value=0
                start2.value=3
                start3.value=1
                start4.value=1
                am41.value=0
                am42.value=6
                am43.value=3
                am44.value=3
                menu.night = 2
            elif night3.fill=='yellow':
                start1.value=1
                start2.value=0
                start3.value=5
                start4.value=2
                am41.value=1
                am42.value=3
                am43.value=7
                am44.value=4
                menu.night = 3
            elif night4.fill=='yellow':
                start1.value='?'
                start2.value=2
                start3.value=4
                start4.value=6
                am41.value='?'
                am42.value=5
                am43.value=6
                am44.value=8                
                menu.night = 4
            elif night5.fill=='yellow':
                start1.value=3
                start2.value=5
                start3.value=7
                start4.value=5
                am41.value=3
                am42.value=8
                am43.value=9
                am44.value=7
                menu.night = 5
            elif night6.fill=='yellow':
                start1.value=4
                start2.value=10
                start3.value=12
                start4.value=16
                am41.value=4
                am42.value=13
                am43.value=14
                am44.value=18
                menu.night = 6
            elif night7.fill=='yellow':
                start1.value='?'
                start2.value='?'
                start3.value='?'
                start4.value='?'
                am41.value='?'
                am42.value='?'
                am43.value='?'
                am44.value='?'                
                menu.night = 7
            
            if key == 'enter' and night7.fill !='yellow' and night4.fill !='yellow':startGame(start1.value,start2.value,start3.value,start4.value)
            elif key == 'enter' and night4.fill=='yellow':
                dice = r.randint(1,2)
                startGame(dice,start2.value,start3.value,start4.value)
            elif key == 'enter' and night7.fill == 'yellow':
                selectMenu.visible=False
                customMenu.visible=True
                menu.menu = 'custom'
                menu.option = 1
                
            elif key == 'escape':
                menu.option = 1
                menu.menu = 'start'
                selectMenu.visible = False
                startMenu.visible = True
        
        #   Tells if the menu is custom
        elif menu.menu == 'custom':
            if menu.option == 1:
                if key == 'up':
                    customFreddy.border='darkGray'
                    customFoxy.border  ='yellow'
                    menu.option = 4
                if key == 'down':
                    customFreddy.border='darkGray'
                    customBonnie.border='yellow'
                    menu.option = 2
            elif menu.option == 2:
                if key == 'up':
                    customBonnie.border='darkGray'
                    customFreddy.border  ='yellow'
                    menu.option -= 1
                if key == 'down':
                    customBonnie.border='darkGray'
                    customChica.border='yellow'
                    menu.option+=1
            elif menu.option == 3:
                if key == 'up':
                    customChica.border='darkGray'
                    customBonnie.border  ='yellow'
                    menu.option -= 1
                if key == 'down':
                    customChica.border='darkGray'
                    customFoxy.border='yellow'
                    menu.option+=1
            elif menu.option == 4:
                if key == 'up':
                    customFoxy.border='darkGray'
                    customChica.border  ='yellow'
                    menu.option -= 1
                if key == 'down':
                    customFoxy.border='darkGray'
                    customFreddy.border='yellow'
                    menu.option=1
            
            if key == 'left':
                if menu.option==1 and freddyCustomAI.value > 0:freddyCustomAI.value -= 1
                if menu.option==2 and bonnieCustomAI.value > 0:bonnieCustomAI.value -= 1
                if menu.option==3 and chicaCustomAI.value > 0:chicaCustomAI.value -= 1
                if menu.option==4 and foxyCustomAI.value > 0:foxyCustomAI.value -= 1
            elif key == 'right':
                if menu.option==1 and freddyCustomAI.value < 20:freddyCustomAI.value += 1
                if menu.option==2 and bonnieCustomAI.value < 20:bonnieCustomAI.value += 1
                if menu.option==3 and chicaCustomAI.value < 20:chicaCustomAI.value += 1
                if menu.option==4 and foxyCustomAI.value < 20:foxyCustomAI.value += 1
                
            elif key == 'enter':startGame(freddyCustomAI.value,bonnieCustomAI.value,chicaCustomAI.value,foxyCustomAI.value)

            elif key == 'escape':
                menu.option = 1
                menu.menu = 'select'
                selectMenu.visible = True
                customMenu.visible = False
            
#####       Rooms, cams, map, etc.

#####       Game Logic and AI
def startGame(freddyLevel,bonnieLevel,chicaLevel,foxyLevel):
    startMenu.visible = False
    selectMenu.visible = False
    customMenu.visible = False
    menu.fill = 'gainsboro'
    
    freddyAI.level=freddyLevel
    bonnieAI.level=bonnieLevel
    chicaAI.level=chicaLevel
    foxyAI.level=foxyLevel
    
    menu.gameStarted = True

class AI:
    def __init__(self,location,level,timerD):
        self.location = location
        self.level = level
        self.timerD = timerD
        self.timer = 0        
freddyAI = AI(0,0,46)
bonnieAI = AI(0,0,54)
chicaAI = AI(0,0,37)
foxyAI = AI(0,0,60)



cmu_graphics.run()

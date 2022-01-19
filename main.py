# This project has been licenced under GPLv3 with permission of the original author.

#       Final Project for Computer Science 1A                                   #
#       So, basically, I wanted to recreate game AI and challenge myself to     #
#       learn new things. I picked to learn classes due to their usefullness in #
#       AI. The specific game I chose to remake in a scuffed format was         #
#       Five Nights at Freddy's due to the simple(ish) AI and it's fun          #


#       A couple key differences here, freddy is no longer affected by cams and #
#       there is only one cam for the whole map. Power is also more forgiving   #
#       at lower usage, harsher at higher usage. Attack speeds are also diff.   #

###         Controls                                      Times                 ###

#   A for west door                                 12 AM: 3600
#   D for east door                                  1 AM: 3000
#                                                    2 AM: 2400
#   J for west light                                 3 AM: 1800
#   L for east light                                 4 AM: 1200
#                                                    5 AM:  600
#   C for cameras                                    6 AM:    0


import cmu_graphics
from cmu_graphics import *

###         AI levels                                                           ###
blueLevel = 0  # 0
yellowLevel = 5  # 5
brownLevel = 1  # 1
redLevel = 2  # 2

#       The way the ai works is that after _ seconds (different for each char.) #
#       it 'rolls a dice' between 1 and 20, and if the roll is less than or     #
#       equal to the level, the enemy can move/attack depending on conditions.  #

#       Also, I did add the 1987 easter egg(but bad), and with a changed order. #
#       So it would be blue(1),yellow(9),brown(8),red(7).                       #

#       The comments next to the levels are just the values for night 3         #


### Game Variables

app.stepsPerSecond = 10

powerLevel = Label(1, 350, 40, fill='white', size=20)
power = Label(100, 50, 40, fill='white', size=20)

power.timer = 0
power.rate = 80  # frames (seconds * 10 for 1% of power)
power.level = 1  # Pasive (1 to 5)

power.camsOn = False

timer = Label(3600, 300, 350, fill='white', size=20, align='left')

import random as r

dice = r.randint(1, 1)

### Graphical Objects

main = Rect(200, 200, 200, 150, fill='gray', border='black', borderWidth=6, align='center')
stage = Rect(main.centerX, main.top + 5, 100, 40, fill='gray', border='black', borderWidth=6, align='bottom')
back = Rect(main.left - 8, main.top, 40, 60, fill='gray', border='black', borderWidth=6, align='top-right')
cove = Rect(main.left + 6, main.bottom - 8, 50, 50, fill='gray', border='black', borderWidth=6, align='bottom-right')
northeast = Rect(main.right + 8, main.bottom, 40, 125, fill='gray', border='black', borderWidth=6, align='bottom-left')
mens = Rect(northeast.right + 8, northeast.bottom, 40, 40, fill='gray', border='black', borderWidth=6,
            align='bottom-left')
womens = Rect(northeast.right + 8, mens.top - 8, 40, 40, fill='gray', border='black', borderWidth=6,
              align='bottom-left')
west = Rect(main.centerX - 28, main.bottom + 8, 40, 125, fill='gray', border='black', borderWidth=6, align='top-right')
east = Rect(main.centerX + 28, main.bottom + 8, 40, 125, fill='gray', border='black', borderWidth=6, align='top-left')
office = Rect(main.centerX, east.bottom, 40, 40, fill='gray', border='black', borderWidth=6, align='bottom')
supply = Rect(west.left - 8, west.centerY - 20, 40, 40, fill='gray', border='black', borderWidth=6, align='right')
kitchen = Rect(east.right + 8, main.bottom + 8, 120, 75, fill='gray', border='black', borderWidth=6, align='top-left')

building = Group(main, stage, back, cove, northeast, mens, womens, west, east, office, supply, kitchen)
building.centerX = 200
building.centerY = 200

## Doors ##
backD = Line(back.right, back.top + 20, main.left, back.top + 20, lineWidth=14, fill='black')
noEaD = Line(main.right, northeast.top + 20, northeast.left, northeast.top + 20, lineWidth=20, fill='black')
mensD = Line(northeast.right, mens.centerY, mens.left, mens.centerY, lineWidth=14, fill='black')
womensD = Line(northeast.right, womens.centerY, womens.left, womens.centerY, lineWidth=14, fill='black')
kitchenD = Line(main.right - 12, kitchen.top, main.right - 12, main.bottom, lineWidth=14, fill='black')
wmD = Line(west.centerX, west.top, west.centerX, main.bottom, lineWidth=20, fill='black')
emD = Line(east.centerX, east.top, east.centerX, main.bottom, lineWidth=20, fill='black')
supplyD = Line(supply.right, supply.centerY, west.left, supply.centerY, lineWidth=14, fill='black')
WestDoor = Line(west.right, office.centerY, office.left, office.centerY, lineWidth=14, fill='red')
EastDoor = Line(east.left, office.centerY, office.right, office.centerY, lineWidth=14, fill='red')

doors = Group(backD, noEaD, mensD, womensD, kitchenD, wmD, emD, supplyD, WestDoor, EastDoor)

cover = Rect(0, 0, 400, 400, fill='black', opacity=50)

EastLight = Polygon(east.left + 6, office.top, east.right - 6, office.top - 4, east.right - 6, office.centerY + 4,
                    east.left + 6, office.centerY, fill='darkGray', visible=False)
WestLight = Polygon(west.right - 6, office.top, west.left + 6, office.top - 4, west.left + 6, office.centerY + 4,
                    west.right - 6, office.centerY, fill='darkGray', visible=False)

### Active variables (altered frequently)

WestDoor.status = False
WestDoor.light = False
EastDoor.status = False
EastDoor.light = False

kitchen.visited = False
northeast.visited = False

## Enemies ##
brown = Circle(stage.centerX, stage.centerY, 8, fill='sienna')
blue = Circle(stage.centerX - 20, stage.centerY, 8, fill='slateBlue')
yellow = Circle(stage.centerX + 20, stage.centerY, 8, fill='goldenrod')
red = Circle(cove.centerX - 8, cove.centerY, 8, fill='fireBrick')

enemies = Group(brown, blue, yellow, red)
enemies.visible = False


###     Controls and Game Over

def gameOver(screenColor, textColor):
    Rect(0, 0, 400, 400, fill=screenColor, opacity=100)
    Label('Game Over!', 200, 200, fill=textColor, size=60)
    app.stop()


def cams():
    if power.camsOn == False:
        cover.opacity = 0
        enemies.visible = True
        power.camsOn = True
        power.level += 1
        power.timer = 0
        power.value -= 1
    else:
        cover.opacity = 50
        enemies.visible = False
        power.camsOn = False
        power.level -= 1
        power.timer = 0
        power.value -= 1


def westDoor():
    if WestDoor.status == False:
        WestDoor.fill = 'forestGreen'
        WestDoor.status = True
        power.level += 1
        power.timer = 0
        power.value -= 1
    else:
        WestDoor.fill = 'red'
        WestDoor.status = False
        power.level -= 1
        power.timer = 0
        power.value -= 1


def eastDoor():
    if EastDoor.status == False:
        EastDoor.fill = 'forestGreen'
        EastDoor.status = True
        power.level += 1
        power.timer = 0
        power.value -= 1
    else:
        EastDoor.fill = 'red'
        EastDoor.status = False
        power.level -= 1
        power.timer = 0
        power.value -= 1


def westLight():
    if WestLight.visible == False:
        WestLight.visible = True
        if blueAI.location == 9:
            blue.visible = True
        else:
            blue.visible = False
        if redAI.location == 9:
            red.visible = True
        else:
            red.visible = False
        power.level += 1
        power.timer = 0
        power.value -= 1
    else:
        WestLight.visible = False
        if blueAI.location == 9:
            blue.visible = False
        else:
            blue.visible = False
        if redAI.location == 9:
            red.visible = False
        else:
            red.visible = False
        power.level -= 1
        power.timer = 0
        power.value -= 1


def eastLight():
    if EastLight.visible == False:
        EastLight.visible = True
        if yellowAI.location == 12:
            yellow.visible = True
        else:
            yellow.visible = False
        power.level += 1
        power.timer = 0
        power.value -= 1
    else:
        EastLight.visible = False
        if yellowAI.location == 12:
            yellow.visible = False
        else:
            yellow.visible = False
        power.level -= 1
        power.timer = 0
        power.value -= 1


def onKeyPress(key):
    if key == 'c' and power.value >= 0:
        cams()
    if key == 'a' and power.camsOn == False and power.value >= 0:
        westDoor()
    if key == 'd' and power.camsOn == False and power.value >= 0:
        eastDoor()
    if key == 'j' and power.camsOn == False and power.value >= 0:
        westLight()
    if key == 'l' and power.camsOn == False and power.value >= 0:
        eastLight()


###     AI

class room:
    stage = 0
    cove = 1
    main = 2
    back = 3
    bath = 4
    food = 5
    supply = 6
    westN = 7
    westS = 8
    westBli = 9
    eastN = 10
    eastS = 11
    eastBli = 12
    office = 13
    player = 14


class AI:
    def __init__(self, location, level, timerD):
        self.location = location
        self.level = level
        self.timerD = timerD
        self.timer = 0


blueAI = AI(0, blueLevel, 46)
yellowAI = AI(0, yellowLevel, 54)
brownAI = AI(0, brownLevel, 37)
redAI = AI(1, redLevel, 60)


def moveBlue():
    if blueAI.location == 0:  # if blue is at stage
        dice = r.randint(1, 3)  # roll between 1 and 3
        if dice == 1:
            blue.centerX = main.centerX - 10
            blue.centerY = main.centerY - 10
            blueAI.location = 2  # go to main

        elif dice == 2:
            blue.centerX = back.centerX + 5
            blue.centerY = back.centerY - 5
            blueAI.location = 3  # go to back

        elif dice == 3:
            blue.centerX = west.centerX - 5
            blue.centerY = west.bottom - 15
            blueAI.location = 8  # go to westS
    # if blue is at stage

    elif blueAI.location == 2:  # if blue is at main
        dice = r.randint(1, 2)  # roll between 1 and 2
        if dice == 1:
            blue.centerX = back.centerX + 5
            blue.centerY = back.centerY - 5
            blueAI.location = 3  # go to back

        elif dice == 2:
            blue.centerX = west.centerX
            blue.centerY = west.top + 15
            blueAI.location = 7  # go to westN
    # if blue is at main

    elif blueAI.location == 3:  # if blue is at back
        dice = r.randint(1, 2)  # roll between 1 and 2
        if dice == 1:
            blue.centerX = main.centerX - 10
            blue.centerY = main.centerY - 10
            blueAI.location = 2  # go to main

        elif dice == 2:
            blue.centerX = west.centerX
            blue.centerY = west.top + 15
            blueAI.location = 7  # go to westN
        # if blue is at back
    # if blue is at back

    elif blueAI.location == 7:  # if blue is at westN
        dice = r.randint(1, 2)  # roll between 1 and 2
        if dice == 1:
            blue.centerX = supply.centerX - 10
            blue.centerY = supply.centerY - 10
            blueAI.location = 6  # go to supply

        elif dice == 2:
            blue.centerX = west.centerX - 5
            blue.centerY = west.bottom - 15
            blueAI.location = 8  # go to westS
    # if blue is at westN

    elif blueAI.location == 6:  # if blue is at supply
        dice = r.randint(1, 2)  # roll between 1 and 2
        if dice == 1:
            blue.centerX = west.centerX + 10
            blue.centerY = office.centerY
            blueAI.location = 9  # go to westBli

        elif dice == 2:
            blue.centerX = west.centerX
            blue.centerY = west.top + 15
            blueAI.location = 7  # go to westN
    # if blue is at supply

    elif blueAI.location == 8:  # if blue is at westS
        dice = r.randint(1, 2)  # roll between 1 and 2
        if dice == 1:
            blue.centerX = west.centerX + 10
            blue.centerY = office.centerY
            blueAI.location = 9  # go to westBli

        elif dice == 2:
            blue.centerX = supply.centerX
            blue.centerY = supply.centerY
            blueAI.location = 6  # go to supply
    # if blue is at westS

    elif blueAI.location == 9:  # if blue is at westBli
        if WestDoor.status == False:  # if door is open
            blue.centerX = office.left + 15
            blue.centerY = office.bottom + 15
            blueAI.location = 13  # go to office

        elif WestDoor.status == True:  # if door is closed
            blue.centerX = main.centerX - 10
            blue.centerY = main.centerY - 10
            blueAI.location = 2  # go to main
    # if blue is at westBli

    elif blueAI.location == 13:  # if blue is in office and camera is down
        if power.camsOn == False:  # if camera's are down
            gameOver('slateBlue', 'fireBrick')  # kill player(blue)
        else:
            blueAI.location = 14  # go by player
    # if blue is in office

    elif blueAI.location == 14:
        gameOver('slateBlue', 'fireBrick')  # kill player
    # if blue is in office*2


def moveYellow():
    if yellowAI.location == 0:  # if yellow is at stage
        yellow.centerX = main.centerX + 20
        yellow.centerY = main.centerY
        yellowAI.location = 2  # go to main
    # if yellow is at stage

    elif yellowAI.location == 2:  # if yellow is at main
        dice = r.randint(1, 3)
        if dice == 1:
            yellow.centerX = northeast.centerX
            yellow.centerY = northeast.centerY + 20
            yellowAI.location = 4
        if dice == 2:
            yellow.centerX = kitchen.centerX
            yellow.centerY = kitchen.centerY
            yellowAI.location = 5
        if dice == 3:
            yellow.centerX = east.centerX
            yellow.centerY = east.top + 40
            yellowAI.location = 10
    # if yellow is at main

    elif yellowAI.location == 4:
        dice = r.randint(1, 2)
        if dice == 1:
            yellow.centerX = main.centerX + 20
            yellow.centerY = main.centerY
            yellowAI.location = 2
        elif dice == 2:
            yellow.centerX = kitchen.centerX
            yellow.centerY = kitchen.centerY
            yellowAI.location = 5
    # if yellow is at bath

    elif yellowAI.location == 5:  # if yellow is at food
        dice = r.randint(1, 3)
        if dice == 1:
            yellow.centerX = main.centerX + 20
            yellow.centerY = main.centerY
            yellowAI.location = 2  # go to main
        if dice == 2:
            yellow.centerX = northeast.centerX
            yellow.centerY = northeast.centerY + 20
            yellowAI.location = 4
        if dice == 3:
            yellow.centerX = east.centerX
            yellow.centerY = east.top + 40
            yellowAI.location = 10
    # if yellow is at food

    elif yellowAI.location == 10:  # if yellow is at eastN
        dice = r.randint(1, 2)
        if dice == 1:
            # eastS
            yellow.centerX = east.centerX + 5
            yellow.centerY = east.bottom - 15
            yellowAI.location = 11  # go to eastS

        if dice == 2:
            # main
            yellow.centerX = main.centerX + 20
            yellow.centerY = main.centerY
            yellowAI.location = 2  # go to main
    # if yellow is at eastN

    elif yellowAI.location == 11:  # if yellow is at eastS
        dice = r.randint(1, 2)
        if dice == 1:
            yellow.centerX = east.centerX
            yellow.centerY = east.top + 40
            yellowAI.location = 10
        if dice == 2:
            yellow.centerX = east.centerX - 10
            yellow.centerY = office.centerY
            yellowAI.location = 12  # go to eastBli
    # if yellow is at eastS

    elif yellowAI.location == 12:
        dice = r.randint(1, 2)
        if EastDoor.status == False:  # if door is open
            yellow.centerX = office.right - 15
            yellow.centerY = office.bottom + 15
            yellowAI.location = 13  # go to office

        elif EastDoor.status == True:  # if door is closed
            yellow.centerX = main.centerX + 20
            yellow.centerY = main.centerY
            yellowAI.location = 2  # go to main
    # if yellow is at eastBli

    elif yellowAI.location == 13:
        if power.camsOn == False:  # if camera's are down
            gameOver('goldenrod', 'pink')  # kill player(blue)
        else:
            blueAI.location = 14  # go by player
    # if yellow is in office

    elif yellowAI.location == 14:
        gameOver('goldenrod', 'pink')  # kill player
    # if yellow is in office*2


def moveBrown():
    if brownAI.location == 0:
        brown.centerX = main.centerX + 50
        brown.centerY = main.centerY + 20
        brownAI.location = 2
    # if brown is at stage

    elif brownAI.location == 2:
        dice = r.randint(1, 3)
        if dice == 1 and kitchen.visited == False:
            brown.centerX = kitchen.left + 50
            brown.centerY = kitchen.bottom - 30
            brownAI.location = 5
            kitchen.visited = True
        elif dice == 2 and northeast.visited == False:
            brown.centerX = womens.centerX
            brown.centerY = womens.centerY
            brownAI.location = 4
            northeast.visited = True
        elif dice == 3:
            brown.centerX = east.right - 20
            brown.centerY = east.top + 20
            brownAI.location = 10
    # if brown is at main

    elif brownAI.location == 4:
        brown.centerX = main.centerX + 50
        brown.centerY = main.centerY + 20
        brownAI.location = 2
    # if brown is at bath

    elif brownAI.location == 5:
        brown.centerX = main.centerX + 50
        brown.centerY = main.centerY + 20
        brownAI.location = 2
    # if brown is at kitchen

    elif brownAI.location == 10:
        brown.centerX = east.left + 20
        brown.centerY = east.bottom - 20
        brownAI.location = 11
    # if brown is at eastN

    elif brownAI.location == 11:
        if EastDoor.status == True:
            brown.centerX = main.centerX + 50
            brown.centerY = main.centerY + 20
            brownAI.location = 2
            kitchen.visited = False
            northeast.visited = False
        else:
            brownAI.location = 13
    # if brown is at eastN

    elif brownAI.location == 13:
        gameOver('sienna', 'tan')
    # if brown is in office


def moveRed():
    if redAI.location == 1:
        red.centerX += 8
        redAI.location = 15
    elif redAI.location == 15:
        red.centerX += 8
        redAI.location = 16
    elif redAI.location == 16:
        red.centerX += 8
        redAI.location = 17
    elif redAI.location == 17:
        red.centerX += 8
        redAI.location = 18
    elif redAI.location == 18:
        red.centerX += 8
        redAI.location = 19
    elif redAI.location == 19:
        red.centerX = west.left + 20
        red.centerY = office.centerY
        redAI.location == 9
        if WestDoor.status == False:
            gameOver('fireBrick', 'tan')
        else:
            red.centerX = cove.centerX - 8
            red.centerY = cove.centerY
            redAI.location = 1


### Frame stuff

def onStep():
    if power.level == 1:
        power.rate = 96
    elif power.level == 2:
        power.rate = 54
    elif power.level == 3:
        power.rate = 48
    elif power.level == 4:
        power.rate = 42
    elif power.level == 5:
        power.rate = 36
    elif power.level == 6:
        power.rate = 30

    power.timer += 1
    if power.timer == power.rate:
        power.timer = 0
        if power.value >= 1: power.value -= 1

    blueAI.timer += 1
    if blueAI.timer == blueAI.timerD:
        blueAI.timer = 0
        dice = r.randint(1, 20)
        if blueAI.level >= dice: moveBlue()

    yellowAI.timer += 1
    if yellowAI.timer == yellowAI.timerD:
        yellowAI.timer = 0
        dice = r.randint(1, 20)
        if yellowAI.level >= dice: moveYellow()

    brownAI.timer += 1
    if brownAI.timer == brownAI.timerD:
        brownAI.timer = 0
        dice = r.randint(1, 20)
        if brownAI.level >= dice: moveBrown()

    redAI.timer += 1
    if power.camsOn == True: redAI.Timer = 0
    if redAI.timer == redAI.timerD:
        redAI.timer = 0
        dice = r.randint(1, 20)
        if redAI.level >= dice and power.camsOn == False:
            moveRed()
        else:
            pass

    if blueAI.location == 9 and WestLight.visible == False:
        blue.visible = False
    elif power.camsOn == True and blueAI.location != 9:
        blue.visible = True
    if redAI.location == 9 and WestLight.visible == False:
        red.visible = False
    elif power.camsOn == True and redAI.location != 9:
        red.visible = True
    if yellowAI.location == 12 and EastLight.visible == False:
        yellow.visible = False
    elif power.camsOn == True and yellowAI.location != 12:
        yellow.visible = True

    if power.value <= 0:
        blueAI.level = 0
        yellowAI.level = 0
        redAI.level = 0
        if WestDoor.status == True: westDoor()
        if EastDoor.status == True: eastDoor()
        if power.camsOn == True: cams()
        if WestLight.visible == True: westLight()
        if EastLight.visible == True: eastLight()

    powerLevel.value = power.level

    timer.value -= 1

    if timer.value == 3000:  # 1 am
        pass
    elif timer.value == 2400:  # 2 am
        blueAI.level += 1
    elif timer.value == 1800:  # 3 am
        blueAI.level += 1
        yellowAI.level += 1
        redAI.level += 1
    elif timer.value == 1200:  # 4 am
        blueAI.level += 1
        yellowAI.level += 1
        redAI.level += 1
    elif timer.value == 600:  # 5 am
        pass
    elif timer.value == 0:
        Rect(0, 0, 400, 400)
        Label('You Win!', 200, 200, size=60, fill='white')
        app.stop()


### misc.

power.toFront()
timer.toFront()
powerLevel.toFront()
if blueLevel == 1 and yellowLevel == 9 and brownLevel == 8 and redLevel == 7:
    gameOver('yellow', 'black')

cmu_graphics.run()

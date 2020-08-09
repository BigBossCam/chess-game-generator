import random
import argparse

parser = argparse.ArgumentParser(description="Generate a random game of chess.")
parser.add_argument("-u", "--unlimited", action="store_true", help="Set no time limit.")
parser.add_argument("-i", "--increment", action="store_true", help="Set no increment varible.")
parser.add_argument("-b", "--bullet", action="store_true", help="Set no bullet modes.")
args = parser.parse_args()


def setGame(gameMode, timeMode, gameTime, incrementTime):

    if gameTime is None:
        gameTime = "None"
    else:
        gameTime = str(gameTime)

    if incrementTime is None:
        incrementTime = "None"
    else:
        incrementTime = str(incrementTime)

    print("The gamemode is: " + gameMode + ".\n The time mode is: " + timeMode + ".\n With " + gameTime + " minutes per side.\n The time increment is: " + incrementTime)


def main():

    modes = [
        "Standard",
        "Crazyhouse",
        "Chess960",
        "King of the Hill",
        "Three-check",
        "Antichess",
        "Atomic",
        "Horde",
        "Racing Kings"
    ]

    time = [
        "Ultra Bullet",
        "Bullet",
        "Realtime Classical",
        "Blitz",
        "Rapid",
        "Unlimited"
    ]

    gameMode = random.choice(modes)
    timeMode = None
    gameTime = None
    incrementTime = None

    if args.unlimited:
        setGame(gameMode, timeMode, gameTime, incrementTime)
    else:
        timeMode = random.choice(time)
        if timeMode != "Unlimited":
            gameTime = random.randint(0, 180)
        else:
            gameTime = "no"

        if args.increment is not True:

            if args.bullet is not True:
                
                if timeMode == "Ultra Bullet":
                    gameTime = random.randint(0, 1)
                    incrementTime = random.randint(0, 1)

                if timeMode == "Bullet":
                    gameTime = random.randint(1, 3)
                    incrementTime = random.randint(1, 3)

            if timeMode == "Blitz":
                gameTime = random.randint(3, 8)
                incrementTime = random.randint(1, 5)

            if timeMode == "Rapid":
                gameTime = random.randint(9, 25)
                incrementTime = random.randint(5, 30)

            if timeMode == "Realtime Classical":
                gameTime = random.randint(25, 180)
                incrementTime = random.randint(30, 180)

        setGame(gameMode, timeMode, gameTime, incrementTime)

if __name__ == '__main__':
    main()

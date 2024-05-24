import time
import random
class streamer():
    def __init__(self,grasstouchtime,age,weight,height,iq,wealth,mood):
        self.grasstouchtime = grasstouchtime
        self.age = age
        self.weight = weight
        self.height = height
        self.iq = iq
        self.wealth = wealth

class fitstreamer(streamer):
    def __init__(self, grasstouchtime, age, weight, height, iq,wealth, gymtime,gymtimedays,mood):
        super().__init__(grasstouchtime, age, weight, height, iq,wealth,mood)
        self.gymtime = gymtime
        self.gymtimedays = gymtimedays
        self.mood = mood
    def gotogym(self):
        for _ in range(15):  
            print("\rbuilding muscles... <" + "=" * _ + ">", end="", flush=True) 
            time.sleep(0.2)
        print("gym day complete!")

        self.gymtime += 3.5
        self.mood += 3
        self.weight -= 0.150
        if self.gymtime > 24:
            self.gymtimedays += 1
            self.gymtime = 0
        time.sleep(0.5)
        print(f"""now you have {self.gymtimedays} days and {self.gymtime} hours, you'll be jacked if you do it regularly!
                  And you got in a better mood -> {self.mood} (+3 p.)""")
        time.sleep(3)

    def info(self):
        print(f"""Let me show you your stats --> you weigh {self.weight},
               your age is {self.age} your height {self.weight} kilos,
               your iq is {self.iq}
               you have {self.wealth} dollars floating in your bank acc.
               you've been in gym for {self.gymtimedays} days and {self.gymtime} hours
               you have {self.mood} mood points""")
        time.sleep(3)

    def stream(self):
        print("alright, camera adjusted, and done!")
        time.sleep(0.5)
        for _ in range(15):  
            print("\rstreaming... <" + "=" * _ + ">", end="", flush=True) 
            time.sleep(0.2)
        print("Stream Done!")
        rand = random.randint(-5,10)
        self.mood += rand
        randdonos = random.randint(150,2000)
        self.wealth += randdonos
        if rand <= 3:
            print(f"you've been harassed and didn't win much games, bad stream")
        elif rand == 5:
            print("you had a normal stream, chat didn't harass him but it wasn't too fun or too bad, he did some clutches")
        elif rand == 4:
            print("the stream was kinda mid, so not too bad, but some people harassed you in chat")
        elif rand > 6:
            print("the stream was good, lotta wins, good comments, a perfect stream  for a cup of tea")
        else:
            print("i don't even know so just look at the stats below")
        time.sleep(2)
        print(f"""you have {self.mood} mood points, may or may not be good
                  you've got {rand} mood points from the stream, and you got {randdonos} bucks from the stream""")
        time.sleep(3)

    def eat(self):
        for _ in range(15):  
            print("\reating... <" + "=" * _ + ">", end="", flush=True) 
            time.sleep(0.2)

        print("you've had a nice meal!")
        rand = random.uniform(0.150,0.568)
        rand = round(rand,3)
        self.weight += rand
        print(f"now you weigh {rand} more, you weight {self.weight}")
        time.sleep(1.3)

    def dodishes(self):
        if self.mood >= 10:
            print("you're not in right mood to do the dishes right now")
            time.sleep(1.3)
        else:
            for _ in range(15):  
                print("\rdoing dishes... <" + "=" * _ + ">", end="", flush=True) 
                time.sleep(0.2)
                print("dishes done!")
                self.mood += 1 #hide it as a secret
                self.gymtime += 0.5 #this too
                time.sleep(0.8)
                print("...You feel some kind of weird relief.")
                time.sleep(1.3)
fortnitegod = fitstreamer(0,25,60,175,110,5050.60,12,10,10)

def start():
    
    print("Hello! This is a streamer simulator, enjoy!")
    time.sleep(1.5)
    while True:
        print("""Please choose one of the options
             
                        1 - info                   
                        2 - stream
                        3 - go to gym
                        4 - eat
                        5 - do the dishes""")
        time.sleep(0.5)
        print("Be careful, stream option might be damaging!")
        time.sleep(0.7)
        option = input("please choose an operating number\n")
        if option == "1":
            fortnitegod.info()
        elif option == "2":
            fortnitegod.stream()
        elif option == "3":
            fortnitegod.gotogym()
        elif option == "4":
            fortnitegod.eat()
        elif option == "5":
            fortnitegod.dodishes()
        else:
            print("wrong number, try again")

start()
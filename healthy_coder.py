from time import time
from pygame import mixer
from datetime import datetime


def alarm(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    stop=input(f"write {stopper} to stop alarm : ")
    while True:
        if stop==stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("log.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    initial_water=time()
    initial_eye_exercise = time()
    initial_physical_exercise = time()
    drink_water=15*60
    eye_exercise=30*60
    physical_exercise=50*60
    while(True):
        if (time()-initial_water)>=drink_water:
            print("Time to drink water")
            alarm("D:\phone storGE\download\y2mate.com - Rain Sound Effect Short  Rain in Nature.mp3","drank")
            initial_water=time()
            log("drank water")

        if (time()-initial_eye_exercise)>=eye_exercise:
            print("Time to eye exercise")
            alarm("D:\phone storGE\download\y2mate.com - Cartoon Rapid Eye Blinks  Sound effect.mp3","eydone")
            initial_eye_exercise=time()
            log("eye exercise done")


        if (time()-initial_physical_exercise)>=physical_exercise:
            print("Time to physical exercise")
            alarm("D:\phone storGE\download\y2mate.com - Carton Falling Sound EffectCopyright Free.mp3","pydone")
            initial_physical_exercise=time()
            log("physical exercise done")
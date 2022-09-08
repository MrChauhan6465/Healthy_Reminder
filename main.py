import datetime
import time
from pygame import mixer

def Music_on(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000)
    while True:
        user_command = input()
        if user_command ==stopper:
            mixer.music.stop()
            break

def file_logs(msg):
    with open("healthy.txt",'a') as f:
        f.write(f"{msg} {datetime.datetime.now()} \n")

if __name__ == '__main__':
    initial_water_time = time.time()
    intitial_eyes_time = time.time()
    initial_exercise_time =time.time()

    water_seconds = 1800
    eyes_seconds = 2700
    exercise_seconds = 3600
 
    while True:

        if time.time() - initial_water_time > water_seconds:
            print("====>>>It's Drinking  water  time champ  \n =====>>Enter dranked to stop the reminder \n ")
            Music_on('water_tune.mp3',"dranked")
            initial_water_time  = time.time()
            file_logs("Water dranked at the time : ")

        
        if time.time() - intitial_eyes_time >eyes_seconds:
            print("====>>> It's Eyes relax time \n Enter eyesrelaxed to stop the reminder :\n")

            Music_on('eye.mp3',"eyesrelaxed")
            intitial_eyes_time = time.time()
            file_logs("Eyes are relaxed at the time : ")
  
        if time.time() - initial_exercise_time >exercise_seconds:
            print("====>>> It's Exercise time bhai\n Enter exercised to stop the reminder :\n")

            Music_on('exercise.mp3',"exercised")
            intitial_exercis_time = time.time()
            file_logs("Exercised at the time : ")  
              
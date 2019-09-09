import rtmidi
import time
import sys
from os import system
import random

try:
    input = raw_input
except NameError:
    StandardError = Exception

if rtmidi.API_WINDOWS_MM in rtmidi.get_compiled_api():
    midiout = rtmidi.MidiOut()
    ports = midiout.get_ports()

    if not ports:
        print("No MIDI ports found.")
    else:
        print("Available MIDI devices:\n")
        for port, name in enumerate(ports):
            print("\t[%i] %s" % (port, name))
    
        reply = input("\nChoose Device: ")
        try:
            val = int(reply)
        except ValueError:
            print("Only Numbers Allowed")
        system('cls') 
        midiout.open_port(val)
        print("Demo Modes:\n\n\t[0] Every Other\n\t[1] Fast Wave\n\t[2] Slow Wave\n\t[3] Line\n\t[4] 1 Up\n\t[5] Exponential\n\t[6] Spike Fall\n\t[7] Lights Only\n\t[8] Full Demo")
        reply = input("\nChoose Mode: ")
        try:
            a = int(reply)
        except ValueError:
            print("Only Numbers Allowed")
        system('cls') 
        print("Press 'Ctrl + C' to end.")
        i = [0]

        def randomLight():
            button = random.randint(28,44)
            if button == 32:
                button = 55
            state = random.randint(0,1)
            if state == 1:
                state = 127
            midiout.send_message([0xB0, int(button), int(state)])
        def fadeI(i):
            if len(period)-1 == i[0]:
                i[0] = 0
            else:
                i[0] += 1
        def mardiGrasLights():
            midiout.send_message([0xB0, 1, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 2, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 3, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 4, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 5, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 6, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 7, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 8, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 9, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 10, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 11, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 12, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 13, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 14, period[i[0]]])
            fadeI(i)
            randomLight()
            midiout.send_message([0xB0, 27, period[i[0]]])
            fadeI(i)
            randomLight()
            time.sleep(clock)
        def mardiGras():
            midiout.send_message([0xB0, 1, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 2, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 3, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 4, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 5, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 6, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 7, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 8, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 9, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 10, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 11, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 12, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 13, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 14, period[i[0]]])
            fadeI(i)
            midiout.send_message([0xB0, 27, period[i[0]]])
            fadeI(i)
            time.sleep(clock)
        # Every Other
        if a == 0:
            period = [0, 127]
            clock = float(0.14)
            try:
                while True:
                    mardiGrasLights()
            except KeyboardInterrupt:
                pass
        # Fast Wave
        elif a == 1:
            period = [0, 42, 84, 126, 84, 42, 0]
            clock = float(0.07)
            try:
                while True:
                    mardiGrasLights()
            except KeyboardInterrupt:
                pass
        # Slow Wave
        elif a == 2:
            period = [0, 16, 32, 48, 64, 80, 96, 112, 127, 112, 96, 80, 64, 48, 32, 16]
            clock = float(0.01)
            try:
                while True:
                    mardiGras()
            except KeyboardInterrupt:
                pass
        # Line
        elif a == 3:
            period = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 127, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
            clock = float(0.03)
            try:
                while True:
                    midiout.send_message([0xB0, 1, period[i[0]]])
                    midiout.send_message([0xB0, 2, period[i[0]]])
                    midiout.send_message([0xB0, 3, period[i[0]]])
                    midiout.send_message([0xB0, 4, period[i[0]]])
                    midiout.send_message([0xB0, 5, period[i[0]]])
                    midiout.send_message([0xB0, 6, period[i[0]]])
                    midiout.send_message([0xB0, 7, period[i[0]]])
                    midiout.send_message([0xB0, 8, period[i[0]]])
                    midiout.send_message([0xB0, 9, period[i[0]]])
                    midiout.send_message([0xB0, 10, period[i[0]]])
                    midiout.send_message([0xB0, 11, period[i[0]]])
                    midiout.send_message([0xB0, 12, period[i[0]]])
                    midiout.send_message([0xB0, 13, period[i[0]]])
                    midiout.send_message([0xB0, 14, period[i[0]]])
                    midiout.send_message([0xB0, 27, period[i[0]]])
                    fadeI(i)
                    time.sleep(clock)
            except KeyboardInterrupt:
                pass
        # 1 Up
        elif a == 4:
            period = [0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            clock = float(0.08)
            try:
                while True:
                    mardiGrasLights()
            except KeyboardInterrupt:
                pass
        # Exponential
        elif a == 5:
            period = [127, 127, 127, 127, 127, 84, 42, 0, 0, 0, 0, 0, 42, 84]
            clock = float(0.08)
            try:
                while True:
                    mardiGrasLights()
            except KeyboardInterrupt:
                pass
        # Spike & Fall
        elif a == 6:
            period = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 127]
            clock = float(0.11)
            try:
                while True:
                    mardiGrasLights()
            except KeyboardInterrupt:
                pass
        # Lights Only      
        elif a == 7:
            clock = float(0.11)
            try:
                while True:
                    randomLight()
                    time.sleep(clock)
            except KeyboardInterrupt:
                pass
        # Full Demo Cycle       
        else:
            try:
                try:
                    while True:
                        t_end = time.time() + 3
                        while time.time() < t_end:
                            period = [0, 127]
                            clock = float(0.14)
                            mardiGrasLights()
                        t_end = time.time() + 3
                        while time.time() < t_end:
                            period = [0, 42, 84, 126, 84, 42, 0]
                            clock = float(0.07)
                            mardiGrasLights()
                        t_end = time.time() + 2
                        while time.time() < t_end:
                            period = [0, 16, 32, 48, 64, 80, 96, 112, 127, 112, 96, 80, 64, 48, 32, 16]
                            clock = float(0.01)
                            mardiGras()
                        t_end = time.time() + 2
                        while time.time() < t_end:
                            period = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 127, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
                            clock = float(0.03)
                            midiout.send_message([0xB0, 1, period[i[0]]])
                            midiout.send_message([0xB0, 2, period[i[0]]])
                            midiout.send_message([0xB0, 3, period[i[0]]])
                            midiout.send_message([0xB0, 4, period[i[0]]])
                            midiout.send_message([0xB0, 5, period[i[0]]])
                            midiout.send_message([0xB0, 6, period[i[0]]])
                            midiout.send_message([0xB0, 7, period[i[0]]])
                            midiout.send_message([0xB0, 8, period[i[0]]])
                            midiout.send_message([0xB0, 9, period[i[0]]])
                            midiout.send_message([0xB0, 10, period[i[0]]])
                            midiout.send_message([0xB0, 11, period[i[0]]])
                            midiout.send_message([0xB0, 12, period[i[0]]])
                            midiout.send_message([0xB0, 13, period[i[0]]])
                            midiout.send_message([0xB0, 14, period[i[0]]])
                            midiout.send_message([0xB0, 27, period[i[0]]])
                            fadeI(i)
                            time.sleep(clock)
                        t_end = time.time() + 4
                        while time.time() < t_end:
                            period = [0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                            clock = float(0.08)
                            mardiGrasLights()
                        t_end = time.time() + 4
                        while time.time() < t_end:
                            period = [127, 127, 127, 127, 127, 84, 42, 0, 0, 0, 0, 0, 42, 84]
                            clock = float(0.08)
                            mardiGrasLights()
                        t_end = time.time() + 2
                        while time.time() < t_end:
                            period = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 127]
                            clock = float(0.11)
                            mardiGrasLights()
                        i = [0]
                except KeyboardInterrupt:
                    pass
            except KeyboardInterrupt:
                pass
        
        print('')
        del midiout

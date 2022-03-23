from psychopy.visual import Window, TextStim
from psychopy.core import Clock, quit, wait
from psychopy.gui import DlgFromDict
from psychopy.hardware import keyboard
from psychopy.event import Mouse

#gui_participant_monitor
exp_info = {'participant_nr': '', 'age': ''}  # no default!
title = 'emo-stroop experiment'
dlg = DlgFromDict(exp_info, title)

if not dlg.OK:
    # Maybe add a nice print statement?
    print("User pressed 'Cancel'!")
    quit()
else:
    # Quit when either the participant nr or age is not filled in
    if not exp_info['participant_nr'] or not exp_info['age']:
        quit()
    if int(exp_info['participant_nr']) > 99 or int(exp_info['age']) < 18:
        quit()
    else:
        print('Started the experiment for participant', exp_info['participant_nr'], 'with age', exp_info['age'])

#Window
my_win = Window(size=(400, 800), color=[-1.0, -1.0, -1.0], colorSpace='rgb', fullscr=True, monitor='laptop' )

#mouse
mouse = Mouse(visible=False)

#clock
clock = Clock()

#keyboard
kb = keyboard.Keyboard()

### START BODY OF EXPERIMENT ###

#welcome
welcome_txt= TextStim(my_win, text="Welcome to this experiment", font='Calibri', height=0.1, color=[-1.0, -1.0, 1.0])
welcome_txt.autoDraw = True
my_win.flip()
wait(2.0)
welcome_txt.text = "Experiment begins in 5 second"
my_win.flip()
wait(2.0)
welcome_txt.autoDraw = False

#instruction to exp
instruct_txt_stim = TextStim(my_win , text=""""In this experiment, you will see emotional faces (either happy or 
angry) with a word above the image (either “happy” or “angry”). Importantly, you need to respond to the EXPRESSION of 
the face and ignore the word. You respond with the arrow keys:" 
                                        
            HAPPY expression = left
            ANGRY expression = right
                                        
  (Press ‘space’ to start the experiment!)""")
instruct_txt_stim.autoDraw = True
my_win.flip()
wait(2)

while True:
    keys = kb.getKeys()
    if "space" in keys:
        break
instruct_txt_stim.autoDraw = False


### END BODY OF EXPERIMENT ###
my_win.close()
quit()
import PySimpleGUI as sg
from pygame import mixer


"""
This program was made by Daniel Izm 
Last Updated: 14/5/22

"""


sg.theme('DarkBrown4')
alarm = False
mixer.init()
sound1 = mixer.Sound("alarm.mp3")
sound1.set_volume(0.2)

def main():
    centered_column = [[sg.T(('Set Time to Study'), font=('Consolas', 20))],
                       [sg.T((''), font=('Consolas', 20), key='countdown')],
                       [sg.B('Exit'),
                        sg.B('Start/Stop')],  # Buttons For Timer
                       [sg.B('Pomodoro'),
                        sg.B('Short Break'),
                        sg.B('Long Break')
                        ],
                       [sg.Input(key="IN")],
                       [sg.B("Set Pomodoro Time"),
                        sg.B("Set Short Break Time"),
                        sg.B("Set Long Break Time")]]


    layout = [[sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
              [sg.Text('', pad=(0, 0), key='-EXPAND2-'),  # the thing that expands from left
               sg.Column(centered_column, vertical_alignment='center', justification='center', k='-C-')]]

    window = sg.Window('StudyWare Timer', layout, size=(500, 300), grab_anywhere=True, resizable=False, finalize=True)
    window['-C-'].expand(True, True, True)
    window['-EXPAND-'].expand(True, True, True)
    window['-EXPAND2-'].expand(True, False, True)



    active = False
    value = 0

    sound_remains_seconds = 0

    while True:
        event, values = window.Read(timeout=1000)
        # print(event, values)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        m, s = divmod(value, 60)    #This formats the timer portion
        h, m = divmod(m, 60)

        timerx = "%02d:%02d:%02d" % (h, m, s)




        if event == 'Pomodoro':                     #these are events for selecting the type of mode
            # active = not active
            value = 1500
            window.Element('countdown').Update(value=timerx)
            sound_remains_seconds = 1509

        if event == 'Short Break':
            # active = not active
            value = 300
            window.Element('countdown').Update(value=timerx)
            sound_remains_seconds = 309
        if event == 'Long Break':
            # active = not active
            value = 900
            window.Element('countdown').Update(value=timerx)
            sound_remains_seconds = 909
        if event == 'Start/Stop':
            active = not active
            sound1.stop()

        if event == '__TIMEOUT__' and active:
            if value > 0:
                window.Element('countdown').Update(value=timerx)
            value -= 1
            sound_remains_seconds -= 1
            if value == 0:
                sound1.play(-1)

        if sound_remains_seconds == 0:
            sound1.stop()

        if event == "Set Pomodoro Time":
            pass



        window.refresh()




if __name__ == '__main__':
    main()


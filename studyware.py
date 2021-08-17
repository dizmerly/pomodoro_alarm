import PySimpleGUI as sg
import time
import winsound

duration = 500  # milliseconds
freq = 100  # Hz





sg.theme('DarkBrown4')
def main():


    centered_column = [[sg.T(('Set Time to Study'), font=('Consolas', 20))],
           [sg.T((''), font=('Consolas', 20), key='countdown')],
           [sg.B('Exit'),
            sg.B('Start/Stop')], #Buttons For Timer
           [sg.B('Pomodoro'),
           sg.B('Short Break'),
            sg.B('Long Break')
            ]]




    layout = [[sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
            [sg.Text('', pad=(0, 0), key='-EXPAND2-'),  # the thing that expands from left
               sg.Column(centered_column, vertical_alignment='center', justification='center', k='-C-')]]


    window = sg.Window('StudyWare Timer', layout, size=(400,200), grab_anywhere=True, resizable=True, finalize=True)
    window['-C-'].expand(True, True, True)
    window['-EXPAND-'].expand(True, True, True)
    window['-EXPAND2-'].expand(True, False, True)


    active = False
    value = 0



    while True:
        event, values = window.Read(timeout=1000)
        #print(event, values)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        m, s = divmod(value, 60)
        timerx = "%02d:%02d" % (m, s)

        if event == 'Pomodoro':
            #active = not active
            value = 1500
            window.Element('countdown').Update(value=timerx)

        if event == 'Short Break':
            #active = not active
            value = 300
            window.Element('countdown').Update(value=timerx)
        if event == 'Long Break':
            #active = not active
            value = 900
            window.Element('countdown').Update(value=timerx)
        if event == 'Start/Stop':
            active = not active





        if event == '__TIMEOUT__' and active:
            window.Element('countdown').Update(value=timerx)
            value -= 1
            if value == -1:
                active = not active
                winsound.Beep(freq, duration)

    window.refresh()


if __name__ == '__main__':
    main()








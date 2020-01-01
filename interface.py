import tkinter as tk
from time import strftime, time, sleep
from playsound import playsound
from threading import Thread

alarm_database = []


def set_alarm():

    while True:

        if strftime("%H:%M") in alarm_database:
            playsound("alarm.mp3")
            alarm_database.remove(strftime("%H:%M"))
            main_listbox.itemconfig(main_listbox.get(
                0, "end").index(strftime("%H:%M")), bg='red')


def save_alarms():
    '''
    Listbox soll aus der alarm_database generiert werden. Dazu brauch jeder alarm noch ein Argument ON/OFF
    für die Färbung in der Listbox.

    '''

    new_alarm = alarm_input.get()
    alarm_input.delete(0, tk.END)

    if new_alarm not in alarm_database:

        alarm_database.append(new_alarm)
        main_listbox.insert(tk.END, f"{new_alarm}", )
        #listbox.insert(END, *strings)
        main_listbox.itemconfig(main_listbox.size() - 1, bg='green')

    if not background_thread.is_alive():
        background_thread.start()


def turn_on_alarm():
    index = main_listbox.curselection()
    main_listbox.itemconfig(index, bg='green')
    alarm_database.append(main_listbox.get(index))
    main_listbox.select_clear(0, 'end')
    if not background_thread.is_alive():
        background_thread.start()


def turn_off_alarm():
    index = main_listbox.curselection()
    main_listbox.itemconfig(index, bg='red')
    del alarm_database[index[0]]
    main_listbox.select_clear(0, 'end')
    if not background_thread.is_alive():
        background_thread.start()


def delet_alarm():
    index = main_listbox.curselection()
    main_listbox.delete(index[0])
    del alarm_database[index[0]]
    if not background_thread.is_alive():
        background_thread.start()


# creating the window
window = tk.Tk()
window.title("ALARM CLOCK")

top_frame = tk.Frame(window)
top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)
middle_frame = tk.Frame(window)
middle_frame.pack(side=tk.BOTTOM)


# widgets
tk.Label(top_frame, text="Alarm (hh:mm)").pack()
alarm_input = tk.Entry(top_frame)
alarm_input.pack()

button = tk.Button(top_frame, text="SAVE", command=save_alarms)
button.pack()

main_listbox = tk.Listbox(middle_frame, height=5)
#main_listbox.insert(tk.END, "Alarms \n")
main_listbox.pack()

button_1 = tk.Button(bottom_frame, text="ON", command=turn_on_alarm)
button_1.pack(side=tk.LEFT)
button_2 = tk.Button(bottom_frame, text="OFF", command=turn_off_alarm)
button_2.pack(side=tk.LEFT)
button_3 = tk.Button(bottom_frame, text="DELET", command=delet_alarm)
button_3.pack(side=tk.LEFT)

background_thread = Thread(target=set_alarm)

window.mainloop()

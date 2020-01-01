import tkinter as tk
from time import strftime, time, sleep
from playsound import playsound
from threading import Thread

alarm_database = []


def set_alarm():

    while True:

        i = 0
        for alarm, status in alarm_database:

            if (alarm == strftime("%H:%M")) and (status == "ON"):
                playsound("alarm.mp3")
                alarm_database[i] = (alarm, "OFF")

            else:
                sleep(1)
            i += 1
        update_listbox()


def save_alarm():

    new_alarm = input_widget.get()
    input_widget.delete(0, tk.END)

    if new_alarm not in alarm_database:
        alarm_database.append((new_alarm, "ON"))
        update_listbox()

        if not background_thread.is_alive():
            background_thread.start()


def update_listbox():
    main_listbox.delete(0, tk.END)
    main_listbox.insert(tk.END, *[i[0] for i in alarm_database])

    i = 0
    for _, status in alarm_database:

        if status == "ON":
            main_listbox.itemconfig(i, bg='green')

        else:
            main_listbox.itemconfig(i, bg='red')

        i += 1


def turn_on_alarm():
    index = main_listbox.curselection()

    if alarm_database[index[0]][1] == "OFF":
        main_listbox.itemconfig(index, bg='green')
        alarm_database[index[0]] = (main_listbox.get(index), "ON")
        update_listbox()

    main_listbox.select_clear(0, 'end')


def turn_off_alarm():
    index = main_listbox.curselection()

    if alarm_database[index[0]][1] == "ON":
        main_listbox.itemconfig(index, bg='red')
        alarm_database[index[0]] = (main_listbox.get(index), "OFF")
        update_listbox()

    main_listbox.select_clear(0, 'end')


def delet_alarm():
    index = main_listbox.curselection()
    del alarm_database[index[0]]
    update_listbox()


window = tk.Tk()
window.title("ALARM CLOCK")

top_frame = tk.Frame(window)
top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)
middle_frame = tk.Frame(window)
middle_frame.pack(side=tk.BOTTOM)

tk.Label(top_frame, text="Alarm (hh:mm)").pack()
input_widget = tk.Entry(top_frame)
input_widget.pack()

button = tk.Button(top_frame, text="SAVE", command=save_alarm)
button.pack()

main_listbox = tk.Listbox(middle_frame, height=5)
main_listbox.pack()

button_1 = tk.Button(bottom_frame, text="ON", command=turn_on_alarm)
button_1.pack(side=tk.LEFT)
button_2 = tk.Button(bottom_frame, text="OFF", command=turn_off_alarm)
button_2.pack(side=tk.LEFT)
button_3 = tk.Button(bottom_frame, text="DELET", command=delet_alarm)
button_3.pack(side=tk.LEFT)

background_thread = Thread(target=set_alarm)

window.mainloop()

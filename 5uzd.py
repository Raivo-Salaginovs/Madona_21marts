logs=sg.Window('logs', dalas,size=(1000,1000))

while True:
    event, values=logs.read()

    if event == sg.WINDOW_CLOSED or event == 'close':
        break
    elif event == 'about':
        sg.popup('Info')

    elif event =='OK':
        vards=values['-vards-']
        uzvards=values['-uzvārds-']
        diena=values['-diena-']
        menesis=values['-menesis-'].lower()
        gads=values['-gads-']
    
    logs['vieta'].update(f"{vards}{uzvards} - Dzimšanas datums {diena}.{menesis}.{gads}")

    if values["-ja-"]==True:
        logs["-vieta1-"].update(f"Ir apguvis checkbox izveidošanu")
    if values["-ne-"]==True:
        logs["-vieta1-"].update(f"Nav apguvis checkbox izveidošanu")

    matematikas=values["-m-"]
    latviesu_valoda=values["-lv-"]
    programmesana=values["-p-"]
    fizika=values["-f-"]
    sports=values["-s-"]
    kimija=values["-k-"]
    literatura=values["-l-"]

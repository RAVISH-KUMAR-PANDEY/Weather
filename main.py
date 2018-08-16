from tkinter import *
import googlemaps
import json
import urllib.parse
import urllib.request
root = Tk()

def validation(key):
    value = key
    if value.isalpha():
        #print('CORRECT')
        return True
    else:
        #print("incorrect")
        if value=="":
            return True
        else:
            return False
def show_weather():
    global msg
    name_place = entryName.get()
    gm = googlemaps.Client(key='AIzaSyB5GBK4ZHMqsmvSV6yWwE9gUw-T26MXnlM')
    geocode_result = gm.geocode(name_place)
    # print(json.dumps(geocode_result,indent=4))
    lttude = geocode_result[0]['geometry']['location']['lat']
    lngtude = geocode_result[0]['geometry']['location']['lng']
    values={'lat':lttude,'lon':lngtude,'appid':'c57ddae96b37c9e72ec74923a606230a'}
    data = urllib.parse.urlencode(values)
    url = "http://api.openweathermap.org/data/2.5/weather?%s" %data
    resp = urllib.request.urlopen(url)
    d = resp.read()
    data = d.decode('utf-8')
    jdata = json.loads(data)
    lt = jdata['coord']['lat']
    ln = jdata['coord']['lon']
    des = jdata['weather'][0]['description']
    max_t = jdata['main']['temp_max']
    min_t = jdata['main']['temp_min']
    name = jdata['name']
    #print(jdata)
    #print('----------------------------------------')
    w_des = ''' Name of entered palce = {},
    lat = {} and lon = {}
    condition of data = {},
    maximum temprature = {},
    minimum tempreture = {}'''.format(name,lt,ln,des,max_t,min_t)
    #msg = Message(root, text=w_des, font=('times', 10, 'italic')).pack()
    msg.config(text =w_des,bg='lightgreen', font=('times', 12, 'italic'),width=250)


#Title...........................................................
root.geometry('500x400')
root.title('Weather Info....')
#Info.............................................................
lbl = "Weather Information Of The Place You Enter in the Entry Box."
msg1 = Message(root, text=lbl)
msg1.config(font=('times', 16, 'italic'), width='400', fg='Red')
msg1.pack()
#Name_Label.......................................................
lblName = Label(root, text="Enter The Name of Place:::", bd=20, font="Times 24")
lblName.pack()
#EntryName........................................................
entryName = Entry(root, width='50', bd=5)
entryName.pack()
regname= root.register(validation)
entryName.config(validate="key",validatecommand=(regname,"%P"))
#Message.........................................................
spacer1 = Label(root, bd=5).pack()
msg = Message(root, text=" ", font=('times', 10, 'italic'),pady=10)
btnSubmit = Button(root, text="Submit", bg='brown', fg='white', pady=8, padx=15, bd=5, command=show_weather)
btnSubmit.pack()
msg.pack()
root.wm_iconbitmap("favicon.ico")
#mainLoop.......................................................
root.mainloop()
from tkinter import *
from tkinter import ttk
import time
import sys
import requests
import json
from pprint import pprint

lat = [64,65,64,38,78]
lon = [-147,-146,-147,-75,15]
url = []
json_data = []
#data = []
temp = []
press = []
humidity = []
clouds = []
desc = []
speed = []
deg = []
for i in range(5):
	url.append('https://api.openweathermap.org/data/2.5/weather?lat='+str(lat[i])+'&lon='+str(lon[i])+'&units=Imperial&APPID=8a5cd4d7eea4f14433004347beea6199')
	
class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master,background='#046ec8')
		self.master = master
		root.Lba = Label(root, text='',justify='left',background='#046ec8',foreground='#ed8a45')
		root.Lba.pack()
		#self.initWeather()
		self.init_window()
	def init_window(self):
		#stuff about the window
		self.master.title('EPGN Weather Monitor')
		self.pack(fill=BOTH, expand=1)
		self.currentTime()
		header = ['Alaska Satellite Facility','Gilmore Creek','SSC Alaska North Pole','Wallops','Svalbard']
		self.tree = ttk.Treeview(root,columns=header)
		for i in range(len(header)):
			self.tree.column(header[i],width=150)
			self.tree.heading(header[i],text=header[i])
		self.treeview = self.tree
		self.tree.pack()
		self.insertData()
	def getWeather(self):
		#weather info
		for i in range(5):
			json_data.append(requests.get(url[i]).json())
			temp.append(json_data[i]['main']['temp'])
			press.append(json_data[i]['main']['pressure'])
			humidity.append(json_data[i]['main']['humidity'])
			clouds.append(json_data[i]['weather'][0]['main'])
			desc.append(json_data[i]['weather'][0]['description'])
			speed.append(json_data[i]['wind']['speed'])
			try:
				deg.append(json_data[i]['wind']['deg'])
			except:
				print('Failed API call')
		#data = requests.get(url[0]).json()
		
		print('Calling API')
	def insertData(self):
		self.getWeather()
		self.tree.insert('','end',text='Temperature (F)',values=temp)
		self.tree.insert('','end',text='Pressure (hPa)',values=press)
		self.tree.insert('','end',text='Humidity (%)',values=humidity)
		self.tree.insert('','end',text='Weather',values=clouds)
		self.tree.insert('','end',text='Cloud Cover',values=desc)
		self.tree.insert('','end',text='Wind Speed (mph)',values=speed)
		self.tree.insert('','end',text='Wind Direction (deg)',values=deg)
		#sself.tree.insert('','end',text='test',values=json_data["weather"])
		root.after(30000,self.delEntry)
	def delEntry(self):
		sel = self.tree.get_children()
		for item in sel:
			self.tree.delete(item)
		del json_data[:]
		#data = []
		del temp[:]
		del press[:]
		del humidity[:]
		del clouds[:]
		del desc[:]
		del speed[:]
		del deg[:]
		self.insertData()
	def currentTime(self):
		now = time.strftime('%H:%M:%S')
		root.Lba.configure(text='Current Time: '+now)
		root.after(1000,self.currentTime)
root = Tk()
root.configure(background='#046ec8')
app = Window(root)
root.mainloop()
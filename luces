import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QColorDialog, QComboBox
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QCoreApplication
import tinytuya
import os
import time
import json
from helper import iu_helper



class candil(tinytuya.BulbDevice):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    

    


class SystemTrayIcon(QSystemTrayIcon):
    
    def __init__(self,parent=None):
        super().__init__()
        QSystemTrayIcon.__init__(self,parent)
        self.setIcon(QIcon('bombilla_2.png'))
        self.setToolTip('Tray - Lights')
        with open('snapshot.json') as json_file:
            self.data = json.load(json_file)
        
        bombillas = open('devices.json', 'r')
        self.bombillas_dict = dict(enumerate(json.load(bombillas)))
        
        self.menu = QMenu()
        
        self.connect_bulb()
        self.initUI()

    def add_items(self ,bombilla, bombilla_name):
        actions = {'color':lambda: self.elige_color(bombilla),
            'brillo 50%': lambda: bombilla.set_brightness_percentage(50),
        'brillo 100%': lambda: bombilla.set_brightness_percentage(100),
        'encender':  lambda: bombilla.turn_on(),
        'apagar': lambda: bombilla.turn_off()}
        self.light_bulb = self.menu.addMenu(bombilla_name)
        for key, value in actions.items():
            action = self.light_bulb.addAction(key)
            action.triggered.connect(value)

        #color = self.light_bulb.addAction(actions[0])
        #color.triggered.connect(actions[1])
        #encender = self.light_bulb.addAction(actions[6])
        #apagar = self.light_bulb.addAction(actions[8])
        #encender.triggered.connect(actions[7])
        #apagar.triggered.connect(actions[9])


    def initUI(self):
        
        
        for item in self.lista_bombillas:
            self.add_items(item, item.name)

      
        


        
        
        exitaction = self.menu.addAction('Exit')
        exitaction.triggered.connect(QCoreApplication.quit)
        self.setContextMenu(self.menu)
        self.show()
        

    

    def connect_bulb(self):
        self.lista_bombillas = []
        
        for item in self.data['devices']:
            self.bulb = candil(
            name= item['name'],
            dev_id = item['id'],
            address = item['ip'],
            local_key = item['key'],
            version = item['ver']
            )
            
            self.lista_bombillas.append(self.bulb)
       
    def elige_color(self, bombilla):
        self.colour = QColorDialog.getColor()
        print(self.colour.name())
        bombilla.set_colour(self.colour.getRgb()[0], self.colour.getRgb()[1], self.colour.getRgb()[2])

    

if __name__ == "__main__":
    app= QApplication.instance() # checks if QApplication already exists 
    if not app: # create QApplication if it doesnt exist 
        app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    tray = SystemTrayIcon()
    sys.exit(app.exec())

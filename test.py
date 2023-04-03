import sys
from PyQt6.QtWidgets import (
QApplication, QWidget,QSlider, QLabel, QMenu,
QFormLayout, QColorDialog, QPushButton, QComboBox, QSystemTrayIcon)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon, QAction
import tinytuya
import json

class candil(tinytuya.BulbDevice):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name


        
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('bombilla_2.png'))
        self.menu = QMenu()
        self.indice = 0

        with open('snapshot.json') as json_file:
            self.data = json.load(json_file)
        self.connect_bulb()
        for item in self.lista_bombillas:
            self.add_items(item, item.name)


        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        #hide_action = QAction("Hide", self)
        shit_action = QAction(QIcon('poo.png'), '&Clickable Image', self)
        show_action.triggered.connect(self.show)
        #hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(app.quit)
        shit_action.triggered.connect(lambda: print('mierda'))

       
        self.menu.addActions([show_action, quit_action, shit_action])
        self.tray_icon.setContextMenu(self.menu)
       
        self.bombo_combo = QComboBox()
        for i in self.lista_bombillas:
            self.bombo_combo.addItem(i.name)
        self.bombo_combo.currentIndexChanged.connect(self.change_lightbulb)
        self.tray_icon.show()
 
        
        #self.setMinimumWidth(200)

        
        layout = QFormLayout()
        self.setLayout(layout)
        

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        slider_2 = QSlider(Qt.Orientation.Horizontal, self)
        slider_2.setRange(0, 100)
        slider_2.setValue(50)
        slider_2.setSingleStep(5)
        slider_2.setPageStep(10)

        bulb_colour = QPushButton('Colour picker')
        bulb_colour.clicked.connect(self.elige_color_2)
        encender = QPushButton('ON')
        apagar = QPushButton('OFF')
        encender.clicked.connect(lambda: self.lista_bombillas[self.indice].turn_on())
        apagar.clicked.connect(lambda: self.lista_bombillas[self.indice].turn_off())
        blanco = QPushButton('White Mode')
        blanco.clicked.connect(lambda: self.lista_bombillas[self.indice].set_mode('white'))


        slider.sliderReleased.connect(lambda: self.lista_bombillas[self.indice].set_brightness_percentage(slider.value()))
        slider_2.sliderReleased.connect(lambda: self.lista_bombillas[self.indice].set_colourtemp_percentage(slider.value()))
        
        
        
        
        layout.addRow(self.bombo_combo)
        layout.addRow('brightness', None)
        layout.addRow(slider)
        
       
        layout.addRow('colour temp', None)
        layout.addRow(slider_2)
        layout.addRow(bulb_colour)
       
        layout.addRow(encender, apagar)
        layout.addRow(blanco)

        

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
            print(f'{self.bulb.name} connected')
            print(self.bulb.status())
            self.lista_bombillas.append(self.bulb)

    def elige_color(self, bombilla):
        self.colour = QColorDialog.getColor()
        print(self.colour.name())
        bombilla.set_colour(self.colour.getRgb()[0], self.colour.getRgb()[1], self.colour.getRgb()[2])
        
    def elige_color_2(self):
        self.colour = QColorDialog.getColor()
        self.lista_bombillas[self.indice].set_colour(self.colour.getRgb()[0], self.colour.getRgb()[1], self.colour.getRgb()[2])
        colorete = self.colour.name()
        self.setStyleSheet(f'background-color: {colorete}')
    
    def change_lightbulb(self):
        print(self.bombo_combo.currentIndex())
        self.indice = self.bombo_combo.currentIndex()
        self.setWindowTitle(self.lista_bombillas[self.indice].name)

        """
        self.setWindowTitle(self.bombo_combo.currentText())
        self.bulb = tinytuya.BulbDevice(
            dev_id = self.bombillas_dict[self.bombo_combo.currentIndex()]['id'],
            address = self.bombillas_dict[self.bombo_combo.currentIndex()]['ip'],
            local_key = self.bombillas_dict[self.bombo_combo.currentIndex()]['key'],
            version = self.bombillas_dict[self.bombo_combo.currentIndex()]['version'])
        """

    def add_items(self ,bombilla, bombilla_name):
        actions = {'color':lambda: self.elige_color(bombilla),
            'brillo 50%': lambda: bombilla.set_brightness_percentage(50),
        'brillo 100%': lambda: bombilla.set_brightness_percentage(100),
        'white mode': lambda: bombilla.set_mode('white'),
        'encender':  lambda: bombilla.turn_on(),
        'apagar': lambda: bombilla.turn_off()}
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(app.quit)
        self.light_bulb = self.menu.addMenu(bombilla_name)

        for key, value in actions.items():
            action = self.light_bulb.addAction(key)
            action.triggered.connect(value)

        


    

    def closeEvent(self, event):
        event.ignore()

        self.hide()
        #self.connect_bulb()
        #self.menu.show()
        self.tray_icon.show()

        """                                                                  
        self.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
        )
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    app.setStyleSheet("""
    QWidget {
        color: "white";
        font-size: 20px
    }
    QPushButton {
        background-color: "#103d10"
    }
    QCombobox {
        background-color: "#103d10"
    }
""")
    window.setGeometry(200, 200, 300, 160)
    window.show()
    sys.exit(app.exec())
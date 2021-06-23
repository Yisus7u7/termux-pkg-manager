#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  prueba.py
#  
#  Copyright 2021 Yisus7u7 <jesuspixel5@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#notas
# [sg.Button("install", size=(40, 2), key='instalar')
#
#

#  modulos 
import PySimpleGUI as sg
import os as termux
import sys

print("""
App: Termux pkg manager
Version : 1.0.8-beta_build
Creator: @Yisus7u7

""")


#  tema de la ventana
sg.theme('BlueMono')

#  contenido del menu superior 


main_menu = [['Actions', ['update mirrors', 'upgrade packages', 'clean cache', 'autoremove cache packages']], ['Help', ['about']]]

#  contenido de las apps recomendadas

apps = ['1. qt-creator', '2. audacious', '3. otter-browser', '4. geany-plugins', '5. openttd',
        '6. the-powder-toy', '7. geany', '8. leafpad', '9. ristretto', '10. kvantum',
        '11. mtpaint', '12. chocolate-doom', '13. featherpad', '14. vim-gtk', '15. mpv-x',
        '16. mate-terminal', '17. hexchat', '18. uget', '19 lxqt-archiver', '20. xfce4-taskmanager',
        'Note: this list will have more content coming soon']

#  contenido de la app

layout = [ 
          [sg.Menu(main_menu, key='wmenu')],
          [sg.Text("Welcome To Termux pkg manager", text_color=("#FF0000"))],
          [sg.Text("Select action:", text_color=("#DA24BA"))],
          [sg.Button("install", key='instalar', button_color=("#1FAA1F")), sg.Button("uninstall", key='eliminar', button_color=("#FF0000")), sg.Button("showinfo", key='info', button_color=("#BDBD25"))],
          [sg.Text("Enter package name:")],
          [sg.Input(key='paquete', size=(50, 1))],
          [sg.Text("Popular apps:")],
          [sg.Listbox(values=apps, select_mode='extended', size=(50, 6))]
          ]
                
        

window = sg.Window('Termux pkg manager', layout, icon=('./app_icon.png'))


#  funciones y acciones de la app

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED:
		break

# funcion del menu superior 
   
	elif event == 'update mirrors':
		acept = termux.system("apt update | zenity --progress --title=\"apt status\" --text=\"updating package list...\" --pulsate")
		if acept == 0:
			sg.Popup('Pkg status', 'Package list successfull updated')
		else:
			sg.PopupError('Error:', 'The list of packages could not be obtained, check your internet connection or your source.list file')
	
	elif event == 'upgrade packages':
		acept = termux.system("apt upgrade -y -o Dpkg::Options::=\"--force-confnew\" | zenity --progress --title=\"dpkg/apt status\" --text=\"Updating installed packages, this may take a while...\" --pulsate")
		if acept == 0:
			sg.Popup('Pkg status', 'Package successfull upgrade')
		else:
			sg.PopupError('Error', 'Could not update the packages, check your internet connection or that dpkg is not broken')
	
	elif event == 'about':
		termux.system("exec ./about.py")
			
	elif event == 'clean cache':
		termux.system("apt clean")
		termux.system("apt autoclean")
		sg.Popup('Info', 'Junk and cache removed correctly')
		
	elif event == 'autoremove cache packages':
		termux.system("apt autoremove -y | zenity --progress --title=\"apt status\" --text=\"removing unused junk packages from cache ...\" --pulsate")
		sg.Popup('pkg status', 'junk packages and cache removed successfull')
			
#  funcion de instalar paquetes

	elif event == 'instalar':
		pkg = values['paquete']
		inspect = termux.system(f"apt show {pkg}")
		if inspect == 0:
			termux.system(f"apt install -y {pkg} | zenity --progress --title=\"installing software\" --text=\"installing {pkg}...\" --pulsate")
			sg.Popup('Pkg status', f'{pkg} successfull installed')
		else:
			termux.system("zenity --error --text=\"Error, package not found\"")

# funcion de desinstalar paquetes

	elif event == 'eliminar':
		pkg = values['paquete']
		inspect = termux.system(f"apt show {pkg}")
		if inspect == 0:
			termux.system(f"apt purge -y {pkg} | zenity --progress --title=\"remove software\" --text=\"uninstalling {pkg}...\" --pulsate")
			sg.Popup('Pkg status', f'{pkg} Successfull removed')
		else:
			termux.system("zenity --error --text=\"Error, package not found\"")	

#  funcion de mostrar informacion acerca del paquete

	elif event == 'info':
		pkg = values['paquete']
		inspect = termux.system(f"apt show {pkg}")
		if inspect == 0:
			package = termux.popen(f"apt show {pkg}").read()
			sg.Popup('Package info:', f'{package}')
		else:
			#sg.PopupError('Error', 'Package not found')
			termux.system("zenity --error --text=\"Error, package not found\"")	
			
			
#  funcion de error por si succede algun error inesperado en el programa
		
	else:
	    sg.Popup('Error', 'An unexpected error has occurred, please report the error on github')
	
	
#  mostrar ventana
	
window.close()

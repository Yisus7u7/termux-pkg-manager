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


#  tema de la ventana
sg.theme('BlueMono')

#  contenido del menu superior 


main_menu = [['Edit', ['update mirrors', 'upgrade packages']], ['help', ['about']]]

#  contenido de la app

layout = [ 
          [sg.Menu(main_menu, key='wmenu')],
          [sg.Text("Welcome To x11-getapps", text_color=("#FF0000"))],
          [sg.Text("Select action:", text_color=("#DA24BA"))],
          [sg.Button("install", key='instalar', button_color=("#1FAA1F")), sg.Button("uninstall", key='eliminar', button_color=("#FF0000")), sg.Button("showinfo", key='info', button_color=("#BDBD25"))],
          [sg.Text("enter package name:")],
          [sg.Input(key='paquete')],
          [sg.Text("popular apps:")]]
                
        

window = sg.Window('x11-getapps', layout)


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

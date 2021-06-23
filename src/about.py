#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  about.py
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

import PySimpleGUI as sg

layout = [
         [sg.Text("""
         x11-getapps is developed by yisus7u7 and its contributors. 
         thanks for using our project!.
         """)]]
         
         


window = sg.Window('about for x11-getapps', layout)


while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED:
		break



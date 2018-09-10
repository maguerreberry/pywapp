'''
Created on Sep 2, 2018

@author: matt_
'''
import wapp
from gcontacts import GoogleContacts
from gui import GUI, Calculator

gui = GUI()
# gui = Calculator()

aa

gcontacts = GoogleContacts()

contacts = gcontacts.get_group_contacts('starred')

for ii in contacts:
    wapp.hl_send(name=ii, text='hola', image='C:\Users\matt_\Downloads\homero.jpg')
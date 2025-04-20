Here in our project we're following the 4xidraw design which makes use of a fixed belt design. Also known as core xy plotter. https://www.instructables.com/4xiDraw/
we're using an arduino board and a cnc board on top of it to make a 2d printer. We're using 2 nema motors which are connected to motor drivers. Servo motor is used for pen up and down commands.
Micro stepping is also allowed in our setup through placement of jumper caps in the cnc.
the whole project is being powered by 12V and 2A. 
firstly we generate our image through inkscape or by the code which is to be converted into gcode. 
we upload the migrbl code to our arduino board which makes it ready to receive gcode.
we generate gcode using inkscape and the migrbl extension. 
now we setup our machine through universal gcode sender and thereby upload gcode once it's ready.
the files can also be accessed here : https://mega.nz/folder/HAsTxTRS#-5s3qjk2Tl7KU3bnAQNW6Q

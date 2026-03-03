    # turn ON display, this is default, but doesn't hurt
OD01.display(True)


# set text size 1 or 2
OD01.set2_x                                                                                                                                                                                                                                                     ()
# set zoom level in or out  
OD01.zoom_in()                                                                      
# clear the display in case of garbage on screen
OD01.clear()


# print hello world on screen with
OD01.show_string("Ken Perry", 0, 0, 1)
OD01.show_string("Old Man!",0, 1, 1)

# sit in loop forever...
def on_forever():
    pass
            
basic.forever(on_forever)
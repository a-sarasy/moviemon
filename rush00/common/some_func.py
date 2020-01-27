from django.conf import settings
import re, os

def get_slots(savedir):
    slots = {'a':"Slot A : Free", "b":"Slot B : Free","c":"Slot C : Free"}
    c = re.compile("^slot([abc])_([0-9]*)_([0-9]*)\.mmg$")

    for slot in os.listdir(savedir):
        match = c.match(slot)
        if match and int(match.group(2)) < int(match.group(3)) and int(match.group(3)) == len(settings.MOVIES):
            slots[match.group(1)] = "Slot {} : {}/{}".format(match.group(1).capitalize(),match.group(2),match.group(3))
            
    return(slots)

def get_val_slots(savedir):
    slots = {'a':None, "b":None,"c":None}
    c = re.compile("^slot([abc])_([0-9]*)_([0-9]*)\.mmg$")
    for slot in os.listdir(savedir):
        match = c.match(slot)
        if match and int(match.group(2)) < int(match.group(3)) and int(match.group(3)) == len(settings.MOVIES):
            slots[match.group(1)] = match.group()
            
    return(slots)
from django.conf import settings
import re, os

def get_slots(savedir):
    slots = {'A':"Slot A : Free", "B":"Slot B : Free","C":"Slot C : Free"}
    c = re.compile("^slot([ABC])_([0-9]*)_([0-9]*)\.mmg$")

    for slot in os.listdir(savedir):
        match = c.match(slot)
        if match and int(match.group(2)) < int(match.group(3)) and int(match.group(3)) == len(settings.MOVIES):
            slots[match.group(1)] = "Slot {} : {}/{}".format(match.group(1),match.group(2),match.group(3))
            
    return(slots)
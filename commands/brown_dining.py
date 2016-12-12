import getVoice
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import db
import talker
import requests
import datetime


def go():
    # Incomplete, as Brown Dining API needs to be updated to use cafebonappetit's new API
    talker.say("I'm sorry, but this feature is currently not functional.")
    option = getVoice.select(["Get current menu", "Get tomorrow's menu"])
    eatery = getVoice.select(["ratty", "vdub"], selector="eatery")
    if option == "Get current menu":
        requests.get("https://api.students.brown.edu/dining/menu?client_id=4283555c-e705-46e3-81b9-25d3db38b6e1&eatery=" + eatery).json
    elif option == "Get tomorrow's menu":
        requests.get("https://api.students.brown.edu/dining/menu?client_id=4283555c-e705-46e3-81b9-25d3db38b6e1&eatery=" + eatery + "&day=" + datetime.datetime.today().day + 1).json

from pytodoist import todoist
import getVoice
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import db
import talker
import requests
import datetime

# go is the main function, is looped since you may want to do many of these operations at once.
def go():
    option = getVoice.select(['list tasks', 'add task', 'check off task', 'cancel'], selector="action")
    with open("/home/pi/todoist.txt", "r") as pw_file:
        pw = pw_file.read().replace('\n', '')
    user = todoist.login('ryanhecht.tse@gmail.com', pw)

    if option == 'list tasks':
        lst(user)
    elif option == "add task":
        add(user)
    elif option == "check off task":
        check(user)

# Lists all open tasks in inbox
def lst(user):
    db.log_action("todoist", "list tasks")
    tasks = user.get_project('Inbox').get_tasks()
    talker.say("You have " + str(len(tasks)) + " open tasks.")
    for task in user.get_project('Inbox').get_tasks():
        talker.say(task.content)
    go()

# Adds a task to the inbox
def add(user):
    talker.say("Speak new task")
    task = getVoice.getVoice(prompt=False)
    user.get_project('Inbox').add_task(task)
    user.get_project('Inbox').update()
    db.log_action("todoist", "added task " + task)
    go()

# Checks off a task from the inbox
def check(user):
    tasks = user.get_project('Inbox').get_tasks()
    option = getVoice.select(map(lambda x: x.content, tasks), selector="task")
    for task in tasks:
        if task.content == option:
            db.log_action("todoist", "checked off task " + task.content)
            task.complete()
            talker.say("Task completed")
    user.get_project('Inbox').update()
    go()

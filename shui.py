import time

def pomodoro(focus_time=25, break_time=5):
    print("开始专注！")
    time.sleep(focus_time * 60)
    print('\a')
    print("休息一下！")
    time.sleep(break_time * 60)
    print('\a')

while True:
    pomodoro()

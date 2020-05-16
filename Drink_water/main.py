import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title="Please drink water now!!",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women",
            app_icon = r"C:\\Users\\Mani\\Drink_water\\glass.ico ",
            timeout=10
        )
        time.sleep(15*60) # press Ctrl+c to exit it
        # to run the python application in background, using pythonw.exe
        # to end the code in running go to task manager, and end the task
        
        
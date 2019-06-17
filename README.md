# Simple counter display

## test.py
* Displays a counter in full screen mode using pygame library
## launcher.sh
* Executes the python script(test.py) in background
* To run the counter on startup for devices such as rpi, you can add the following line in rc.local file (just before ```exit 0```) located under etc directory 
(make sure to change the path of the launcher script in the below command)

	``` sudo /path/to/launcher.sh & > /tmp/launcher_log 2>&1 ```

* This will run the launcher script which will inturn run the python file. Any errors will be logged in launcher_log
* Alternative methods for running the script on startup are mentioned [here](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
* If you want to directly run the script as soon as the rpi is booted, you can remove splash screen, recovery screen and the rainbow image

__WARNING:__ Currently the functionality to exit from the python script has not been added, so only option for now is reboot. However, for debugging purpose counter value is limited to 1002 (starts from 1000 and ends at 1002).
## Screenshot
<img src = "https://github.com/Saurabh702/counter-display/blob/master/Screenshot.PNG" width = "500" />
## References
*https://pythonprogramming.net/displaying-text-pygame-screen/

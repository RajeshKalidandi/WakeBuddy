[app]

# (str) Title of your application
title = WakeBuddy

# (str) Package name
package.name = wakebuddy

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = "D:/WakeBuddy"

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/images/splash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/images/icon.png

# (list) Supported platforms
target = android

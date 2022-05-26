from pywinauto import keyboard
from pywinauto.application import Application

# enter path to putty.exe
app = Application().start(cmd_line=r"C:\Program Files\PuTTY\putty.exe")
app = Application().connect(title="PuTTY Configuration")
window = app.PuTTYConfigBox
window.set_focus()
# enter the host name instead HOSTNAME
window[u'Host name (or IP address):Edit'].type_keys("HOSTNAME")
# connection port (if empty, then 22 default)
window[u"Port:Edit"].type_keys("PORT")
window["Open"].click()
# server window capture (enter the host name instead HOSTNAME)
dlg = app['HOSTNAME - PuTTY']
dlg.set_focus()
# login
keyboard.send_keys('LOGIN{ENTER}')
# password
keyboard.send_keys('PASSWORD{ENTER}')
keyboard.send_keys('{SPACE}')

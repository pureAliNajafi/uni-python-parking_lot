from Components.check_in import check_in
from Components.check_out import check_out
from Components.manager import manager
from Components.Gui import gui
def main():
    choice = gui.input("""
    What would you like to do, Manager?

    1) check in
    2) check out
    3) manager panel
    0) exit                   
    Please select an option: """)
    if choice == "1" :
        check_in()
    elif choice == "2" :
        check_out()
    elif choice == "3" :
        manager()
    else :
        gui.print("Invalid Inputs")   


try:
    main()
except:
    gui.print("Invalid Inputs")   

from Components.Gui import gui
from Components.Utility import utility
def manager():

    # gui.list("search results:",utility.manager.search("ali"))
    # utility.manager.report.past_week_parked_vehicles()
    # utility.manager.report.vehicle_details_by_type()
    # utility.manager.report.vehicle_details_by_city()
    # utility.manager.report.even_and_odd_plates()
    # utility.manager.report.past_week_income()

    def authentication():
        password = gui.input("Password?")
        if password == "1234":
            return True
        
        print("authentication failed")
        return False
    if authentication() == False :
        return 
    
    while True:
        choice = gui.input("""
        What would you like to do, Manager?

        1) Search for a vehicle (by name or plate number)
        2) View report of vehicles parked in the past week
        3) View vehicle details grouped by type
        4) View vehicle details grouped by city
        5) View vehicles grouped by odd or even plate numbers
        6) View past week's income
        0) Exit

        Please select an option: """)

        # Handle User Selection
        if choice == "1":
            search_query = gui.input("Enter the name or plate number to search: ")
            search_results = utility.manager.search(search_query)
            gui.list("Search Results:", search_results)
            gui.input("Press Enter to Continue")

        elif choice == "2":
            utility.manager.report.past_week_parked_vehicles()
            gui.input("Press Enter to Continue")

        elif choice == "3":
            utility.manager.report.vehicle_details_by_type()
            gui.input("Press Enter to Continue")


        elif choice == "4":
            utility.manager.report.vehicle_details_by_city()
            gui.input("Press Enter to Continue")


        elif choice == "5":
            utility.manager.report.even_and_odd_plates()
            gui.input("Press Enter to Continue")

        elif choice == "6":
            utility.manager.report.past_week_income()
            gui.input("Press Enter to Continue")

        elif choice == "0":
            gui.print("Exiting the manager. Goodbye!")
            break

        else:
            gui.print("Invalid option. Please try again.")



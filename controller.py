from datetime import date
from events import *
import view


class Controller:

    def __init__(self):
        self.view = view.View()

    def start(self):

        is_working = True

        while is_working:
            self.view.print_main_menu()
            choice = self.view.get_choice()
            try:
                if choice not in ["1", "2", "3", "4", "5", "6", "0"]:
                    raise ValueError
                elif choice == "1":
                    self.book_event(PrivateMentoring(self.get_date()))
                elif choice == "2":
                    self.book_event(Checkpoint(self.get_date()))
                elif choice == "3":
                    self.print_all_events()
                elif choice == "4":
                    self.remove_event()
                elif choice == "5":
                    self.save_to_file()
                elif choice == "6":
                    self.read_from_file()
                elif choice == "0":
                    is_working = False
            except ValueError:
                self.view.print_message("Wrong number.")

        self.say_goodbye()

    def print_all_events(self):

        self.view.print_all_events(Event.get_events())

    def book_event(self, event):

        if type(event) == PrivateMentoring:
            event.preferred_mentor = self.view.get_input("Enter preffered mentor: ")
            event.goal = self.view.get_input("Enter your goal: ")

    def remove_event(self):

        event_str = self.view.get_input("Enter date and name of event to cancel: ")
        Event.remove_ev(event_str)

    def say_goodbye(self):

        self.view.print_goodbye()

    def get_date(self):

        try:
            date = self.view.get_input("Enter the date (yyyy-mm-dd): ")
            date = self.__class__.convert_date(date)
        except ValueError:
            self.view.print_message("Invalid date string")

        return date

    def save_to_file(self):

        with open("events.csv", "a") as file:
            for event in Event.events:
                if type(event) == PrivateMentoring:
                    file.write("Private mentoring|{}|{}|{}".format(event.date,
                                                                   event.preferred_mentor,
                                                                   event.goal) + "\n")
                elif type(event) == Checkpoint:
                    file.write("Checkpoint|{}".format(event.date) + "\n")

    def read_from_file(self):

        with open("events.csv", "r") as file:
            for line in file:
                line = line.strip()
                line = line.split("|")
                if line[0] == "Checkpoint":
                    Event.add_event(Checkpoint(self.__class__.convert_date(line[1])))

    @staticmethod
    def convert_date(date_str):

        date_list = date_str.split("-")

        return date(int(date_list[0]), int(date_list[1]), int(date_list[2]))

class View:

    def print_all_events(self, events):

        for event in events:
            print(event)

    def print_main_menu(self):

        print("""Choose option
            1. Book private mentoring
            2. Book checkpoint
            3. Show all my events
            4. Remove an event
            5. Save events to file
            6. Read events from file
            0. Close the program
            """)

    def print_message(self, message):
        print(message)

    def print_goodbye(self):

        print("bye bye!")

    def get_choice(self):

        return input("Choose option: ")

    def get_input(self, message):

        return input(message)

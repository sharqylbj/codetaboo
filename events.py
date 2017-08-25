class Event:

    events = []

    def __init__(self, date):
        '''
        date: Date obj.
        '''
        self.date = date

    def get_date(self):
        return self.date

    @classmethod
    def sort_events(cls):
        is_sorted = False
        while not is_sorted and len(cls.events) > 1:
            is_sorted = True
            for i in range(len(cls.events) - 1):
                if cls.events[i].date > cls.events[i + 1].date:
                    temp = cls.events[i]
                    cls.events[i] = cls.events[i + 1]
                    cls.events[i + 1] = temp
                    is_sorted = False

    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        return cls.events

    @classmethod
    def remove_ev(cls, event_str):
        for event in cls.events:
            if event_str == event.__str__():
                cls.events.remove(event)


class Checkpoint(Event):

    def __init__(self, date):
        super().__init__(date)
        Event.add_event(self)

    def __str__(self):
        return '{} Checkpoint'.format(self.date)


class PrivateMentoring(Event):

    def __init__(self, date):
        super().__init__(date)
        self.preferred_mentor = None
        self.goal = None
        Event.add_event(self)

    def set_goal(self, goal):
        self.goal = goal

    def set_preffered_mentor(self, preferred_mentor):
        self.preferred_mentor = preferred_mentor

    def __str__(self):
        return '{} Private mentoring with {} about {}'.format(self.date, self.preferred_mentor, self.goal)

class DatetimeEventStore:

    def __init__(self, dateTime, eventTitle, location):
        self.DateTime = dateTime
        self.EventTitle = eventTitle
        self.Location = location

    def store_event(self):

        #A dd to the database
        print("Event added to database")


    def get_events(self):
        # Query database for matching events
        print(1)

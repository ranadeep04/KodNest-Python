class MetroTickets:

    def __init__(self):

        self.passenger = 1



    def __iter__(self):

        return self



    def __next__(self):

        if self.passenger <= 3:

            ticket = self.passenger

            self.passenger += 1

            return f"Metro Ticket {ticket} issued"

        else:

            raise StopIteration





tickets = MetroTickets()



for ticket in tickets:

    print(ticket)
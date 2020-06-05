#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = {}
    for x in tickets:
        route[x.source] = x.destination

    routes = []
    num = 0
    while len(routes) != length:
        if routes != []:
            routes.append(route[routes[num]])
            num += 1
        elif routes == []:
            routes.append(route["NONE"])

    return routes


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
reconstruct_trip(tickets, 3)

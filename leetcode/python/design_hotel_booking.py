"""
### Problem ###
https://leetcode.com/discuss/interview-question/124744/Design-an-online-hotel-booking-system/

Design an online hotel booking system

"""


class Hotel(object):
    def __init__(self, num_rooms=100):
        self.num_rooms = num_rooms

        self.available_rooms_by_date = [[]] * 365
        for date in range(365):
            available_rooms = []
            for j in range(num_rooms):
                available_rooms.append(Room(j, date))
            self.available_rooms_by_date[date] = available_rooms

        self.unavailable_rooms_by_date = [[]] * 365

    def book_room(self, customer, date):
        available_rooms = self.available_rooms_by_date[date]

        if available_rooms:
            room = available_rooms.pop()
            self.unavailable_rooms_by_date[date].append(room)
            room.booked = True
            room.customer = customer
            return room
        else:
            raise Exception("No rooms available")

    def checkin(self, customer, room):
        room.checkin(customer)

    def checkout(self, customer, room):
        room.checkout(customer)


class Room(object):
    def __init__(self, number, date, occupied=False):
        self.number = number
        self.date = date
        self.occupied = occupied
        self.booked = False
        self.customer = None

    def book(self, customer):
        self.customer = customer
        self.booked = True

    def checkin(self, customer):
        if not self.booked: raise Exception("Cannot check in to an unbooked room")
        if self.occupied: raise Exception("Cannot check in to an occupied room")
        if customer != self.customer: raise Exception("Wrong customer attempting to check in")

        self.occupied = True
        self.customer = customer

    def checkout(self, customer):
        if not self.occupied: raise Exception("Cannot check out to an unoccupied room")
        if customer != self.customer: raise Exception("Wrong customer attempting to check out")

        self.occupied = False
        self.customer = None


class Customer(object):
    def __init__(self, name):
        self.name = name


hotel = Hotel(5)

customer = Customer("Mr Customer")

room = hotel.book_room(customer, 10)
hotel.checkin(customer, room)
hotel.checkout(customer, room)

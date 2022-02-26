# Air Management System


from datetime import datetime


class Airport:
    def __init__(self, city: str, planes: list, schedule_departures: list, schedule_arraivals: list):
        self.city = city
        self.planes = planes
        self.schedule_departures = schedule_departures
        self.schedule_arraivals = schedule_arraivals

    def schedule_flight(self, destination, datetime):
        for plane in self.planes:
            if plane.next_flight.date != datetime:
                plane.next_flight.append(destination)

    def info(self, start_date, end_date):
        print("Arrivals:")
        for arrival in self.scheduled_arrivals:
            if start_date < arrival.date < end_date:
                print(arrival.id)

        print("\nDepartures:")
        for departure in self.scheduled_departures:
            if start_date < departure.date < end_date:
                print(departure.id)


class Company:
    def __init__(self, id: str, name: str, planes: list):
        self.id = id
        self.name = name
        self.planes = planes


class Airplane:
    def __init__(self, id: int, current_location: Airport, company: str, next_flight: list):

        self.next_flight = next_flight
        self.id = id
        self.current_location = current_location
        self.company = company

    def fly(self, destination):
        self.next_flight.append(destination)

    def location_on_date(self, date):
        for flight in self.next_flight:
            if flight.date == date:
                return flight.destination.city

    def available_on_date(self, date, location):
        if self.location_on_date(date):
            return location

    def __str__(self):
        return f"{'-' * 20}\nNumber Of Flights: {len(self.next_flight)}\n{'-' * 20}"


class Flight:
    def __init__(self, date: datetime.date, destination: Airport, origin: Airport, plane: Airplane, id: str):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = id

    def take_off(self):
        self.origin.schedule_departures.pop(self)
        print(f"Flight{self.plane}{self.id} has departure")

    def land(self):
        self.destination.schedule_arraivals.pop(self)
        print(f"Flight{self.plane}{self.id} has landed")

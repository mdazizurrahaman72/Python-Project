import os
import uuid
from datetime import datetime, date

os.makedirs("DATA", exist_ok=True)
os.makedirs("REPORTS", exist_ok=True)

USER_FILE = "DATA/users.txt"
BUS_FILE = "DATA/buses.txt"
BOOKING_FILE = "REPORTS/bookings.txt"

# ================= PERSON =================
class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class User(Person):
    pass


class Admin(Person):
    def verify(self, pwd):
        return self.password == pwd


# ================= BUS =================
class Bus:
    def __init__(self, id, route, time, capacity, fare, type):
        self.id = id
        self.route = route
        self.time = time
        self.capacity = capacity
        self.fare = fare
        self.type = type

    def get_fare(self):
        return self.fare


class ACBus(Bus):
    def __init__(self, id, route, time, capacity, fare):
        super().__init__(id, route, time, capacity, fare, "AC")

    def get_fare(self):
        return self.fare + 100


class NonACBus(Bus):
    def __init__(self, id, route, time, capacity, fare):
        super().__init__(id, route, time, capacity, fare, "Non-AC")


# ================= BOOKING =================
class Booking:
    def __init__(self, booking_id, bus_id, passenger, route, seats, date, fare, type):
        self.booking_id = booking_id
        self.bus_id = bus_id
        self.passenger = passenger
        self.route = route
        self.seats = seats
        self.date = date
        self.total_fare = seats * fare
        self.type = type

    def book(self):
        print("\nBooking Confirmed!")


# ================= GLOBAL =================
buses = []
bookings = {}
users = {}
logged_in_user = None
admin = Admin("admin", "azizur123")


# ================= FILE =================
def load_users():
    if not os.path.exists(USER_FILE):
        return
    with open(USER_FILE) as f:
        for line in f:
            p = line.strip().split(",")
            users[p[0]] = User(p[0], p[1])


def save_users():
    with open(USER_FILE, "w") as f:
        for u in users.values():
            f.write(f"{u.username},{u.password}\n")


def load_buses():
    if not os.path.exists(BUS_FILE):
        seed_data()
        return
    with open(BUS_FILE) as f:
        for line in f:
            p = line.strip().split(",")
            if p[5] == "AC":
                buses.append(ACBus(p[0], p[1], p[2], int(p[3]), float(p[4])))
            else:
                buses.append(NonACBus(p[0], p[1], p[2], int(p[3]), float(p[4])))


def save_buses():
    with open(BUS_FILE, "w") as f:
        for b in buses:
            f.write(f"{b.id},{b.route},{b.time},{b.capacity},{b.fare},{b.type}\n")


def load_bookings():
    if not os.path.exists(BOOKING_FILE):
        return
    with open(BOOKING_FILE) as f:
        for line in f:
            p = line.strip().split(",")
            bookings[p[0]] = Booking(p[0], p[1], p[2], p[3], int(p[4]), p[5], float(p[6]), p[7])


def save_bookings():
    with open(BOOKING_FILE, "w") as f:
        for b in bookings.values():
            f.write(f"{b.booking_id},{b.bus_id},{b.passenger},{b.route},{b.seats},{b.date},{b.total_fare},{b.type}\n")


# ================= SEED =================
def seed_data():
    buses.append(ACBus("B101-A", "Dhaka-Barisal", "08:00 AM", 40, 500))
    buses.append(NonACBus("B102-N", "Dhaka-Barisal", "08:00 AM", 40, 500))


# ================= HELPERS =================
def find_bus(id):
    for b in buses:
        if b.id.lower() == id.lower():
            return b
    return None


def view_schedule():
    print("\n--- Available Buses ---")
    for b in buses:
        print(f"{b.id} | {b.route} | {b.time} | {b.type} | Seats:{b.capacity} | Fare:{b.get_fare():.2f}")


# ================= USER =================
def register():
    uname = input("Enter username: ")
    if uname in users:
        print("Username already exists!")
        return

    while True:
        pwd = input("Enter password (4 digit): ")
        if len(pwd) == 4 and pwd.isdigit():
            break
        print("Error: Password must be exactly 4 digits.")

    users[uname] = User(uname, pwd)
    save_users()
    print("Registration successful!")


def login():
    global logged_in_user
    uname = input("Enter username: ")
    pwd = input("Enter password: ")

    if uname in users and users[uname].password == pwd:
        logged_in_user = users[uname]
        print("Login successful!")
    else:
        print("Invalid username or password.")


# ================= BOOK =================
def book_ticket():
    view_schedule()

    route = input("Enter Route: ")
    type = input("Choose Bus Type (AC / Non-AC): ").strip()

    matched = [b for b in buses if b.route.lower() == route.lower() and b.type.lower() == type.lower()]

    if not matched:
        print("No bus found.")
        return

    print("\n--- Buses Found ---")
    for b in matched:
        print(f"{b.id} | {b.route} | {b.time} | Seats:{b.capacity} | Fare:{b.get_fare():.2f}")

    bus_id = input("Enter Bus ID: ")
    bus = find_bus(bus_id)

    if not bus:
        print("Invalid Bus ID!")
        return

    name = input("Passenger Name: ")
    seats = int(input("Seats: "))

    if seats > bus.capacity:
        print("Not enough seats.")
        return

    user_date = input("Enter Date (YYYY-MM-DD): ")
    try:
        d = datetime.strptime(user_date, "%Y-%m-%d").date()
        if d < date.today():
            print("Invalid Date!")
            return
    except:
        print("Invalid date format!")
        return

    total = seats * bus.get_fare()
    print("Total Fare:", total)

    payment = float(input("Enter Payment: "))
    if payment < total:
        print("Insufficient Payment!")
        return

    if payment > total:
        print("Change Returned:", payment - total)

    bid = str(uuid.uuid4())[:8].upper()

    bk = Booking(bid, bus_id, name, route, seats, user_date, bus.get_fare(), bus.type)
    bookings[bid] = bk
    bus.capacity -= seats

    save_buses()
    save_bookings()

    bk.book()
    print("\nBooking ID:", bid)


# ================= CANCEL =================
def cancel_ticket():
    bid = input("Enter Booking ID: ")
    if bid in bookings:
        bus = find_bus(bookings[bid].bus_id)
        if bus:
            bus.capacity += bookings[bid].seats
        del bookings[bid]
        save_bookings()
        save_buses()
        print("Booking cancelled.")
    else:
        print("Not found.")


# ================= VIEW =================
def view_booking():
    bid = input("Enter Booking ID: ")
    if bid in bookings:
        b = bookings[bid]
        print("\nBooking ID:", b.booking_id)
        print("Bus:", b.bus_id, "| Type:", b.type)
        print("Passenger:", b.passenger, "| Seats:", b.seats)
        print("Route:", b.route)
        print("Total Fare:", b.total_fare)
        print("Journey Date:", b.date)
    else:
        print("Not found.")


# ================= ADMIN =================
def admin_panel():
    pwd = input("Admin Password: ")
    if not admin.verify(pwd):
        print("Access denied.")
        return

    while True:
        print("\n--- Admin Panel ---")
        print("1. Add Bus")
        print("2. Remove Bus")
        print("3. View All Bookings")
        print("0. Back")

        c = input("Choose: ")

        if c == "1":
            add_bus()
        elif c == "2":
            remove_bus()
        elif c == "3":
            view_all_bookings()
        elif c == "0":
            return


def add_bus():
    id = input("Bus ID: ")
    route = input("Route: ")
    time = input("Time: ")
    cap = int(input("Capacity: "))
    fare = float(input("Fare: "))

    buses.append(NonACBus(id + "-N", route, time, cap, fare))
    buses.append(ACBus(id + "-A", route, time, cap, fare))

    save_buses()
    print("AC & Non-AC Both Bus Added.")


def remove_bus():
    id = input("Bus ID: ")
    bus = find_bus(id)
    if bus:
        buses.remove(bus)
        save_buses()
        print("Bus removed.")
    else:
        print("Not found.")


def view_all_bookings():
    for b in bookings.values():
        print(f"{b.booking_id} | {b.bus_id} | {b.passenger} | {b.type} | Seats:{b.seats} | Fare:{b.total_fare:.2f}")


# ================= MAIN =================
def main():
    load_users()
    load_buses()
    load_bookings()

    global logged_in_user

    while True:
        if not logged_in_user:
            print("\n=== Bus Ticket Booking System ===")
            print("1. Register")
            print("2. Login")
            print("0. Exit")

            c = input("Choose: ")

            if c == "1":
                register()
            elif c == "2":
                login()
            elif c == "0":
                save_users()
                save_buses()
                save_bookings()
                print("Goodbye!")
                break

        else:
            print(f"\n=== Welcome, {logged_in_user.username} ===")
            print("1. Book Ticket")
            print("2. Cancel Ticket")
            print("3. View Booking Details")
            print("4. Admin Panel")
            print("0. Logout")

            c = input("Choose: ")

            if c == "1":
                book_ticket()
            elif c == "2":
                cancel_ticket()
            elif c == "3":
                view_booking()
            elif c == "4":
                admin_panel()
            elif c == "0":
                logged_in_user = None
                print("Logged out!")


if __name__ == "__main__":
    main()
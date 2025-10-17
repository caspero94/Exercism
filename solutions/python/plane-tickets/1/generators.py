"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat = ["A","B","C","D"]
    index = 0
    while number > 0:
        yield seat[index]
        index = (index + 1) % 4
        number -= 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats = generate_seat_letters(number)
    x = 0
    f = 1
    for seat in seats:
        seaty = str(f)+seat
        yield seaty
        x += 1
        if seaty == "12D":
            f +=1
        if x == 4:
            f +=1
            x = 0
def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    
    se = generate_seats(len(passengers))
    listado = {}
    for pas in passengers:
        listado[pas] = next(se)    
    return listado

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket = str(seat)+str(flight_id)+((12-len(seat)-len(flight_id))*"0")
        yield ticket


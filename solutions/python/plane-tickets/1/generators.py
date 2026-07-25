"""Functions for plane ticket exercise."""


def generate_seat_letters(number: int):
    """Yield seat letters sequentially (A, B, C, D) up to the requested number."""
    seat_letters = ["A", "B", "C", "D"]

    # Loop exactly 'number' times
    for i in range(number):
        # Use modulo to perfectly cycle the index: 0, 1, 2, 3, 0, 1, 2, 3...
        yield seat_letters[i % 4]


def generate_seats(number: int):
    """Generate a sequential list of seat assignments, bypassing row 13."""
    seat_letters = ["A", "B", "C", "D"]
    seats_issued = 0
    row = 1

    # The Outer Engine: Keeps running until the total ticket order is filled
    while seats_issued < number:
        # The Superstition Override Switch
        if row == 13:
            row += 1
            continue  # Instantly bypass the rest of this cycle and jump to 14!

        # The Inner Engine (The 4-Cylinder Rotor)
        for letter in seat_letters:
            # The Emergency Kill Switch: If the order is filled mid-row, shut down!
            if seats_issued >= number:
                return

            # Yield exactly one seat code to the passenger and pause the engine
            yield f"{row}{letter}"

            # When the engine unpauses, update the ledger tally
            seats_issued += 1

        # Once all 4 seats in the row are issued, shift the transmission up one gear
        row += 1


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Pair a list of passengers with an on-demand generator of seat assignments."""

    # 1. Count the queue and fire up the factory to build exactly that many seats
    ticket_machine = generate_seats(len(passengers))

    # 2. Zip the passenger list and the generator output together, then format as a dictionary
    return dict(zip(passengers, ticket_machine))


def generate_codes(seat_numbers: list[str], flight_id: str):
    """Yield unique 12-character ticket codes padded with trailing zeros."""

    # Loop through the list of passengers' seats
    for seat in seat_numbers:
        # 1. Weld the seat and flight ID together
        base_ticket = f"{seat}{flight_id}"

        # 2. Stamp zeros until it is exactly 12 characters long, then yield!
        yield base_ticket.ljust(12, "0")

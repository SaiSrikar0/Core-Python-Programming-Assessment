'''4. Movie Ticket Booking System

Scenario:

A cinema hall wants to manage ticket bookings. Write a program to keep track of **available** and **booked seats**. Allow users to **book** or **cancel** a seat.

Requirements:

- Use functions to handle seat booking and cancellation.

- Prevent booking an already booked seat.

Input Example:

total_seats = 10

booked_seats = [2, 5, 7]

book_seat = 3

cancel_seat = 5

Expected Output:

Available seats: [1, 4, 6, 8, 9, 10]'''

def book_seat(booked, seat, total_seats):
    if seat in booked:
        print(f"Seat {seat} is already booked.")
    elif 1 <= seat <= total_seats:
        booked.append(seat)
    else:
        print("Invalid seat number.")
    return booked

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    else:
        print(f"Seat {seat} is not booked.")
    return booked

def available_seats(total_seats, booked):
    return [s for s in range(1, total_seats + 1) if s not in booked]

if __name__ == "__main__":
    total_seats = 10
    booked = [2, 5, 7]
    booked = book_seat(booked, 3, total_seats)
    booked = cancel_seat(booked, 5)
    print("Available seats:", available_seats(total_seats, booked))

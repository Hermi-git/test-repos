class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total_seats = [0] *n
       
        for booking in bookings:
            first, last, seats = booking
            total_seats[first-1] += seats
            if last < n:
                total_seats[last] -= seats

        for seat in range(1, n):
            total_seats[seat] += total_seats[seat -1]
        return total_seats
        
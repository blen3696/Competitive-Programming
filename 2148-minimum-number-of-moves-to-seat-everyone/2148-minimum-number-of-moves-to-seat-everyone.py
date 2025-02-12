class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        students.sort()
        seats.sort()
        ctn = 0
        for i in range(len(seats)):
            ctn += abs(students[i] - seats[i])

        return ctn

        
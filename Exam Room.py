''' There is an exam room with n seats in a single row labeled from 0 to n - 1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0.

Design a class that simulates the mentioned exam room.

Implement the ExamRoom class:

ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
int seat() Returns the label of the seat at which the next student will set.
void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.
 '''

class ExamRoom:

    def __init__(self, n: int):
        self.n=n
        self.seats=[]

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        mdis=self.seats[0]
        curseat=0
        for i in range(len(self.seats)-1):
            l1,l2=self.seats[i], self.seats[i+1]
            dis=(l2-l1)//2
            if dis>mdis:
                mdis=dis
                curseat=l1+dis
        if (self.n - 1) - self.seats[-1] > mdis:
            curseat = self.n - 1

        # Insert seat in sorted order
        import bisect
        bisect.insort(self.seats, curseat)
        return curseat


    def leave(self, p: int) -> None:
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

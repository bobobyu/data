import threading


class DiningPhilosophers:
    def __init__(self):
        self.con = threading.Condition()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self, philosopher: int, *actions) -> None:
        with self.con:
            [i() for i in actions]


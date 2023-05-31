class UndergroundSystem:

    def __init__(self):
        self.travels = { }
        self.travelling = { }
        return        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelling[id] = (stationName, t)
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        travel_from = self.travelling[id]

        route = (travel_from[0], stationName)
        time = t - travel_from[1]

        if route in self.travels:
            self.travels[route] = (self.travels[route][0] + 1, self.travels[route][1] + time)
        else:
            self.travels[route] = (1, time)

        self.travelling.pop(id)

        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = self.travels[(startStation, endStation)]

        return travel[1] / travel[0]
    
sys = UndergroundSystem()

sys.checkIn(45, "Leyton", 3)
sys.checkIn(32, "Paradise", 8)
sys.checkIn(27, "Leyton", 10)
sys.checkOut(45, "Waterloo", 15) # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
sys.checkOut(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
sys.checkOut(32, "Cambridge", 22) # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14

assert sys.getAverageTime("Paradise", "Cambridge") == 14.00 # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
assert sys.getAverageTime("Leyton", "Waterloo") == 11.00 # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11

sys.checkIn(10, "Leyton", 24)

assert sys.getAverageTime("Leyton", "Waterloo") == 11.00 # return 11.00000

sys.checkOut(10, "Waterloo", 38) # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14

assert sys.getAverageTime("Leyton", "Waterloo") == 12.00 # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
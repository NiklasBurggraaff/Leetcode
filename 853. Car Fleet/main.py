from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        fleets = 0
        currentFleetArrival = None

        for x, v in cars:
            carArrival = (target - x) / v

            if currentFleetArrival is None or carArrival > currentFleetArrival:
                fleets += 1
                currentFleetArrival = carArrival

        return fleets


def main():
    print(Solution().carFleet(
        target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]
    ))
    print(Solution().carFleet(
        target=10, position=[0, 4, 2], speed=[2, 1, 3]
    ))


if __name__ == "__main__":
    main()

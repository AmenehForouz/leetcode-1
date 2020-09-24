"""
Problem 1436 - Destination City

You are given the array paths, where paths[i] = [cityAi, cityBi] means 
there exists a direct path going from cityAi to cityBi. Return the 
destination city, that is, the city without any path outgoing to another 
city.

It is guaranteed that the graph of paths forms a line without any loop, 
therefore, there will be exactly one destination city.
"""

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origins = [i[0] for i in paths]
        destinations = [i[1] for i in paths]
        destination_city = set(destinations) - set(origins)
        return destination_city.pop()


if __name__ == "__main__":
    paths = [
        ["London", "New York"],
        ["New York", "Lima"],
        ["Lima", "Sao Paolo"],
    ]
    # Should return Sao Paolo
    print(Solution().destCity(paths))

    paths = [["B", "C"], ["D", "B"], ["C", "A"]]
    # Should return A
    print(Solution().destCity(paths))

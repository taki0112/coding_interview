class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        x = []
        for person in people:
            x.insert(person[1], person)

        return x

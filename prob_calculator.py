import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):
        self.contents = []
        for key,value in colors.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        drawn_list = []
        for i in range(num):
            drawn_color = self.contents.pop(random.randrange(len(self.contents)))
            drawn_list.append(drawn_color)
        return drawn_list
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for x in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        drawn_list = Hat.draw(hatCopy, num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if (drawn_list.count(key) < value):
                 success = False
        if success:
            count += 1
    return count/num_experiments
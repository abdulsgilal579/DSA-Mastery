"""
There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!

Note:
Your points are not included in the array of your class's points. Do not forget them when calculating the average score!
"""


def better_than_average(class_points, your_points):
    sum_of_class_marks = 0
    for cp in class_points:
        sum_of_class_marks += cp
    average_of_students = sum_of_class_marks / len(class_points)
    if average_of_students < your_points:
        return True
    else:
        return False

#Alternative Solution:

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)
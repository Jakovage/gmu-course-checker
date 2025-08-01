from course_checker import CourseChecker
from course import Course

class CourseList:
    def __init__(self, course_checkers: list[CourseChecker]):
        self.course_checkers = course_checkers

    def update_all(self):
        for course_checker in self.course_checkers:
            course_checker.update()

    def __str__(self):
        concat = "\n"

        for course_checker in self.course_checkers:
            concat += f'{course_checker.__str__()}\n\n'

        return concat
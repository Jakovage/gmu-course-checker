from course_scraper import CourseScraper
from course_checker import CourseChecker
from course_list import CourseList
from data import BASE_URL, ENDPOINTS
import re

def tokenize_course_code(code):
    # lenient with input, accepting codes like "cs461", " enGh 101", or "MatH114   "
    match = re.match(r'\s*([a-zA-Z]+)\s*(\d{1,3})\s*$', code) 
    if match:
        course_prefix = match.group(1).upper()
        course_number = match.group(2)
        return course_prefix, course_number
    else:
        return None, None
    
def main():
    term = '202570'
    course_code = 'cs110' # accepted formats
    course_section = '001'.upper()

    # course prefix: CS, ECE, MATH, ENGH | course_number: 112, 211, 310, 483
    course_subject, course_number = tokenize_course_code(course_code)

    scraper = CourseScraper(term)
    course1 = scraper.get_course(course_subject, course_number, course_section)
    course2 = scraper.get_course("CS", "211", "203")
    course3 = scraper.get_course("CS", "310", "002")
    course4 = scraper.get_course("CS", "367", "308")

    course_checker1 = CourseChecker(course1)
    course_checker2 = CourseChecker(course2)
    course_checker3 = CourseChecker(course3)
    course_checker4 = CourseChecker(course4)

    course_list = CourseList([course_checker1, course_checker2, course_checker3, course_checker4])

    print(course_list)

if __name__ == '__main__':
    main()
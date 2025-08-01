from course_scraper import CourseScraper
from course_checker import CourseChecker
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
    course = scraper.get_course(course_subject, course_number, course_section)
    print(course)

    course_checker = CourseChecker(course)
    print(course_checker)

if __name__ == '__main__':
    main()
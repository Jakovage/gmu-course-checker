from course_scraper import CourseScraper
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
    course_code = 'stat344' # accepted formats
    course_section = '008'

    # course prefix: CS, ECE, MATH, ENGH | course_number: 112, 211, 310, 483
    course_subject, course_number = tokenize_course_code(course_code)
    course_section = course_section.upper()

    scraper = CourseScraper(term)
    crn = scraper.get_crn(course_subject, course_number, course_section)

    course_url = f"{BASE_URL}{ENDPOINTS["detail_sched"]}?term_in={term}&crn_in={crn}"

    print(f"The CRN for {course_subject} {course_number} Section {course_section} is {crn}, and the link to the specific course page is:\n{course_url}\n")

if __name__ == '__main__':
    main()
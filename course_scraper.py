from bs4 import BeautifulSoup
import requests
import re

#print("start")

def tokenize_course_code(course_code):
    # lenient with input, accepting codes like "cs461", " enGh 101", or "MatH114   "
    match = re.match(r'\s*([a-zA-Z]+)\s*(\d{1,3})\s*$', course_code) 
    if match:
        course_prefix = match.group(1).upper()
        course_number = match.group(2)
        return course_prefix, course_number
    else:
        return None, None

course_code = 'cs108' # accepted formats
course_section = '001'

# course prefix: CS, ECE, MATH, ENGH | course_number: 112, 211, 310, 483
course_prefix, course_number = tokenize_course_code(course_code)


url = "https://patriotweb.gmu.edu/pls/prod/bwckschd.p_disp_dyn_sched"
session = requests.Session()

#print("defined session")

try:
    response = session.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")

#print("get request tried")

soup = BeautifulSoup(response.text, "html.parser")

#print("soup object created")

select = soup.find("select", attrs={"name" : "p_term"})
options = select.find_all("option")
term = options[1].get("value")

#print("soup findall for terms")

form = soup.find("form")
hidden_inputs = form.find_all("input", type="hidden")
data = {input.get("name"): input.get("value") for input in hidden_inputs}
data["p_term"] = term

#print("pre post to all those options")

post_url = "https://patriotweb.gmu.edu/pls/prod/bwckgens.p_proc_term_date"
post_response = session.post(post_url, data=data)
soup = BeautifulSoup(post_response.text, "html.parser")

#print("post the post")

select = soup.find("select", {"name" : "sel_subj"})
subjects = select.find_all("option")

# gets all valid course prefixes directly from patriot web
valid_prefixes = set()
for subject in subjects:
    value = subject.get("value")
    if value and value != "dummy":
        valid_prefixes.add(value)

#print("put all valid prefixes from the soup into a set")

#print(valid_prefixes)

if course_prefix not in valid_prefixes:
    print(f"{course_prefix} is not a valid subject!")
    exit()

#print("checked if course_prefix was not in valid_prefix (should be o(1) cuz its a hash set)")

data2 = {
    "term_in": "202570",
    
    # multi-select-style fields use list
    "sel_subj": ["dummy", course_prefix],
    "sel_schd": ["dummy", "%"],
    "sel_camp": ["dummy", "%"],
    "sel_levl": ["dummy", "%"],
    "sel_ptrm": ["dummy", "%"],
    "sel_instr": ["dummy", "%"],
    
    # still required, even if empty
    "sel_day": "dummy",
    "sel_insm": "dummy",
    "sel_sess": "dummy",
    "sel_attr": "dummy",
    
    # filters (empty or wildcard)
    "sel_crse": "",
    "sel_title": "",
    "sel_from_cred": "",
    "sel_to_cred": "",
    
    # time (required, even if not filtering by time)
    "begin_hh": "0",
    "begin_mi": "0",
    "begin_ap": "a",
    "end_hh": "0",
    "end_mi": "0",
    "end_ap": "a"
}

#print("put all data into data")

#'''
post_url2 = "https://patriotweb.gmu.edu/pls/prod/bwckschd.p_get_crse_unsec"
post_response2 = session.post(post_url2, data=data2)
#print(post_response2.status_code)
#with open("response_output.txt", "w", encoding="utf-8") as file:
#    file.write(post_response2.text)
#print("Final URL (after post):", post_response2.url)
#print("Redirect chain:", post_response2.history)

#print(post_response2.text[:500])

#print("posted again to get to all the courses")

soup = BeautifulSoup(post_response2.text, "html.parser")
#print(soup.text)

def find_course_crn(soup, target_number, target_section):
    table = soup.find("table", {"class" : "datadisplaytable"})
    rows = table.find_all("th", class_="ddtitle") # only html rows with class ddtitle contain the relevant information for extracting the CRN

    for row in rows:
        listing = row.find("a")
        listing_text = listing.get_text(strip=True)

        # converts something like this: "Precalculus Mathematics - 71565 - MATH 105 - 001"
        # into this: ["Precalculus Mathematics", "71565", "MATH 105", "001"]
        parts = listing_text.split(" - ") 

        if len(parts) >= 4: # in case the course name has a dash in it
            course_code = parts[-2] # e.g., "MATH 125"
            course_number = course_code.split()[-1] # extracts the number from course_code. e.g., "Math 125" -> "125"
            course_section = parts[-1]

            # returns the CRN if a valid c
            if course_number == target_number and course_section == target_section:
                return parts[-3]

#'''

crn = find_course_crn(soup, course_number, course_section)
print(crn)
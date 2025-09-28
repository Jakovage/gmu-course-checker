# PatriotWeb Course Scraper Library

A collaborative Python library and API that extracts course registration data from George Mason University's PatriotWeb system. Designed for developers who need programmatic access to live data on course offerings, seat availability, meeting times, instructors, and more.

## Features

- Scrapes real-time course registration data from PatriotWeb
- Retrieves:
  - Course titles and CRNs
  - Seat counts and enrollment caps
  - Meeting days, times, and locations
  - Waitlist availability
- Tokenizes and parses course codes (e.g., `cs112`, `  MATH   203`) for flexible querying
- Outputs data in JSON format for easy integration

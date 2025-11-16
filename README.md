# US Bikeshare Data Analysis

A Python program that allows users to explore and analyze bikeshare data from three major US cities: Chicago, New York City, and Washington. The program provides statistics on travel times, popular stations, trip durations, and user demographics. It also allows users to view raw trip data in chunks.

---

## Features

- Select city, month, and day to filter data
- Display statistics on:
  - Most frequent times of travel
  - Most popular start and end stations, including station combinations
  - Total and average trip duration
  - User demographics: user types, gender, and birth years (where available)
- Option to view raw trip data 5 rows at a time
- Easy-to-use menu interface with input validation
- Option to restart analysis or exit at any time

---

## Libraries Used

- Python 
- Pandas
- NumPy
- Calendar
- Time
- Sys

---

## Before Usage

1. Ensure Python 3.x is installed on your system  
2. Install required libraries: Pandas and NumPy  
3. Download the CSV data files for each city and place them in the same directory as the program:
   - `chicago.csv`
   - `new_york_city.csv`
   - `washington.csv`

---

## Usage

1. Run the program  
2. Follow the on-screen prompts to select:
   - City
   - Month (or "all")
   - Day of the week (or "all")  
3. View the calculated statistics for your selection  
4. Optionally, view 5 rows of raw data at a time  
5. Choose to restart analysis or exit the program when finished

---

## Notes

- Gender and birth year data are not available for Washington  
- Input validation ensures only valid options are selected  
- The program calculates the time taken to display statistics for performance insights

---

## Example Output

Welcome! Let's start exploring some US bikeshare data!  
Choose a city: Chicago  
Choose a month: March  
Choose a day: Friday  

The most common month in Chicago is March.  
The most common day of the week is Friday.  
The most common start hour for your selection is 17 o'clock.  

---

##  Contact Information
For any questions or recommendations:  
- **Bashar Bayatna**, Mechatronics Engineer | Junior Data Scientist  
- Email: [Basharbayatna11@gmail.com](mailto:Basharbayatna11@gmail.com)

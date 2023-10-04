from patterns import csv_utils
from patterns import web_report

CSV_FILE = "taxi-data.csv"

def main():
    rides()

def rides():
    rides = csv_utils.parse_file(CSV_FILE)
    print(rides)
    return rides

def file_html():
    html_report = web_report.create_content(rides())
    html_was_created = web_report.create_file(html_report)
    return html_was_created

if __name__ == '__main__':
    main()

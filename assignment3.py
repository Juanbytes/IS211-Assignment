import argparse
import re
import urllib.request
import csv


def csvfile_content(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

    return data


def main(url):
    print(f"Running main with URL = {url}... ")


def downloadData(url):
    for data_lines in downloadData(url).split("\n"):

        for i, row in enumerate(csv.reader(data_lines)):
            if i > 10000: break
        pop_browser = row[0]
        time_used = row[1]
        status = row[2]
        size = row[3]
        print(row)



    browser_count = {'FIREFOX': 0, 'CHROME': 0, 'MSIE': 0, 'SAFARI': 0}
    image_count = 0

    if re.search("PNG|GIF|JPG|JPEG", pop_browser.upper()):
        image_count += 1
    print(image_count)

    if pop_browser.upper().find("FIREFOX") != -1:
        browser_count['FIREFOX'] += 1
    elif pop_browser.upper().find("MSIE") != -1:
        browser_count['MSIE'] += 1
    elif pop_browser.upper().find("CHROME") != -1:
        browser_count['CHROME'] += 1
    elif pop_browser.upper().find("SAFARI") != -1:
        browser_count['SAFARI'] += 1


if __name__ == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to cvs_file", type=str, required=True)
    args = parser.parse_args()
    main(args.url)

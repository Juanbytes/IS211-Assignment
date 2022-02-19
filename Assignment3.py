import argparse
import urllib.request
import csv
import re


def downloadData(url):
    with urllib.request.urlopen(url) as response:
        datafile = response.read().decode('utf-8')
    return datafile


def processData(datafile):
    readfile = csv.reader(datafile)
    line_count = 0
    imagecount = 0

    chrome = ['Google Chrome', 0]
    msie = ['Internet Explorer', 0]
    safari = ['Safari', 0]
    firefox = ['Firefox', 0]
    for line in readfile:
        line_count += 1
        if re.search("firefox", line[2], re.I):
            firefox[1] += 1
        elif re.search(r"MSIE", line[2]):
            msie[1] += 1
        elif re.search(r"Chrome", line[2]):
            chrome[1] += 1
        elif re.search(r"Safari", line[2]) and not re.search("Chrome", line[2]):
            safari[1] += 1
        if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
            imagecount += 1

    image_hit = (float(imagecount) / line_count) * 100
    pop_browser = [chrome, msie, safari, firefox]
    top_browser = 0
    top_name = ' '
    for b in pop_browser:
        if b[1] > top_browser:
            top_browser = b[1]
            top_name = b[0]
        else:
            continue

    msg = ('There were {} page hits today, image requests account for {}% of'
           'hits. \n{} has the most hits with {}.').format(line_count, image_hit,
                                                           top_name, top_browser)
    print(msg)


def main(url):
    print(f"Running main with URL = {url}...")
    content = downloadData(url)
    print(content)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
        args = parser.parse_args()
        main(args.url)
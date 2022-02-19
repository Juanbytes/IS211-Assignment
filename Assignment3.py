import urllib.request
import csv
import re
import time
import argparse


def download_data():
    required_args = ['url']
    parser = argparse.ArgumentParser()
    for r in required_args:
        parser.add_argument("--{0}".format(r), required=True)
    args = parser.parse_args()
    urllib.request.urlretrieve(args.url, 'weblog.csv')


def process_data():
    with open('weblog.csv', 'r') as f:
        csv_reader = csv.reader(f)
        count_images = 0
        safari = 0
        firefox = 0
        chrome = 0
        ie = 0
        n_list = []
        for line in csv_reader:
            if re.findall("jpg|png|gif", line[0], flags=re.I):
                count_images += 1
                s = line[1]
                k = time.strptime(s, "%Y-%m-%d %H:%M:%S").tm_hour
                n_list.append(k)
                if re.search("safari/", line[2], flags=re.I):
                    if not re.search("chrome", line[2], flags=re.I):
                        safari += 1
                if re.search("firefox/", line[2], flags=re.I):
                    if not re.search("seamonkey/", line[2], flags=re.I):
                        firefox += 1
                if re.search("chrome/", line[2], flags=re.I):
                    if not re.search("chromium", line[2], flags=re.I):
                        chrome += 1
                if re.search("msie", line[2], flags=re.I):
                    ie += 1
    browsers = {'Safari': safari,'Firefox': firefox,'Chrome': chrome,'IE': ie}

    row_count = sum(1 for row in csv.reader(open('weblog.csv')))
    math = 100 * count_images / row_count
    print("Image requests account for {} of all requests".format(math))

    pop_browser = max(browsers, key=browsers.get)
    print("The most popular browser was {}".format(pop_browser))

    count_hits_list = [[x, n_list.count(x)] for x in set(n_list)]
    for n in count_hits_list:
        print("Hour {} has {} hits".format(n[0], n[1]))
    f.close()


if __name__ == "__main__":
    download_data()
    process_data()

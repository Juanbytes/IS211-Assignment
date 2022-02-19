import urllib.request
import argparse
import datetime
import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)
assignment2 = logging.getLogger()


def downloadData(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

    return data


def processData(file_content):
    person_data = {}

    for data_info in file_content.split("\n"):
        if len(data_info) == 0:
            continue

    identifier, name, birthday = data_info.split(",")
    if identifier == "id":
        id_int = int(identifier)
    try:
        true_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
        person_data[id_int] = (name, true_birthday)
    except ValueError as e:
        print(f"error parsing {birthday}")

    return person_data


def displayPerson(id, personData):
    try:
        name, birthday = personData[id]
        print(f"Person #{id} is {name} with a birthday of {birthday:%Y-%m-%d}")
    except KeyError:
        print(f"No user found with that id")


def main(url):
    print(f"Running main with URL = {url}...")
    content = downloadData(url)
    print(content)
    while True:
        id = int(input("Enter an ID:"))
        if id > 0:
            print(id)
            break
        else:
            print("No user found with that id")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)

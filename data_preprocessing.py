import csv
import tts


def sort_data(file):
    data = []

    tts.speak("Getting Data", print_text=True)
    with open(file, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    tts.speak("Done Getting Data", print_text=True)

    headers = data[0]
    planet_data = data[1:]

    tts.speak("Converting data to lower case", print_text=True)
    for data_point in planet_data:
        data_point[2] = data_point[2].lower()
    tts.speak("Done converting data to lower case", print_text=True)

    tts.speak("Sorting Data", print_text=True)
    planet_data.sort(key=lambda planet_data: planet_data[2])
    tts.speak("Done Sorting Data", print_text=True)

    tts.speak("Creating new sorted csv file", print_text=True)
    with open("confirmed_sorted.csv", "a+") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)
    tts.speak("Done creating new sorted csv file", print_text=True)


def merge_data(file, file_2):
    dataset_1 = []
    dataset_2 = []

    with open(file, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dataset_1.append(row)

    with open(file_2, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dataset_2.append(row)

    headers_1 = dataset_1[0]
    planet_data_1 = dataset_1[1:]

    headers_2 = dataset_2[0]
    planet_data_2 = dataset_2[1:]

    headers = headers_1 + headers_2
    planet_data = []

    for index, row in enumerate(planet_data_1):
        planet_data.append(planet_data_1[index] + planet_data_2[index])

    with open("final.csv", "a+") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)


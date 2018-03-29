# -*- encoding: utf-8 -*-


def process(data, events, car):
    pas_car = {}
    train_cars = {}
    cars = list()

    for train in data:
        for carr in train["cars"]:
            for man in carr["people"]:
                pas_car[man] = carr["name"]

        train_cars[train["name"]] = [carr["name"] for carr in train["cars"]]

    for event in events:
        if event["type"] == "walk" and pas_car[event["passenger"]]:
            for train in train_cars:
                for counter, carr in enumerate(train_cars[train]):
                    if pas_car[event["passenger"]] == carr:
                        if 0 <= counter + event["distance"] < len(carr):
                            pas_car[event["passenger"]] = train_cars[train][counter + event["distance"]]
                            break
                        else:
                            return -1

        elif train_cars[event["train_from"]]:
            if 0 < event["cars"] <= len(train_cars[event["train_from"]]):
                for number in range(event["cars"]):
                    cars.append(train_cars[event["train_from"]][-event["cars"] + number])
                del train_cars[event["train_from"]][-event["cars"]:]
                for number in range(event["cars"]):
                    train_cars[event["train_to"]].append(cars[number])
                cars.clear()
            else:
                return -1
        else:
            return -1

    count = 0
    for man in pas_car:
        if pas_car[man] == car:
            count += 1
    return count

    for train in data:
        print(train['name'])
        for car in train['cars']:
            print('\t{}'.format(car['name']))
            for man in car['people']:
                print('\t\t{}'.format(man))
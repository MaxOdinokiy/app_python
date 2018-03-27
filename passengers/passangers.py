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
        if event["type"] == "walk":
            for man in pas_car:
                if man == event["passenger"]:
                    for train in train_cars:
                        for counter, carr in enumerate(train_cars[train]):
                            if pas_car[man] == carr:
                                if 0 <= counter + event["distance"] < len(train_cars[train]):
                                    pas_car[man] = train_cars[train][counter + event["distance"]]
                                    break
                                else:
                                    return -1
        
        else:
            for train in train_cars:
                if train == event["train_from"]:
                    if 0 < event["cars"] <= len(train_cars[train]):
                        lenght = len(train_cars[train]) - event["cars"]
                        for number in range(event["cars"]):
                            cars.append(train_cars[train][lenght + number])
                        del train_cars[train][-event["cars"]:]
                        for train2 in train_cars:
                            if train2 == event["train_to"]:
                                for number in range(event["cars"]):
                                    train_cars[train2].append(cars[number])
                        cars.clear()
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
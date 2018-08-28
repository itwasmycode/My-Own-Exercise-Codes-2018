# midwfapao , best solution for iterating. :P


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    return [value[0] for key, value in cars.items()]


def get_all_matching_models(grep='CO'):
    return sorted([y for z in [y for x, y in cars.items()] for y in z if grep.lower() in str(y).lower()])


def sort_car_models():
    return {x: sorted(y) for x, y in cars.items()}


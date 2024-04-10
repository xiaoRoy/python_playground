signals = {'red': 'smile for the camera', 'green': 'go', 'yellow': 'go faster'}


def learn_iterate_dictionary_keys():
    for signal_key in signals:
        print(signal_key)


def learn_iterate_dictionary_values():
    for signal_value in signals.values():
        print(signal_value)


def learn_iterate_dictionary_first():
    for signal in signals.items():
        print(signal)


def learn_iterate_dictionary_second():
    for signal_key, signal_value in signals.items():
        print(f'{signal_key}:{signal_value}')

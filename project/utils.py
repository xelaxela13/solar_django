import configparser


def add_settings(database_dict, file):
    try:
        data = database_dict['default']
    except KeyError:
        return
    config = configparser.ConfigParser()
    try:
        config.read(file)
        for section in config.sections():
            for key in config[section]:
                data[key.upper().strip()] = config[section][key].strip()
    except KeyError:
        pass
    except configparser.MissingSectionHeaderError:
        return
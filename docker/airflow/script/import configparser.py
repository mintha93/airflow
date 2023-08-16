import configparser

def list_config_differences(config1_path, config2_path):
    config1 = configparser.ConfigParser()
    config2 = configparser.ConfigParser()

    config1.read("C:/Users/Admin/Documents/airflow_in_docker_compose-main/mnt/airflow/airflow.cfg")
    config2.read("C:/Users/Admin/Downloads/Compressed/airflow-materials/airflow-materials/airflow-section-3/mnt/airflow/airflow.cfg")

    differences = {}
    for section in config1.sections():
        if section in config2.sections():
            options_only_in_section1 = set(config1.options(section)) - set(config2.options(section))
            options_only_in_section2 = set(config2.options(section)) - set(config1.options(section))
            differing_options = {}

            for option in config1.options(section):
                if option in config2.options(section):
                    value1 = config1.get(section, option)
                    value2 = config2.get(section, option)
                    if value1 != value2:
                        differing_options[option] = (value1, value2)

            if options_only_in_section1 or options_only_in_section2 or differing_options:
                differences[section] = {
                    "options_only_in_section1": options_only_in_section1,
                    "options_only_in_section2": options_only_in_section2,
                    "differing_options": differing_options
                }

    print("\nOptions differences within sections:")
    for section, diffs in differences.items():
        print(f"\nIn section '{section}':")
        if diffs["options_only_in_section1"]:
            print("Options only in the first config:")
            for option in diffs["options_only_in_section1"]:
                value = config1.get(section, option)
                print(f"  Option: {option}\n    Value in config1: {value}")
        if diffs["options_only_in_section2"]:
            print("Options only in the second config:")
            for option in diffs["options_only_in_section2"]:
                value = config2.get(section, option)
                print(f"  Option: {option}\n    Value in config2: {value}")
        if diffs["differing_options"]:
            print("Differing option values:")
            for option, (value1, value2) in diffs["differing_options"].items():
                print(f"Option: {option}\n  Value in config1: {value1}\n  Value in config2: {value2}")

if __name__ == "__main__":
    config1_path = "path_to_first_config_file.conf"
    config2_path = "path_to_second_config_file.conf"
    list_config_differences(config1_path, config2_path)
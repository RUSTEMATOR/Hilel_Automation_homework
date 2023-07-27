string = input()

string_length_unique = len(set(string))

report_structure = "" + string + ""

report = f"Word {report_structure} has {len(string)} letters. {set(string)} of them are Unique"

recomendation = f"Word needs {10 - len(string)} more characters to get True"

positive_attempts_list = []
negative_attempts_list = []


if string_length_unique >= 10:
    print(True)
    print(report)
    positive_attempts_list.append(string)
    print("A new word is added to the positives")
    file_path = "C://Users//samoi//OneDrive//Рабочий стол//list_of_positives.txt"
    with open(file_path, "a") as file:
        file.write(str(positive_attempts_list))

else:
    print(False)
    print(report)
    print(recomendation)
    negative_attempts_list.append(string)
    print('A new word is added to the negatives')
    file_path = "C://Users//samoi//OneDrive//Рабочий стол//list_of_negatives.txt"
    with open(file_path, "a") as file:
        file.write(str(negative_attempts_list))

# STUDENTS MARKS DATA to get highest marks scored
# for maths

def calculate_highest_mark_in_maths(student_list):
    highest_score_in_maths = 0
    highest_score_in_maths_name = " "
    for student in student_list:
        if student.get("maths") > highest_score_in_maths:
            highest_score_in_maths = student.get("maths")
            highest_score_in_maths_name = student.get("name")

    print(f"highest score in maths is {highest_score_in_maths} scored by {highest_score_in_maths_name}")


# for science
def calculate_highest_mark_in_science(student_list):
    highest_score_in_science = 0
    highest_score_in_science_name = " "
    for student in student_list:
        if student.get("science") > highest_score_in_science:
            highest_score_in_science = student.get("science")
            highest_score_in_science_name = student.get("name")

    print(f"higest score in science is {highest_score_in_science} scored by {highest_score_in_science_name}")


def calculate_highest_mark_in_english(student_list):
    highest_score_in_english = 0
    highest_score_in_english_name = " "
    for student in student_list:
        if student.get("english") > highest_score_in_english:
            highest_score_in_english = student.get("english")
            highest_score_in_english_name = student.get("name")

    print(f"higest score in english is {highest_score_in_english} scored by {highest_score_in_english_name}")


def calculate_highest_mark_in_hindi(student_list):
    highest_score_in_hindi = 0
    highest_score_in_hindi_name = " "
    for student in student_list:
        if student.get("hindi") > highest_score_in_hindi:
            highest_score_in_hindi = student.get("hindi")
            highest_score_in_hindi_name = student.get("name")

    print(f"highest score in hindi is {highest_score_in_hindi} scored by {highest_score_in_hindi_name}")



student_1 = {
    'name': "sathish",
    'maths': 75,
    'science': 95,
    'english': 65,
    'hindi': 80
}
student_2 = {
    "name": "umesh",
    "maths": 85,
    "science": 65,
    "english": 70,
    "hindi": 90
}
student_3 = {
    "name": "shruthi",
    "maths": 90,
    "science": 70,
    "english": 95,
    "hindi": 70
}
student_4 = {
    "name": "vinay",
    "maths": 95,
    "science": 80,
    "english": 45,
    "hindi": 60
}
student_list = [student_1, student_2, student_3, student_4]


calculate_highest_mark_in_maths(student_list)
calculate_highest_mark_in_science(student_list)
calculate_highest_mark_in_english(student_list)
calculate_highest_mark_in_hindi(student_list)



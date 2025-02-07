from school_schedule.student import *


def test_adding_one_class_increases_class_length():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)

    ellis.add_class("Pottery")

    assert ellis.get_num_classes() == 2
    assert ellis.classes == ["Painting", "Pottery"]
    assert "Pottery" in ellis.classes

# write 3 more unit tests

def test_init_sets_student_data():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Geometry"]

    ellis = Student(name, grade, classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes

def test_get_num_classes_returns_correct_length():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Geometry", "Basket Weaving", "Table Tennis"]

    ellis = Student(name, grade, classes)

    assert ellis.get_num_classes() == 4

def test_display_classes_returns_classes_as_strings():
    name = "Ellis"
    grade = "junior"
    classes = ["Basket Weaving", "Table Tennis"]

    ellis = Student(name, grade, classes)

    assert ellis.display_classes() == "Basket Weaving, Table Tennis"

# - create a function that will return the student with more classes
# - create a test for that function

def test_return_student_with_more_classes():
    name = "Ellis"
    grade = "junior"
    classes = ["Basket Weaving", "Table Tennis"]
    name2 = "Julia"
    grade2 = "freshman"
    classes2 = ["Basket Weaving", "Table Tennis", "Drama"]

    ellis = Student(name, grade, classes)
    julia = Student(name2, grade2, classes2)

    student = student_with_more_classes(ellis, julia)

    assert student == julia
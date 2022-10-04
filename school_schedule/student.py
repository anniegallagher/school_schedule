class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        self.classes.append(class_name)

    def get_num_classes(self):
        return len(self.classes)

    def display_classes(self):
        return(", ".join(self.classes))

    def summary(self):
        return (f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes : {self.display_classes()}")

def student_with_more_classes(student1, student2):
    if student1.get_num_classes() > student2.get_num_classes():
        return student1
    return student2
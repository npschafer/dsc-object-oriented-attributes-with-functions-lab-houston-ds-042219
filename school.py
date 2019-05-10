class School:
    def __init__(self, name):
        self.name = name
        self.roster = {}
    def add_student(self, name, grade):
        if grade in self.roster.keys():
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
    def grade(self, grade):
        return self.roster[grade]
    def sort_roster(self):
        sorted_roster = {}
        for grade, class_list in self.roster.items():
            sorted_roster[grade] = sorted(class_list)
        return sorted_roster
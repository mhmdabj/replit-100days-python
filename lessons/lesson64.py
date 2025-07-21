class animal:
    species = None
    name = None
    sound = None
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    def talk(self):
        print((f"{self.name} says {self.sound}"))

class bird(animal):
    def __init__(self, color):
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color

def animal_example():
    cow = animal("Ermintrude", "Bo Taurus", "Moo")
    print(cow.sound)
    polly = bird("Green")
    polly.talk()
    print(polly.color)

class job:
    name = None
    salary = None
    hours = None
    def __init__(self, name, salary, hours):
        self.name = name
        self.salary = salary
        self.hours = hours
class doctor(job):
    def __init__(self, speciality, yearsExperience):
        self.name = "no name"
        self.salary = "$ Doing very nicely thank you"
        self.hours = "50"
        self.speciality = speciality
        self.yearsExperience = yearsExperience
class teacher(job):
    def __init__(self, subject, position):
        self.name = "test"
        self.salary = "$ Nowhere near enough"
        self.hours = "All of them"
        self.subject = subject
        self.position = position

def job_example():
    print("🌟Jobs Jobs Jobs!🌟")
    lawyer = job("Lawyer", "$ Squillions", "60")
    print(f"Job Type: {lawyer.name}")
    print(f"Salary: {lawyer.salary}")
    print(f"Hours worked: {lawyer.hours}")
    teacherSpecial = teacher("test", "test32")
    print(f"Job Type: {teacherSpecial.name}")
    print(f"Salary: {teacherSpecial.salary}")
    print(f"Hours worked: {teacherSpecial.hours}")

if __name__ == "__main__":
    animal_example()
    job_example() 
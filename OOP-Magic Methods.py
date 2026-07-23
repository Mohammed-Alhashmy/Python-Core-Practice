class skill:
    def __init__(self):
        self.mySkills = ["Python", "Html", "Css"]
    def __str__(self):
        return f"My skill is {self.mySkills}"
    def __len__(self):
        return len(self.mySkills)
MyFile = skill()

print(MyFile)
print(len(MyFile))

MyFile.mySkills.append("Java script")
MyFile.mySkills.append("MySQL")
MyFile.mySkills.append("Java")

print(MyFile)
print(len(MyFile))


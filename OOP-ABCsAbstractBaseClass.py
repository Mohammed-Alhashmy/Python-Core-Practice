from abc import ABCMeta, abstractmethod


class Programming(metaclass=ABCMeta) :


    @abstractmethod
    def has_oop(self):

        pass

    def has_name(self):

        pass
    

class python(Programming):

    def has_oop(self):

        return "Yes"

class pascal(Programming):

    def has_oop(self):

        return "No"
    
    #def has_name(self):

        return "Pascal"



test = pascal()

print(test.has_oop())
print(test.has_name())
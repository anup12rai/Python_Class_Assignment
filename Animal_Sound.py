# # Create a base class Animal with a method sound().
# # Then, create two derived classes Dog and Cat 
# # that override the sound() method to return the 
# # sound a dog and a cat make, respectively. Demonstrate
# # polymorphism by creating a list of animals and calling 
# # their sound() method in a loop

# from playsound import playsound
# # playsound(r"C:\Users\ACER\Documents\Desktop\assigment\E4L39FT-cat-meow.mp3")
# # playsound(r"C:\Users\ACER\Documents\Desktop\assigment\Z5QVAKY-dog.mp3")
# class Animal:
#     def sound(self):
#         pass
# class Cat():
#     def     

class Animal:
    def sound(self):
       pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"


animals = [Dog(), Cat(), Dog(), Cat()]

for animal in animals:
    print(animal.sound())

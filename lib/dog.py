#!/usr/bin/env python3

class Dog:
    def bark(self):
        print("Woof!")

    # Instance method definition
    def sit(self):
        print("The dog is sitting.")

if __name__ == "__main__":
    fido = Dog()
    fido.bark()  
    fido.sit()   

import random as rm
symbols = "[]{}()!@#$%^&*"
numbers = "1234567890"
lower = "abcdefghijklmnopqurstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"
all = upper + symbols + numbers + lower
lenght = 9
password = "".join(rm.sample(all, lenght))
print(" The Password Is : ",password)
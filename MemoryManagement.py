import os

def predict_memory(file1, file2):

    print(file2 + "'s size: " + str(os.path.getsize(file2)))

    a = open(file2, 'r')
    a2 = file1
    b2 = a.read()


    if a2 == b2:
       print("Approximate size of " + file1[0:5] + " is " + str(os.path.getsize(file1)))
    else:
       x = len(a2)
       y = len(b2)
       if x > y:
          i = y
          j = 0
          while not i == x:
             i += 1
             j += 1
          print(file1[0:5] + " is bigger than " + file2 + " by " + str(j))
        elif x < y:
          i = x
          j = 0
          while not i == y:
              i += 1
              j += 1
         print(file2 + " is bigger than " + file1[0:5] + " by " + str(j))

predict_memory("Hello", 'Test2.txt')
print("Hello")

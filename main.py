#take one input in  hour and another input in minutes convert hour into minutes and add them
"""a = int(input("enter number of hours:"))
b = int(input("enter number of minutes:"))
c = a * 60
d = c + b
print("total number of minutes:",d,"minutes")"""
#take two names as input and get output as names separated by comma
"""name1 = input("enter name1:")
name2 = input("enter name2:")
name3 = input(name1 + ","+ name2)
print(name3)"""
#take username and favourite color as input and print username and favourite color
"""username = input("enter your name:")
color = input("enter your favourite color:")
print(f'hello {username}.Your favourite color is {color}')"""
#take integer as input and get its remainder when it divides by 2
"""a = int(input("enter a number: "))
b = a % 2 
print("remainder is : ",b)"""
#take superhero as input and print i am (superhero)
"""super_hero = input("enter your superhero: ")
print(f"I am {super_hero}")"""

#take two inputs m and n check 1 to m is divisible by n and sum of those numbers
"""m = int(input("enter a number:"))
n = int(input("enter another number:"))
sum = 0
for i in range (1,m+1):
  if i % n == 0:
    sum = sum + i
print("sum is ",sum)"""

#check whether the given number is prime
"""n = int(input("enter a number:"))
flag = True
for i in range(2,n):
  if n % i == 0:
    flag = False
    break
if flag:
  print("prime")
else:
  print("not prime")"""
#find gcd between two numbers
"""n = int(input("enter a number:"))
m = int(input("enter another number:"))
gcd = 1
for i in range(1,min(n,m)+1):
  if n % i == 0 and m % i == 0:
    gcd = i
print("gcd is ",gcd)"""
#take two range of inputs and print sum of odd and even numbers separately
"""n = int(input("enter a number:"))
m = int(input("enter another number:"))
sum_even = 0
sum_odd = 0
for i in range(n,m+1):
  if i % 2 == 0:
    sum_even = sum_even + i
  else:
    sum_odd = sum_odd + i
print("sum of even numbers is " ,sum_even)
print("sum of odd numbers is ",sum_odd)"""
#ATM has currency notes of 10,50,100.Calculate number of  notes to withdraw a certain amount and total number of notes.
"""n = int(input("enter a number:"))
note_10 = 0
note_50 = 0
note_100 = 0
while n > 0:
  if n >= 100:
    note_100 = note_100 + 1
    n = n - 100
  elif n >= 50:
    note_50 = note_50 + 1
    n = n - 50
  else:
    note_10 = note_10 + 1
    n = n - 10
print("total number of notes of 100 is ",note_100)
print("total number of notes of 50 is ",note_50)
print("total number of notes of 10 is ",note_10)
print("total number of notes are ",note_10+note_50+note_100)"""

#take list of numbers as input and find the index of smallest element
"""n = int(input("enter a number(range):"))
l = []
for i in range(n):
  l.append(int(input("enter a number:")))
print(l)
min = l[0]
for i in range(n):
  if l[i] < min:
    min = l[i]
print("index of smallest number is ",l.index(min))"""
#take tuple as input and pack and unpack it
"""t = (1,2,3,4,5)
print(t)
x,y,z,w,v = t
print(x,y,z,w,v)"""
#take two lists as input and find the union of those lists
"""n = int(input("enter the number of values in list :"))
l1 = []
l2 = []
for i in range(n):
  l1.append(int(input("enter a number in list1 :")))
for i in range(n):
  l2.append(int(input("enter a number in list2 :")))
print(l1)
print(l2)
l3 = l1 + l2
print(l3)
l3 = list(set(l3))
print(l3)"""
#program for addition of two matrices
"""
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]
y = [[2,2,3],
     [4,9,6],
     [7,8,2]]
z = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(x)):
  for j in range(len(x[0])):
    z[i][j] = x[i][j] + y[i][j]
print(z)"""
#take tuple of numbers as input and find mean and median
"""x = eval(input("enter a tuple of numbers:"))
print(x)
print("mean is ",sum(x)/len(x))

n = len(x)

if n % 2 == 0:
  print("median is ",(x[n//2-1]+x[n//2])/2)
else:
  print("median is ",x[n//2])"""
#input satellite name as string and find length of each string

"""satellite_name = input("enter a satellite names (comma-separated):")
satellite_list = satellite_name.split(",")
for name in satellite_list:
  name = name.strip()
  length = len(name)
  print(f"The length of {name} is {length} characters.")"""

#input list of book genre as string and count number of occurence of each book genre
"""genre = input("enter a book genre (comma-separated):")
genre_list = genre.split(",")
for genre in genre_list:
  genre = genre.strip()
  count = genre_list.count(genre)
  print(f"{genre} occurs {count} times.")"""



#input list of book genre as string and count number of occurence of each book genre
"""book_genres = input("enter a book genre (comma-separated):")
book_genres_list = book_genres.split(",")
print(book_genres_list)


genre_counts = {}


for genre in book_genres_list:
    
    if genre in genre_counts:
        
        genre_counts[genre] += 1
    else:
        
        genre_counts[genre] = 1


for genre, count in genre_counts.items():
    print(f"{genre}: {count}")"""
#input cricketer's name as string and find length of each name
"""cricketer_name = input("enter a cricketer's name (comma-separated):")
cricketer_name_list = cricketer_name.split(",")
for name in cricketer_name_list:
 
  print(name,":",len(name))"""
#input student srn,marks in 5 subjects and create a dictionary of srn and total marks
"""info=input("take std srn,marks for 5 subjects")
details=info.split(',')
d={}
d['srn']=details[0]
d['m1']=details[1]
d['m2']=details[2]
d['m3']=details[3]
d['m4']=details[4]
d['m5']=details[5]
d['tot']=int(d['m1'])+int(d['m2'])+ int(d['m3'])
print(d)"""
#input of cars in specified format and create a dictionary with brand name as keyvalue and list of unique cc value offered by it with format of brandname,launchyear,modelname,cc
"""car_data = {}


while True:
    car_info = input("Enter car information (brand name, launch year, model name, cc), or 'done' to finish: ")

    if car_info.lower() == 'done':
        break

    brand, launch_year, model_name, cc = car_info.split(',')
    brand = brand.strip()
    cc = cc.strip()"""

    
   
"""restaurant= {}
n = int(input("Enter the number of restaurants: "))
for i in range(n):
    name, location1, revenue1 = input("Enter restaurant name, location1, and revenue separated by commas: ").split(',')
    revenue1 = float(revenue1)  
    location2, revenue2 = input(f"Enter location2 and revenue for {name} separated by a comma: ").split(',')
    revenue2 = float(revenue2)
    restaurant[name] = {
        location1: revenue1,
        location2: revenue2
    }
print("Restaurant Data:")
print(restaurant)"""
"""tup1 = input("enter some numbers:")
tup2 = tup1.split(',')
tup3 = tuple(tup2)
print(tup3)
for i in tup3:
  print(i)"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.pop("model"))

"""i = 0
while i < 6:
  i += 1
  if i == 3:
    continue

  print(i)"""

"""i = 0
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")"""

def my_function(*kids):

  print("The youngest child is " + kids[2])

my_function()










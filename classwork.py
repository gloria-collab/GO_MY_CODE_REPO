# 🚨 Don't change the code below 👇
# print("Welcome to Python Smoothie Shop!")
'''size = input("Choose a size: S, M, or L ")
add_protein = input("Add protein powder? Y or N ")
add_berries = input("Add berries? Y or N ")
add_sweetener = input("Add natural sweetener? Y OR N")
size_sweetener= input.lower("S, M, or L ")

bill= 0

if size.lower() == "s":
  bill += 5
elif size.lower() == "m":
  bill += 7
elif size.lower() == "l":
  bill += 9
else:
    print("Invalid size.")

if add_protein == "y":
    bill += 2
  
if add_berries and size == "s":
    bill += 1
elif add_berries and size in ["m", "l"]:
    bill += 1.5
if add_sweetener == "y":
    if add_sweetener == "s":
     print("There are no available sweetner in small size")
    else:
     bill += 0.5

print(f"your total price is {bill}, pls make your way to the cashier stand to make payment")
'''
### nsted list , 
'''nested_list = ['goria', 'george', 'john', 'luck','chidi','johana',[1,2,3,4,5,6,['true', 'false']]]
print(nested_list[6][6][1])'''



nested_list = [
    1,
    [2, 3, [4, 5]],
    [
        [6, 7],
        [
            8,
            [9, 10, [11, [12, 13]]]
        ]
    ],
    [
        "a",
        ["b", ["c", ["d", ["e", ["f", ["g", 14]]]]]]
    ],
    [15, [16, [17, [18, [19, [20, "end"]]]]]
]]


#print (nested_list[1][2][1])
5

#question 2
x=nested_list[2]
y=x[1]
#print(y)
xy= y[1]
#print(xy)
xyx= xy[2]
print(xyx)
xyxx= xyx[1][0]
print(xyxx)

#question 3
print(nested_list[3][1][1][1][1][1][1][0])

#question 4
print(nested_list[2][1][1][2][1][0])
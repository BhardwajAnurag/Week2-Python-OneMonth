#looping over a list
nos = [1, 3, 10, 100]
stocks = ["TSLA", "GOOG", "AAPL"]
rndm = ["dogs", 24, ["another list", "yes", 66], 1/3]

for i in nos:
    print("the nos are: ", i)

for i in stocks:
    print("stocks are: ", i)

for n in rndm:
    print("random things: ", n)

#to add or remove from a list or create a new list
nos.append(55)
nos.append("Anurag")

nos.remove(3)
print(nos)

#squared challenge
sq = int(input("Enter a number i will tell you square: \n"))
sq2 = int(input("Enter a 2nd number i will tell you square: \n"))
sq3 = int(input("Enter a 3rd number i will tell you square: \n"))

# sq = sq ** 2
# sq2 = sq2 ** 2
# sq3 = sq3 ** 2

sqlist = [sq, sq2, sq3]
for i in sqlist:
    print("The square is: ", i**2)

#range
for i in range(1,11):
    print(i, "Square is ", i**2)

wohoo = list(range(1,6))
print(wohoo)

#accessing data in list using []
second_stock = stocks[1]
print(second_stock)

print("Total in stock list are", len(stocks))
print("its type is: ", type(stocks))

demo = rndm[-2]
print(demo)
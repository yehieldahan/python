print("Cost of products in the supermarket:""\nPrices:""\n---------""\ncolas=5""\nchicken=20kg""\ncucumber=2""\ntomato=3")

colas=int(input("Enter how many colas:"))
chicken=int(input("Enter how many chicken:"))
cucumber=int(input("Enter how many cucumber:"))
tomato=int(input("Enter how many tomato:"))

print("\nSummary of your order:\n-----------\ntomato: " + str(tomato) + "\ncucumber: " + str(cucumber) + "\ncolas: " + str(colas) + "\nchicken: " + str(chicken))

summary=(colas*5)+(chicken*20)+(cucumber*2)+(tomato*3)
print("Total price of the purchase= " + str(summary) + " NIS without tax")
print("Total price of the purchase= " + str("%.2f" %(summary*1.17)) + " NIS with tax")

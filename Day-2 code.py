x = float(input("What was the total bill? ")) # x = bill # y = percentage tip
y = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
z = int(input("how many people should split the bill? "))
k = (x*y)/(z*100) +x/z                        #x/z(1+(y/100))
k = print(round(k, 2))

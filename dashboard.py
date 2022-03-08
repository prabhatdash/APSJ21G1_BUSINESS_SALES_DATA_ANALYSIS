
import GitHub.functions as functions
def dashboard():
      print("#" * 50)
      print("Enter 1 to print the TOTAL SALES")
      print("Enter 2 to print the TOTAL NO. OF ITEMS SOLD ALL THROUGHOUT")
      print("Enter 3 to print the AVERAGE SALES")
      print("Enter 4 to print the TOP 5 SALES BY PRODUCT CATEGORY")
      print("Enter 5 to print the TOTAL REVENUE CITY WISE")
      print("Enter 6 to print the TOTAL REVENUE CUSTOMER TYPE WISE")
      print("Enter 7 to print the TOTAL REVENUE TRANSACTION MODE WISE GRAPHICALLY")
      print("Enter 8 to print the TOTAL REVENUE PRODUCT CATEGORY WISE GRAPHICALLY")
      print("Enter 9 to print the TOTAL REVENUE GROSS INCOME WISE GRAPHICALLY")
      print("Enter 10 to exit")
      print('#' * 50)
      inp=int(input())
      if inp == 1:
          functions.totalsales()
          dashboard()
      elif inp == 2:
          functions.itemssold()
          dashboard()
      elif inp == 3:
          functions.avgsale()
          dashboard()
      elif inp == 4:
          functions.prodsales()
          dashboard()
      elif inp == 5:
          functions.revenuepercity()
          dashboard()
      elif inp == 6:
          functions.revenuecustomerwise()
          dashboard()
      elif inp == 7:
          functions.revenuetransactionmode()
          dashboard()
      elif inp == 8:
          functions.revenueproductcategory()
          dashboard()
      elif inp == 9:
          functions.revenuegrossincome()
          dashboard()
      elif inp==10:
          exit()




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('dataset.csv',engine="python" )
list = df['Unit price'] * df['Quantity']
df['FinalPrice'] = list
df1=df

def totalsales():
        total_sale = df['FinalPrice'].sum()
        print('TOTAL SALE=', total_sale)

def itemssold():
        items_sold = df['Quantity'].sum()
        print('ITEMS SOLD=', items_sold)

def avgsale():
        total_sale = df['FinalPrice'].sum()
        items_sold = df['Quantity'].sum()
        avg_sale = total_sale / items_sold
        print('AVERAGE SALE=', avg_sale)

def prodsales():
        prod_sales = pd.DataFrame(df.groupby('Product category').sum()['FinalPrice'])
        prod_sales.sort_values(by=['FinalPrice'], inplace=True, ascending=False)
        top_products = prod_sales.head(5)
        print(top_products)

def revenuepercity():
        print('REVENUE PER CITY')
        x = pd.DataFrame(df.groupby('City').sum()['FinalPrice'])
        print(x)

def revenuecustomerwise():
        print('REVENUE PER CUSTOMER TYPE')
        mostvalcus = pd.DataFrame(df.groupby('Customer type').sum()['FinalPrice'])
        print(mostvalcus)


def revenuetransactionmode():
        mostvalcus = pd.DataFrame(df.groupby('Payment').sum()['FinalPrice'])

        l5=[]
        l6=[]
        for i in mostvalcus.iterrows():
                l5.append(i[0])
                l6.append(i[1][0])
        plt.plot(l5,l6, linewidth=5)
        plt.xlabel('Payment Type',size=15)
        plt.ylabel('Revenue',size=15)
        plt.title("Transaction Mode",size=20)
        plt.show()

def revenueproductcategory():
        list = df['Unit price'] * df['Quantity']
        df['FinalPrice'] = list
        prod_sales = pd.DataFrame(df.groupby('Product category').sum()['FinalPrice'])
        prod_sales.sort_values(by=['FinalPrice'], inplace=True, ascending=False)
        top_prods = prod_sales.head(5)
        l1 = []
        l2 = []
        for i in top_prods.iterrows():
                l1.append(i[0])
                l2.append(i[1][0])
        plt.bar(l1, l2, width=0.5)
        plt.ylabel(' Total Price', size=20)
        plt.xlabel('Product Category', size=20)
        plt.title('Graph of Top Five Product Category per Price ', size=25)
        plt.show()

def revenuegrossincome():
        list = df['gross income'] * df['Quantity']
        df['FinalPrice'] = list
        prod_sales = pd.DataFrame(df.groupby('Product category').sum()['FinalPrice'])
        prod_sales.sort_values(by=['FinalPrice'], inplace=True, ascending=False)
        top_prods = prod_sales.head(5)
        l1 = []
        l2 = []
        for i in top_prods.iterrows():
                l1.append(i[0])
                l2.append(i[1][0])
        plt.bar(l1, l2, width=0.5)
        plt.ylabel('Gross income', size=20)
        plt.xlabel('Product Category', size=20)
        plt.title('Graph of Total Revenue Gross Income Wise ', size=25)
        plt.show()


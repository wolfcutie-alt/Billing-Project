from tkinter import *
from tkinter import messagebox
import random, os
# Functionality Part

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}','r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
        else:
            messagebox.showerror('Error', 'Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def savebill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        billnumber = random.randint(500, 1000)
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/ {billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'Bill number {billnumber} is saved successfully')
        
def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif cosmeticpriceEntry.get() and grocerypriceEntry.get() == '' and drinkspriceEntry.get() == '':
        messagebox.showerror('Error', 'No Product Are Selected')
    elif cosmeticpriceEntry.get() == '$0' and grocerypriceEntry.get() == '$0' and drinkspriceEntry.get() == '$0':
        messagebox.showerror('Error', 'No Products Are Selected')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END, '\n======================================================')
        textarea.insert(END, '\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n======================================================')
        if bathsoapEntry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t${soapprice}')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t${hairsprayrice}')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{facecreamEntry.get()}\t\t\t${facecreamprice}')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{facewashEntry.get()}\t\t\t${facewashprice}')
        if hairgelEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairgelEntry.get()}\t\t\t${hairgelprice}')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{bodylotionEntry.get()}\t\t\t${bodylotionprice}')
            
        if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t${riceprice}')
        if oilEntry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t${oilprice}')
        if daalEntry.get() != '0':
            textarea.insert(END, f'Daal\t\t\t{daalEntry.get()}\t\t\t${daalprice}')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'Wheat\t\t\t{wheatEntry.get()}\t\t\t${wheatprice}')
        if sugarEntry.get() != '0':
            textarea.insert(END, f'Sugar\t\t\t{sugarEntry.get()}\t\t\t${sugarprice}')
        if teaEntry.get() != '0':
            textarea.insert(END, f'Tea\t\t\t{teaEntry.get()}\t\t\t${teaprice}')
            
        if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t${maazaprice}')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t${pepsiprice}')
        if spriteEntry.get() !='0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t${spriteprice}')
        if dewprice.get() !='0':
            textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t${dewprice}')
        if frootiEntry.get() !='0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t${frootiprice}')
        if cocacolaEntry.get() !='0':
            textarea.insert(END, f'\nCocacola\t\t\t{cocacolaEntry.get()}\t\t\t${cocacolaprice}')
        
        textarea.insert(END, '\n------------------------------------------------------')
        
        if cosmetictaxEntry.get() != '$0.0':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get() != '$0.0':
            textarea.insert(END, f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if drinkstaxEntry.get() != '$0.0':
            textarea.insert(END, f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}')
        textarea.insert(END, f'\nTotal Price \t\t\t\t{totalbill}')
        textarea.insert(END, '\n------------------------------------------------------')
        savebill()
        
def total():
    global soapprice, facecreamprice, facewashprice, hairsprayrice, hairgelprice, bodylotionprice, riceprice, oilprice, daalprice, wheatprice, sugarprice, teaprice, maazaprice, pepsiprice, spriteprice, dewprice, frootiprice, cocacolaprice, totalbill
    # Cosmetics Price Calculation
    soapprice = int(bathsoapEntry.get()) * 20 
    facecreamprice = int(facecreamEntry.get()) * 50
    facewashprice = int(facewashEntry.get()) * 100
    hairsprayrice = int(hairsprayEntry.get()) * 150
    hairgelprice = int(hairgelEntry.get()) * 80
    bodylotionprice = int(bodylotionEntry.get()) * 60
    
    totalcosmeticsprice = soapprice + facecreamprice + facewashprice + hairgelprice + hairsprayrice + bodylotionprice
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, f'${totalcosmeticsprice}') 
    cosmetictax = totalcosmeticsprice * 0.12
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, f'${cosmetictax}')

    # Grocery Price Calculation
    riceprice = int(riceEntry.get()) * 30
    oilprice = int(oilEntry.get()) * 100
    daalprice = int(daalEntry.get()) * 120
    wheatprice = int(wheatEntry.get()) * 50
    sugarprice = int(sugarEntry.get()) * 140
    teaprice = int(teaEntry.get()) * 80
    
    totalgroceryprice = riceprice + oilprice + daalprice + wheatprice + sugarprice + teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f'${totalgroceryprice}')
    grocerytax = totalcosmeticsprice * 0.12
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f'${grocerytax}')
    
    # Cold Drink Price Calculation
    maazaprice = int(maazaEntry.get()) * 20
    pepsiprice = int(pepsiEntry.get()) * 20
    spriteprice = int(spriteEntry.get()) * 20
    dewprice = int(dewEntry.get()) * 20
    frootiprice = int(frootiEntry.get()) * 20
    cocacolaprice = int(cocacolaEntry.get()) * 20
    
    totaldrinkprice = maazaprice + pepsiprice + spriteprice + dewprice + frootiprice + cocacolaprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0, f'${totaldrinkprice}')
    drinkstax = totaldrinkprice * 0.12
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, f'${drinkstax}')
    
    totalbill = totalcosmeticsprice + totalgroceryprice + totaldrinkprice + cosmetictax + grocerytax + drinkstax
        
# GUI Part
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')

headinglabel = Label(root, text='Retail Billing System',font=('times new roman', 30, 'bold'), bg='gray20', fg='gold', bd=12, relief=GROOVE)
headinglabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text='Customer Details',font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
nameLabel.grid(row=0, column=0, padx=20, pady=2)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='Search', font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics',font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
cosmeticsFrame.grid(row=0, column=0)

bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

bathsoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathsoapEntry.insert(0, 0)

facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facecreamEntry.grid(row=1, column=1, pady=9, padx=10)
facecreamEntry.insert(0, 0)

facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facewashEntry.grid(row=2, column=1, pady=9, padx=10)
facewashEntry.insert(0, 0)

hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

hairsprayEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10)
hairsprayEntry.insert(0, 0)

hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

hairgelEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
hairgelEntry.insert(0, 0)

bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

bodylotionEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
bodylotionEntry.insert(0, 0)

groceryFrame = LabelFrame(productsFrame, text='Grocery',font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
riceLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

riceEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=1, column=1, pady=9, padx=10)
riceEntry.insert(0, 0)

oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
oilLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

oilEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=2, column=1, pady=9, padx=10)
oilEntry.insert(0, 0)

daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
daalLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

daalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
daalEntry.grid(row=3, column=1, pady=9, padx=10)
daalEntry.insert(0, 0)

wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
wheatLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

wheatEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=4, column=1, pady=9, padx=10)
wheatEntry.insert(0, 0)

sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
sugarLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

sugarEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=5, column=1, pady=9, padx=10)
sugarEntry.insert(0, 0)

teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
teaLabel.grid(row=6, column=0, pady=9, padx=10, sticky='w')

teaEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=6, column=1, pady=9, padx=10)
teaEntry.insert(0, 0)

drinksFrame = LabelFrame(productsFrame, text='Cold Drinks',font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
drinksFrame.grid(row=0, column=2)

maazaLabel = Label(drinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
maazaLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

maazaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
maazaEntry.grid(row=1, column=1, pady=9, padx=10)
maazaEntry.insert(0, 0)

pepsiLabel = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
pepsiLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

pepsiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=2, column=1, pady=9, padx=10)
pepsiEntry.insert(0, 0)

spriteLabel = Label(drinksFrame, text='Sprite', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
spriteLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

spriteEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=3, column=1, pady=9, padx=10)
spriteEntry.insert(0, 0)

dewLabel = Label(drinksFrame, text='Dew', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
dewLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

dewEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
dewEntry.grid(row=4, column=1, pady=9, padx=10)
dewEntry.insert(0, 0)

frootiLabel = Label(drinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
frootiLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

frootiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=5, column=1, pady=9, padx=10)
frootiEntry.insert(0, 0)

cocacolaLabel = Label(drinksFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
cocacolaLabel.grid(row=6, column=0, pady=9, padx=10, sticky='w')

cocacolaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cocacolaEntry.grid(row=6, column=1, pady=9, padx=10)
cocacolaEntry.insert(0, 0)

billFrame = Frame(productsFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=10)

billareaLabel = Label(billFrame, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack()

scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billFrame, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu',font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
billmenuFrame.pack()

cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic Price', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel = Label(billmenuFrame, text='Grocery Price', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinkspriceLabel = Label(billmenuFrame, text='Cold Drinks Price', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
drinkspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')

drinkspriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

cosmetictaxLabel = Label(billmenuFrame, text='Cosmetic Tax', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

cosmetictaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

grocerytaxLabel = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

grocerytaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinkstaxLabel = Label(billmenuFrame, text='Cold Drinks Tax', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
drinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')

drinkstaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, padx=5, pady=20)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, padx=5, pady=20)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10)
emailButton.grid(row=0, column=2, padx=5, pady=20)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10)
printButton.grid(row=0, column=3, padx=5, pady=20)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10)
clearButton.grid(row=0, column=4, padx=5, pady=20)

root.mainloop()
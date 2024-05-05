gross_price=int(input("Enter the gross price: "))
discount=gross_price*10//100
netprice=gross_price-discount
print(f'{gross_price:6}')
print(f'{discount:6}')
print(f'{netprice:6}')
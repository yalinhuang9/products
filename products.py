products = []
while True:
	name = input('請輸入商品名稱:（離開請按:Ｑ）')
	if name == 'Q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

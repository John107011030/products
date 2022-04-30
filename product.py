product = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price)
	#另解：p = [name, price]
	product.append(name)
	product.append(p)
print(product)
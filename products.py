
products = []
while True:
	name = input('请输入商品名称:')
	if name == 'q': # 离开
		break
	price = input('请输入商品价格:')
	p = []
	p.append(name) # 把商品名称装入小清单
	p.append(price) # 把商品价格装入下清单
	products.append(p) # 把小清单装入products清单

for product in products: # 用for loop印出products清单
	print(product[0], '的价格是', product[1])
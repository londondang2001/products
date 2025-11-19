
products = []
while True:
	name = input('请输入商品名称:')
	if name == 'q': # 离开
		break
	products.append(name)
print(products)

products = []                           # 二维清单架构, 清单里有个清单
while True:
	name = input('请输入商品名称:')      # 不能交替放name和price
	if name == 'q':                     
		break
	price = input('请输入商品价格:')     # 也不能分开放

	# np = []
	# np.append(name)                     
	# np.append(price)                    
	np = [name, price]                  # 把name和price都装入小清单
	products.append(np)                 # 把小清单装入大清单
	# products.append([name, price])

print(products)

print(products[0][0])               # 存取二维清单
                                    # 先走进大清单的第0格, 再走进小清单的第0格

for product in products:            # 印出商品和价格         
	print(product[0], '的价格是', product[1]) 
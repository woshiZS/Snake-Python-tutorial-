def make_sandwhich(*orders):
    print("\nYour sandwhich will add those items below:")
    for order in orders:
        print(order)

make_sandwhich('cheese')
make_sandwhich('bacon','hot dog','eggs')
make_sandwhich('salad','beef','pork')
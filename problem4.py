highestPalin = 0
for x in range(100,1000):
    for y in range(100,1000):
        product = x * y

        productStr = str(product)
        reversedNum = productStr[::-1]
        if(productStr == reversedNum and product > highestPalin ):
            highestPalin = product
        
print(highestPalin)
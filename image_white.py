import ddddocr

ocr = ddddocr.DdddOcr(beta=True, show_ad=False)

with open("./train_images/linxia/0加5=_1HofZOhygHTe6xqrjaWhhjXCJUAWVEx3.jpg", 'rb') as f:
    image = f.read()

res = ocr.classification(image)
print(res)
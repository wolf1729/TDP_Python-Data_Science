def calculate_area(length, width):
    if(length == width):
        return 'This is a square!'

    area = length*width
    return area

leng = int(input("enter the lenght : "))
bred = int(input("enter the bredth : "))

print(calculate_area(leng, bred))

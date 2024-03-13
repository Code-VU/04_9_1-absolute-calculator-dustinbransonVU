def ab_dif(in_num):
    in_num = int(in_num)  # Convert the input to an integer
    diff = abs(in_num - 21)
    if in_num > 21:
        return diff * 2
    else:
        return diff

in_num = input("Enter a number: ")
result = ab_dif(in_num)
print("Absolute difference:", result)
    
    
    
    
    

   

original_str=input('enter the original string:')
rotated_str=input('enter the rotated string:')
temp_str=rotated_str+rotated_str

if temp_str.find(original_str) == -1:
    print(rotated_str,'is not rotated string of',original_str)
else:

    print({rotated_str},'is not rotated string of',original_str)

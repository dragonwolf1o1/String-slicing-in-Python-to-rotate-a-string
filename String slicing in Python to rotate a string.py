def rotate_a_string(string,num):

    left_slicing_first=string[0:num]
    left_slicing_second = string[num:]
    print("Left_Slicing is:",left_slicing_second+left_slicing_first)

    right_slicing_first=string[0:len(string)-num]
    right_slicing_second = string[len(string) - num:]
    print("Right_Slicing:",right_slicing_second+right_slicing_first)

rotate_a_string(input("Enter the String: "),int(input("Enter the shifting number:")))
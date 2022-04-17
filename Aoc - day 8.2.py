with open('/Users/bzabert/Documents/Python/Adevent of code/Day 8/AoC- day 8 input.txt', 'r') as file: 
    #create a list of the .txt file
    lectures = list(file)

    def define_two_or_five(dic, value):
        count= 0
        if dic[4][0] in value:
            count += 1
        if dic[4][1] in value:
            count += 1
        if dic[4][2] in value:
            count += 1
        if dic[4][3] in value:
            count += 1
        return count
        

    # divide each line in the display and the lectures
    def count_numbers (list):
        # create variables for counting
        nro_four_digit=0
        sum_of_digit= 0
        # edting the .txt input in order to use it
        for input in lectures:
            each_lecture= input.split(' ')
            clean_input= []
            for digit in each_lecture:
                digit = digit.rstrip()
                digit = digit.strip('|')
                if digit != '':
                    clean_input.append(digit)
            #print(clean_input)
            
            # sorted values of the input
            clean_sort_input= []
            for value in clean_input:
                value_sorted = sorted(value)
                new_value= ''.join(value_sorted)
                clean_sort_input.append(new_value)
            #print(clean_sort_input)
            # Select the first 8 and sorted
            clean_sort_input_fisrt= sorted(clean_sort_input, key=len)
            #print(clean_sort_input_fisrt)

            # 
            code= {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
            for value in clean_sort_input_fisrt:
                if len(value) == 2:
                    code[1]= value
                if len(value) == 4:
                    code[4]= value
                if len(value) == 3:
                    code[7]= value
                if len(value) == 7:
                    code[8]= value
                if len(value) == 5:
                    if code[7][0] in value and code[7][1] in value and code[7][2] in value:
                        code[3]= value
                    elif  define_two_or_five(code,value) == 3:
                        code[5]= value
                    else:
                        code[2]= value
                if len(value) == 6:
                    if code[4][0] in value and code[4][1] in value and code[4][2] in value and code[4][3] in value:
                        code[9]= value
                    elif code[7][0] in value and code[7][1] in value and code[7][2] in value:
                        code[0]=value
                    else:
                        code[6]=value
                


            
            first_nro= [*code.keys()][[*code.values()].index(clean_sort_input[10])]
            second_nro= [*code.keys()][[*code.values()].index(clean_sort_input[11])]
            third_nro= [*code.keys()][[*code.values()].index(clean_sort_input[12])]
            four_nro= [*code.keys()][[*code.values()].index(clean_sort_input[13])]
            nro_four_digit= first_nro * 1000 + second_nro * 100 + third_nro *10 + four_nro
            sum_of_digit += nro_four_digit

            print(sum_of_digit)
        
                       
    count_numbers(lectures)

    
# matrix
matrix=[
    ["7","i","3"],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ","#"],
    ["s","M"," "],
    ["$","a"," "],
    ["#","t","%"],
    ["^","r","!"]
    ]

def decrypt_matrix(matrix):
    col_1=[]
    col_2=[]
    col_3=[]

    for item in matrix:
        if item[0].isalpha():
            col_1.append(item[0][0])
        if item[1].isalpha():
            col_2.append(item[1][0])
        if " " in item[1]:
            col_2.append("")
        if item[2].isalpha():
            col_3.append(item[2][0])
    str1=" ".join(col_1)   
    str2=" ".join(col_2)
    str3=" ".join(col_3)
    print(str1,"",str2,str3)
decrypt_matrix(matrix)                

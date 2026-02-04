
a= ["FIC10521HAR", "BIO20753OXF", "SCI30584PEN"] 

def codes(book_Codes):
    new_li = []
    for i in book_Codes:
        dic ={"book":i,"Category":i[:3],"Shelf_Number":i[3:5],"Book_Number":i[5:8],"Publisher_Code":i[8:]}
        new_li.append(dic)
         
         
    return new_li 

    
result = codes(a)

for book in result:
    print("The book is :",book['book'],end="")
    print(f"""          
Category        : {book['Category']}
Shelf Number    : {book['Shelf_Number']}
Book Number     : {book['Book_Number']}
Publisher Code  : {book['Publisher_Code']}
""")
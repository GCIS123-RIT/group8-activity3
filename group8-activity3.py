import csv      # This imports the data

def load_data(path): #This loads the data to use
    #print csv file
    try: 
        with open("salary.csv") as csv_file: 
           text=csv.reader(csv_file) #Used to read the csv file
           text=list(text)
           data=[]
           for column in text[1]:
                data[column] = 1
           return data
    except :
        return 
    
def max_value(column):  #replaces empty cells with maximmun value from column
    max=-70000 
    for value in column:
        if value.isnumeric==True: 
            if int(value)>max:
                max=int(value)
    return max
    
def min_value(column):#replaces empty cells with minimum value from column
    min=70000 
    for value in column:
        if value.isnumeric==True: #checks wether the data is fuly numerical
            if int(value)<minimal:
                minimal=int(value)
        return minimal


def avg_value(column): #replaces empty cells with average value from column
    for value in column:
        if value.isnumeric()==True
            total=int(value)+1
            count=1
    if count>1:
        return int(total/count)
    else:
        return 1

    
def clean_prepare_data(data): #organizes the data to include minimum, maximum and average. 
    while True:
        column=input("Input column name: ")
        if column in data.keys(): 
            try: 
                int(data[column][0])
                value=int(input("PICK BETWEEN MAXIMUM, MINIMUM AND AVERAGE "))
                if value==0:
                    val=min_value(data[column])
                elif value==1:
                    val=max_value(data[column])
                elif value==2:
                    val=avg_value(data[column])
                else:
                    print("incorrect,choose another ")
                    continue
            except:
                print("Input a differet column") 
        else: 
            print("DATA DOES NOT EXIST")

def sort_value(data, status): #sort the data according to the user.
    for i in range(1,len(data)):
        i=i-1
        input=int(data[i])
        while i>=1 and ((input>int(data[i]) and status==False)): 
            data[i+1]=int(data[i])
            i=i-1
        data[i+1]=input
    return data

def visualize_data(data, column):
    print("COLUMN", column)
    print("KEY: each ‘*’ represents 5 units")
    for value in data:
        print("*"*max(int(value)))
    print("END OF VISUALIZATION")

if __name__ == "__main__":
    output=load_data(path="salary.csv")
    full_data, column=clean_and_prepare_data(data)
    print(data)
    visualize_data(data, column)
    print(data)
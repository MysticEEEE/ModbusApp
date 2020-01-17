import pandas as pd
import os

def excelEdit(path):
    file_path = []
    filenames = os.listdir(path)
    for file in filenames:
        file_ext = os.path.splitext(file)
        if file_ext[1] == '.xlsx' or file_ext[1] == '.xls':
            file_path.append(path+'\\'+file)
            data = pd.read_excel(path+'\\'+file,0)
            # data1 = []
            newData = pd.DataFrame()
            for i in range(len(data)//5 +1):
                #print(i)
                data0 = data.loc[data['id']==(i*5) +1]
                newData = pd.concat([newData,data0])
            #     data1.append(data.loc[i*5])
            # newData = pd.DataFrame(data1)
            newData = newData.set_index('id')
            newData = newData.reset_index(drop=True)
            newData.to_excel(file_ext[0]+'new'+file_ext[1])
            print(newData.to_excel(file_ext[0]+'new'+file_ext[1]))
        #print(newData.iloc[-1])



if __name__ == "__main__":
    path = os.getcwd()
    excelEdit(path)
    # print(os.listdir(path)) 
# print(file_path)
# #def excelEdit(path)
# path = 'C:/Users/mythi/Desktop/node0102.xlsx'
# data = pd.read_excel(path,0)
# data1 = []
# for i in range(len(data)//5 +1):
#     #print(i)
#     data1.append(data.loc[i*5])
# newData = pd.DataFrame(data1)
# newData = newData.set_index('id')
# newData.to_excel('G:/node0102new.xlsx')
# print(newData.iloc[-1])
#print(path)





#用VBA代码
# for i=5 to 1000 step 10
# n=n+1
# sheet2.cells（n，1）=sheet1.cells（i，1）
# next
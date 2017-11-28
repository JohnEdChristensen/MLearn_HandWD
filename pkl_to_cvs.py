import pickle


with open('mnist.pkl', 'rb') as f:
    train_set,valid_set,test_set = pickle.load(f)
train_set_imgs, train_set_labels = train_set
valid_set_imgs, valid_set_labels = valid_set
test_set_imgs, test_set_labels = test_set
def image_csv_convert(data,path):
    output = ""
    outFile = open(path,"w") 
    for i in range(0, len(data)):
        for j in range(0,len(data[i])):
            output += str(data[i][j])
            if (j < (len(data[j]) -1)):
                output += ","
        output += "\n"
    outFile.write(output)
    outFile.close()
image_csv_convert(train_set_imgs,"train_set_imgs.txt")

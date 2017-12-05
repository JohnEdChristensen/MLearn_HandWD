import pickle


with open('Data/mnist.pkl', 'rb') as f:
    train_set,valid_set,test_set = pickle.load(f)
train_set_imgs, train_set_labels = train_set
valid_set_imgs, valid_set_labels = valid_set
test_set_imgs, test_set_labels = test_set
def image_txt_convert(data,path):
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
#image_txt_convert(train_set_imgs,"Data/train_set_imgs.txt")
#image_txt_convert(valid_set_imgs,"Data/valid_set_imgs.txt")
#image_txt_convert(test_set_imgs,"Data/test_set_imgs.txt")
def label_txt_convert(data,path):
    output = ""
    outFile = open(path,"w") 
    for i in range(0, len(data)):
        output += str(data[i])
        if (i < (len(data) -1)):
            output += ","
    outFile.write(output)
    outFile.close()
label_txt_convert(train_set_labels,"Data/train_set_labels.txt")
label_txt_convert(valid_set_labels,"Data/valid_set_labels.txt")
label_txt_convert(test_set_labels,"Data/test_set_labels.txt")

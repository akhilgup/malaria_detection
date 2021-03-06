import cv2
import os
import pandas
from sklearn.utils import shuffle


path = "cell_images/"
folder_list = os.listdir(path)
df = pandas.DataFrame(columns = ['filename', 'label'])

for i in range(len(folder_list)):

	if folder_list[i] != '.DS_Store':
		sub_fol_list = os.listdir(path+folder_list[i])
		# print(path + folder_list[i])
		
		for images in sub_fol_list:
			img_path = path + folder_list[i] + "/" + images
			img = cv2.imread(img_path,0)
			resize_img = cv2.resize(img, (64,64))

			if folder_list[i] == 'Parasitized':
				img_name = "P" + images
				df = df.append({'filename' : img_name, 'label' : 0}, ignore_index = True)
				cv2.imwrite("testdata/" + img_name,resize_img)
			if folder_list[i] == 'Uninfected':
				img_name = "U" + images
				df = df.append({'filename' : img_name, 'label' : 1}, ignore_index = True)
				cv2.imwrite("testdata/" + img_name,resize_img)


df = shuffle(df)
df.to_csv("malaria_dataset.csv")
print(df.head())



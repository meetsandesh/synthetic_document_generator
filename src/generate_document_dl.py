from faker import Faker
from PIL import Image, ImageDraw, ImageFont
import os
import sys

class DLData:
    dl_value: ""
    doi: ""
    dov: ""
    dob: ""
    blood_group: ""
    name: ""
    father_name: ""
    address: ""
    sign: ""
    file_number: ""


faker = Faker()
font_1 = ImageFont.truetype("arial.ttf", 35)
font_2 = ImageFont.truetype("arial.ttf", 20)
font_3 = ImageFont.truetype("arialbd.ttf", 25)
font_4 = ImageFont.truetype("arial.ttf", 23)
font_5 = ImageFont.truetype("arial.ttf", 30)
font_6 = ImageFont.truetype("arialbd.ttf", 25)
font_sign = ImageFont.truetype("segoesc.ttf", 25)
dl_data = 1620240000001
args = sys.argv
max_dl = int(args[1])
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s/%s ...%s\r' % (bar, str(count), str(total), suffix))
    sys.stdout.flush()


def createDatasetFolders():
    newpath = r'../generated_documents'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/images'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/images/dl_v1_p1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata/dl_v1_p1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def get_dl_value(temp):
    value = ""
    for i in range(15):
        a = temp % 10
        if i < 13:
            value = str(int(a)) + value
        else:
            value = alphabets[int(a)] + value
        temp /= 10
        if i == 10:
            value = "  " + value
    return value


def get_file_number(temp):
    value = ""
    for i in range(12):
        a = temp % 10
        if i < 2 or i > 10:
            value = alphabets[int(a)] + value
        else:
            value = str(int(a)) + value
        temp /= 10
    return value


def get_dl_metadata(temp):
    dl = DLData()
    dl.dl_value = get_dl_value(temp)
    date1 = faker.date().split("-")
    dl.doi = date1[2] + "/" + date1[1] + "/" + date1[0]
    date2 = faker.date().split("-")
    dl.dov = date2[2] + "/" + date2[1] + "/" + date2[0]
    date3 = faker.date().split("-")
    dl.dob = date3[2] + "/" + date3[1] + "/" + date3[0]
    dl.blood_group = faker.random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    dl.name = faker.name()
    dl.father_name = faker.name()
    dl.address = faker.address()
    dl.sign = faker.name()
    dl.file_number = get_file_number(temp)
    return dl


createDatasetFolders()
for i in range(max_dl):
    dl = get_dl_metadata(dl_data)
    # P1
    image = Image.open("../base_documents/DL_V1_P1.jpg")
    draw = ImageDraw.Draw(image)
    draw.text((200, 90), dl.dl_value, font=font_1, fill=(0, 0, 0))
    draw.text((238, 195), dl.doi, font=font_2, fill=(0, 0, 0))
    draw.text((435, 180), dl.dov, font=font_2, fill=(0, 0, 0))
    draw.text((238, 280), dl.dob, font=font_2, fill=(0, 0, 0))
    draw.text((435, 260), dl.blood_group, font=font_2, fill=(0, 0, 0))
    draw.text((70, 350), dl.name, font=font_3, fill=(0, 0, 0))
    draw.text((70, 430), dl.father_name, font=font_4, fill=(0, 0, 0))
    image.save("../generated_documents/images/dl_v1_p1/dl_v1_p1_" + str(i+1) + ".jpg")
    file1 = open("../generated_documents/metadata/dl_v1_p1/dl_v1_p1_" + str(i+1) + ".txt", "w")
    L = [dl.dl_value + "::" + dl.doi + "::" + dl.dov + "::" + dl.dob + "::" + dl.blood_group + "::" + dl.name + "::" + dl.father_name]
    file1.writelines(L)
    file1.close()
    progress(i + 1, max_dl, "Driving Licence Generated")
    dl_data += 1

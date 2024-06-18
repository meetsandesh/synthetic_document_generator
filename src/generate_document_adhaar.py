from faker import Faker
from PIL import Image, ImageDraw, ImageFont
import os
import sys


class AdhaarData:
    name_hi: ""
    name_en: ""
    dob: ""
    gender_hi: ""
    gender_en: ""
    adhaar_value: ""


faker = Faker()
faker_hi = Faker("hi_IN")
font = ImageFont.truetype("arial.ttf", 80)
font_2 = ImageFont.truetype("arial.ttf", 70)
font_val = ImageFont.truetype("arialbd.ttf", 150)
font_hi = ImageFont.truetype("C:/Users/meets/OneDrive/Desktop/MS Thesis Work/Code/Nirmala.ttf", 80)
font_hi_2 = ImageFont.truetype("C:/Users/meets/OneDrive/Desktop/MS Thesis Work/Code/Nirmala.ttf", 70)
adhaar_count = 1
args = sys.argv
max_adhaar = int(args[1])


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
    newpath = r'../generated_documents/images/adhaar_v1_p1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata/adhaar_v1_p1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def get_adhaar_value(temp):
    value = ""
    for i in range(12):
        a = temp % 10
        value = str(int(a)) + value
        temp /= 10
        if i == 3 or i == 7:
            value = " " + value
    return value


def get_adhaar_metadata(temp):
    adhaar = AdhaarData()
    adhaar.name_hi = faker_hi.name()
    adhaar.name_en = faker.name()
    if (temp <= max_adhaar * 0.4) or (max_adhaar * 0.8 < temp <= max_adhaar * 0.9):
        adhaar.gender_hi = "पुरुष"
        adhaar.gender_en = "Male"
    else:
        adhaar.gender_hi = "महिला"
        adhaar.gender_en = "Female"
    date = faker.date().split("-")
    adhaar.dob = date[2] + "/" + date[1] + "/" + date[0]
    adhaar.adhaar_value = get_adhaar_value(temp)
    return adhaar


createDatasetFolders()
for i in range(max_adhaar):
    adhaar = get_adhaar_metadata(adhaar_count)
    # P1
    image = Image.open("../base_documents/ADHAAR_V1_P1.jpg")
    draw = ImageDraw.Draw(image)
    draw.text((925, 440), adhaar.name_hi, font=font_hi, fill=(0, 0, 0))
    draw.text((925, 570), adhaar.name_en, font=font, fill=(0, 0, 0))
    draw.text((1640, 690), adhaar.dob, font=font, fill=(0, 0, 0))
    draw.text((925, 790), adhaar.gender_hi + " / " + adhaar.gender_en, font=font_hi, fill=(0, 0, 0))
    draw.text((900, 1350), adhaar.adhaar_value, font=font_val, fill=(0, 0, 0))
    image.save("../generated_documents/images/adhaar_v1_p1/adhaar_v1_p1_" + str(adhaar_count) + ".jpg")
    file1 = open("../generated_documents/metadata/adhaar_v1_p1/adhaar_v1_p1_" + str(adhaar_count) + ".txt", "w")
    L = [adhaar.name_en + "::" + adhaar.dob + "::" + adhaar.gender_en + "::" + adhaar.adhaar_value]
    file1.writelines(L)
    file1.close()
    progress(i + 1, max_adhaar, "Adhaar Card Generated")
    adhaar_count += 1

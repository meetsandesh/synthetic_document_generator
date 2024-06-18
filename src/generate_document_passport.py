from faker import Faker
from PIL import Image, ImageDraw, ImageFont
import os
import sys

class PassportData:
    passport_value: ""
    surname: ""
    name: ""
    gender: ""
    dob: ""
    pob: ""
    poi: ""
    doi: ""
    doe: ""
    father_name: ""
    mother_name: ""
    spouse_name: ""
    address: ""
    file_number: ""
    old_passport_value: ""
    old_passport_doi: ""
    old_passport_poi: ""


faker = Faker()
font_1 = ImageFont.truetype("arialbd.ttf", 80)
font_2 = ImageFont.truetype("arialbd.ttf", 60)
font_3 = ImageFont.truetype("arialbd.ttf", 70)
font_4 = ImageFont.truetype("arial.ttf", 80)
font_5 = ImageFont.truetype("arial.ttf", 30)
font_6 = ImageFont.truetype("arialbd.ttf", 25)
font_sign = ImageFont.truetype("segoesc.ttf", 80)
passport_data = 1
args = sys.argv
max_passport = int(args[1])
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
    newpath = r'../generated_documents/images/passport_v1_p1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata/passport_v1_p1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def get_passport_value(temp):
    value = ""
    for i in range(8):
        a = temp % 10
        if i < 7:
            value = str(int(a)) + value
        else:
            value = alphabets[int(a)] + value
        temp /= 10
    return value


def get_file_number(temp):
    value = ""
    for i in range(15):
        a = temp % 10
        if i > 12:
            value = alphabets[int(a)] + value
        else:
            value = str(int(a)) + value
        temp /= 10
    return value


def get_passport_metadata(temp):
    passport = PassportData()
    passport.passport_value = get_passport_value(temp)
    passport.surname = faker.name().split(" ")[-1].upper()
    passport.name = faker.name().split(" ")[0]
    passport.gender = faker.random.choice(['M', 'F'])
    date3 = faker.date().split("-")
    passport.dob = date3[2] + "/" + date3[1] + "/" + date3[0]
    passport.pob = faker.random.choice(
        ["Tokyo", "Jakarta", "Delhi", "Guangzhou", "Mumbai", "Manila", "Shanghai", "São Paulo", "Seoul", "Mexico City",
         "Cairo", "New York", "Dhaka", "Beijing", "Kolkata", "Bangkok", "Shenzhen", "Moscow", "Buenos Aires", "Lagos",
         "Bangalore"]).upper()
    passport.poi = faker.random.choice(
        ["Tokyo", "Jakarta", "Delhi", "Guangzhou", "Mumbai", "Manila", "Shanghai", "São Paulo", "Seoul", "Mexico City",
         "Cairo", "New York", "Dhaka", "Beijing", "Kolkata", "Bangkok", "Shenzhen", "Moscow", "Buenos Aires", "Lagos",
         "Bangalore"]).upper()
    date1 = faker.date().split("-")
    passport.doi = date1[2] + "/" + date1[1] + "/" + date1[0]
    date2 = faker.date().split("-")
    passport.doe = date2[2] + "/" + date2[1] + "/" + date2[0]
    passport.father_name = faker.name().upper()
    passport.mother_name = faker.name().upper()
    passport.spouse_name = faker.name().upper()
    passport.address = faker.address().upper()
    passport.file_number = get_file_number(temp)
    passport.old_passport_value = get_passport_value(temp - 1)
    date4 = faker.date().split("-")
    passport.old_passport_doi = date4[2] + "/" + date4[1] + "/" + date4[0]
    passport.old_passport_poi = faker.random.choice(
        ["Tokyo", "Jakarta", "Delhi", "Guangzhou", "Mumbai", "Manila", "Shanghai", "São Paulo", "Seoul", "Mexico City",
         "Cairo", "New York", "Dhaka", "Beijing", "Kolkata", "Bangkok", "Shenzhen", "Moscow", "Buenos Aires", "Lagos",
         "Bangalore"]).upper()
    return passport


createDatasetFolders()
for i in range(max_passport):
    passport = get_passport_metadata(passport_data)
    # P1
    image = Image.open("../base_documents/PASSPORT_V1_P1.jpg")
    draw = ImageDraw.Draw(image)
    draw.text((2200, 230), passport.passport_value, font=font_1, fill=(0, 0, 0))
    draw.text((1000, 370), passport.surname, font=font_2, fill=(0, 0, 0))
    draw.text((1000, 540), passport.name.upper(), font=font_2, fill=(0, 0, 0))
    draw.text((1000, 710), passport.dob, font=font_2, fill=(0, 0, 0))
    draw.text((1750, 710), passport.gender, font=font_2, fill=(0, 0, 0))
    draw.text((1000, 880), passport.pob, font=font_2, fill=(0, 0, 0))
    draw.text((1000, 1050), passport.poi, font=font_2, fill=(0, 0, 0))
    draw.text((1000, 1220), passport.doi, font=font_2, fill=(0, 0, 0))
    draw.text((2100, 1220), passport.doe, font=font_2, fill=(0, 0, 0))
    draw.text((300, 1100), passport.name, font=font_sign, fill=(0, 0, 0))
    draw.text((200, 1600), "P<IND<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", font=font_4, fill=(0, 0, 0))
    draw.text((200, 1700), passport.passport_value + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", font=font_4, fill=(0, 0, 0))
    image.save("../generated_documents/images/passport_v1_p1/passport_v1_p1_" + str(i+1) + ".jpg")
    file1 = open("../generated_documents/metadata/passport_v1_p1/passport_v1_p1_" + str(i+1) + ".txt", "w")
    L = [passport.passport_value + "::" + passport.surname + "::" + passport.name + "::" + passport.dob + "::" + passport.gender + "::" + passport.pob + "::" + passport.poi + "::" + passport.doi + "::" + passport.doe]
    file1.writelines(L)
    file1.close()
    progress(i + 1, max_passport, "Passport Generated")
    passport_data += 1

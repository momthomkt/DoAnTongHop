import os
import xlsxwriter
from xlsxwriter import Workbook
path = os.path.abspath(os.getcwd())
inputdir = "result_correction"
fix_inputdir = "fix_input"
Fix = {'7': 'T', 'Ủ': 'Ŭ', 'Ũ': 'Ŭ','Ø':'B','#':'H','?':'D'}
InHoaViet = ["A", "À", "Á", "Ă", "Ắ", "Ằ", "Â", "Ấ", "Ầ", "B", "C", "D", "Đ", "E", "É", "È", "Ê","Ế","Ề","G", "H","I","Í","Ì",\
              "K","L", "M", "N", "O", "Ó","Ò","Ô","Ố","Ồ", "Ơ","Ớ","Ờ","P", "Q", "R", "S", "T", "U", "Ư", "V", "X", "Y"]
InHoaBana = ["A", "Ă","Â","B","\'B","C","D","\'D","Đ","E","Ê","G","H","I","J","\'J","K","L","\'L","M","\'M","N","\'N","O","Ô","Ơ",\
             "P","R","S","T","U","Ư","X","Y"]


def get_size(filename):
    size = 0
    file = open(filename, encoding='utf-8')
    for line in file:
        size += 1
    return size


def FIX_ERROR_TXT(filename):
    size = get_size(inputdir+"/"+filename)
    file = open(inputdir+"/"+filename, encoding='utf-8')
    line = next(file)
    f = open(fix_inputdir+"/"+filename, 'w', encoding='utf-8')
    cnt = 1
    while cnt <= size:
        s = ""
        for i in range(len(line)):
            if line[i] in Fix:
                s += Fix[line[i]]
            else:
                s += line[i]
        f.write(s)
        if (cnt < size):
            cnt += 1
            line = next(file)
        else:
            break


def READ_TXT_WRITE_TO_XLSX(row,row1, worksheet,worksheet1, name):
    size = get_size(inputdir+"/"+name)
    if size == 0:
        return row,row1
    FIX_ERROR_TXT(name)
    cnt = 1
    size = get_size(fix_inputdir + "/" + name)
    file = open(fix_inputdir+"/" + name, encoding='utf-8')
    line = next(file)
    while cnt <= size:
        if len(line) == 0 or line[0] not in InHoaViet:
            if (cnt < size):
                cnt += 1
                line = next(file)
            else:
                break
            continue
        col1 = []
        col2 = []
        s1 = ""
        s2 = ""
        CHECK_BANA = False
        OK_END_LINE = False
        while (OK_END_LINE == False):
            for i in range(len(line)):
                if line[i] == ".":
                    col2.append(s2)
                    OK_END_LINE = True
                    break
                elif CHECK_BANA == False:
                    if (line[i] == ","):
                        col1.append(s1)
                        s1 = ""
                    elif line[i] in InHoaBana and s1 != "":
                        col1.append(s1)
                        s2 += line[i]
                        CHECK_BANA = True
                    else:
                        s1 += line[i]
                else:
                    if (line[i] == ","):
                        col2.append(s2)
                        s2 = ""
                    else:
                        s2 += line[i]
            if (cnt < size and OK_END_LINE == False):
                cnt += 1
                line = next(file)
            else:
                break
        for i in range(len(col1)):
            for j in range(len(col2)):
                worksheet.write(row, 0, col1[i])
                worksheet.write(row, 1, col2[j])
                if i == 0:
                    worksheet1.write(row1,0,col2[j])
                    row1 += 1
                row += 1

        if (cnt < size):
            cnt += 1
            line = next(file)
        else:
            break
    return row, row1


def WRITE_TO_XLSX():
    workbook = xlsxwriter.Workbook('Output_correct.xlsx')
    worksheet = workbook.add_worksheet("VIET - BANA")
    worksheet1 = workbook.add_worksheet("BANA")
    row = 0
    row1 = 0
    for name in os.listdir(path + "/"+ inputdir):
        if name[-1] == 't' and name[-2] == 'x' and name[-3] == 't':
            row,row1 = READ_TXT_WRITE_TO_XLSX(row,row1, worksheet,worksheet1, name)
    workbook.close()

WRITE_TO_XLSX()
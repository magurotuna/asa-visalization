# -*- coding: utf-8 -*-
input = 'location.csv'
output = 'output.csv'
file_i = open(input, 'r')
file_o = open(output, 'w')
firsttext = '店名,台数,都道府県,市区郡,区町\n'
file_o.write(firsttext)

linecount = 0
for line in file_i:
    linecount += 1
    if linecount % 2 == 1:
        file_o.write(line[:-1] + ',')
        if line[0] == '♪':
            file_o.write('9,')
        elif line[0] == '♫':
            file_o.write('6,')
        else:
            file_o.write('3,')
    elif linecount % 2 == 0:
        kencount = 0
        citycount = 0
        kucount = 0
        metroflag = 0
        gunflag = 0
        out23ku = 1
        for i in range(len(line)):
            if line[i] == '県' or line[i] == '道' or line[i] == '府':
                kencount = i
                continue
            elif line[i] == '都':
                kencount = i
                metroflag = 1
                continue
            elif line[i] == '市' or line[i] == '郡':
                citycount = i
                if metroflag == 1:
                    out23ku = 0
                if line[i] == '郡':
                    gunflag = 1
                continue
            elif line[i] == '区':
                kucount = i
                continue
            elif line[i] == '町' and gunflag == 1:
                kucount = i
                continue

        ken = 'null'
        city = 'null'
        ku = 'null'
        ken = line[0:kencount+1]  # 都道府県名
        if metroflag == 0:  # 道府県
            city = line[kencount+1:citycount+1]  # 市か郡の名前
            if kucount != 0:  # 政令指定都市
                ku = line[citycount+1:kucount+1]
            if gunflag == 1:  # 郡の場合
                ku = line[citycount+1:kucount+1]
        elif metroflag == 1 and out23ku == 1:  # 23区のとき
            city = line[kencount+1:kucount+1]
        elif metroflag == 1 and out23ku == 0:  # 東京都下
            city = line[kencount+1:citycount+1]

        file_o.write(ken + ',' + city + ',' + ku + '\n')

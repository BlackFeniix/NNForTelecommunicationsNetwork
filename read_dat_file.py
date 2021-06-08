# -*- coding: utf-8 -*-
"""
Created on Jan 20 13:45:20 2021

@author: Nikolay
"""

# Списки для одной записи и для записи в файл
baselist = []
listoflists = []

# Паттерны поиска в лог файлах
substrings = ["ca_system_id:","source_id:", "source_id=", "ecm_pid:"]
#substrings = ["url(qam://sourceid=","locator=qam://sourceid=" , "source_id:", "ca_system_id:"]

# Открытие файла и считывание его в переменную datContent
datContent = [i.strip().split() for i in open("log_chunk_2020_11_11_20_02_28_2020_11_11_20_04_38_log.dat").readlines()]

# Добавление имен столбцов
listoflists.append(["DATETIME", "DEVICE_ID", "CHANNEL_ID", "DEVICE_STATE"])

# Поиск и проверка всех записей на наличие паттернов
for i in datContent:
    for j in i:
        for substring in substrings:
            if (substring == j):
                """
                Берем дату и время, ID? устройства и присваиваем код паттерна
                """
                baselist.append([i[1],i[2]])
                baselist.append(i[2])
                baselist.append(i[3])
                if (substring == substrings[0]):
                    baselist.append("0")
                if (substring == substrings[1]):
                    baselist.append("1")
                if (substring == substrings[2]):
                    baselist.append("2")
                if (substring == substrings[3]):
                    baselist.append("3")
                listoflists.append(baselist)
                #listoflists.append(i)
                baselist=[]
                
import csv

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(listoflists)
    
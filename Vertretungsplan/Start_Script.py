import Vertretungsplan
import time

path = "C:/Users/Frede/OneDrive/Dokumente/Vertretungspläne/Server/Vertretungenspeicher/"

posClasses = ["5a", "5b", "5c", "5d", "5e", "6a", "6b", "6c", "6d", "6e", "7a", "7b", 
             "7c", "7d", "7e" ,"8a", "8b", "8c", "8d", "8e", "9a", "9b", "9c", "9d", "9e", "EF", "Q1", "Q2"]

#while True:
#    if Vertretungsplan.reloadtime(3):

Date, Weekday, Year = Vertretungsplan.getDate()
#Schoolclass, Date = Vertretungsplan.readInfofile(path)

pages = Vertretungsplan.Download()

Vertretungsplan.HtmltoCsv(pages, Year)

if Vertretungsplan.checkday(16):
    Date = Vertretungsplan.addDay(Date)
    print(Date)

#Vertretungsplan.searchVertretungen(Schoolclass, Date)
Vertretungsplan.sortAllClass(posClasses, Date, path)

#Vertretungsplan.writeInHtml(path, Date, Weekday)
Vertretungsplan.writeAll(Date, Weekday, posClasses, path)
print("Updated")

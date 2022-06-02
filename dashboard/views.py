from sre_constants import SUCCESS
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dashboard.models import AddBook
from dashboard.templatetags.index import index
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
# from . import User
# Create your views here.
def countbook(author,title):
    count = len(AddBook.objects.all().filter(Title=title,Author=author))
    return count
def dashboard(request):
    if request.user.is_authenticated:
        usercount=len(User.objects.all())
        
        books=AddBook.objects.all().order_by('Date')
        newbookscount=len(books)
        books=books[0:10]
        recentbook=[]
        for book in books:
            lstofcount=[]
            lstofcount.append(countbook(book.Author,book.Title))
            lstofcount.append(book)    
            recentbook.append(lstofcount)
        print(recentbook)   
        lstofpop=[]
        for i in range(len(recentbook)):
            for j in range(len(recentbook)):
                if i!=j:
                    if j not in lstofpop:
                        if recentbook[i][1].Author==recentbook[j][1].Author and recentbook[i][1].Title==recentbook[j][1].Title:
                            lstofpop.append(i)
        newlst=[]
        for i in range(len(recentbook)):
            if i not in lstofpop:
                newlst.append(recentbook[i])
        print(newlst)
        return render(request,"dashboard.html",{"books":newlst,"usercount":usercount,"newbookscount":newbookscount})
    else:
        return redirect("/")

def addbook(request):
    books = AddBook.objects.all().latest("Date")
    print(books)
    return render(request,"forms-layouts.html")

def showbook(request):
    books= AddBook.objects.all()
    return render(request, "tables-data.html" ,{"books":books})

def addbooksub(request):
    if request.method == "POST":
        try:
            boolean=request.POST["aslikeprev"]
        except MultiValueDictKeyError:
            boolean="off"
        print(boolean)
        if boolean=="on":
            books=AddBook.objects.all().latest('Date')
            if len(request.POST["remark"])==0:
                remark=books.Remark
            else:
                remark=request.POST["remark"]
            if len(request.POST["withdrawndate"])==0:
                withdrawndate=books.Withdrawn_Date
            else:
                withdrawndate=request.POST["withdrawndate"]
            if len(request.POST["billdate"])==0:
                billdate=books.Bill_Date
            else:
                billdate=request.POST["billdate"]
            if len(request.POST["billnumber"])==0:
                billnumber=books.Bill_Number
            else:
                billnumber=request.POST["billnumber"]
            if len(request.POST["classnumber"])==0:
                classnumber=books.class_No
            else:
                classnumber=request.POST["classnumber"]
            booknumber=request.POST["booknumber"]
            if len(request.POST["pages"])==0:
                pages=books.Pages
            else:
                request.POST["pages"]
            if len(request.POST["publisher"])==0:
                publisher=books.Publisher
            else:
                publisher=request.POST["publisher"]
            if len(request.POST["place"])==0:
                place=books.Place
            else:
                place=request.POST["place"]
            if len(request.POST["source"])==0:
                source=books.Source
            else:
                source=request.POST["source"]
            if len(request.POST["yearofpublication"])==0:
                yearofpublication=books.Year_Of_Publication
            else:
                yearofpublication=request.POST["yearofpublication"]
            if len(request.POST["volume"])==0:
                volume=books.Volume
            else:
                volume=request.POST["volume"]
            if len(request.POST["title"])==0:
                title=books.Title
            else:
                title=request.POST["title"]
            if len(request.POST["author"])==0:
                author=books.Author
            else:
                author=request.POST["author"]
            if len(request.POST["date"])==0:
                date=books.Date
            else:
                date=request.POST["date"]
            if len(request.POST["category"])==0:
                category=books.Category
            else:
                category=request.POST["category"]
            print(category)
            book=AddBook(Date = date,Author = author,Title = title,Volume = volume,Place = place,Publisher = publisher,Year_Of_Publication = yearofpublication,Source = source,Pages = pages,Book_Number = booknumber,Bill_Number = billnumber,Bill_Date = billdate,Withdrawn_Date = withdrawndate,Remark = remark,class_No=classnumber,Category=category)
            book.save()
            return HttpResponse("SUCCESS")
        else:
            remark=request.POST["remark"]
            withdrawndate=request.POST["withdrawndate"]
            billdate=request.POST["billdate"]
            billnumber=request.POST["billnumber"]
            classnumber=request.POST["classnumber"]
            booknumber=request.POST["booknumber"]
            pages=request.POST["pages"]
            publisher=request.POST["publisher"]
            place=request.POST["place"]
            source=request.POST["source"]
            yearofpublication=request.POST["yearofpublication"]
            volume=request.POST["volume"]
            title=request.POST["title"]
            author=request.POST["author"]
            date=request.POST["date"]
            print(date,author,title,volume,yearofpublication,source,publisher,pages,booknumber,classnumber,billnumber,billdate,withdrawndate,remark)
            book=AddBook(Date = date,Author = author,Title = title,Volume = volume,Place = place,Publisher = publisher,Year_Of_Publication = yearofpublication,Source = source,Pages = pages,Book_Number = booknumber,Bill_Number = billnumber,Bill_Date = billdate,Withdrawn_Date = withdrawndate,Remark = remark,class_No=classnumber)
            book.save()
    return HttpResponse("SUCCESS")

def reports(request):
    books=AddBook.objects.all().order_by('Date')
    books=books[0:10]
    recentbook=[]
    for book in books:
        lstofcount=[]
        lstofcount.append(countbook(book.Author,book.Title))
        lstofcount.append(book)    
        recentbook.append(lstofcount)
    # print(recentbook)   
    lstofpop=[]
    for i in range(len(recentbook)):
        for j in range(len(recentbook)):
            if i!=j:
                if j not in lstofpop:
                    if recentbook[i][1].Author==recentbook[j][1].Author and recentbook[i][1].Title==recentbook[j][1].Title:
                        lstofpop.append(i)
    newlst=[]
    for i in range(len(recentbook)):
        if i not in lstofpop:
            newlst.append(recentbook[i])
    # print(newlst)
    return render(request,"report.html",{"books":newlst})
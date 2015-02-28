from django.shortcuts import render
from bible.models import Reading #use bible reading database to print bible

# Create your views here.
def disick(request):
    bible = ""
    
    #Get all reading days to print whole bible
    for x in range(0, 365):
        reading = Reading.objects.filter(day=x)[0]
        bible = bible + str(reading)
    
    #Replace God and Lord with Lord Disick
    lord = bible.replace("Lord", """<a href="http://assets-s3.usmagazine.com/uploads/assets/articles/54272-scott-disick-becomes-british-royalty-gets-knighted-in-london/1342447713_scott-disick-article.jpg">Lord Disick</a>""")
    LORD = bible.replace("LORD", """<a href="http://assets-s3.usmagazine.com/uploads/assets/articles/54272-scott-disick-becomes-british-royalty-gets-knighted-in-london/1342447713_scott-disick-article.jpg">Lord Disick</a>""")
    god = LORD.replace("God", """<a href="http://assets-s3.usmagazine.com/uploads/assets/articles/54272-scott-disick-becomes-british-royalty-gets-knighted-in-london/1342447713_scott-disick-article.jpg">Lord Disick</a>""")
    
    return render(request, "disick.html", {'bible': god})
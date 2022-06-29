from django.shortcuts import render
from django.http import HttpResponse
from . helpers import *
from . models import *


# Create your views here.
def home(request):
    pass 
    return HttpResponse("wellcome")
def pdf_req(request):
    context={"name":"shashank"}
    #pdf=pdf_html_to_dawnload("pdf.html","shashank",context)
    #pdf=pdf_html_to_render("pdf.html",context)
    dbpdf=pdf_html_to_db("pdf.html","genuine",context)
    myfile=Storage(name="shashank pathe",pdf_file=dbpdf)
    myfile.save()
    return HttpResponse("thanks for using this")
    # response['Content-Disposition'] = 'attachment;filename="INV - {0}.pdf"'.format(invoice_no)
    # inv_save.invoicefile= SimpleUploadedFile('INV-'+ str(inv_save.id) +'.pdf', pdf, content_type='application/pdf')
    # msg.attach('INV.pdf',pdf,"application/pdf")
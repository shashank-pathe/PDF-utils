from weasyprint import HTML
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.files.uploadedfile import SimpleUploadedFile

#........................................pdf utility ................................#
def convert_to_pdf(template_name,context):
    template = get_template(template_name)
    html = template.render(context)   
    htmldoc = HTML(string=html, base_url="")
    pdf=htmldoc.write_pdf()
    return pdf
def pdf_html_to_db(template_name,filename,context):
    pdf=convert_to_pdf(template_name,context)
    pdfile=SimpleUploadedFile('INV-'+ filename +'.pdf', pdf, content_type='application/pdf')
    return pdfile    

def pdf_html_to_render(template_name,context):
    pdf=convert_to_pdf(template_name,context)
    response = HttpResponse(pdf, content_type='application/pdf')
    return response 

def pdf_html_to_dawnload(template_name,filename,context):
    pdf=convert_to_pdf(template_name,context)
    response = HttpResponse(pdf, content_type='application/pdf')
    pdfname='INV-'+ str(filename) +'.pdf'
    response['Content-Disposition'] = f"attachment;filename={filename}.pdf"
    return response    
def pdf_html_to_mail(template_name,filename,context):
    pdf=convert_to_pdf(template_name,context)
    attachment=msg.attach('INV.pdf',pdf,"application/pdf") 
    return attachment

#........................................end of pdf ............................#


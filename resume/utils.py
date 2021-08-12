# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template

# from xhtml2pdf import pisa

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template("index.html")
#     html  = template.render({})
#     result = BytesIO()
#     # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     # print(pdf)
#     # if not pdf.err:
#     #     return HttpResponse(result.getvalue(), content_type='application/pdf')
#     # return None
#     result_file = open("test.pdf", "w+b")
#     html = """
#     """
#     # convert HTML to PDF
#     pisa_status = pisa.CreatePDF(
#             html,                # the HTML to convert
#             dest=result_file)           # file handle to recieve result

#     # close output file
#     result_file.close()      
# -*- coding: utf-8 -*-
# from .models import Objectives
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
# from .models import Email, Personal_Details

# def generate_pdf(request,context):
#     """Generate pdf."""
#     # Model data
#     # people = Objectives.objects.all()

#     # Rendered
#     # current_user = request.user
#     # id=current_user.id
#     # Personal_ob=Personal_Details.objects.filter(user=id)
#     html_string = render_to_string('index.html',context=context)
#     print('html_string',html_string)
#     html = HTML(string=html_string)
#     result = html.write_pdf()

#     # Creating http response
#     # response = HttpResponse(content_type='application/pdf;')
#     # response['Content-Disposition'] = 'inline; filename=list_people.pdf'
#     # response['Content-Transfer-Encodig'] = 'binary'
#     with open('test.pdf', 'wb') as output:
#         output.write(result)
#         output.flush()
#         # output = open(output.name, 'rb')
#         # response.write(output.read())
        
        # print("Grgr")

    # return response
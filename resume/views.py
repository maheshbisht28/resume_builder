# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic, View
# Create your views here.

# from .forms import urresume_form
# # from .models import urresume

from .forms import Registrationform , Language_form,testform, Email_form, Personal_Details_form ,Other_link_form ,Objectives_form , Education_form , Experience_form , Projects_form, Skills_form , Certification_form,Address_form ,Interest_form

from .models import User_Email, Language, Personal_Details,Other_link , Objectives ,Language, Education , Experience , Projects, Skills , Certification,Address ,Interest

from django.http import HttpResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect , Http404, FileResponse

from django.urls import reverse

from user.models import User
from django.forms import modelformset_factory, formset_factory
from django.http import HttpResponse
from django.template import loader
# import pdfkit
# import io
from django.shortcuts import render
from io import BytesIO
# from .utils import generate_pdf
from django.template.loader import get_template
# from django.views import V
from xhtml2pdf import pisa


# def render_to_pdf(template_src, context_dict={}):
# 	template = get_template(template_src)
# 	html  = template.render(context_dict)
# 	result = BytesIO()
# 	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
# 	if not pdf.err:
# 		return HttpResponse(result.getvalue(), content_type='application/pdf')
# 	return None

from fpdf import FPDF
def make_pdf(request,context_dict):
	# return render(request,'template_1.html')
	current_user = request.user
	id=current_user.id	
	# Address_ob=(Address.objects.all().values('flat_no','city',
	# 		'state','pincode','country'))[0]
	Address_ob=context_dict['Address_ob'][0]
	Personal_ob=context_dict['Personal_Details_ob'][0]
	Email_ob=context_dict['Email_ob'][0]
	Other_link_ob=context_dict['Other_link_ob']
	Objectives_ob=context_dict['Objectives_ob'][0]
	Skill_name_ob=context_dict['skill_ob']
	Experience_ob=context_dict['Experience_ob']
		
	Education_ob=context_dict['Education_ob']
	Certification_ob=context_dict['Certification_ob']

	Projects_ob=context_dict['Projects_ob']	

	Interest_ob=context_dict['Interest_ob']   
	Language_ob=context_dict['Language_ob']



	print("Address_ob ",Address_ob)
	pdf = FPDF(orientation='P', unit='mm',
            format=(216,290))
	pdf.add_page()
	pdf.set_text_color(151, 47, 45)
	pdf.set_font('times', size=24,style='B')
	pdf.cell(200,10,txt="Mahesh Bisht",ln=1,align="l")
	pdf.ln(1)
	# pdf.set_draw_color(255, 0, 0)
	pdf.set_line_width(2)
	pdf.line(0, 30, 250, 30)
	pdf.ln(20)
	pdf.set_text_color(0,0,0)
	pdf.set_font('times', size=12)
	pdf.cell(100,5,txt=Address_ob['flat_no']+", "+Address_ob['city']+", "+Address_ob['state']+" "+str(Address_ob['pincode'])+", "+Address_ob['country'],ln=5,align="l")
	# Personal_ob=(Personal_Details.objects.all().values('first_name','middle_name','last_name','dob','contact'))[0]	
	pdf.set_font('times', size=12,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(15,5,txt="Mobile:",align="l")
	pdf.set_font('times', size=12)
	pdf.set_text_color(0,0,0)
	pdf.cell(15,5,txt=str(Personal_ob['contact']),align="l")

	pdf.ln(5)
	pdf.set_font('times', size=12,style='B')

	# Email_ob=(Email.objects.all().values('email_name'))[0]
	
	pdf.set_text_color(151, 47, 45)
	pdf.cell(13,5,txt="Email:",align="l")
	pdf.set_font('times', size=12)
	pdf.set_text_color(0,0,0)
	pdf.cell(15,5,txt=str(Email_ob['email_name']),align="l")

	pdf.ln(5)
	pdf.set_font('times', size=12,style='B')
	# Other_link_ob=Other_link.objects.filter(user=id).values('name','link')
	for ob in Other_link_ob:
		if ob['name'] == 'Linkedin':
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset-5
			pdf.set_font('times', size=12,style='B')
			pdf.set_text_color(151, 47, 45)
			pdf.cell(14,5,txt="Linkedin:",align="l")
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset
			pdf.set_font('times', size=12)
			pdf.set_text_color(0,0,0)
			pdf.cell(15,5,txt=str(ob['link']),align="l")
			
		elif ob['name'] == 'Github':
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset-5
			pdf.set_font('times', size=12,style='B')
			pdf.set_text_color(151, 47, 45)
			pdf.cell(10,5,txt="Github: ",align="l")
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset
			pdf.set_font('times', size=12)
			pdf.set_text_color(0,0,0)
			pdf.cell(15,5,txt=str(ob['link']),align="l")			
		pdf.ln(5)		


	pdf.ln(6)

	# Objectives_ob=(Objectives.objects.filter(user=id).values('objective_text'))[0]
	top = pdf.y
	offset = pdf.x + 30
	# print('top ',top)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Objective",align="l",ln = 0)
	pdf.y = top
	pdf.x = offset+5 
	# print('pdf.y ',pdf.y)
	# print('pdf.x ',pdf.x)
	pdf.set_font('times', size=12)
	pdf.set_text_color(0,0,0)
	pdf.multi_cell(160,5,txt=Objectives_ob['objective_text'],align="l")



	# skill_ob=list(Skills.objects.filter(user=id).values('name'))
	pdf.ln(6)
	top = pdf.y
	offset = pdf.x + 30	
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Skills",align="l",ln = 0)
	# sk=skill_ob[0]['name']
	# for i in range(len(skill_ob)):
	# 	sk+=", "+skill_ob[i]['name']
	# pdf.y = top
	# pdf.x = offset+5 		
	# pdf.set_font('times', size=12)
	# pdf.set_text_color(0,0,0)
	# pdf.multi_cell(160,5,txt=sk,align="l",ln = 1)
	lk=[]
	for i in range(len(Skill_name_ob)):
		lk.append(Skill_name_ob[i]['name'])
		print("skill_ob[i]['name'] ",Skill_name_ob[i]['name'])
	print("sk ",lk)
	top = pdf.y
	offset = pdf.x - 15	
	pdf.y = top
	pdf.x = offset 		
	pdf.set_text_color(0,0,0)
	pdf.set_font('times', size=12)
	pdf.multi_cell(160,5,txt=", ".join(lk),align="l",border=0,ln = 1)





	# Experience_ob=Experience.objects.filter(user=id).values('company','date_from',
	# 		'date_to','total_experience_time','summary')
	print('Experience_ob ',Experience_ob)
	pdf.ln(6)
	pdf.set_text_color(151, 47, 45) 
	pdf.set_font('times', size=14,style='B')
	pdf.cell(50,5,txt="Experience",align="l",ln = 0)
	count=0;
	for Exp in Experience_ob:
		print("Exp ",Exp)
		if count==0:
				if (pdf.y>260):
					pdf.add_page()
					print("pdf.add_page()")			   
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top
				pdf.x = offset-20
				pdf.set_font('times', size=12,style='B')
				pdf.set_text_color(0,0,0) 
				pdf.multi_cell(80,5,txt=Exp['company'],align="l",ln=0)
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top-5
				pdf.x = offset+5 
				pdf.multi_cell(71,5,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)		
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top+1
				pdf.x = offset-18.5 				 
				pdf.multi_cell(74,5,txt="Experience"+" "+str(Exp['total_experience_time']),align="R",ln = 1)
				top = pdf.y
				offset = pdf.x+30
				pdf.y = top
				pdf.x = offset+5 
				pdf.set_font('times', size=12)
				# for i in ls_sum:
				# 	pdf.cell(3, 5, '¤', 0, 0)
				# 	pdf.multi_cell(160,5,txt=str(i).replace('\n',''),align="l",ln = 1)
				# 	top = pdf.y
				# 	offset = pdf.x
				# 	pdf.y = top
				# 	pdf.x = offset+35
				ls_sum=str(Exp['summary']).split('\r')
				for i in ls_sum:
					pdf.cell(3, 5, '¤', 0, 0)
					pdf.multi_cell(160,5,txt=str(i).replace('\n',''),align="l",ln = 1)
					top = pdf.y
					offset = pdf.x
					pdf.y = top
					pdf.x = offset+35								
				# 	pdf.cell(3, 5, '¤', 0, 0)
				# pdf.multi_cell(160,5,txt=str(Exp['summary']),align="l")
				


		else:		
			if (pdf.y>260):
				pdf.add_page()
				print("pdf.add_page()")            
			top = pdf.y
			offset = pdf.x + 30
			# print("top ",top)
			# print("offset ",offset)
			pdf.y = top
			pdf.x = offset+5 

			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(80,2,txt=Exp['company'],align="l",ln=0)
			top = pdf.y
			offset = pdf.x + 5
			pdf.y = top-3 
			pdf.x = offset+17
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(60,5,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)
			pdf.set_font('times', size=12,style='B') 
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top+1
			pdf.x = offset-18.5

			pdf.multi_cell(74,5,txt="Experience"+" "+str(Exp['total_experience_time']),align="R",ln = 1)
			top = pdf.y
			offset = pdf.x+30
			pdf.y = top
			pdf.x = offset+5 
			pdf.set_font('times', size=12)
			ls_sum=str(Exp['summary']).split('\r')
			top = pdf.y
			offset = pdf.x
			pdf.y = top
			pdf.x = offset 
			print("ls_sum ",ls_sum) 
			for i in ls_sum:
				pdf.cell(3, 5, '¤', 0, 0)
				pdf.multi_cell(160,5,txt=str(i).replace('\n',''),align="l",ln = 1)
				top = pdf.y
				offset = pdf.x
				pdf.y = top
				pdf.x = offset+35
				# print("str(i) ",str(i))				
			# print('Exp mahesh',str(Exp['summary']).split('\r'))
		pdf.ln(6)
		count+=1;

	# Education_ob=Education.objects.filter(user=id).values('board','degree',
	# 		'date_from','date_to','marks','about')
	# pdf.add_page()
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Education",align="l",ln = 0)
	pdf.set_text_color(0,0,0)
	count=0;
	for Edu in Education_ob:
		print("Exp ",Exp)
		if count==0:
				if (pdf.y>260):
					pdf.add_page()
					print("pdf.add_page()")
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top
				pdf.x = offset-20			
				pdf.set_font('times', size=12,style='B')
				pdf.multi_cell(80,5,txt=Edu['degree'],align="l",ln=0)
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top-5
				pdf.x = offset+19
				pdf.multi_cell(57,5,txt=str(Edu['date_from'].strftime("%b "))+str(Edu['date_from'].strftime("%Y"))+" - "+str(Edu['date_to'].strftime("%b "))+Edu['date_to'].strftime("%Y"),align="R",ln=1)		
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top+1
				pdf.x = offset+30
				pdf.multi_cell(70,5,txt="Board:"+" "+str(Edu['board']),border=0,align="l",ln = 1)
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top
				pdf.x = offset+30
				pdf.multi_cell(70,5,txt="Marks:"+" "+str(Edu['marks']),border=0,align="l",ln = 1)				
				top = pdf.y
				offset = pdf.x+30.5
				pdf.y = top
				pdf.x = offset+5
				pdf.cell(3, 5, '¤', 0, 0)
				pdf.set_font('times', size=12,)
				pdf.multi_cell(150,5,txt=str(Edu['about']),border=0,align="l")
		else:		
			if (pdf.y>250):
				pdf.add_page()
				print("pdf.add_page()")
			top = pdf.y
			offset = pdf.x + 30
			print("top ",top)
			print("offset ",offset)
			pdf.y = top 
			pdf.x = offset+5.5
			print("pdf.y ",pdf.y)
			print("pdf.x ",pdf.x)
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(80,2,txt=Edu['degree'],align="l",ln=0)
			top = pdf.y
			offset = pdf.x + 5
			pdf.y = top-3
			pdf.x = offset+15
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(60,5,txt=str(Edu['date_from'].strftime("%b "))+str(Edu['date_from'].strftime("%Y"))+" - "+str(Edu['date_to'].strftime("%b "))+Edu['date_to'].strftime("%Y"),align="R",ln=1)
			pdf.set_font('times', size=12,style='B') 
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset+30.5 			
			pdf.multi_cell(200,5,txt="Board:"+" "+str(Edu['board']),border=0,align="l",ln = 1)
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset+30
			pdf.multi_cell(70,5,txt="Marks:"+" "+str(Edu['marks']),border=0,align="l",ln = 1)			
			top = pdf.y
			offset = pdf.x+30
			pdf.y = top
			pdf.x = offset+5.5
			pdf.set_font('times', size=12,)
			pdf.set_draw_color(0, 23, 255)
			# pdf.rect(pdf.x-1,pdf.y+2.5,0.1111111,0.1111,style='FD')
			# pdf.cell(5, 5, '¤', 0, 0)
			pdf.cell(3, 5, '¤', 0, 0)
			pdf.multi_cell(150,5,txt=str(Edu['about']),border=0,align="l")
		pdf.ln(6)
		count+=1;	
	if (pdf.y>270):
		pdf.add_page()
		# print("pdf.add_page()")	


	# Certification_ob=Certification.objects.filter(user=id).values('name','date_from','date_to','expired_date','about')	
	# print("Certification_ob ",Certification_ob)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Certification",align="l",ln = 0)
	count=0;
	pdf.set_text_color(0,0,0)

	for Exp in Certification_ob:
		# print("Exp ",Exp)
		if count==0:
				if (pdf.y>260):
					pdf.add_page()
					print("pdf.add_page()")			
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top
				pdf.x = offset-20
				pdf.set_font('times', size=12,style='B')
				pdf.multi_cell(80,5,txt=Exp['name'],align="l",ln=0)
				pdf.set_font('times', size=12,style='B')

				top = pdf.y
				offset = pdf.x +29
				pdf.y = top-5
				pdf.x = offset+1 
				pdf.multi_cell(50,5,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)
				# print("Exp['date_from'] ",Exp['date_from'].strftime("%Y"))		
				pdf.set_font('times', size=12,style='B')
				if (Exp['date_from']):
					top = pdf.y
					offset = pdf.x +5
					pdf.y = top+1
					pdf.x = offset+1 				 
					pdf.multi_cell(74,5,txt="Expiry Date"+" "+str(Exp['expired_date']),align="R",ln = 1)
				top = pdf.y
				offset = pdf.x+30
				pdf.y = top
				pdf.x = offset+6 
				pdf.set_font('times', size=12)
				pdf.multi_cell(160,5,txt=str(Exp['about']),align="l")
		else:		
			if (pdf.y>260):
				pdf.add_page()
				print("pdf.add_page()")            
			top = pdf.y
			offset = pdf.x + 30
			# print("top ",top)
			# print("offset ",offset)
			pdf.y = top
			pdf.x = offset+5.5 
			# print("pdf.y ",pdf.y)
			# print("pdf.x ",pdf.x)
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(80,2,txt=Exp['name'],align="l",ln=0)
			top = pdf.y
			offset = pdf.x + 5
			pdf.y = top-3 
			pdf.x = offset+25
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(50,5,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)
			# print(type(Exp['expired_date'])," ",Exp['expired_date'])
			if (Exp['expired_date']):
				pdf.set_font('times', size=12,style='B') 
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top+1
				pdf.x = offset-18.5 			
				pdf.multi_cell(74,5,txt="Expiry Date"+" "+str(Exp['expired_date']),align="R",ln = 1)
			top = pdf.y
			offset = pdf.x+30
			pdf.y = top
			pdf.x = offset+ 5.5
			pdf.set_font('times', size=12)
			pdf.multi_cell(160,5,txt=str(Exp['about']),align="l")
		pdf.ln(6)
		count+=1;
	if (pdf.y>260):
		pdf.add_page()


	count=0;
	for Edu in Projects_ob:
		
		if count==0:
				if (pdf.y>260):
					pdf.add_page()
					# print("pdf.add_page()")			
				pdf.set_font('times', size=14,style='B')
				pdf.set_text_color(151, 47, 45)
				pdf.cell(50,5,txt="Projects",align="l",ln = 0)
				top = pdf.y
				offset = pdf.x+5
				pdf.y = top
				pdf.x = offset-19.5			
				pdf.set_text_color(0,0,0)
				pdf.set_font('times', size=12,style='B')
				pdf.multi_cell(70,5,border=0,txt=Edu['title'],align="l",ln=0)
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x+5
				pdf.y = top-5
				pdf.x = offset+35 
				pdf.multi_cell(50,5,border=0,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)		
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x+5
				pdf.y = top+1
				pdf.x = offset+31
				pdf.multi_cell(100,5,txt="Technogy used:"+" "+str(Edu['technogy_used']),align="l",ln = 1)
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x+5
				pdf.y = top
				pdf.x = offset+31
				pdf.multi_cell(70,5,txt="Total member:"+" "+str(Edu['total_member']),align="l",ln = 1)
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x+5
				pdf.y = top
				pdf.x = offset+31
				pdf.multi_cell(70,5,txt="Your role:"+" "+str(Edu['your_role']),align="l",ln = 1)								
				top = pdf.y
				offset = pdf.x+30.5
				pdf.y = top
				pdf.x = offset+5
				pdf.set_font('times', size=12,)
				pdf.multi_cell(150,5,txt=str(Edu['summary']),align="l")
		else:		
			if (pdf.y>260):
				pdf.add_page()
				# print("pdf.add_page()")
            
			top = pdf.y
			offset = pdf.x + 30
			pdf.y = top 
			pdf.x = offset+6.5
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(120,5,txt=Edu['title'],border=0,align="l",ln=0)
			top = pdf.y
			offset = pdf.x + 5
			pdf.y = top-5
			pdf.x = offset
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(30,5,txt=str(Edu['date_from'])+" - "+str(Edu['date_to']),border=0,align="R",ln=1)
			pdf.set_font('times', size=12,style='B') 
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top+1
			pdf.x = offset+31  			
			# print("top 111",top)
			# print("offset 11",offset)
			# print("pdf.y 11",pdf.y)
			# print("pdf.x 11",pdf.x)

			pdf.multi_cell(100,5,txt="Technogy used:"+" "+str(Edu['technogy_used']),border=0,align="l",ln = 1)
			pdf.set_font('times', size=12,style='B')
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset+31
			pdf.multi_cell(70,5,txt="Total member:"+" "+str(Edu['total_member']),border=0,align="l",ln = 1)
			pdf.set_font('times', size=12,style='B')
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset+31
			pdf.multi_cell(70,5,txt="Your role:"+" "+str(Edu['your_role']),border=0,align="l",ln = 1)
			top = pdf.y
			offset = pdf.x+30
			pdf.y = top
			pdf.x = offset+6.5

			pdf.set_font('times', size=12,)
			pdf.multi_cell(150,5,txt=str(Edu['summary']),border=0,align="l")
		pdf.ln(6)
		count+=1;	
	if (pdf.y>280):
		pdf.add_page()
	# print("pdf.add_page() pdf.y //////////////////////////////////////////////////////", pdf.y)
	
	# Interest_ob=list(Interest.objects.filter(user=id).values('name'))
	pdf.ln(3)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(10,5,txt="Interest",align="l",ln = 0)
	pdf.set_text_color(0,0,0)
	sk=[]
	for i in range(len(Interest_ob)):
		sk.append(Interest_ob[i]['name'])
	top = pdf.y
	offset = pdf.x + 27	
	pdf.y = top
	pdf.x = offset-1 		
	pdf.set_font('times', size=12)
	pdf.multi_cell(160,5,txt=", ".join(sk),align="l",ln = 1)

	# Language_ob=list(Language.objects.filter(user=id).values('name'))
	# print("Language_ob ",Language_ob)
	# print(type(Language_ob))
	pdf.ln(3)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(10,5,txt="Language",align="l",ln = 0)
	pdf.set_text_color(0,0,0)
	lk=[]
	for i in range(len(Language_ob)):
		lk.append(Language_ob[i]['name'])
		# print("Language_ob[i]['name'] ",Language_ob[i]['name'])
	# print("sk ",lk)
	top = pdf.y
	offset = pdf.x + 27	
	pdf.y = top
	pdf.x = offset-1 		
	pdf.set_font('times', size=12)
	pdf.multi_cell(160,5,txt=", ".join(lk),align="l",ln = 1)
	# pdf.set_fill_color(25, 23, 255)
	# pdf.rect(pdf.x,pdf.y+4,0.1,0.1,style='FD')
	# pdf.eclippse(pdf.x,pdf.y+4,2,2,style='FD')
	pdf.output("media/simple_demo.pdf")
	response = HttpResponse(pdf,content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="simple_demo.pdf"'
	# return response
	v_or_d=context_dict['view_or_down']
	if v_or_d['view']==1:
		return FileResponse(open('media/simple_demo.pdf', 'rb'), content_type='application/pdf')
		# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaayes template_name_1")

	if v_or_d['down']==1:
		# print("ddddddddddddddddddddddddddddddddddddddddddddddddddd")
		return FileResponse(open('media/simple_demo.pdf', 'rb'),as_attachment=True, content_type='application/pdf') #// to downoad 

	# return FileResponse(open('media/simple_demo.pdf', 'rb'), content_type='application/pdf')
	# return FileResponse(open('media/simple_demo.pdf', 'rb'),as_attachment=True, content_type='application/pdf') // to downoad 

def make_pdf2(request,context_dict):
	# return render(request,'template_1.html')
	current_user = request.user
	id=current_user.id	
	print("////////////////////////////////////////////////////")
	print("context_dict ",context_dict)
	# print("context_dict ",context_dict)
	# Education_ob_test=context_dict['Education_ob'][0]
	# print("Education_ob_test ",Education_ob_test)


	# Address_ob=(Address.objects.all().values('flat_no','city',
	# 		'state','pincode','country'))[0]
	Address_ob=context_dict['Address_ob'][0]
	# print("Address_ob ",context_dict['Address_ob'][0])
	pdf = FPDF(orientation='P', unit='mm',
            format=(216,290))
	pdf.add_page()
	pdf.set_text_color(151, 47, 45)
	pdf.set_font('times', size=24,style='B')
	pdf.cell(200,10,txt="Mahesh Bisht",ln=1,align="l")
	pdf.ln(1)
	# pdf.set_draw_color(255, 0, 0)
	pdf.set_line_width(2)
	pdf.line(0, 30, 250, 30)
	pdf.ln(20)
	pdf.set_text_color(0,0,0)
	pdf.set_font('times', size=12)
	pdf.cell(100,5,txt=Address_ob['flat_no']+", "+Address_ob['city']+", "+Address_ob['state']+" "+str(Address_ob['pincode'])+", "+Address_ob['country'],ln=5,align="l")
	


	# Personal_ob=(Personal_Details.objects.all().values('first_name','middle_name','last_name','dob','contact'))[0]	
	
	Personal_ob=context_dict['Personal_Details_ob'][0]

	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print("context_dict['Personal_Details_ob' ] ",context_dict['Personal_Details_ob'][0])

	pdf.set_font('times', size=12,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(15,5,txt="Mobile:",align="l")
	pdf.set_font('times', size=12)
	pdf.set_text_color(0,0,0)
	pdf.cell(15,5,txt=str(Personal_ob['contact']),align="l")

	pdf.ln(5)
	pdf.set_font('times', size=12,style='B')
	
	Email_ob=context_dict['Email_ob'][0]
	print("Email_ob_test ",Email_ob)


	# Email_ob=(Email.objects.all().values('email_name'))[0]
	pdf.set_text_color(151, 47, 45)
	pdf.cell(13,5,txt="Email:",align="l")
	pdf.set_font('times', size=12)
	pdf.set_text_color(0,0,0)
	pdf.cell(15,5,txt=str(Email_ob['email_name']),align="l")

	pdf.ln(5)
	pdf.set_font('times', size=12,style='B')
	

	Other_link_ob=context_dict['Other_link_ob']
	# print("Other_link_ob_test ////////////////",Other_link_ob_test)

	# Other_link_ob=Other_link.objects.filter(user=id).values('name','link')
	for ob in Other_link_ob:
		print("ob ",ob)
		if ob['name'] == 'Linkedin':
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset-5
			pdf.set_font('times', size=12,style='B')
			pdf.set_text_color(151, 47, 45)
			pdf.cell(14,5,txt="Linkedin:",align="l")
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset
			pdf.set_font('times', size=12)
			pdf.set_text_color(0,0,0)
			pdf.cell(15,5,txt=str(ob['link']),align="l")
			
		elif ob['name'] == 'Github':
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset-5
			pdf.set_font('times', size=12,style='B')
			pdf.set_text_color(151, 47, 45)
			pdf.cell(10,5,txt="Github: ",align="l")
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top
			pdf.x = offset
			pdf.set_font('times', size=12)
			pdf.set_text_color(0,0,0)
			pdf.cell(15,5,txt=str(ob['link']),align="l")			
		pdf.ln(5)		


	pdf.ln(6)

	# Objectives_ob=(Objectives.objects.filter(user=id).values('objective_text'))[0]
	
	Objectives_ob=context_dict['Objectives_ob'][0]
	# print("context_dict['Other_link_ob'] ",con/text_dict['Objectives_ob'][0])
	top = pdf.y
	offset = pdf.x + 30
	# print('top ',top)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Objective",align="l",ln = 1)
	pdf.y = top+6
	# pdf.x = offset+5 
	# print('pdf.y ',pdf.y)
	# print('pdf.x ',pdf.x)
	pdf.set_font('times', size=12)
	pdf.set_text_color(0,0,0)
	pdf.multi_cell(160,5,txt=Objectives_ob['objective_text'],align="l")

	# print(" Skill_name_ob ", Skill_name_ob)
	
	# skill_ob=list(Skills.objects.filter(user=id).values('name'))
	
	Skill_name_ob=context_dict['skill_ob']
	pdf.ln(6)
	top = pdf.y
	offset = pdf.x + 30	
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Skills",align="l",ln = 1)

	lk=[]
	for i in range(len(Skill_name_ob)):
		lk.append(Skill_name_ob[i]['name'])
		print("skill_ob[i]['name'] ",Skill_name_ob[i]['name'])
	print("sk ",lk)
	top = pdf.y+6
	# offset = pdf.x - 15	
	# pdf.y = top
	# pdf.x = offset 		
	pdf.set_text_color(0,0,0)
	pdf.set_font('times', size=12)
	pdf.multi_cell(160,5,txt=", ".join(lk),align="l",border=0,ln = 1)




	Experience_ob=context_dict['Experience_ob']
	# print("Experience_ob_t ",Experience_ob_t)
	# Experience_ob=Experience.objects.filter(user=id).values('company','date_from',
	# 		'date_to','total_experience_time','summary')
	# print('Experience_ob ',Experience_ob)
	pdf.ln(6)
	pdf.set_text_color(151, 47, 45) 
	pdf.set_font('times', size=14,style='B')
	pdf.cell(50,5,txt="Experience",align="l",ln = 1)
	pdf.ln(1)
	count=0;
	for Exp in Experience_ob:
		print("Exp ",Exp)
		if count==0:
				if (pdf.y>260):
					pdf.add_page()
					print("pdf.add_page()")			   
				top = pdf.y+6
				# offset = pdf.x +5
				# pdf.y = top
				# pdf.x = offset-20
				pdf.set_font('times', size=12,style='B')
				pdf.set_text_color(0,0,0) 
				pdf.multi_cell(150,5,txt=Exp['company'],align="l",ln=0)
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				offset = pdf.x +5
				pdf.y = top-5
				# pdf.x = offset+3 
				pdf.multi_cell(50,5,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)		
				pdf.set_font('times', size=12,style='B')
				top = pdf.y
				# offset = pdf.x +5
				# pdf.y = top+1
				# pdf.x = offset-18.5 				 
				pdf.multi_cell(190,5,txt="Experience"+" "+str(Exp['total_experience_time']),align="l",ln = 1)
				top = pdf.y
				# offset = pdf.x+30
				# pdf.y = top
				# pdf.x = offset+5 
				pdf.set_font('times', size=12)
				# for i in ls_sum:
				# 	pdf.cell(3, 5, '¤', 0, 0)
				# 	pdf.multi_cell(160,5,txt=str(i).replace('\n',''),align="l",ln = 1)
				# 	top = pdf.y
				# 	offset = pdf.x
				# 	pdf.y = top
				# 	pdf.x = offset+35
				ls_sum=str(Exp['summary']).split('\r')
				for i in ls_sum:
					pdf.cell(3, 5, '¤', 0, 0)
					pdf.multi_cell(190,5,txt=str(i).replace('\n',''),align="l",ln = 1)
					top = pdf.y
					# offset = pdf.x
					# pdf.y = top
					# pdf.x = offset+35								
				# 	pdf.cell(3, 5, '¤', 0, 0)
				# pdf.multi_cell(160,5,txt=str(Exp['summary']),align="l")
				


		else:		
			if (pdf.y>260):
				pdf.add_page()
				# print("pdf.add_page()")            
			top = pdf.y
			# offset = pdf.x + 30
			# print("top ",top)
			# print("offset ",offset)
			pdf.y = top
			# pdf.x = offset+5 

			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(150,2,txt=Exp['company'],align="l",ln=0)
			top = pdf.y
			offset = pdf.x +5
			pdf.y = top-3.5

			# pdf.y = top-3 
			# pdf.x = offset+17
			pdf.set_font('times', size=12,style='B')
			pdf.multi_cell(50,5,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)
			pdf.set_font('times', size=12,style='B') 
			top = pdf.y
			# offset = pdf.x +5
			# pdf.y = top+1
			# pdf.x = offset-18.5

			pdf.multi_cell(190,5,txt="Experience"+" "+str(Exp['total_experience_time']),align="l",ln = 1)
			top = pdf.y
			# offset = pdf.x+30
			# pdf.y = top
			# pdf.x = offset+5 
			pdf.set_font('times', size=12)
			ls_sum=str(Exp['summary']).split('\r')
			top = pdf.y
			# offset = pdf.x
			# pdf.y = top
			# pdf.x = offset 
			print("ls_sum ",ls_sum) 
			for i in ls_sum:
				pdf.cell(3, 5, '¤', 0, 0)
				pdf.multi_cell(180,5,txt=str(i).replace('\n',''),align="l",ln = 1)
				top = pdf.y
				# offset = pdf.x
				# pdf.y = top
				# pdf.x = offset+35
				# print("str(i) ",str(i))				
			# print('Exp mahesh',str(Exp['summary']).split('\r'))
		pdf.ln(6)
		count+=1;

	Education_ob=context_dict['Education_ob']
	# print("Experience_ob_t ",Education_ob_t)
	# Education_ob=Education.objects.filter(user=id).values('board','degree',
	# 		'date_from','date_to','marks','about')
	# pdf.add_page()
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Education",align="l",border=0,ln = 1)
	pdf.set_text_color(0,0,0)
	count=0;
	for Edu in Education_ob:
		print("Exp ",Exp)
		# if count==0:
		if (pdf.y>260):
			pdf.add_page()
			print("pdf.add_page()")
		top = pdf.y
		offset = pdf.x +20
		pdf.y = top
		pdf.x = offset-20			
		pdf.set_font('times', size=12,style='B')
		pdf.multi_cell(80,5,txt=Edu['degree'],align="l",border=0,ln=0)
		pdf.set_font('times', size=12,style='B')
		top = pdf.y
		offset = pdf.x +44
		pdf.y = top-5
		pdf.x = offset+19
		pdf.multi_cell(57,5,border=0,txt=str(Edu['date_from'].strftime("%b "))+str(Edu['date_from'].strftime("%Y"))+" - "+str(Edu['date_to'].strftime("%b "))+Edu['date_to'].strftime("%Y"),align="R",ln=1)		
		pdf.set_font('times', size=12,style='B')
		top = pdf.y
		offset = pdf.x
		pdf.y = top+1
		pdf.x = offset
		pdf.multi_cell(70,5,txt="Board:"+" "+str(Edu['board']),border=0,align="l",ln = 1)
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset
		pdf.multi_cell(70,5,txt="Marks:"+" "+str(Edu['marks']),border=0,align="l",ln = 1)				
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset
		pdf.cell(3, 5, '¤', 0, 0)
		pdf.set_font('times', size=12,)
		pdf.multi_cell(150,5,txt=str(Edu['about']),border=0,align="l")

		pdf.ln(6)
		count+=1;	
	if (pdf.y>270):
		pdf.add_page()
		print("pdf.add_page()")	

	
	Certification_ob=context_dict['Certification_ob']
	# print("Certification_ob ",Certification_ob)

	# Certification_ob=Certification.objects.filter(user=id).values('name','date_from','date_to','expired_date','about')	
	# print("Certification_ob ",Certification_ob)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(50,5,txt="Certification",align="l",ln = 1)
	count=0;
	pdf.set_text_color(0,0,0)

	for Exp in Certification_ob:
		print("Exp ",Exp)
		# if count==0:
		if (pdf.y>260):
			pdf.add_page()
			print("pdf.add_page()")			
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset
		pdf.set_font('times', size=12,style='B')
		pdf.multi_cell(80,5,border=0,txt=Exp['name'],align="l",ln=0)
		pdf.set_font('times', size=12,style='B')

		top = pdf.y
		offset = pdf.x +29
		pdf.y = top-5
		pdf.x = offset+40 
		pdf.multi_cell(50,5,border=0,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)
		
		pdf.set_font('times', size=12,style='B')
		if (Exp['date_from']):
			top = pdf.y
			offset = pdf.x
			pdf.y = top+1
			pdf.x = offset				 
			pdf.multi_cell(74,5,border=0,txt="Expiry Date"+" "+str(Exp['expired_date']),align="l",ln = 1)
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset 
		pdf.set_font('times', size=12)
		pdf.multi_cell(160,5,border=0,txt=str(Exp['about']),align="l")
		
		pdf.ln(6)
		count+=1;
	if (pdf.y>260):
		pdf.add_page()
		print("pdf.add_page()")

	
	Projects_ob=context_dict['Projects_ob']	
	# Projects_ob=Projects.objects.filter(user=id).values('title','date_from','date_to','technogy_used', 
	# 	'total_member','your_role','summary','user')
	# pdf.add_page()

	count=0;
	for Edu in Projects_ob:
		
		
		pdf.set_font('times', size=14,style='B')
		pdf.set_text_color(151, 47, 45)
		pdf.cell(50,5,txt="Projects",align="l",ln = 1)
		if (pdf.y>260):
			pdf.add_page()
			print("pdf.add_page()")			
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset			
		pdf.set_text_color(0,0,0)
		pdf.set_font('times', size=12,style='B')
		pdf.multi_cell(140,5,border=0,txt=Edu['title'],align="l",ln=0)
		pdf.set_font('times', size=12,style='B')
		top = pdf.y
		offset = pdf.x+5
		pdf.y = top-5
		pdf.x = offset+4 
		pdf.multi_cell(50,5,border=0,txt=str(Exp['date_from'].strftime("%b "))+str(Exp['date_from'].strftime("%Y"))+" - "+str(Exp['date_to'].strftime("%b "))+Exp['date_to'].strftime("%Y"),align="R",ln=1)		
		pdf.set_font('times', size=12,style='B')
		top = pdf.y
		offset = pdf.x
		pdf.y = top+1
		pdf.x = offset
		pdf.multi_cell(200,5,border=0,txt="Technogy used:"+" "+str(Edu['technogy_used']),align="l",ln = 1)
		pdf.set_font('times', size=12,style='B')
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset
		pdf.multi_cell(70,5,border=0,txt="Total member:"+" "+str(Edu['total_member']),align="l",ln = 1)
		pdf.set_font('times', size=12,style='B')
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset
		pdf.multi_cell(70,5,border=0,txt="Your role:"+" "+str(Edu['your_role']),align="l",ln = 1)								
		top = pdf.y
		offset = pdf.x
		pdf.y = top
		pdf.x = offset
		pdf.set_font('times', size=12,)
		pdf.multi_cell(200,5,border=0,txt=str(Edu['summary']),align="l")

		pdf.ln(6)
		count+=1;	
	if (pdf.y>280):
		pdf.add_page()
	# print("pdf.add_page() pdf.y //////////////////////////////////////////////////////", pdf.y)
	
	Interest_ob=context_dict['Interest_ob']
	# print("Certification_ob ",Certification_ob)	
	# Interest_ob=list(Interest.objects.filter(user=id).values('name'))
	pdf.ln(3)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(10,5,txt="Interest",align="l",ln = 1)
	pdf.set_text_color(0,0,0)
	sk=[]
	for i in range(len(Interest_ob)):
		sk.append(Interest_ob[i]['name'])
	top = pdf.y
	offset = pdf.x 
	pdf.y = top
	pdf.x = offset 		
	pdf.set_font('times', size=12)
	pdf.multi_cell(190,5,border=0,txt=", ".join(sk),align="l",ln = 1)
 

	Language_ob=context_dict['Language_ob']
	# list(Language.objects.filter(user=id).values('name'))
	# print("Language_ob ",Language_ob)
	# print(type(Language_ob))
	pdf.ln(3)
	pdf.set_font('times', size=14,style='B')
	pdf.set_text_color(151, 47, 45)
	pdf.cell(10,5,txt="Language",align="l",ln = 1)
	pdf.set_text_color(0,0,0)
	lk=[]
	for i in range(len(Language_ob)):
		lk.append(Language_ob[i]['name'])
		print("Language_ob[i]['name'] ",Language_ob[i]['name'])
	# print("sk ",lk)
	top = pdf.y
	offset = pdf.x 
	pdf.y = top
	pdf.x = offset
	pdf.set_font('times', size=12)
	pdf.multi_cell(190,5,border=0,txt=", ".join(lk),align="l",ln = 1)
	# pdf.set_fill_color(25, 23, 255)
	# pdf.rect(pdf.x,pdf.y+4,0.1,0.1,style='FD')
	# pdf.eclippse(pdf.x,pdf.y+4,2,2,style='FD')
	pdf.output("media/simple_demo.pdf")
	response = HttpResponse(pdf,content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="simple_demo.pdf"'
	print("context_dict context_dictcontext_dict",context_dict)
	# return response
	v_or_d=context_dict['view_or_down']
	if v_or_d['view']==1:
		return FileResponse(open('media/simple_demo.pdf', 'rb'), content_type='application/pdf')
		# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaayes template_name_1")

	if v_or_d['down']==1:
		# print("ddddddddddddddddddddddddddddddddddddddddddddddddddd")
		return FileResponse(open('media/simple_demo.pdf', 'rb'),as_attachment=True, content_type='application/pdf') #// to downoad 

	# return FileResponse(open('media/simple_demo.pdf', 'rb'), content_type='application/pdf')



def index(request):
		form = Registrationform()
		# print(form)
		current_user = request.user
		id=current_user.id

		Personal_ob=Personal_Details.objects.filter(user=id).values('first_name')
		# print('Personal_ob',Personal_ob)
		# # generate_pdf(None,{'Personal_ob':Personal_ob});
		# pdf=render_to_pdf('index.html',{'Personal_ob':Personal_ob})

		return render(request,'index1.html',{'form':form,'Personal_ob':Personal_ob}) #,{'sset':sset,'freqs':freqs,'posts':posts,})


def resume_template(request):

	current_user = request.user
	id=current_user.id	
	# skill_name = dict(Skills.objects.filter(user=id).values('name').first()['name'])

	# prin/t(skill_name)	
	return render(request,'srt-resume.html')


def make_resume1(request):
	current_user = request.user
	id=current_user.id	
	qdict=dict(request.POST)
	print("qdict mahesh ",qdict)	

	skill_ob=Skills.objects.filter(id__in=qdict['Skill_name']).values('name')
	Objectives_ob=(Objectives.objects.filter(id__in=qdict['Objectives_name']).values('objective_text'))
	Experience_ob=Experience.objects.filter(id__in=qdict['Experience_name']).values('company','date_from',
		'date_to','total_experience_time','summary')	
	Education_ob=Education.objects.filter(id__in=qdict['Education_name']).values('board','degree',
		'date_from','date_to','marks','about')
	
	Personal_Details_ob=Personal_Details.objects.filter(id__in=qdict['Personal_name']).values('first_name',
		'middle_name','last_name','dob','contact')
	
	Email_ob=Email.objects.filter(id__in=qdict['Email_name']).values('email_name')

	Certification_ob=Certification.objects.filter(id__in=qdict['Certification_name']).values('name',
		'date_from','date_to','expired_date','about')
	
	Projects_ob=Projects.objects.filter(id__in=qdict['Projects_name']).values('title','date_from',
		'date_to','technogy_used', 'total_member','your_role','summary')		
	
	Interest_ob=Interest.objects.filter(id__in=qdict['Interest_name']).values('name')
	
	Other_link_ob=Other_link.objects.filter(id__in=qdict['Other_link_name']).values('link','name')
	# print("Other_link_obOther_link_ob ",Other_link_ob)
	# print("qdict['Other_link_name'] ",qdict['Other_link_name'])
	Address_ob=Address.objects.filter(id__in=qdict['Address_name']).values('flat_no','city',
		'state','pincode','country')
	Language_ob= Language.objects.filter(id__in=qdict['Language_name']).values('name','user')


	# print("///////////////Address_ob ",Address_ob)
	print("request.POST ",request.POST)	
	print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
	view_or_down={'view':0,'down':0}
	# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	if 'checkBtn' in qdict:
		view_or_down['down']=1
		# print("view_or_down['down']=1view_or_down['down']=1view_or_down['down']=1")
	if "ViewBtn" in request.POST:
		# print("view_or_down['down']=1view_or_down['down']=1view_or_down['down']=1")
		view_or_down['view']=1

	context={'skill_ob':skill_ob,'Objectives_ob':Objectives_ob,
		'Experience_ob':Experience_ob,'Education_ob':Education_ob,'Personal_Details_ob':Personal_Details_ob,
		'Address_ob':Address_ob,'Email_ob':Email_ob,'Certification_ob':Certification_ob,
		'Interest_ob':Interest_ob,'Projects_ob':Projects_ob,
		'Other_link_ob':Other_link_ob,'Language_ob':Language_ob,'view_or_down':view_or_down}
	# if 'template_name_2' in qdict:
	# 	print("yes template_name_2")
	if 'template_name_1' in qdict:
		return make_pdf(request,context)
	if 'template_name_2' in qdict:
		return make_pdf2(request,context)


	# return render(request,'template_1.html',{'skill_ob':skill_ob,'Objectives_ob':Objectives_ob,
	# 	'Experience_ob':Experience_ob,'Education_ob':Education_ob,'Personal_Details_ob':Personal_Details_ob,
	# 	'Address_ob':Address_ob,'Email_ob':Email_ob,'Certification_ob':Certification_ob,
	# 	'Interest_ob':Interest_ob,'Projects_ob':Projects_ob,
	# 	'Other_link_ob':Other_link_ob})


def make_resume(request):

	current_user = request.user
	id=current_user.id	
	qdict=dict(request.POST)
	print("qdict mahesh ",qdict)
	# print(
	if request.method == 'POST':
		skill_ob=Skills.objects.filter(id__in=qdict['Skill_name']).values('name')
		Objectives_ob=(Objectives.objects.filter(id__in=qdict['Objectives_name']).values('objective_text'))
		# print("Objectives_ob Objectives_ob Objectives_ob Objectives_ob ",Objectives_ob)
		Experience_ob=Experience.objects.filter(id__in=qdict['Experience_name']).values('company','date_from',
			'date_to','total_experience_time','summary')

		Education_ob=Education.objects.filter(id__in=qdict['Education_name']).values('board','degree',
			'date_from','date_to','about')
		Personal_Details_ob=Personal_Details.objects.filter(id__in=qdict['Personal_name']).values('first_name',
			'middle_name','last_name','dob','contact')
		Address_ob=Address.objects.filter(id__in=qdict['Address_name']).values('flat_no','city',
			'state','pincode','country')
		Email_ob=Email.objects.filter(id__in=qdict['Email_name']).values('email_name')
		Certification_ob=Certification.objects.filter(id__in=qdict['Certification_name']).values('name',
			'date_from','date_to','expired_date','about')
		Projects_ob=Projects.objects.filter(id__in=qdict['Projects_name']).values('title','date_from',
			'date_to','technogy_used', 'total_member','your_role','summary')		
		Interest_ob=Interest.objects.filter(id__in=qdict['Interest_name']).values('name')
		Other_link_ob=Other_link.objects.filter(id__in=qdict['Other_link_name']).values('link')



		return render(request,'template_1.html',{'skill_ob':skill_ob,'Objectives_ob':Objectives_ob,
			'Experience_ob':Experience_ob,'Education_ob':Education_ob,'Personal_Details_ob':Personal_Details_ob,
			'Address_ob':Address_ob,'Email_ob':Email_ob,'Certification_ob':Certification_ob,
			'Interest_ob':Interest_ob,'Projects_ob':Projects_ob,
			'Other_link_ob':Other_link_ob})


	else:
		Email_from=Email.objects.filter(email_user=id).all()
		Personal_Details_from=Personal_Details.objects.filter(user=id).all()
		Other_link_from=Other_link.objects.filter(user=id).all()
		# print("Other_link_from Other_link_from ////////",Other_link_from)

		Objectives_from=Objectives.objects.filter(user=id).all()
		Education_from=Education.objects.filter(user=id).all()
		Experience_from=Experience.objects.filter(user=id).all()
		Projects_from=Projects.objects.filter(user=id).all()

		Certification_from=Certification.objects.filter(user=id).all()
		Address_from=Address.objects.filter(user=id).all()
		Interest_from=Interest.objects.filter(user=id).all()

		skill_from = Skills.objects.filter(user=id).all()
		# print("skill_from \\\\\\",skill_from)
		Language_from=Language.objects.filter(user=id).all() 
		# print("Language_form \\\\\\",Language_form)

		return render(request,'make_resume.html',{'skill_from':skill_from,
			'Email_from':Email_from,
			'Personal_Details_from':Personal_Details_from,
			'Other_link_from':Other_link_from,
			'Objectives_from':Objectives_from,
			'Education_from':Education_from,
			'Experience_from':Experience_from,
			'Projects_from':Projects_from,
			'Certification_from':Certification_from,
			'Address_from':Address_from,
			'Interest_from':Interest_from,
			'Language_from':Language_from,
			})

		


def show_details(request):
	current_user = request.user
	id=current_user.id
	print("id ",id)
	# Personal_ob=Personal_Details.objects.filter(user=id)
	# print(Personal_ob)	
	if request.method == 'POST':
		form1 = Skills_form(request.POST)
		form2 = Email_form(request.POST)
		form7 =Experience_form(request.POST) 
		form8 =Projects_form(request.POST)
		form9 =Certification_form(request.POST)
		form10 =Address_form(request.POST)

		ur=User.objects.get(pk=id)
		qdict=dict(request.POST)
		print(qdict)

		if 'sk_form' in qdict:
			print("its a skill from")
			if 'text_fields_skills' in qdict:

				if qdict['text_fields_skills']!=['']:
					for v in qdict['text_fields_skills']:
						ur=User.objects.get(pk=id)  
						sk = Skills.objects.create(name=v,user=ur)
						sk.save()

			if 'name' in qdict:

				if qdict['name']!=['']:
					Skills.objects.filter(id__in=qdict['name'],user=id).delete()

		if 'Address_form' in qdict:
			print("DsssssssssssS")
			if 'flat_no' in  qdict:
				count=len(qdict['flat_no'])
				# print("count ",count)
				if count:
					for i in range(count):
						ob = Address.objects.create(flat_no=qdict['flat_no'][i],
							city=qdict['city'][i],
							state=qdict['state'][i],
					    	pincode=qdict['pincode'][i],
							country=qdict['country'][i],
							user=ur)

						ob.save()

			if 'form_Addr' in qdict:

				if qdict['form_Addr']!=['']:
					Address.objects.filter(id__in=qdict['form_Addr'],user=ur).delete()			

		if 'Certification_form' in qdict:
			print("DsssssssssssS")
			if 'name' in  qdict:
				count=len(qdict['name'])
				if count:
					for i in range(count):
						ob = Certification.objects.create(name=qdict['name'][i],
							date_from=qdict['date_from'][i],date_to=qdict['date_to'][i],
					    	expired_date=qdict['expired_date'][i],
							about=qdict['about'][i],
							user=ur)

						ob.save()
			if 	'form_Cert' in qdict:
					
				if qdict['form_Cert']!=['']:
					Certification.objects.filter(id__in=qdict['form_Cert'],user=ur).delete()			
					print("geeee")


		if 'Projects_form' in qdict:
			if 'title' in  qdict:
				count=len(qdict['title'])
				# print("count ",count)
				if count:
					for i in range(count):
						ob = Projects.objects.create(title=qdict['title'][i],
							date_from=qdict['date_from'][i],date_to=qdict['date_to'][i],
					    	technogy_used=qdict['technogy_used'][i],
							total_member=qdict['total_member'][i],
							your_role=qdict['your_role'][i],
							summary=qdict['summary'][i],user=ur)

						ob.save()
			if 'form_Projt' in qdict:

				if qdict['form_Projt']!=['']:
					Projects.objects.filter(id__in=qdict['form_Projt'],user=ur).delete()			


		if 'Experience_form' in qdict:
			if 'company' in  qdict:
				count=len(qdict['company'])
				if count:
					for i in range(count):
						ob = Experience.objects.create(company=qdict['company'][i]
							,total_experience_time=qdict['total_experience_time'][i],
							date_from=qdict['date_from'][i],date_to=qdict['date_to'][i],
							summary=qdict['summary'][i],user=ur)
						ob.save()
			if 'form_Exper' in qdict:

				if qdict['form_Exper']!=['']:
					Experience.objects.filter(id__in=qdict['form_Exper'],user=ur).delete()			


		form6 =Education_form(request.POST)

		if 'Education_form' in qdict:
			print("in ")
			print(qdict)
			if 'board' in  qdict:
				count=len(qdict['board'])
				print("count ",count)
				if count:
					for i in range(count):
						ob = Education.objects.create(board=qdict['board'][i],degree=qdict['degree'][i],
							date_from=qdict['date_from'][i],date_to=qdict['date_to'][i],
							about=qdict['about'][i],user=ur)
						ob.save()

			if 'form_educ' in qdict:

				if qdict['form_educ']!=['']:
					Education.objects.filter(id__in=qdict['form_educ'],user=ur).delete()			


		form4 =Other_link_form(request.POST) 
		if 'Other_link_form' in qdict:
			# form4.save()
			if 'text_fields_Other_link' in qdict:
				count=len(qdict['Other_link_name'])
			# if qdict['text_fields_Other_link']!=['']:
				for i in range(count):
					ur=User.objects.get(pk=id)  
					ob = Other_link.objects.create(link=qdict['text_fields_Other_link'][i],name=qdict['Other_link_name'][i],user=ur)
					print(i)
					print("heererr")
					ob.save()


			if 'objective_text' in qdict:

				if qdict['objective_text']!=['']:
					Other_link.objects.filter(id__in=qdict['objective_text'],user=id).delete()	


		if 'Email_form' in qdict:
			if qdict['text_fields_Email']!=['']:
				for v in qdict['text_fields_Email']:
					ur=User.objects.get(pk=id)  
					ob = Email.objects.create(email_name=v,email_user=ur)
					ob.save()


			if 'email_name' in qdict:

				if qdict['email_name']!=['']:
					Email.objects.filter(id__in=qdict['email_name'],email_user=id).delete()			


		form11=Interest_form(request.POST)
		if 'Interest_form' in qdict:
			if qdict['text_fields_Interest']!=['']:
				for v in qdict['text_fields_Interest']:
					ur=User.objects.get(pk=id)  
					ob = Interest.objects.create(name=v,user=ur)
					ob.save()


			if 'name' in qdict:

				if qdict['name']!=['']:
					Interest.objects.filter(id__in=qdict['name'],user=id).delete()			


		form5 =Objectives_form(request.POST)
		if 'Objectives_form' in qdict:
			# print("gere")
			# print("its a Objective from")
			if qdict['text_fields_objective']!=['']:
				for v in qdict['text_fields_objective']:
					ur=User.objects.get(pk=id)  
					ob = Objectives.objects.create(objective_text=v,user=ur)
					print(v)
					# ob.save()


			if 'objective_text' in qdict:

				if qdict['objective_text']!=['']:
					Objectives.objects.filter(id__in=qdict['objective_text'],user=id).delete()			


		
			
			

		form3 =Personal_Details_form(request.POST,instance=Personal_Details.objects.get(user=id)) 
		if 'Personal_Details_form' in qdict:
			print("gere")
			print(form3.is_valid())
			print(form3)
			print(form3.save())
			form3.save()


		form_skill = Skills_form(initial={'user':id,
			'name':list(Skills.objects.filter(user=id).values('name','id','user'))})


		form_Objectives =Objectives_form(initial={'user':id,
			'objective_text':list(Objectives.objects.filter(user=id).values('objective_text','user','id'))}) 


		form_email = Email_form(initial={'email_user':id,
			'email_name':list(Email.objects.filter(email_user=id).values('email_name','email_user','id'))}
			)

		# form_Personal_Details =Personal_Details_form(instance=Personal_Details.objects.get(user=id)) 
		form_Personal_Details =Personal_Details_form(initial={'user':id,
			'first_name':Personal_Details.objects.filter(user=id).values('first_name').first()['first_name'],
			 'middle_name':Personal_Details.objects.filter(user=id).values('middle_name').first()['middle_name'],
		    'last_name':Personal_Details.objects.filter(user=id).values('last_name').first()['last_name'],
		    'dob':Personal_Details.objects.filter(user=id).values('dob').first()['dob'],   
		    'contact':Personal_Details.objects.filter(user=id).values('contact').first()['contact']}) 

		# form_Other_link =Other_link_form(initial={'user':id,
		# 	'link':Other_link.objects.filter(user=id).values('link').first()['link']}) 
		


		form_Interest =Interest_form(initial={'user':id,
			'name':list(Interest.objects.filter(user=id).values('name','user','id'))})



		Other_link_FormSet = modelformset_factory(Other_link, form=Other_link_form,extra=0)
		Other_link_formSet = Other_link_FormSet(queryset=Other_link.objects.filter(user=id))	
		# print("////////////////////////////////////////////////////////////////////////////")
		# print("Other_link_formSet ",Other_link_formSet)

		EduFormSet = modelformset_factory(Education, form=Education_form,extra=0)
		formset = EduFormSet(queryset=Education.objects.filter(user=id))

		ExperienceFormSet = modelformset_factory(Experience, form=Experience_form,extra=0)
		Expformset = ExperienceFormSet(queryset=Experience.objects.filter(user=id))		
		

		ProjectFormSet = modelformset_factory(Projects, form=Projects_form,extra=0)
		Projectformset = ProjectFormSet(queryset=Projects.objects.filter(user=id))		
		
		CertificationFormSet = modelformset_factory(Certification, form=Certification_form,extra=0)
		Certificationformset = CertificationFormSet(queryset=Certification.objects.filter(user=id))		


		AddressFormSet = modelformset_factory(Address, form=Address_form,extra=0)
		Addressformset = AddressFormSet(queryset=Address.objects.filter(user=id))	

	
		return render(request,'show_details_1.html',
		{'form_skill':form_skill,'form_email':form_email,'form_Personal_Details':form_Personal_Details,
		# 'form_Other_link' :form_Other_link,
		 'form_Objectives': form_Objectives,
		  'form_Interest' :form_Interest,
		 'formset': formset,'Expformset':Expformset,
		 'Projectformset':Projectformset,
		 'Certificationformset':Certificationformset,
		 'Addressformset':Addressformset,
		 'Other_link_formSet':Other_link_formSet,
		 }) 
	else:

		# if Personal_Details.objects.get(user=id)==null: 


		form_skill = Skills_form(initial={'user':id,
			'name':list(Skills.objects.filter(user=id).values('name','id','user'))})
		# print("form_skill ",form_skill)


		form_Objectives =Objectives_form(initial={'user':id,
			'objective_text':list(Objectives.objects.filter(user=id).values('objective_text','user','id'))}) 
		# print("form_Objectives ",form_Objectives)

		form_email = Email_form(initial={'email_user':id,
			'email_name':list(Email.objects.filter(email_user=id).values('email_name','email_user','id'))}
			)

		# form_Personal_Details =Personal_Details_form(initial={'user':id,
		# 	'first_name':Personal_Details.objects.filter(user=id).values('first_name'),
		# 	 'middle_name':Personal_Details.objects.filter(user=id).values('middle_name'),
		#     'last_name':Personal_Details.objects.filter(user=id).values('last_name'),
		#     'dob':Personal_Details.objects.filter(user=id).values('dob'),   
		#     'contact':Personal_Details.objects.filter(user=id).values('contact')}) 

		form_Personal_Details =Personal_Details_form(instance=Personal_Details.objects.get(user=id))

		# form_Other_link =Other_link_form(instance=Other_link.objects.get(user=id)) 

		form_Other_link =Other_link_form(initial={'user':id,
			'link':list(Other_link.objects.filter(user=id).values('link','name','user','id'))})		
		# print("form_Other_link ",form_Other_link)

		form_Interest =Interest_form(initial={'user':id,
			'name':list(Interest.objects.filter(user=id).values('name','user','id'))})

		EduFormSet = modelformset_factory(Education, form=Education_form,extra=0)
		formset = EduFormSet(queryset=Education.objects.filter(user=id))

		ExperienceFormSet = modelformset_factory(Experience, form=Experience_form,extra=0)
		Expformset = ExperienceFormSet(queryset=Experience.objects.filter(user=id))		
		

		ProjectFormSet = modelformset_factory(Projects, form=Projects_form,extra=0)
		Projectformset = ProjectFormSet(queryset=Projects.objects.filter(user=id))		
		
		CertificationFormSet = modelformset_factory(Certification, form=Certification_form,extra=0)
		Certificationformset = CertificationFormSet(queryset=Certification.objects.filter(user=id))		


		AddressFormSet = modelformset_factory(Address, form=Address_form,extra=0)
		Addressformset = AddressFormSet(queryset=Address.objects.filter(user=id))	
		# print("form_Personal_Details ",form_Personal_Details)

	
		return render(request,'show_details_1.html',
		{'form_skill':form_skill,'form_email':form_email,'form_Personal_Details':form_Personal_Details,
		'form_Other_link' :form_Other_link, 'form_Objectives': form_Objectives,
		  'form_Interest' :form_Interest,
		 'formset': formset,'Expformset':Expformset,
		 'Projectformset':Projectformset,
		 'Certificationformset':Certificationformset,
		 'Addressformset':Addressformset,
		 # 'form_Personal_Details_test':form_Personal_Details_test
		 # 'form_Personal_Details_new':form_Personal_Details_new
		 }) 
		 # 'form_Education_list' :form_Education_list ,
		  # 'form_Experience': form_Experience,
		 # 'form_Projects': form_Projects,
		  # 'form_Certification': form_Certification,
		 # 'form_Address': form_Address,
		 # 'form_text':form_text,
		# form_Education_list=[]

		# for i in Education.objects.filter(user=id):

		# 	# .values('id','board','degree','date_from','date_to','about','user')):
		# 	print("hereeee")
		# 	# print(Education_form(instance=i))
		# 	ob=Education_form(instance=i)
		# 	print(ob)
		# 	form_Education_list.append(ob)
		# print("ob ",form_Education_list)	

		# form_Education =Education_form(initial={'user':id,
		# 	'board':Education.objects.filter(user=id).values('board').first()['board'],
		# 	'degree':Education.objects.filter(user=id).values('degree').first()['degree'],
		# 	'date_from':Education.objects.filter(user=id).values('date_from').first()['date_from'],
		# 	'date_to':Education.objects.filter(user=id).values('date_to').first()['date_to'],
		# 	'marks':Education.objects.filter(user=id).values('marks').first()['marks'],
		# 	'about':Education.objects.filter(user=id).values('about').first()['about'],}) 
		# print("form_Education")
		# print(form_Education)
		
		# form_Experience =Experience_form(initial={'user':id,
		# 	'company':Experience.objects.filter(user=id).values('company').first()['company'],
		# 	'total_experience_time':Experience.objects.filter(user=id).values('total_experience_time').first()['total_experience_time'],
		# 	'date_from':Experience.objects.filter(user=id).values('date_from').first()['date_from'],
		# 	'date_to':Experience.objects.filter(user=id).values('date_to').first()['date_to'],
		# 	'summary':Experience.objects.filter(user=id).values('summary').first()['summary'],}) 
		
		# form_Projects =Projects_form(initial={'user':id,
		# 	'title':Projects.objects.filter(user=id).values('title').first()['title'],
		# 	'date_from':Projects.objects.filter(user=id).values('date_from').first()['date_from'],
		# 	'date_to':Projects.objects.filter(user=id).values('date_to').first()['date_to'],
		# 	'technogy_used':Projects.objects.filter(user=id).values('technogy_used').first()['technogy_used'],
		# 	'total_member':Projects.objects.filter(user=id).values('total_member').first()['total_member'],
		# 	'your_role':Projects.objects.filter(user=id).values('your_role').first()['your_role'],
		# 	'summary':Projects.objects.filter(user=id).values('summary').first()['summary'],})
		

		# form_Certification =Certification_form(initial={'user':id,
		# 	'name':Certification.objects.filter(user=id).values('name'),
		# 	'date_from':Certification.objects.filter(user=id).values('date_from'),
		# 	'date_to':Certification.objects.filter(user=id).values('date_to'),
		# 	'expired_date':Certification.objects.filter(user=id).values('expired_date'),
		# 	'about':Certification.objects.filter(user=id).values('about')})


		# form_Address =Address_form(initial={'user':id,
		# 	'flat_no':Address.objects.filter(user=id).values('flat_no').first()['flat_no'],
		# 	'city':Address.objects.filter(user=id).values('city').first()['city'],
		# 	'state':Address.objects.filter(user=id).values('state').first()['state'],
		# 	'pincode':Address.objects.filter(user=id).values('pincode').first()['pincode'],
		# 	'country':Address.objects.filter(user=id).values('country').first()['country'],})




def enter_details(request):
	current_user = request.user
	id=current_user.id

	Personal_ob=Personal_Details.objects.filter(user=id)
	print(Personal_ob)	
	if request.method == 'POST':
		# if 
		form1 = Skills_form(request.POST)
		form2 = Email_form(request.POST)
		form3 =Personal_Details_form(request.POST) 
		form4 =Other_link_form(request.POST) 
		form5 =Objectives_form(request.POST) 

		form6 =Education_form(request.POST) 
		form7 =Experience_form(request.POST) 
		form8 =Projects_form(request.POST)
		form9 =Certification_form(request.POST)
		form10 =Address_form(request.POST)
		form11=Interest_form(request.POST)

		print(form11)
		if form1.is_valid() & form2.is_valid() & form3.is_valid() & form4.is_valid() & form5.is_valid() & form6.is_valid() & form7.is_valid()  & form8.is_valid() & form9.is_valid() & form10.is_valid() & form11.is_valid():
			form1.save()
			form2.save()
			form3.save()
			form4.save()
			form5.save()
			form6.save()
			form7.save()
			form8.save()
			form9.save()
			form10.save()
			form11.save()
			return render(request,'enter_details_1.html',{'form_skill':form1,'form_email':form2,'form_Personal_Details':form3,
					'form_Other_link' :form4, 'form_Objectives': form5,
					 'form_Education' :form6 , 'form_Experience': form7,
					 'form_Projects': form8, 'form_Certification': form9,
					 'form_Address': form10, 'form_Interest' :form11,
					 'Personal_ob':Personal_ob})
		else:


			return render(request,'enter_details_1.html',
					{'form_skill':form1,'form_email':form2,'form_Personal_Details':form3,
					'form_Other_link' :form4, 'form_Objectives': form5,
					 'form_Education' :form6 , 'form_Experience': form7,
					 'form_Projects': form8, 'form_Certification': form9,
					 'form_Address': form10, 'form_Interest' :form11,
					 'Personal_ob':Personal_ob})			

	else:
		form_skill = Skills_form()
		form_email = Email_form()		
		form_Personal_Details =Personal_Details_form() 
		form_Other_link =Other_link_form() 
		form_Objectives =Objectives_form() 

		form_Education =Education_form() 
		form_Experience =Experience_form() 
		form_Projects =Projects_form()
		form_Certification =Certification_form()
		form_Address =Address_form()
		form_Interest =Interest_form()
		# print(form_email)
		# print(form_skill)
		return render(request,'enter_details_1.html',
		{'form_skill':form_skill,'form_email':form_email,'form_Personal_Details':form_Personal_Details,
		'form_Other_link' :form_Other_link, 'form_Objectives': form_Objectives,
		 'form_Education' :form_Education , 'form_Experience': form_Experience,
		 'form_Projects': form_Projects, 'form_Certification': form_Certification,
		 'form_Address': form_Address, 'form_Interest' :form_Interest,
		 'Personal_ob':Personal_ob}) 


def register(request):
	print("bisht")
	print(request.method == "POST" and request.is_ajax())
	print(request.method)

	form=Registrationform(request.POST)
	if request.method == "POST":
		# print("maheshs")
		print(request.POST)
		print("fef", form.is_valid())
		print(form)
		if form.is_valid():
			print("here")
			print(form.cleaned_data['password1'])
			print(form.cleaned_data['password1'])

			form.save()
			return HttpResponse(json.dumps("successsfully register"),content_type="application/json")
		else:
			# print(type(form.errors))
			mess=(((form.errors.get_json_data(escape_html=False))['email'])[0])['message']
			print(mess)
			# print(form.is_bound)
			return HttpResponse(json.dumps(mess),content_type="application/json")

	else:
		return render(request,'index.html',{'form':form})


# 	# return render(request,'sentiment_result.html',{'result':test.predict(test_lda),
# 	# 	                                            'data':data})	
# 	return HttpResponse(json.dumps(" not succesly"),content_type="application/json")

	# obj=urresume.objects.all()
	# print(obj)
	# return render(request,'test_data.html',{'obj':obj}) #,{'sset':sset,'freqs':freqs,'posts':posts,})



# class index(View):
# 	#model=Post


# class test(View):
# 	#model=Post
# 	def get(self,request):
# 		#sset = Post.objects.filter(category='travel').order_by('-created_on')
# 		#posts=Post.objects.all()[0:3]
# 		#freqs=Post.objects.values('category').order_by().annotate(Count('category'))



# def test(request):
# 	if request.method =='POST':
# 		print(request)
# 		new_stud=urresume_form(request.POST)
		
# 		print(new_stud.is_valid())
# 		if new_stud.is_valid():
# 			new_stud.save(True)
# 			print(new_stud)
# 			print("g4rggrgrg")
# 			# messages.success(request,"Successfully Created ")
# 			#temprol=new_stud.cleaned_data.get('roll_no')
# 			#print(type(temprol))
# 			#print(temprol)
# 			# form= attform()
# 			#context['form']= attform()
# 			return render(request, "index1.html",) 

# 		else:
# 			return render(request,'test.html',{'form':new_stud} ) 
# 	else:

# 		new_stud=urresume_form()
# 		# return render(request,'signuppage.html',{'form':new_stud} )
# 		return render(request,'test.html',{'form':new_stud}) #,{'sset':sset,'freqs':freqs,'posts':posts,})


		



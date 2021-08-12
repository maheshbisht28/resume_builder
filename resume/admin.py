from django.contrib import admin

# Register your models here.

from user.models import User


from .models import User_Email, Personal_Details,Other_link , Objectives ,Language, Education , Experience , Projects, Skills , Certification,Address ,Interest



class User_table(admin.ModelAdmin):
    list_display = (
    "id",
    "first_name",
    "last_name",
    "email",
    "date_joined",
    "last_login",
    "is_admin",
    "is_active",
    "is_staff",
 )



class Interest_table(admin.ModelAdmin):
	list_display = ("id",
 "name",
  
    "user",
    "created_at",
    "modified_at")


class Address_table(admin.ModelAdmin):
	list_display = ("id",
  "flat_no",
    "city",
    "state",
    "pincode",
    "country",
    "user",
    "created_at",
    "modified_at")


class Certification_table(admin.ModelAdmin):
	list_display = ("id",
    "name",
    "date_from",
    "date_to",
    "expired_date",
    "about",
  
    "user",
    "created_at",
    "modified_at")


class Projects_table(admin.ModelAdmin):
	list_display = ("id",
    "title",
    "date_from",
    "date_to",
    "technogy_used",
    "total_member",
    "your_role" ,
    "summary",
    "user",
    "created_at",
    "modified_at")



class Skills_table(admin.ModelAdmin):
	list_display = ("id",
	"name",	
    "user",
    "created_at",
    "modified_at")


class Experience_table(admin.ModelAdmin):
	list_display = ("id",
	    "company",
	    "date_from",
	    "date_to",
	    "total_experience_time",
	    "summary",
    "user",
    "created_at",
    "modified_at")

class Education_table(admin.ModelAdmin):
	list_display = ("id",
	    "board",
    "degree",
    "date_from",
    "date_to",
    "about",
    "user",
    "marks",
    "created_at",
    "modified_at")

class Objectives_table(admin.ModelAdmin):
	list_display = ("id","objective_text", "user",
    "created_at",
    "modified_at")

class Email_table(admin.ModelAdmin):
    # email_name=models.CharField(max_length=20)
	list_display = ("id", "email_name","email_user","created_at","modified_at")



class Personal_Details_table(admin.ModelAdmin):
	list_display = ("id",
	    "first_name",
    "middle_name",
    "last_name"  ,
    "dob" ,   
     
    "contact",
     "user",
    "created_at",
    "modified_at")



class Other_link_table(admin.ModelAdmin):
	list_display = ("id","link","name", "user",
    "created_at",
    "modified_at")


class Language_table(admin.ModelAdmin):
    list_display = ( "name",
    "user",)


# # # class Userresumetable(admin.ModelAdmin):
# # # 	list_display = ("user","education")


# Email, Personal_Details,Other_link , Objectives , Education ,
#  Experience , Projects, Skills , Certification,Address ,Interest

admin.site.register(Language,Language_table)
admin.site.register(User,User_table)
admin.site.register(User_Email,Email_table)
admin.site.register(Personal_Details,Personal_Details_table)	
admin.site.register(Other_link,Other_link_table)
admin.site.register(Objectives,Objectives_table)
admin.site.register(Education,Education_table)
admin.site.register(Experience,Experience_table)
admin.site.register(Projects,Projects_table)
admin.site.register(Skills,Skills_table)
admin.site.register(Certification,Certification_table)
admin.site.register(Address,Address_table)
admin.site.register(Interest,Interest_table)

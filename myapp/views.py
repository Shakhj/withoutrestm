from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
import json
from django.views.generic import View

# Create your views here.
class EmployeeDetails(View):
	def get(self,request,*args, **kwargs):
		emp=Employee.objects.get(id=2)
		emp_data={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}
		json_data=json.dumps(emp_data)
		return HttpResponse(json_data,content_type="application/json_data")
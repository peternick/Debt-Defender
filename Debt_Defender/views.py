from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import psycopg2
import json
from settings import POSTGRES_STRING
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return redirect('/')

    name = request.POST['name']
    school = request.POST['school']
    income = request.POST['income']
    commitment = request.POST['commitment']
    major = request.POST['major']
    scholarship_amount = request.POST['scholarships']
    total_semesters = request.POST['semesters']

    params = (username, school, commitment, 
            major, scholarship_amount, total_semesters)

    conn = psycopg2.connect(POSTGRES_STRING)
    curr = conn.cursor()
    query = """INSERT INTO Students 
                  (name, school, income, commitment, major,
                   scholarship_amount, semesters) VALUES
                   (%s, %s, %s, %s, %s, %s, %s);"""
                   
    curr.execute(query, params)
    conn.commit()
    conn.close()

    return "beep"

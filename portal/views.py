from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import LoginForm, ProfileForm, DisabledForm
from .models import Customuser, Subjectz, Subject_2, Subject_3, Course, Payment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import slugify
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
from django.contrib.auth import logout
from paystackapi.transaction import Transaction
from django.http import HttpResponse, HttpResponseNotFound

from paystackapi.paystack import Paystack
paystack_secret_key = "sk_test_e56f0936942534b4bb68c97f96ec5478d3177c2d"
paystack_public_key = "pk_test_b5844de2f9b615efc128374d8b500c7109d903bd"
paystack = Paystack(secret_key=paystack_secret_key)

current_year = '2020/2021'
current_term = 'First Term'
current_term_url = 'first_term'
current_year_url = '2020-2021'

classes_list = ['JSS 1 BLUE', 'JSS 1 GREEN', 'JSS 1 YELLOW', 'JSS 2 BLUE', 'JSS 2 GREEN', 'JSS 2 YELLOW',
             'JSS 3 BLUE', 'JSS 3 GREEN', 'JSS 3 YELLOW', 'SSS 1 HARMONY', 'SSS 1 SMART', 'SSS 1 SPECIAL',
             'SSS 2 HARMONY', 'SSS 2 SMART', 'SSS 2 SPECIAL', 'SSS 3 HARMONY', 'SSS 3 SMART', 'SSS 3 SPECIAL',
             'Graduated']
terms_list = ['First Term', 'Second Term', 'Third Term']
year_list = ['2019/2020','2020/2021','2021/2022','2022/2023','2023/2024','2024/2025','2025/2026','2026/2027',
             '2027/2028','2028/2029','2029/2030','2030/2031','2031/2032','2032/2033','2033/2034','2034/2035']


@login_required()
def trans(request, term = None, session = None):
    session = session.replace('-', '/')
    #term  = current_term_url
    term = term.split('_')
    term = term[0].capitalize() + ' ' + term[1].capitalize()
    student = request.user
    print(student.email)
    response = Transaction.initialize(amount='36500', email=student.email)
    print(response['status'])
    print(response)
    ref = response['data']['reference']
    access_code = response['data']['access_code']
    pay_instance = get_object_or_404(Customuser, username=request.user.username)
    if response['status'] == True:
        if Payment.objects.all().filter(student=student, session=session, term=term).exists():
            pay_instance = Payment.objects.all().filter(student=student, session=session, term=term)
            pay_instance.update(student = student, session=session, term=term, reference=ref, access_code=access_code)
            print('payment instance exists')


        elif term in terms_list and session in year_list:
            print('payment instance does not exists but we will create an instance right away')
            Payment.objects.create(student=student, session=session, term=term)
            pay_instance = Payment.objects.all().filter(student=student, session=session, term=term)
            pay_instance.update(student = student, session=session, term=term, reference=ref, access_code= access_code)
        else:
            print('invalid term entered ...we just cannot help you man!!!')
            #return HttpResponseNotFound('<h1>Oops!!! The page you are looking for does not Exits</h1>')
        a_url = response['data']['authorization_url']
        print(a_url)
        return redirect(a_url)
        
    else:
        print(response['message'])
    return HttpResponse(response)

@login_required()
def pdf_payments(request):
    student = request.user
    session = current_year_url
    term = current_term_url
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "inline; filename={username}--payment_slip.pdf".format(
        username = student.username,
    )
    html = render_to_string("portal/pdf_payments.html", {'student': student})
    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response
"""
    if session == None and term ==None:
        student = request.user
        session = session
        term = term
        response = HttpResponse(content_type="application/pdf")
        response['Content-Disposition'] = "inline; filename={username}--payment_slip.pdf".format(
        username = student.username,
        )
        html = render_to_string("portal/pdf_payments.html", {'student': student})
        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response
    else:
        print("not None")
"""
@login_required()
def pdf_redirect(request):
    session = current_year_url
    term = current_term_url
    return redirect('pdf_payments', session=session, term=term )

@login_required()
def pdf_results(request, choice = None, session = None):
    student = get_object_or_404(Customuser, username=request.user.username)
    session = session.replace('-','/')
    term = choice.replace('_',' ')
    choice = choice.lower()
    #print(session)
    #print(term)
    if choice =='first_term':
        #print('First term')
        subjects = Subjectz.objects.all().filter(student=student, session=session)
    elif choice =='second_term':
        #print('Second term')
        subjects = Subject_2.objects.all().filter(student=student, session=session)
    elif choice =='third_term':
        #print('Third term')
        subjects = Subject_3.objects.all().filter(student=student, session=session)
    else:
        print('None of the terms were selected')
    unsolved_list = []
    list_of_subjects = []
    for subject in subjects:
        unsolved_list.append(subject)
    #print(list_of_subjects)
    for i in unsolved_list:
        ca1_score = i.ca1_score
        ca2_score = i.ca2_score
        exam_score = i.exam_score
        total = ca1_score + ca2_score + exam_score
        if total != 0:
            #print(i.title)
            list_of_subjects.append(i)

    #print(list_of_subjects)
    overall_total = 0
    nc = len(list_of_subjects)

    for subject in list_of_subjects:

        subject_title = subject.title
        ca1_score = subject.ca1_score
        ca2_score = subject.ca2_score
        exam_score = subject.exam_score
        total = ca1_score + ca2_score + exam_score
        overall_total += total
        grade = ''
        remark = ''
        if choice == 'first_term':
            subject_instance = Subjectz.objects.all().filter(student = student, title = subject_title, session=session)
        elif choice == 'second_term':
            subject_instance = Subject_2.objects.all().filter(student=student, title=subject_title, session=session)
        elif choice == 'third_term':
            subject_instance = Subject_3.objects.all().filter(student=student, title=subject_title, session=session)
        if total >= 70:
            grade = 'A'
            remark = 'Excellent'
        elif total >= 60 and total <= 69:
            grade = 'B'
            remark = 'Very Good'
        elif total >= 50 and total <= 59:
            grade = 'C'
            remark = 'Average'
        elif total >= 45 and total <= 49:
            grade = 'D'
            remark = 'Fair'
        elif total >= 40 and total <= 44:
            grade = 'E'
            remark = 'Pass'
        elif total < 40:
            grade = 'F'
            remark = 'Failed'
        else:
            grade = 'Nil'
            remark = 'Nil'

        subject_instance.update(title = subject_title, ca1_score = ca1_score, ca2_score = ca2_score, exam_score = exam_score,
                                total = total, grade = grade, remark = remark, session=session)
    if nc == 0:
        average = 0
    else:
        average = overall_total/nc

    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "inline; filename={username}-{current_class}-result.pdf".format(
        username = student.username,
        current_class= student.current_class,
    )
    html = render_to_string("portal/pdf_results.html", {'student': student, 'subjectz': list_of_subjects, 'session': session,
                                                        'term': term, 'average':average, 'overall_total': overall_total} )
    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response

def home(request):
    return render(request, 'portal/home.html', {'title': 'Homepage'})

def about(request):
    return render(request, 'portal/about.html', {'title': 'About Us'})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required()
def logged_in(request):
    return render(request, 'portal/loggedin.html' )



@login_required()
def subjects(request):
    sender = request.user
    subz = Subjectz.objects.all().filter(student = sender, session = current_year, term = current_term)
    dcourses = []
    coursez = Course.objects.all()
    for sub in subz:
        subtitle = sub.title
        Course.objects.all().filter(title = subtitle)
        dcourse = Course.objects.all().filter(title = subtitle).first()
        if dcourse not in dcourses:
            dcourses.append(dcourse)
        else:
            print('{} is present already'.format(dcourse))
    print(dcourses)
    #print(sender.current_class)
    return render(request, 'portal/subjects.html', {'sender': sender, 'subz': subz, 'coursez': coursez, 'dcourses': dcourses})


@login_required()
def results(request):
    student = get_object_or_404(Customuser, username=request.user.username)
    years = ['2019/2020','2020/2021','2021/2022','2022/2023','2023/2024','2024/2025','2025/2026','2026/2027','2027/2028']
    available = []
    clz_dict = {}
    for year in years:
        if Subjectz.objects.all().filter(student=student, session=year).exists():
            available.append(year)
        else:
            pass
    #print(available)
    for i in available:
        dfirst = Subjectz.objects.all().filter(student=student, session=i).first()
        c = dfirst.session
        c = c.replace('/','-')
        clz_dict[dfirst] = c
    print(clz_dict)
    return render(request, 'portal/results.html',{'student':student, 'clz_dict':clz_dict, 'current_year':current_year,
                                                  'current_term':current_term})







@login_required()
#this is a tool for the admin to generate a pdf of all students in the based on thier current class
def all_students(request, class_name = None ):
    clss = class_name.replace('-',' ')
    clss = clss.upper()
    #verifying if the class is a valid classname
    if clss in classes_list:
        students_in = Customuser.objects.all().filter(current_class=clss)
        response = HttpResponse(content_type="application/pdf")
        response['Content-Disposition'] = "inline; filename= All students.pdf"
        html = render_to_string("portal/students.html", {'students': students_in})
        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response
    else:
        print('the class selected is not a valid class Name')

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)


            #custom_user = Customuser.objects.filter(email=username)
            custom_user = authenticate(request, username=username, password=password)
            if custom_user is not None:
                #messages.success(request, 'Login Succesful')
                login(request, custom_user)
                #print('user has been logged in')
                return redirect('logged_in')
            elif custom_user is None:
                print('message section')
                messages.warning(request, 'Password or email address is incorrect')
            print(custom_user)
        else:
            print('else portion')
        #print(username)
        #print(password)
    else:
        form = LoginForm()
        print('this is a get request')
    return render(request, 'portal/login.html', {'form': form})



@login_required()
def dashboard(request):
    sender = request.user
    #print(sender)
    #print(sender.username)
    student_instance = Customuser.objects.filter(username=sender.username).first()

    data = model_to_dict(student_instance,
            fields=['first_name', 'last_name', 'middle_name', 'gender', 'email', 'phonenumber', 'date_of_birth', 'religion', 'nok1_name',
                  'nok1_phone', 'nok1_relationship', 'admission_no', 'state_of_origin',
                  'lga', 'resident_type', 'house_address',  'prev_school', 'passport' ])
    #print(data)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        disabled_form = DisabledForm(request.POST)
        if profile_form.is_valid():
            first_name = profile_form.cleaned_data.get('first_name').capitalize()
            last_name = profile_form.cleaned_data.get('last_name').capitalize()
            middle_name = profile_form.cleaned_data.get('middle_name').capitalize()
            gender = profile_form.cleaned_data.get('gender')
            email = profile_form.cleaned_data.get('email').capitalize()
            phonenumber = profile_form.cleaned_data.get('phonenumber')
            date_of_birth = profile_form.cleaned_data.get('date_of_birth')
            religion = profile_form.cleaned_data.get('religion')
            nok1_name = profile_form.cleaned_data.get('nok1_name').capitalize()
            nok1_phone = profile_form.cleaned_data.get('nok1_phone')
            nok1_relationship = profile_form.cleaned_data.get('nok1_relationship')
            admission_no = profile_form.cleaned_data.get('admission_no')
            state_of_origin = profile_form.cleaned_data.get('state_of_origin')
            lga = profile_form.cleaned_data.get('lga').capitalize()
            resident_type = profile_form.cleaned_data.get('resident_type')
            house_address = profile_form.cleaned_data.get('house_address').capitalize()
            prev_school = profile_form.cleaned_data.get('prev_school').capitalize()
            passport = request.FILES.get('passport')
            student = Customuser.objects.filter(username=sender.username)
            student_exact = Customuser.objects.filter(username=sender.username).first()
            passport = request.FILES.get('passport')
            student_exact.passport = passport
            student_exact.save()

            student.update(first_name=first_name,last_name=last_name, middle_name=middle_name,gender='Male', email=email,
                           phonenumber=phonenumber, date_of_birth=date_of_birth, religion=religion, nok1_name=nok1_name,
                           nok1_phone=nok1_phone, nok1_relationship=nok1_relationship, admission_no=admission_no,
                           state_of_origin=state_of_origin, lga=lga, resident_type=resident_type, house_address=house_address,
                           prev_school=prev_school, submitted=True)
            messages.success(request, 'Your Profile Information was successfully updated')
            print('updated successfully profile')
        elif disabled_form.is_valid():
            first_name = disabled_form.cleaned_data.get('first_name')
            last_name = disabled_form.cleaned_data.get('last_name')
            middle_name = disabled_form.cleaned_data.get('middle_name')
            gender = disabled_form.cleaned_data.get('gender')
            email = disabled_form.cleaned_data.get('email').capitalize()
            phonenumber = disabled_form.cleaned_data.get('phonenumber')
            date_of_birth = disabled_form.cleaned_data.get('date_of_birth')
            religion = disabled_form.cleaned_data.get('religion')
            nok1_name = disabled_form.cleaned_data.get('nok1_name').capitalize()
            nok1_phone = disabled_form.cleaned_data.get('nok1_phone')
            nok1_relationship = disabled_form.cleaned_data.get('nok1_relationship')
            admission_no = disabled_form.cleaned_data.get('admission_no')
            state_of_origin = disabled_form.cleaned_data.get('state_of_origin')
            lga = disabled_form.cleaned_data.get('lga')
            resident_type = disabled_form.cleaned_data.get('resident_type')
            house_address = disabled_form.cleaned_data.get('house_address').capitalize()
            prev_school = disabled_form.cleaned_data.get('prev_school').upper()
            student = Customuser.objects.filter(username=sender.username)
            student_exact = Customuser.objects.filter(username=sender.username).first()
            passport = request.FILES.get('passport')
            student_exact.passport = passport
            student_exact.save()
            student.update( email=email, phonenumber=phonenumber,  religion=religion, nok1_name=nok1_name,
                           nok1_phone=nok1_phone, nok1_relationship=nok1_relationship, house_address=house_address,
                           prev_school=prev_school,submitted=True)
            messages.success(request, 'Your Profile Information was successfully updated, \n Reload page to see updated info')
            print('updated successfully disabled')


        else:
            print('form submitted was invalid')
    else:
        profile_form = ProfileForm(initial=data)
        disabled_form = DisabledForm(initial=data)
    return render(request, 'portal/dashboard.html', {'profile_form': profile_form, 'sender': sender, 'disabled_form':disabled_form})

def profile(request):
    data = { 'first_name': 'Gideon' }
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            print('valid input')
        else:
            print('invalid input')
    else:
        form = ProfileForm()
    return render(request, 'portal/profile.html', {'form': form})

""""@login_required()
def payment(request):
    sender = request.user
    return render(request, 'portal/payment.html', {'sender': sender})  """

@login_required()
def payment(request):
    sender = request.user
    return render(request, 'portal/payment.html', {'sender': sender, 'current_term_url': current_term_url,
                                                    'current_year_url': current_year_url})


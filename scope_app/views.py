from django.shortcuts import render , redirect
from .forms import ContactForm
from django.core.mail import send_mail
from .forms import StudentForm
from .models import Student
from .models import Course,Country,State,City        
from django.http import JsonResponse

# Create your views here.

def insert_india_data():

    if Country.objects.exists():
        return

    india = Country.objects.create(name="India")

    data = {

        "Andhra Pradesh": ["Visakhapatnam","Vijayawada","Guntur","Nellore"],
        "Arunachal Pradesh": ["Itanagar","Tawang","Ziro"],
        "Assam": ["Guwahati","Dibrugarh","Silchar"],
        "Bihar": ["Patna","Gaya","Bhagalpur"],
        "Chhattisgarh": ["Raipur","Bilaspur","Durg"],
        "Goa": ["Panaji","Margao","Vasco da Gama"],
        "Gujarat": ["Ahmedabad","Surat","Vadodara","Rajkot"],
        "Haryana": ["Gurgaon","Faridabad","Panipat"],
        "Himachal Pradesh": ["Shimla","Manali","Dharamshala"],
        "Jharkhand": ["Ranchi","Jamshedpur","Dhanbad"],
        "Karnataka": ["Bangalore","Mysore","Mangalore","Hubli"],
        "Kerala": [
            "Thiruvananthapuram","Kollam","Pathanamthitta","Alappuzha",
            "Kottayam","Idukki","Ernakulam","Thrissur","Palakkad",
            "Malappuram","Kozhikode","Wayanad","Kannur","Kasaragod"
        ],
        "Madhya Pradesh": ["Bhopal","Indore","Gwalior","Jabalpur"],
        "Maharashtra": ["Mumbai","Pune","Nagpur","Nashik","Aurangabad"],
        "Manipur": ["Imphal","Thoubal","Churachandpur"],
        "Meghalaya": ["Shillong","Tura","Jowai"],
        "Mizoram": ["Aizawl","Lunglei","Champhai"],
        "Nagaland": ["Kohima","Dimapur","Mokokchung"],
        "Odisha": ["Bhubaneswar","Cuttack","Rourkela"],
        "Punjab": ["Ludhiana","Amritsar","Jalandhar"],
        "Rajasthan": ["Jaipur","Jodhpur","Udaipur","Kota"],
        "Sikkim": ["Gangtok","Namchi","Gyalshing"],
        "Tamil Nadu": ["Chennai","Coimbatore","Madurai","Salem","Trichy"],
        "Telangana": ["Hyderabad","Warangal","Nizamabad"],
        "Tripura": ["Agartala","Dharmanagar","Udaipur"],
        "Uttar Pradesh": ["Lucknow","Kanpur","Varanasi","Agra","Noida"],
        "Uttarakhand": ["Dehradun","Haridwar","Nainital"],
        "West Bengal": ["Kolkata","Howrah","Durgapur","Siliguri"]

    }

    for state_name, cities in data.items():

        state = State.objects.create(name=state_name, country=india)

        for city in cities:
            City.objects.create(name=city, state=state)
def base(request):

    return render(request,'base.html')
                  
def home(request):

    insert_india_data()
    insert_courses()
    return render(request,'home.html')

def about(request):

    return render(request,'about.html')

def contact(request):

    msg=""

    if request.method=="POST":

        form=ContactForm(request.POST)

        if form.is_valid():

            form.save()

            try:

                send_mail(

                    subject=form.cleaned_data['subject'],

                    message=form.cleaned_data['message'],

                    from_email=form.cleaned_data['email'],

                    recipient_list=['geethug398@gmail.com'],

                    fail_silently=False
                    )
                msg="Email sent successfully"

            except:

                msg="Unable to send email"

    else:

        form=ContactForm()

    return render(request,'contact.html',{'form':form,'msg':msg})

def register(request):

    insert_india_data()

    countries = Country.objects.all()

    if request.method == "POST":

        student = Student.objects.create(

            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),

            country_id=request.POST.get('country'),
            state_id=request.POST.get('state'),
            city_id=request.POST.get('city'),

            avatar=request.FILES.get('avatar')
        )

        return redirect('password', student.id)

    return render(request,'register.html',{'countries': countries})

def load_states(request):

    country_id = request.GET.get('country')

    states = State.objects.filter(country_id=country_id).values('id','name')

    return JsonResponse(list(states),safe=False)

def load_cities(request):

    state_id = request.GET.get('state')

    if not state_id:
        return JsonResponse([], safe=False)

    cities = City.objects.filter(state_id=state_id).values('id', 'name')

    return JsonResponse(list(cities), safe=False)

def password(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.password = request.POST.get('password')

        student.save()

        return redirect('login')

    return render(request, 'password.html',{'student': student})

def login(request):

    if request.method=="POST":

        email=request.POST['email']
        password=request.POST['password']

        try:

            student=Student.objects.get(email=email,password=password)

            request.session['student_id']=student.id

            return redirect('dashboard')

        except:

            return render(request,'login.html',{'msg':'Invalid Login'})

    return render(request,'login.html')

def dashboard(request):

    if 'student_id' not in request.session:

        return redirect('login')

    courses=Course.objects.all()

    return render(request,'dashboard.html',{'courses':courses})

def logout(request):

    request.session.flush()

    return redirect('login')

def profile(request):

    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(
        id=request.session['student_id']
    )

    courses = Course.objects.all()

    return render(
        request,
        'profile.html',
        {
            'student': student,
            'courses': courses
        }
    )

def insert_courses():

    if Course.objects.exists():
        return

    Course.objects.create(
        course_name="Python Full Stack",
        duration="6 Months",
        fee=50000
    )

    Course.objects.create(
        course_name="Data Science",
        duration="8 Months",
        fee=70000
    )

    Course.objects.create(
        course_name="UI/UX Design",
        duration="4 Months",
        fee=35000
    )
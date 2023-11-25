from django.shortcuts import render
from pgapp.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage



def home(request):
    return render(request, 'home.html')

def mysave(request):
    if request.method == "POST" and request.is_ajax():
        name = request.POST.get('name')
        email = request.POST.get('email')
        mssg = request.POST.get('mssg')
        contact.objects.create(name=name, email=email, mssg=mssg)
        return JsonResponse({'success': 'Data saved successfully'}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def index(request):
    return render(request,'index.html')

def PG_Register_DataSaving(request):
    
    if request.method =="POST" and request.is_ajax():
        pg_name=request.POST.get('pg_name')
        pg_loaction=request.POST.get('pg_loaction')
        pg_type=request.POST.get('pg_type')
        pg_email=request.POST.get('pg_email')
        pg_phone=request.POST.get('pg_phone')
        room_type=request.POST.get('room_type')
        meals=request.POST.get('meals')
        ac_room=request.POST.get('ac_room')
        laundary=request.POST.get('laundary')
        furnish=request.POST.get('furnish')
        wifi=request.POST.get('wifi')
        m_rent=request.POST.get('m_rent')
        s_amount=request.POST.get('s_amount')
        a_charge=request.POST.get('a_charge')
        o_name=request.POST.get('o_name')
        o_phone=request.POST.get('o_phone')
        o_address=request.POST.get('o_address')
        description=request.POST.get('description')

        image=request.FILES.get('file11',False)
        supdoc = request.FILES['file11']
        folder='media/images'
        fs=FileSystemStorage(location=folder)
        files=fs.save(supdoc.name,supdoc)
        upload_pdf=fs.url(files)
        upload_pdf=str(upload_pdf).split('media/')
        upload_pdf='images/'+upload_pdf[1]
        print('upload_pdf',upload_pdf,'/////////////////////////////////////////////////////')

        rule=request.FILES.get('file12',False)
        supdoc1 = request.FILES['file12']
        folder='media/images'
        fs1=FileSystemStorage(location=folder)
        files1=fs1.save(supdoc1.name,supdoc1)
        upload_pdf1=fs1.url(files1)
        upload_pdf1=str(upload_pdf1).split('media/')
        upload_pdf1='images/'+upload_pdf1[1]
        print('upload_pdf1',upload_pdf1,'///////////////////////////////////////////////////')

        document=request.FILES.get('file13',False)
        supdoc2 = request.FILES['file13']
        folder='media/images'
        fs2=FileSystemStorage(location=folder)
        files2=fs2.save(supdoc2.name,supdoc2)
        upload_pdf2=fs2.url(files2)
        upload_pdf2=str(upload_pdf2).split('media/')
        upload_pdf2='images/'+upload_pdf2[1]
        print('upload_pdf2',upload_pdf2,'///////////////////////////////////////////////////////')

        pg_record = PGRegister.objects.create(pg_name=pg_name,pg_loaction=pg_loaction,pg_type=pg_type,pg_email=pg_email,pg_phone=pg_phone,room_type=room_type,meals=meals,ac_room=ac_room,laundary=laundary,furnish=furnish,wifi=wifi,m_rent=m_rent,s_amount=s_amount,a_charge=a_charge,o_name=o_name,o_phone=o_phone,o_address=o_address,description=description,image=upload_pdf,rule=upload_pdf1,document=upload_pdf2)

        # Return a success response
        return JsonResponse({'success': 'Data saved successfully'})

    return JsonResponse({'error': 'Invalid request method'})

def pg_register(request):
    
    return render(request,'Pg_register.html')   



def index1(request):
    # obj=formdata.objects.filter(delete_flag=False).all()
    # context={
    #     'obj':obj,
    # }
    return render(request,'login.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        
        user = UserCredentials(username=username, password=password)
        user.save()

        # return redirect('home/') 

    return render(request, 'login.html')
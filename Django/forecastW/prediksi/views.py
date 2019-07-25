from django.shortcuts import render
from data.models import data_klimat, indeks_musiman
from django.db.models import Sum, Count
from .forms import FormField


def index(request):
    posts = data_klimat.objects.all()
    context ={
        'Posts':posts,
    }
    if request.method =='POST':
        context['case'] = request.POST['jenis_data']

    return render(request,'prediksi_views.html',context)

def temp_rata(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('temp_rata2')))
    y_tot = float((query_y['temp_rata2__sum']))

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('temp_rata2')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    comp_tahun=''
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','temp_rata2')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_rata2')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_rata2')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_rata2')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_rata2')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_rata2')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_rata2')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_rata2')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_rata2')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_rata2')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_rata2')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        
    y=''

    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_rata2')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1
                
    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_rata2')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_rata2')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_rata2')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_rata2')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1


 

    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }
    return render(request,'temp_rata.html',context)

def temp_max(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('temp_max')))
    y_tot = float((query_y['temp_max__sum']))
    print('y_tot=',y_tot)

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('temp_max')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    comp_tahun=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
   
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','temp_max')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_max')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_max')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_max')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_max')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
        
        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_max')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_max')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_max')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_max')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_max')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_max')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
        
    y=''
    
    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
            print(im)
        elif bulan == 'Februari':
            print(im)
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_max')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_max')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_max')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_max')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_max')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1
                



    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }
    return render(request,'temp_max.html',context)

def temp_min(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('temp_min')))
    y_tot = float((query_y['temp_min__sum']))
    print('y_tot=',y_tot)

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('temp_min')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    comp_tahun=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
   
   
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','temp_min')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_min')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_min')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
        
        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_min')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_min')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_min')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_min')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_min')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_min')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','temp_min')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','temp_min')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
              
    y=''
    
    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
            print(im)
        elif bulan == 'Februari':
            print(im)
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_min')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_min')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_min')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_min')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','temp_min')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1



    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }
    return render(request,'temp_min.html',context)

def curah_hujan(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('curah_hujan')))
    y_tot = float((query_y['curah_hujan__sum']))
    print('y_tot=',y_tot)

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('curah_hujan')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    comp_tahun=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
   
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','curah_hujan')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','curah_hujan')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','curah_hujan')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','curah_hujan')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','curah_hujan')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','curah_hujan')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','curah_hujan')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','curah_hujan')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','curah_hujan')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','curah_hujan')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','curah_hujan')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
    y=''
    
    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
            print(im)
        elif bulan == 'Februari':
            print(im)
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','curah_hujan')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','curah_hujan')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','curah_hujan')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','curah_hujan')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','curah_hujan')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1



    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }

    return render(request,'curah_hujan.html',context)

def penyinaran_matahari(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('penyinaran_matahari')))
    y_tot = float((query_y['penyinaran_matahari__sum']))
    print('y_tot=',y_tot)

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('penyinaran_matahari')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    comp_tahun=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
   
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','penyinaran_matahari')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','penyinaran_matahari')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','penyinaran_matahari')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','penyinaran_matahari')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','penyinaran_matahari')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','penyinaran_matahari')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','penyinaran_matahari')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','penyinaran_matahari')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','penyinaran_matahari')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','penyinaran_matahari')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','penyinaran_matahari')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
    y=''
    
    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
            print(im)
        elif bulan == 'Februari':
            print(im)
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','penyinaran_matahari')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','penyinaran_matahari')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','penyinaran_matahari')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','penyinaran_matahari')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','penyinaran_matahari')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1



    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }

    return render(request,'penyinaran_matahari.html',context)

def tekanan_udara(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('tekanan_udara')))
    y_tot = float((query_y['tekanan_udara__sum']))
    print('y_tot=',y_tot)

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('tekanan_udara')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    comp_tahun=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
   
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','tekanan_udara')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','tekanan_udara')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','tekanan_udara')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','tekanan_udara')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','tekanan_udara')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','tekanan_udara')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','tekanan_udara')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','tekanan_udara')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','tekanan_udara')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','tekanan_udara')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','tekanan_udara')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
    y=''
    
    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
            print(im)
        elif bulan == 'Februari':
            print(im)
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','tekanan_udara')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','tekanan_udara')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','tekanan_udara')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','tekanan_udara')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','tekanan_udara')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1



    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }

    return render(request,'tekanan_udara.html',context)

def kelembaban(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('kelembaban')))
    y_tot = float((query_y['kelembaban__sum']))
    print('y_tot=',y_tot)

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('kelembaban')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    comp_tahun=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
   
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','kelembaban')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kelembaban')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kelembaban')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kelembaban')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kelembaban')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kelembaban')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kelembaban')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kelembaban')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kelembaban')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kelembaban')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kelembaban')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        

    y=''
    
    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
            print(im)
        elif bulan == 'Februari':
            print(im)
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kelembaban')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kelembaban')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kelembaban')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kelembaban')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kelembaban')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1



    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }

    return render(request,'kelembaban.html',context)

def kec_angin(request):
    posts = data_klimat.objects.all()
    
    form_field= FormField()
    #query mengambil sum id #mencari x-total 
    query_x = (data_klimat.objects.aggregate(Sum('id')))
    x_tot=int((query_x['id__sum']))

    #mencari x^2
    query_x2 = (data_klimat.objects.values_list('id')) 
    i=0 
    x2=0
    for j in query_x2:
        j=((int(query_x2[i][0])**2))
        x2+=j
        i+=1
    print('x**2=',x2)

    #query mengambil count id
    query_count = data_klimat.objects.annotate(Count('id')) 
    n=0
    for count in query_count:                               
        n+=1
    print('n=',n)
    
    #query mengambil sum y
    query_y = (data_klimat.objects.aggregate(Sum('kec_rata_angin')))
    y_tot = float((query_y['kec_rata_angin__sum']))
    print('y_tot=',y_tot)

    #x-bar y-bar
    x_bar=x_tot/n 
    y_bar = y_tot/n
    print('y bar =',y_bar)
    print('x bar =',x_bar)

    #mencari x.y
    tupId = data_klimat.objects.values_list('id')
    tupValue = data_klimat.objects.values_list('kec_rata_angin')
    i=0
    j=0
    xy=0
    for k in tupId:
        k=(float(tupId[i][0])*float(tupValue[j][0]))
        xy+=k
        i+=1
        j+=1
    print('x*y=',xy)

    #mencari b
    b1=(xy-(n*x_bar*y_bar))
    b2=(x2-(n*(x_bar**2)))
    b=b1/b2
    print('b=',b)

    #Mencari a
    a=(y_bar-(b*x_bar))
    print('a=',a)

     #mencari Y
    tahun=''
    bulan=''
    list_y=''
    list_bln=''
    bln=''
    comp_tahun=''
    list_comp_y=''
    list_comp_bln=''
    value_from_select=''
    compare_y=''
    compare_bln=''
    qs_compare=''
   
    if request.method =='POST':
        bulan=request.POST['input_bulan']
        tahun=request.POST['input_tahun']
        comp_tahun=request.POST['compTahun']
        if bulan != 'Semua Bulan':
            indeks=indeks_musiman.objects.filter(bulan=bulan).values_list('bulan','kec_rata_angin')
            im=float(indeks[0][1])
            bln=(indeks[0][0])
        if comp_tahun != '====':
            list_comp_bln=[0]
            list_comp_y=[0]
        if comp_tahun == '2014':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kec_rata_angin')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kec_rata_angin')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2015':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kec_rata_angin')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kec_rata_angin')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2016':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kec_rata_angin')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kec_rata_angin')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2017':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kec_rata_angin')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kec_rata_angin')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])

        if comp_tahun == '2018':
            j=0
            list_comp_bln=[]
            list_comp_y=[]
            if bulan == 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun).values_list('bulan','kec_rata_angin')
                for y in range(12):
                    compare_y = float((qs_compare[j][1]))
                    compare_bln = (qs_compare[j][0])
                    list_comp_y.append(compare_y)
                    list_comp_bln.append(compare_bln)
                    j+=1
            if bulan != 'Semua Bulan':
                qs_compare = data_klimat.objects.filter(tahun=comp_tahun, bulan=bulan).values_list('bulan','kec_rata_angin')
                compare_y = float((qs_compare[j][1]))
                compare_bln = (qs_compare[j][0])
    y=''
    
    if tahun == '2019':
        x_pred = 60
        if bulan =='Januari':
            x_pred =61
            y=((a+(b*x_pred))*im)/100
            print(im)
        elif bulan == 'Februari':
            print(im)
            x_pred =62
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =63
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =64
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =65
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =66
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =67
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =68
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =69
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =70
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =71
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =72
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kec_rata_angin')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2020':
        x_pred = 72
        if bulan =='Januari':
            x_pred =73
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =74
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =75
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =76
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =77
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =78
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =79
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =80
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =81
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =82
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =83
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =84
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kec_rata_angin')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2021':
        x_pred = 84
        if bulan =='Januari':
            x_pred =85
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =86
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =87
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =88
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =89
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =90
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =91
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =92
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =93
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =94
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =95
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =96
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kec_rata_angin')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2022':
        x_pred = 96
        if bulan =='Januari':
            x_pred =97
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =98
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =99
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =100
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =101
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =102
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =103
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =104
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =105
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =106
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =107
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =108
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kec_rata_angin')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1

    if tahun == '2023':
        x_pred = 108
        if bulan =='Januari':
            x_pred =109
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Februari':
            x_pred =110
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Maret':
            x_pred =111
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'April':
            x_pred =112
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Mei':
            x_pred =113
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juni':
            x_pred =114
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Juli':
            x_pred =115
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Agustus':
            x_pred =116
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'September':
            x_pred =117
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Oktober':
            x_pred =118
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'November':
            x_pred =119
            y=((a+(b*x_pred))*im)/100
        elif bulan == 'Desember':
            x_pred =120
            y=((a+(b*x_pred))*im)/100
        elif bulan =='Semua Bulan':
            indeks=indeks_musiman.objects.values_list('bulan','kec_rata_angin')
            z=0
            list_y = []
            list_bln = []
            for y in range(12):
                im=float(indeks[z][1])
                bln=(indeks[z][0])
                x_pred+=1
                y=((a+(b*x_pred))*im)/100
                list_y.append(y)
                list_bln.append(bln)
                z+=1



    context ={
        'Posts':posts,
        'Hasil':y,
        'Bulan':bln,
        'Tahun':tahun,
        'List_y':list_y,
        'List_bln':list_bln,
        'Bu':bulan,
        'List_comp_y':list_comp_y,
        'List_comp_bln':list_comp_bln,
        'List_comp_thn':comp_tahun,
        'Comp_y':compare_y,
        'Comp_bln':compare_bln,
    }

    return render(request,'kec_angin.html',context)

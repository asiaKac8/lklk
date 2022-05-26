from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.http import JsonResponse
from .models import PredictionResults
from django.contrib.auth.decorators import login_required

# udb 
from .models import Zbior
from .models import Atrybut
from .models import Dana
from .models import Obserwacja
from .models import Klasa

from .models import UniversalTableZbior
from .models import UniversalTableAtrybut
from .models import UniversalTable


# train model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd
import sqlite3


# strona glowna
def index(request):
    return render(request, 'index.html')




def wyborzbioru(request):
    # lista dostepnych zbiorow
    x = UniversalTableZbior.objects.all()
    lst = []
    for i in x:
        lst.append(i)

    data = {"dataset1": lst}
    return render(request, 'wyborzbioru.html', {'data':data})


def ile_atrybutow(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    nazwa_modelu = int(str(nazwa_modelu).split('.')[0])
    
    
    atrybuty = UniversalTableAtrybut.objects.filter(id_zbior=nazwa_modelu)
    lst1 = []
    for i in atrybuty[1:]:
        lst1.append(i)
    # lst1_len ile atrybutow ma zbior aby przekierowac do odpowiedniego formularza
    lst1_len = len(lst1)
    
    # nazwa zbioru wybranego w poprzednim ekranie
    nazwa = UniversalTableZbior.objects.filter(id_zbior=nazwa_modelu).first()
    nazwa = str(nazwa).split('. ')[1]

    if lst1_len == 2:
        link = "/args2/"
    elif lst1_len == 3:
        link = "/args3/"
    elif lst1_len == 4:
        link = "/args4/"
    elif lst1_len == 5:
        link = "/args5/"
    elif lst1_len == 6:
        link = "/args6/"
    elif lst1_len == 7:
        link = "/args7/"
    elif lst1_len == 8:
        link = "/args8/"
    elif lst1_len == 9:
        link = "/args9/"

    print()
    print()
    print('nazwa zbioru:',nazwa)
    print('liczba atrybutow:',lst1_len)
    print(link)

    data = {"nazwa": nazwa, "lst1_len": lst1_len, "link": link}

    return render(request, 'ile_atrybutow.html', {'data':data})





### predykcja dla roznej ilosci argumentow (formularze)
def args2(request):
    #?nazwa_modelu=
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    # musimy znalezc id zbioru do torego naleza atrybuty w bazie danych
    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1]}
    return render(request, 'args2.html',{'data':data})




def args2_name(request):
    return render(request, 'args2_name.html')
def args3_name(request):
    return render(request, 'args3_name.html')
def args4_name(request):
    return render(request, 'args4_name.html')
def args5_name(request):
    return render(request, 'args5_name.html')
def args6_name(request):
    return render(request, 'args6_name.html')
def args7_name(request):
    return render(request, 'args7_name.html')
def args8_name(request):
    return render(request, 'args8_name.html')
def args9_name(request):
    return render(request, 'args9_name.html')









def args2_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':

        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))

        #model = pd.read_pickle(r"new_model.pickle")
        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2},safe=False)


def args3(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2]}
    return render(request, 'args3.html',{'data':data})

def args3_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':

        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))

        #model = pd.read_pickle(r"new_model.pickle")
        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2, a3]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3},safe=False)


def args4(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3]}
    return render(request, 'args4.html',{'data':data})

def args4_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))

        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2, a3, a4]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4},safe=False)



def args5(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4]}
    return render(request, 'args5.html',{'data':data})

def args5_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))

        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2, a3, a4, a5]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5},safe=False)



def args6(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5]}
    return render(request, 'args6.html',{'data':data})

def args6_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))

        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2, a3, a4, a5, a6]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6},safe=False)

def args7(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5],"a7":args_lst[6]}
    return render(request, 'args7.html',{'data':data})

def args7_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))
        a7 = float(request.POST.get('a7'))

        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2, a3, a4, a5, a6, a7]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6,'a7':a7},safe=False)


def args8(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5],"a7":args_lst[6],"a8":args_lst[7]}
    return render(request, 'args8.html',{'data':data})

def args8_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))
        a7 = float(request.POST.get('a7'))
        a8 = float(request.POST.get('a8'))

        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2, a3, a4, a5, a6, a7, a8]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6,'a7':a7,'a8':a8},safe=False)


def args9(request):
    nazwa_modelu = request.GET.get('nazwa_modelu')
    request.session['nazwa_modelu'] = nazwa_modelu

    jakie_id_zbioru = UniversalTableZbior.objects.filter(nazwa=nazwa_modelu).values_list(flat = True)
    dataset1 = UniversalTableAtrybut.objects.filter(id_zbior=jakie_id_zbioru[0])

    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)

    data = {"nazwa_modelu": nazwa_modelu, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5],"a7":args_lst[6],"a8":args_lst[7],"a9":args_lst[8]}
    return render(request, 'args9.html',{'data':data})

def args9_chances(request):
    nazwa_modelu = request.session.get('nazwa_modelu')
    nazwa_modelu1 = nazwa_modelu+'_model.pickle'

    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))
        a7 = float(request.POST.get('a7'))
        a8 = float(request.POST.get('a8'))
        a9 = float(request.POST.get('a9'))

        model = pd.read_pickle(nazwa_modelu1)
        result = model.predict([[a1, a2, a3, a4, a5, a6, a7, a8, a9]])
        classification = result[0]

        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6,'a7':a7,'a8':a8,'a9':a9},safe=False)
                             
                            


#===============================================================================================================

def choice_name_import_csv(request):
    return render(request, 'choice_name_import_csv.html')


from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neural_network import MLPClassifier

def import_csv(request):
    # http://127.0.0.1:8000/iris_import/?nazwa_zbioru=c
    # to bylo
    nazwa_zbioru = request.GET.get('nazwa_zbioru')

    # to dodane
    nazwa_modelu = request.GET.get('nazwa_modelu')



    if request.method == 'POST':
        new_csv = request.FILES['importData']
        df = pd.read_csv(new_csv)
        #print(df)

        con = sqlite3.connect("db.sqlite3")
        dfcolumns = list(df.columns)

        ### zbior
        z = UniversalTableZbior(nazwa=nazwa_zbioru)
        z.save()

        ### atrybuty
        for i in range(len(dfcolumns)):
            a = UniversalTableAtrybut(id_zbior=z, nazwa=dfcolumns[i])
            a.save()

        if len(dfcolumns) == 3:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2])
                d.save()
                #print(d)

        if len(dfcolumns) == 4:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3])
                d.save()
                #print(d)

        if len(dfcolumns) == 5:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4])
                d.save()
                #print(d)

        if len(dfcolumns) == 6:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5])
                d.save()
                #print(d)

        if len(dfcolumns) == 7:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6])
                d.save()
                #print(d)
        
        if len(dfcolumns) == 8:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6],
                    a7=df.values[row][7])
                d.save()
                #print(d)

        if len(dfcolumns) == 9:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6],
                    a7=df.values[row][7],
                    a8=df.values[row][8])
                d.save()
                #print(d)

        if len(dfcolumns) == 10:
            for row in range(len(df.values)):
                d = UniversalTable(id_zbior=z, 
                    c1=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6],
                    a7=df.values[row][7],
                    a8=df.values[row][8],
                    a9=df.values[row][9])
                d.save()
                #print(d)
 

        ### uczenie
        col_names = []
        for (columnName, columnData) in df.iteritems():
            col_names.append(columnName)

        col_namesX = col_names[1:]
        col_namesY = col_names[0]

        X = df[col_namesX]
        y = df[col_namesY]
        
        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)



        if nazwa_modelu == 'svm':
            model = SVC(gamma='auto')
        elif nazwa_modelu == 'knn':
            model = KNeighborsClassifier(n_neighbors=3)
        elif nazwa_modelu == 'nb':
            model = GaussianNB()
        elif nazwa_modelu == 'tree':
            model = tree.DecisionTreeClassifier()
        elif nazwa_modelu == 'nn':
            model = MLPClassifier()
        else:
            model = SVC(gamma='auto')

        model.fit(X_train, Y_train)

        #pd.to_pickle(model,r'new_model2.pickle')
        nazwa_pickle = str(nazwa_zbioru) + '_model.pickle'
        pd.to_pickle(model,nazwa_pickle)

        con.close()
        print('zaimportowano')

    print()
    print()
    print()
    print(nazwa_zbioru)
    print(nazwa_modelu)

    return render(request, 'import_csv.html')







def import_csv_message(request):
    #request.session['nazwa_zbioru'] = nazwa_zbioru
    '''
    nazwa_zbioru = request.POST["form"]
    data = {"nazwa_zbioru": nazwa_zbioru}
    return render(request, 'import_csv_message.html', {'data':data})
    '''
    #return HttpResponse("Zaimportowano")
    return render(request, 'import_csv_message.html')
    


def testcss(request):

    data = {"dataset1": UniversalTableZbior.objects.all().iterator(),
            "dataset2": UniversalTable.objects.all().iterator(),
            "dataset3": UniversalTableAtrybut.objects.all().iterator()}
    
    return render(request, "testcss.html",{'data':data})






def form_choice(request):

    return render(request, 'form_choice.html')










# test (narazie nidzie nie uzywane)
def import_csv1(request):
    # http://127.0.0.1:8000/iris_import/?nazwa_zbioru=c
    nazwa_zbioru = request.GET.get('nazwa_zbioru')
    #nazwa_zbioru = 'aaa'


    if request.method == 'POST':
        new_csv = request.FILES['importData']
        df = pd.read_csv(new_csv)
        #print(df)


        
        con = sqlite3.connect("db.sqlite3")

        ### nazwy kolumn w df
        dfcolumns = list(df.columns)

        
        ### zbior
        z = Zbior(nazwa=nazwa_zbioru)
        z.save()

        ### atrybut
        '''
        for i in dfcolumns:
            a = Atrybut(id_zbior=z, nazwa=i)
            #a.save()
        '''

        # wartosci: print(df.values)
        
        ### klasa_lst
        klasa_lst = []
        for i in df.values:
            klasa_lst.append(i[-1])

        kolumny_lst = []
        for r in range(len(dfcolumns)):
            tmp = []
            for i in df.values:
                tmp.append(i[r])
            kolumny_lst.append(tmp)
        #print(kolumny_lst[:-1])

        counter = 0
        for row in df.values:
            k = Klasa(nazwa=klasa_lst[counter])
            k.save()
            counter += 1

            o = Obserwacja(id_klasa=k)
            o.save()
            counter2 = 0
            for v in row[:-1]:
                a = Atrybut(id_zbior=z, nazwa=dfcolumns[counter2])
                a.save()
                counter2 += 1
                
                d = Dana(id_obserwacja=o, id_atrybut=a, wartosc=v)
                d.save()
        

        ### uczenie

        col_names = []
        for (columnName, columnData) in df.iteritems():
            col_names.append(columnName)

        col_namesX = col_names[:-1]
        col_namesY = col_names[-1]
        
        X = df[col_namesX]
        y = df[col_namesY]
        
        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

        model = SVC(gamma='auto')
        model.fit(X_train, Y_train)

        #pd.to_pickle(model,r'new_model2.pickle')
        nazwa_pickle = str(nazwa_zbioru) + '_model.pickle'
        pd.to_pickle(model,nazwa_pickle)
        


        print()
        con.close()
    return render(request, 'import_csv.html')
    















### IRIS
def predict(request):
    return render(request, 'predict.html')

def predict_chances(request):

    if request.POST.get('action') == 'post':

        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        #model = pd.read_pickle(r"new_model.pickle")
        model = pd.read_pickle(r"new_model.pickle")
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        classification = result[0]

        PredictionResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification)

        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)


# iris istoria wprowadzanych danych
def iris_view_results(request):
    data = {"dataset": PredictionResults.objects.all()}
    return render(request, "iris_results.html", data)


# iris import export
from tablib import Dataset
from .resources import IrisImportExportResource
from .models import IrisImportExport

def iris_import_data(request):
    # http://127.0.0.1:8000/iris_import/?nazwa_zbioru=c
    #nazwa_zbioru = request.GET.get('nazwa_zbioru')

    if request.method == 'POST':
        file_format = request.POST['file-format']
        iris_resource = IrisImportExportResource()
        dataset = Dataset()
        new_iris = request.FILES['importData']


        if file_format == 'CSV':
            imported_data = dataset.load(new_iris.read().decode('utf-8'),format='csv')

            #print(imported_data)
            #print(imported_data[-1][:])
            #print(imported_data.headers)
            #print(imported_data[0][0])

            '''
            con = sqlite3.connect("db.sqlite3")

            
            print()
            nazwa_zbioru = 'titanic'
            # zbior
            z = Zbior(nazwa=nazwa_zbioru)
            z.save()

            
            # atrybut lista
            atrybut_lst = []
            for i in imported_data.headers[:-1]:
                a = Atrybut(id_zbior=z, nazwa=i)
                a.save()
                atrybut_lst.append(i)
            #print(atrybut_lst)


            # klasa lista
            klasa_lst = []
            for j in imported_data:
                klasa_lst.append(j[-1])
            #print(klasa_lst)

            # zaimportowanie csv jako df (tu od razu mozna zrobic uczenie)
            columns_lst = []
            for i in imported_data.headers:
                #a = Atrybut(id_zbior=z, nazwa=i)
                #a.save()
                columns_lst.append(i)
            data = [imported_data[f] for f in range(len(klasa_lst))]
            df = pd.DataFrame(data, columns = columns_lst)
            print(df)

            print()
            print()

            #print(df.values)


            # wprowadzenie danych do bazy
            print()
            for row in df.values:
                #print(row)
                print()
                for v in row[:-1]:
                    print(v)
                print(row[-1])
            print()


            counter = 0
            for row in df.values:
                k = Klasa(nazwa=klasa_lst[counter])
                k.save()
                counter += 1

                o = Obserwacja(id_klasa=k)
                o.save()
                counter2 = 0
                for v in row[:-1]:
                    a = Atrybut(id_zbior=z, nazwa=atrybut_lst[counter2])
                    a.save()
                    counter2 += 1
                    
                    d = Dana(id_obserwacja=o, id_atrybut=a, wartosc=v)
                    d.save()
            
            print()
            con.close()
            '''

            result = iris_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            imported_data = dataset.load(new_iris.read().decode('utf-8'),format='json')
            result = iris_resource.import_data(dataset, dry_run=True)
            
        if not result.has_errors():
            iris_resource.import_data(dataset, dry_run=False)

    return render(request, 'iris_import.html')


def iris_export_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        iris_resource = IrisImportExportResource()
        dataset = iris_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'iris_export.html')


# iris imported
def iris_imported(request):
    # Submit prediction and show all
    data = {"dataset": IrisImportExport.objects.all()}
    return render(request, "iris_imported.html", data)


def iris_train_model(request):
    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect("db.sqlite3")
    df = pd.read_sql_query("SELECT * from predict_irisimportexport", con)
    con.close()

    X = df[['sepal_length','sepal_width','petal_length','petal_width']]
    y = df['classification']
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    model = SVC(gamma='auto')
    model.fit(X_train, Y_train)

    predictions = model.predict(X_test)

    pd.to_pickle(model,r'new_model.pickle')

    #html = "<html><body> Model created </body></html>"
    #return HttpResponse(html)
    return render(request, 'iris_train_model.html')



### UDB

def udb(request):
    data = {"dataset1": Zbior.objects.all().iterator(),
            "dataset2": Klasa.objects.all().iterator(),
            "dataset3": Atrybut.objects.all().iterator(),
            "dataset4": Obserwacja.objects.all().iterator(),
            "dataset5": Dana.objects.all().iterator()}

    return render(request, 'udb.html',{'data':data})


# udbdf
def udbdf(request):
    con = sqlite3.connect("db.sqlite3")

    #nr_zbioru = 1
    # aby zobaczyc  zbior nr 1 w przegladarce trzeba wpisac:
    # http://127.0.0.1:8000/test/?id=1
    # /?id=1 - jest to metoda get, mozemy zmieniac 1 np. na 2 
    nr_zbioru = request.GET.get('id')

    # ile obserwacji w zbiorze nr 1
    select2 = '''SELECT predict_obserwacja.id_obserwacja
        FROM predict_obserwacja INNER JOIN predict_dana 
        ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
        INNER JOIN predict_atrybut ON predict_atrybut.id_atrybut = predict_dana.id_atrybut_id
        INNER JOIN predict_zbior ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
        WHERE predict_zbior.id_zbior='''+str(nr_zbioru)

    x1 = pd.read_sql_query(select2, con)
    x2 = x1.values.tolist()
    x3 = []
    for m in x2:
        for n in m:
            x3.append(n)
    #x4 = max(x3)   
    
    try:
        x4 = max(x3)
    except:
        #return HttpResponse('Nie ma zbioru o takim numerze!')
        return render(request, 'error404.html')


    # wiersze w tworzonym df
    rows = []
    rows_add = []
    for i in range(1,x4+1):
        # select do zmiennych niezaleznych - do zapisania w wierszu w df
        select1 = '''SELECT predict_dana.wartosc
            FROM predict_obserwacja INNER JOIN predict_klasa ON predict_klasa.id_klasa = predict_obserwacja.id_klasa_id
            INNER JOIN predict_dana ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
            INNER JOIN predict_atrybut ON predict_atrybut.id_atrybut = predict_dana.id_atrybut_id
            INNER JOIN predict_zbior ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
            WHERE predict_zbior.id_zbior='''+str(nr_zbioru)+' AND id_obserwacja='+str(i)
        
        # select do zmiennych zaleznych - do doklejenia do wiersza w df
        select2 = '''SELECT predict_klasa.nazwa
            FROM predict_obserwacja INNER JOIN predict_klasa ON predict_klasa.id_klasa = predict_obserwacja.id_klasa_id
            INNER JOIN predict_dana ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
            INNER JOIN predict_atrybut ON predict_atrybut.id_atrybut = predict_dana.id_atrybut_id
            INNER JOIN predict_zbior ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
            WHERE predict_zbior.id_zbior='''+str(nr_zbioru)+' AND id_obserwacja='+str(i)

        rows1 = pd.read_sql_query(select1, con)
        rows2 = rows1.values.tolist()
        rows3 = []
        for o in rows2:
            for p in o:
                rows3.append(p)
        if rows3:
            rows.append(rows3)

        #print(rows)

        rows_add1 = pd.read_sql_query(select2, con)
        rows_add2 = rows_add1.values.tolist()
        rows_add3 = []
        for m in rows_add2:
            for n in m:
                rows_add3.append(n)
        
        if rows_add3:
            rows_add.append(rows_add3)

    for elem in range(len(rows)):
        rows[elem].append(rows_add[elem][0])



    # nazwy kolumn do df
    select3 = '''SELECT predict_atrybut.nazwa
        FROM predict_atrybut INNER JOIN predict_zbior
        ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
        WHERE id_zbior='''+str(nr_zbioru)

    col1 = pd.read_sql_query(select3, con)
    col2 = col1.values.tolist()
    col3 = []
    for v in col2:
        for b in v:
            col3.append(b)
    col3.append('klasa')
    #print(col3)

    DataFrame = pd.DataFrame(rows, columns = col3)
    #print(DataFrame)
    html = DataFrame.to_html()

    con.close()
    return HttpResponse(html)



def udbchoice(request):
    return render(request, 'udbchoice.html')


# to chyba dzialalo w poprzednich wersjach, a teraz troce inaczej wyglada
def train_model(request):
    con = sqlite3.connect("db.sqlite3")

    nr_zbioru = request.GET.get('id')

    # ile obserwacji w zbiorze nr 1
    select2 = '''SELECT predict_obserwacja.id_obserwacja
        FROM predict_obserwacja INNER JOIN predict_dana 
        ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
        INNER JOIN predict_atrybut ON predict_atrybut.id_atrybut = predict_dana.id_atrybut_id
        INNER JOIN predict_zbior ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
        WHERE predict_zbior.id_zbior='''+str(nr_zbioru)

    x1 = pd.read_sql_query(select2, con)
    x2 = x1.values.tolist()
    x3 = []
    for m in x2:
        for n in m:
            x3.append(n)
    x4 = max(x3)

    # wiersze w tworzonym df
    rows = []
    rows_add = []
    for i in range(1,x4+1):
        # select do zmiennych niezaleznych - do zapisania w wierszu w df
        select1 = '''SELECT predict_dana.wartosc
            FROM predict_obserwacja INNER JOIN predict_klasa ON predict_klasa.id_klasa = predict_obserwacja.id_klasa_id
            INNER JOIN predict_dana ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
            INNER JOIN predict_atrybut ON predict_atrybut.id_atrybut = predict_dana.id_atrybut_id
            INNER JOIN predict_zbior ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
            WHERE predict_zbior.id_zbior='''+str(nr_zbioru)+' AND id_obserwacja='+str(i)
        
        # select do zmiennych zaleznych - do doklejenia do wiersza w df
        select2 = '''SELECT predict_klasa.nazwa
            FROM predict_obserwacja INNER JOIN predict_klasa ON predict_klasa.id_klasa = predict_obserwacja.id_klasa_id
            INNER JOIN predict_dana ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
            INNER JOIN predict_atrybut ON predict_atrybut.id_atrybut = predict_dana.id_atrybut_id
            INNER JOIN predict_zbior ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
            WHERE predict_zbior.id_zbior='''+str(nr_zbioru)+' AND id_obserwacja='+str(i)

        rows1 = pd.read_sql_query(select1, con)
        rows2 = rows1.values.tolist()
        rows3 = []
        for o in rows2:
            for p in o:
                rows3.append(p)
        if rows3:
            rows.append(rows3)
        #print(rows)

        rows_add1 = pd.read_sql_query(select2, con)
        rows_add2 = rows_add1.values.tolist()
        rows_add3 = []
        for m in rows_add2:
            for n in m:
                rows_add3.append(n)
        
        if rows_add3:
            rows_add.append(rows_add3)

    for elem in range(len(rows)):
        rows[elem].append(rows_add[elem][0])

    # nazwy kolumn do df
    select3 = '''SELECT predict_atrybut.nazwa
        FROM predict_atrybut INNER JOIN predict_zbior
        ON predict_atrybut.id_zbior_id = predict_zbior.id_zbior
        WHERE id_zbior='''+str(nr_zbioru)

    col1 = pd.read_sql_query(select3, con)
    col2 = col1.values.tolist()
    col3 = []
    for v in col2:
        for b in v:
            col3.append(b)
    col3.append('klasa')

    df = pd.DataFrame(rows, columns = col3)

    col_names = []
    for (columnName, columnData) in df.iteritems():
        #print(columnName)
        col_names.append(columnName)

    col_namesX = col_names[:-1]
    col_namesY = col_names[-1]

    X = df[col_namesX]
    y = df[col_namesY]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    model = SVC(gamma='auto')
    model.fit(X_train, Y_train)

    pd.to_pickle(model,r'new_model1.pickle')

    con.close()
    return HttpResponse('Model created')


# udb import plikow csv
def import_data(request):
    #con = sqlite3.connect("db.sqlite3")
    

    #con.close()
    return render(request, "import_data.html")




### INNE



def classification(request):
    #con = sqlite3.connect("db.sqlite3")
    #con.close()
    return render(request, "classification.html")

# dforms
'''
from .forms import MyForm

def myview(request):
    if request.method == 'POST':
        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print ("valid!")
    else:
        form = MyForm()
    return render(request, "template", { 'form': form })
'''

def error404(request):
    return render(request, 'error404.html')


#rejestracja

from .forms import MyRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout



def register(request):
    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           messages.success(request, 'Pomyślnie utworzono konto')

           return redirect('/login')
    
    form = MyRegisterForm()
    return render(
        request=request,
        template_name='register.html',
        context={
            'form': form
        }
    ) 

#login

def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/choice_name_import_csv')
        else:
            messages.info(request, 'E-mail lub hasło nie jest prawidłowy')
                
                

            
    form = AuthenticationForm()

    return render(
        request=request,
        template_name='login.html',
        context={
            'form': form
        } 
    )

@login_required(login_url='/login/')
def panel(request):
    return render(
        request=request,
        template_name='panel.html'
    )


#wylogowywanie

def logoutUser(request):
    logout(request)
    return redirect('/')















from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.http import JsonResponse
import pandas as pd
from platformdirs import user_runtime_dir
from .models import PredictionResults
from django.contrib.auth.decorators import login_required



def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        model = pd.read_pickle(r"new_model.pickle")
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        classification = result[0]

        PredictionResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification)

        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)


def iris_view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredictionResults.objects.all()}
    return render(request, "iris_results.html", data)


# strona glowna
def index(request):
    return render(request, 'index.html')



### udb 
from .models import Zbior
from .models import Atrybut
from .models import Dana
from .models import Obserwacja
from .models import Klasa

def udb(request):
    data = {"dataset1": Zbior.objects.all().iterator(),
            "dataset2": Klasa.objects.all().iterator(),
            "dataset3": Atrybut.objects.all().iterator(),
            "dataset4": Obserwacja.objects.all().iterator(),
            "dataset5": Dana.objects.all().iterator()}

    return render(request, 'udb.html',{'data':data})



# iris import export
from tablib import Dataset
from .resources import IrisImportExportResource
from .models import IrisImportExport


def iris_import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        iris_resource = IrisImportExportResource()
        dataset = Dataset()
        new_iris = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_iris.read().decode('utf-8'),format='csv')
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


# train model from imported iris db
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd
import sqlite3

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


# test1
# testowanie, mozna wkorzystac od ponizej do widoku (ktory jest pod tym widokiem)
def test1(request):
    con = sqlite3.connect("db.sqlite3")

    # tworzenie rekordow do DataFrame
    data1 = pd.read_sql_query("SELECT wartosc from predict_dana", con)
    numDataInRow = Atrybut.objects.all().count()
    numData = Dana.objects.all().count()
    numOfIter = numData // numDataInRow
    
    tab =[]
    counter = -1
    for i in range(numOfIter):
        tab1 = []
        for j in range(numDataInRow):
            counter += 1 
            tab1.append(data1.loc[counter,:].values.flatten().tolist())
        tab.append(tab1)
    
    flat_list = []
    for sublist in tab:
        for sublist2 in sublist:
            for sublist3 in sublist2:
                flat_list.append(sublist3)
    
    counter2 = -1
    rows = []
    for i in range(numOfIter):
        tab2 = []
        for j in range(numDataInRow):
            counter2 += 1 
            tab2.append(flat_list[counter2])
        rows.append(tab2)


    # tworzenie kolumn do DataFrame
    col1 = pd.read_sql_query("SELECT nazwa from predict_atrybut", con)
    col2 = col1.values.tolist()

    col = []
    for o in col2:
        for p in o:
            col.append(p)

    DataFrame = pd.DataFrame(rows, columns = col)
    html = DataFrame.to_html()


    select01 = '''SELECT predict_dana.wartosc, predict_obserwacja.id_obserwacja 
        FROM predict_obserwacja INNER JOIN predict_dana 
        ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
        WHERE id_obserwacja=1'''

    select02 = '''SELECT "predict_dana"."wartosc", "predict_obserwacja"."id_obserwacja"
        FROM "predict_obserwacja" INNER JOIN "predict_dana" 
        ON "predict_obserwacja"."id_obserwacja" = "predict_dana"."id_obserwacja_id"
        WHERE id_obserwacja=1'''

    select1 = '''SELECT predict_dana.wartosc, predict_obserwacja.id_obserwacja, predict_atrybut.nazwa
        FROM predict_obserwacja INNER JOIN predict_dana 
        ON predict_obserwacja.id_obserwacja = predict_dana.id_obserwacja_id
        INNER JOIN predict_atrybut
        ON predict_atrybut.id_atrybut = predict_dana.id_atrybut_id'''

    print()
    print(html)
    print(pd.read_sql_query(select1, con))
    print()

    con.close()
    #render(request, 'test.html', {'DataFrame': DataFrame })
    #render(request, 'test.html', {'DataFrame': html})
    return HttpResponse(html)



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
    #print(col3)

    DataFrame = pd.DataFrame(rows, columns = col3)
    #print(DataFrame)
    html = DataFrame.to_html()

    con.close()
    return HttpResponse(html)




def udbchoice(request):
    return render(request, 'udbchoice.html')




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



def testcss(request):

    return render(request, "testcss.html")



# udb import pliow csv
@login_required(login_url='/login/')
def import_data(request):
    #con = sqlite3.connect("db.sqlite3")
    

    #con.close()
    return render(request, "import_data.html")


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
                return redirect('/prediction_page')
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










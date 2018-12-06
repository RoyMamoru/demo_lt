from django.shortcuts import render, redirect
from .forms import InputForm
from datetime import date
from .models import Customers
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# グローバル変数としてモデルをロード
# loaded_model = pickle.load(open('demo_app/model.pkl', 'rb'))
loaded_model = pickle.load(open('/home/roynishizawa/roynishizawa.pythonanywhere.com/demo_app/model.pkl', 'rb'))

# Create your views here.
def index(request):
    return render(request, 'demo_app/index.html', {})

# 自前で書いたForm
def input(request):
    return render(request, 'demo_app/input.html', {})

# Form画面
def input_form(request):
    if request.method == "POST":
        form = InputForm(request.POST) # 入力データの取得
        if form.is_valid(): # Formの記載の検証
            data = form.cleaned_data # 入力データの取得（辞書型で取得する事が可能）
            data_keys = list(data.keys()) # 辞書のKeyのリストを取得
            # モデルをインスタンス化し、値を渡す
            register = Customers.objects.create(\
                last_name=data['last_name'],\
                first_name=data['first_name'],\
                limit_balance=form.cleaned_data['limit_balance'],\
                sex=form.cleaned_data['sex'],\
                education=form.cleaned_data['education'],\
                marriage=form.cleaned_data['marriage'],\
                age=form.cleaned_data['age'],\
                pay_0=form.cleaned_data['pay_0'],\
                pay_2=form.cleaned_data['pay_2'],\
                pay_3=form.cleaned_data['pay_3'],\
                pay_4=form.cleaned_data['pay_4'],\
                pay_5=form.cleaned_data['pay_5'],\
                pay_6=form.cleaned_data['pay_6'],\
                bill_amt_1=form.cleaned_data['bill_amt_1'],\
                pay_amt_1=form.cleaned_data['pay_amt_1'],\
                pay_amt_2=form.cleaned_data['pay_amt_2'],\
                pay_amt_3=form.cleaned_data['pay_amt_3'],\
                pay_amt_4=form.cleaned_data['pay_amt_4'],\
                pay_amt_5=form.cleaned_data['pay_amt_5'],\
                pay_amt_6=form.cleaned_data['pay_amt_6'],
                )
            register.proba = 0.0 # 必須項目である「proba」の値を仮置き
            register.registered_date = date.today()
            register.save() # 入力データをDBに保存
            print('save scceed')
            return redirect('result') # resultの関数の実行
    else:
        form = InputForm()
        return render(request, 'demo_app/input_form.html', {'form':form})


def result(request):
    new_id = len(Customers.objects.all()) -1 # 最新の登録のIDを取得
    _data = Customers.objects.order_by('id')[new_id] # 該当データを取得
    # それぞれの値を変数に格納に入力データ作成
    limit_balance=_data.limit_balance
    sex=_data.sex
    education=_data.education
    marriage=_data.marriage
    age=_data.age
    pay_0=_data.pay_0
    pay_2=_data.pay_2
    pay_3=_data.pay_3
    pay_4=_data.pay_4
    pay_5=_data.pay_5
    pay_6=_data.pay_6
    bill_amt_1=_data.bill_amt_1
    pay_amt_1=_data.pay_amt_1
    pay_amt_2=_data.pay_amt_2
    pay_amt_3=_data.pay_amt_3
    pay_amt_4=_data.pay_amt_4
    pay_amt_5=_data.pay_amt_5
    pay_amt_6=_data.pay_amt_6

    # 推論
    x = [limit_balance, sex, education, marriage, age, pay_0, pay_2, pay_3, pay_4, pay_5, pay_6, bill_amt_1, pay_amt_1, pay_amt_2, pay_amt_3, pay_amt_4, pay_amt_5,pay_amt_6]
    y = loaded_model.predict(np.array([x])) # 推論
    _y_proba = loaded_model.predict_proba(np.array([x])) # 確率の推論
    y_proba = _y_proba * 100

    # 結果に基づいてコメントを返す
    if y[0] == 0:
        if y_proba[0][y[0]] > 75:
            comment = 'この方への貸し出しは危険です'
        else:
            comment = 'この方への貸し出しは要検討です'
    else:
        if y_proba[0][y[0]] > 75:
            comment = 'この方への貸し出しは全く問題ありません'
        else:
            comment = 'この方への貸し出しは問題ないでしょう'

    # 推論結果をDBに上書き
    _data.proba = _y_proba[0][y[0]]
    _data.result = y[0]
    _data.comment = comment
    _data.save()

    return render(request, 'demo_app/result.html', {'y':y[0], 'y_proba':round(y_proba[0][y[0]], 2), 'comment':comment}) # 確率は結果を元に自信度を表示する：結果が1番目の場合, 確率は1番目になる

def history(request):
    customers = Customers.objects.all()
    return render(request, 'demo_app/history.html', {'customers':customers})

def delete(request):
    if request.method == 'POST':
        d_id = request.POST
        d_customer = Customers.objects.filter(id=d_id['d_id'])
        d_customer.delete()
        customers = Customers.objects.all()
        return render(request, 'demo_app/history.html', {'customers':customers})
    else:
        customers = Customers.objects.all()
        return render(request, 'demo_app/history.html', {'customers':customers})

from contract import *

s3_Path = "https://s3.ap-northeast-2.amazonaws.com/dogeproject/"

# Session으로 alertMsg가 넘어올 경우 메시지를 제공하는 함수.
def saveAlert(context, request):
    try:
        context['alertMsg'] = request.session.pop('alertMsg')
    except:
        pass
    return context

# form의 서명을 확인하는 함수.
def isSignedForm(form, address):
    if checkSign(form.cleaned_data['sigData'], address):
        del form.fields['sigData']
        return True
    return False
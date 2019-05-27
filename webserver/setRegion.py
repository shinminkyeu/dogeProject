import os
import django
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
django.setup()
from trade.models import RegionTable

class regionClass :
    def __init__(self, _stepone, _steptwo):
        self.stepone = _stepone
        self.steptwo = _steptwo                   #0,소형,1:중형,2:대형

seoul_list = ['종로구','중구','용산구','성동구','광진구','동대문구','중랑구','성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구','구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구']
busan_list = ['중구','서구','동구','영도구','부산진구','동래구','남구','북구','해운대구','사하구','금정구','강서구','연제구','수영구','사상구','기장군']
daegu_list = ['중구','동구''서구','남구','북구','수성구','달서구','달성군']
incheon_list = ['중구','동구','남구','연수구','남동구','부평구','계양구','서구','강화군','옹진군']
gwangju_list = ['동구','서구','남구','북구','광산구']
daejeon_list = ['동구','중구','서구','유성구','대덕구']
ulsan_list = ['중구','남구','동구','북구','울주군']
sejong_list = ['']
gyeonggi_list = ['수원시','성남시','고양시','용인시','부천시','안산시','안양시','남양주시','화성시','평택시','의정부시','시흥시','파주시','광명시','김포시','군포시','광주시','이천시','양주시','오산시','구리시','안성시','포천시','의왕시','하남시','여주시','양평군','동두천시','과천시','가평군','연천군']
gangwon_list = ['춘천시','원주시','강릉시','동해시','태백시','속초시','삼척시','홍천군','횡성군','영월군','평창군','정선군','철원군','화천군','양구군','인제군','고성군','양양군',]
Chungcheongbuk_list = ['청주시','충주시','제천시','보은군','옥천군','영동군','진천군','괴산군','음성군','단양군','증평군']
Chungcheongnam_list = ['천안시','공주시','보령시','아산시','서산시','논산시','계룡시','당진시','금산군','부여군','서천군','청양군','홍성군','예산군','태안군']
jeonbuk_list = ['전주시','군산시','익산시','정읍시','남원시','김제시','완주군','진안군','무주군','장수군','임실군','순창군','고창군','부안군']
jeonnam_list = ['목포시','여수시','순천시','나주시','광양시','담양군','곡성군','구례군','고흥군','보성군','화순군','장흥군','강진군','해남군','영암군','무안군','함평군','영광군','장성군','완도군','진도군','신안군']
gyeongbuk_list = ['포항시','경주시','김천시','안동시','구미시','영주시','영천시','상주시','문경시','경산시','군위군','의성군','청송군','영양군','영덕군','청도군','고령군','성주군','칠곡군','예천군','봉화군','울진군','울릉군']
gyeongnam_list = ['창원시','진주시','통영시','사천시','김해시','밀양시','거제시','양산시','의령군','함안군','창녕군','고성군','남해군','하동군','산청군','함양군','거창군','합천군']
jeju_list = ['제주시','서귀포시']

def setTable() :
    b_list = []
    for each in seoul_list:
        b_list.append(regionClass("서울시", each))
    for each in busan_list:
        b_list.append(regionClass("부산", each))
    for each in daegu_list:
        b_list.append(regionClass("대구", each))
    for each in incheon_list:
        b_list.append(regionClass("인천", each))
    for each in gwangju_list:
        b_list.append(regionClass("광주", each))
    for each in daejeon_list:
        b_list.append(regionClass("대전", each))
    for each in ulsan_list:
        b_list.append(regionClass("울산", each))
    for each in sejong_list:
        b_list.append(regionClass("세종", each))
    for each in gyeonggi_list:
        b_list.append(regionClass("경기도", each))
    for each in gangwon_list:
        b_list.append(regionClass("강원도", each))
    for each in Chungcheongbuk_list:
        b_list.append(regionClass("충청북도", each))
    for each in Chungcheongnam_list:
        b_list.append(regionClass("충청남도", each))
    for each in jeonbuk_list:
        b_list.append(regionClass("전라북도", each))
    for each in jeonnam_list:
        b_list.append(regionClass("전라남도", each))
    for each in gyeongbuk_list:
        b_list.append(regionClass("경상북도", each))
    for each in gyeongnam_list:
        b_list.append(regionClass("경상남도", each))
    for each in jeju_list:
        b_list.append(regionClass("제주도", each))
    return b_list

if __name__=='__main__':
    regionList = setTable()
    for each in regionList :
        RegionTable(stepOne=each.stepone, stepTwo=each.steptwo).save()


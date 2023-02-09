from urllib.parse import urlencode, unquote, quote_plus
import json
import urllib.request
from urllib.request import urlopen , Request

def barcode_scan(BRCD_NO):
    keyId = '3584007bcb4342839eff'  #인증키(필수)
    serviceId = 'I2570'             #서비스명(필수)
    dataType = 'json'               #요청파일 타입(필수)
    startIdx = '1'                  #요청시작위치(필수)
    endIdx = '5'                    #요청종료위치(필수)
    #CHNG_DT = '20170101'           #변경일자(선택)
    #PRDLST_REPORT_NO = ''          #품목제조보고번호(선택)
    #PRDT_NM = ''                   #제품명(선택)
    #BRCD_NO = ''                   #바코드번호(선택) 다만 바코드번호로 검색하기때문에 무조건 들어가야하는 파라미터
    #BRCD_NO = '8809360172547'      #테스트용 '황금빛하늘내린황태포5미370g'

    #test
    testurl1 = 'http://openapi.foodsafetykorea.go.kr/api/3584007bcb4342839eff/I2570/xml/1/5/BRCD_NO=8809360172547' #황태포
    testurl2 = 'http://openapi.foodsafetykorea.go.kr/api/3584007bcb4342839eff/I2570/xml/1/5/BRCD_NO=8809549135325' #돈까스

    # request url 정의
    url = 'http://openapi.foodsafetykorea.go.kr/api/3584007bcb4342839eff/I2570/json/1/5/BRCD_NO='+ BRCD_NO
    request = urllib.request.Request(url)

    #request 요청
    response = urllib.request.urlopen(request)

    # response 결과
    rescode = response.getcode()

def allergy_check(prdlstReportNo):
    serviceKey = 'xPc0kxBXexkj0qNFjAwbQvtIo4zzKZMWwGTNf95HscDNOkxDO8DtJ3nzAjcNB3dLVRBL9JqAXLW4rt%2BXboEotw%3D%3D'  #인증키(필수) Encoding

    #prdlstReportNo = ''            #품목보고번호(선택) 다만 본 프로그램에서는 필수로 입력해야함
    # prdlstNm = ''                   #제품명(선택)
    # returnType = 'json'             #리턴타입(선택)
    # pageNo = '1'                    #페이지 번호(선택)
    # numOfRows = '10'                #한 페이지 결과 수(선택)

    #test
    #prdlstReportNo = '201704760012'#테스트용 '미소담은 돈까스'
    testurl3 = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService?serviceKey=xPc0kxBXexkj0qNFjAwbQvtIo4zzKZMWwGTNf95HscDNOkxDO8DtJ3nzAjcNB3dLVRBL9JqAXLW4rt%2BXboEotw%3D%3D&prdlstReportNo=201704760012&returnType=xml'
    testurl4 = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService?serviceKey=xPc0kxBXexkj0qNFjAwbQvtIo4zzKZMWwGTNf95HscDNOkxDO8DtJ3nzAjcNB3dLVRBL9JqAXLW4rt%2BXboEotw%3D%3D&prdlstReportNo=8809360172547&returnType=xml'
    testurl5 = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService?serviceKey=xPc0kxBXexkj0qNFjAwbQvtIo4zzKZMWwGTNf95HscDNOkxDO8DtJ3nzAjcNB3dLVRBL9JqAXLW4rt%2BXboEotw%3D%3D&prdlstReportNo=195505090011&returnType=xml'
    testurl6 = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService?serviceKey=xPc0kxBXexkj0qNFjAwbQvtIo4zzKZMWwGTNf95HscDNOkxDO8DtJ3nzAjcNB3dLVRBL9JqAXLW4rt%2BXboEotw%3D%3D&prdlstReportNo=195505090011&returnType=xml' #지워도됨

    # request url 정의
    url = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService?serviceKey='+serviceKey+'&prdlstReportNo='+ prdlstReportNo+'&returnType=xml'
    request = urllib.request.Request(url)

    #request 요청
    response = urllib.request.urlopen(request)

    # response 결과
    rescode = response.getcode()

    if (rescode == 200): # 요청 결과 성공시에만
        response_body = response.read()
        res = xml.dom.minidom.parseString(response_body.decode('utf-8'))
        pretty_res = res.toprettyxml()
        print(pretty_res)
    else: # 실패시 -> 에러코드 출력
        print("Error Code:" + rescode)    

# def VilageFcstInfoService():
#     encodingKey = "{인코딩 key값}"
#     decodingKey = "{디코딩 key값}"

#     # request url 정의
#     url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?ServiceKey=" + encodingKey + "&pageNo=1&numOfRows=1000&dataType=XML&base_date=20220802&base_time=0200&nx=60&ny=127"
#     request = urllib.request.Request(url)

#     # request 요청
#     response = urllib.request.urlopen(request)

#     # response 결과
#     rescode = response.getcode()

#     if (rescode == 200): # 요청 결과 성공시에만
#         response_body = response.read()
#         res = xml.dom.minidom.parseString(response_body.decode('utf-8'))
#         pretty_res = res.toprettyxml()
#         print(pretty_res)
#     else: # 실패시 -> 에러코드 출력
#         print("Error Code:" + rescode)
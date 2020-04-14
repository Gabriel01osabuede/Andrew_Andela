import time
class ResponseTimeMiddware:

    def __init__(self, get_response):
        self.get_response=get_response

    def  __call__(self,request):
        start_time=time.time()
        response=self.get_response(request)
        file = open('log.txt','a')
        serveTime=time.time() - start_time
        status = request.status
        line = request.method +"    "+request.path +"    "+  status  +  "   " +str(serveTime) +"MS\n"
        file.write(line)
        file.close()
        return response



from torrequest import TorRequest
except:
  os.system("pip install torrequest && clear")                                                                            from torrequest import TorRequest
 
  tr=TorRequest(password=None)
 
  headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}               a = str(input("URL    - ")                                                                                              x = int(input("Amount - ")                                                                                              
  def run():
    for i in range(x):                                                                                                              tr.reset_identity()                                                                                                     response= tr.get(a)
    print(i+1)             

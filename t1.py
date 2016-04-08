def TestUrlOpen():
    import urllib
    import urllib2
    test_data = {'collaborationCode':'aaaa','passcode':'bbbbb','username':'8835@galloptec.com','password':'1234','displayName':'rrrrr'}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = "https://192.168.1.101/capi/rest/conferences/join"
    res_data = urllib.urlopen(requrl,test_data_urlencode)
    res = res_data.read()
    print res
if __name__ == '__main__':
    TestUrlOpen()

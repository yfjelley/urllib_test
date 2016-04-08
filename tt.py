def TestUrlOpen():
    import urllib
    page = urllib.urlopen("https://192.168.1.101/capi/rest/system/settings")
    lines = page.readlines()
    page.close()
    print lines

if __name__ == '__main__':
    TestUrlOpen()

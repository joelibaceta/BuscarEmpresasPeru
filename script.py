import re
import mechanize

def getRuc(razSoc):
    br = mechanize.Browser()

    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    br.open("https://www.universidadperu.com/empresas/")

    response = br.response()

    br.select_form("InfoEmpresa1")
    br.form["buscaempresa"] = razSoc

    response = br.submit()
    response_string = response.read()

    pattern = re.compile('\<strong\>RUC:\<\/strong\>([0-9\s]+)\<\/li\>')

    ruc = re.search(pattern, str(response_string)).group(1)

    return ruc


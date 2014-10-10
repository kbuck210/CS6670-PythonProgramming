import urllib.request
from urllib.error import  URLError
import re
import pickle


def visit_url(url, domain, pickle_file):
    global crawler_backlog
    if(len(crawler_backlog)>100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")
            regexp_alttext = re.compile('<img id=".+" class="image" src=".+" alt="(?P<alttext>(.*))" />')
            result = regexp_title.search(content_string, re.IGNORECASE)

            title = ""
            if result:
                title = result.group("title")
                print(title)

            result = regexp_keywords.search(content_string, re.IGNORECASE)

            if result:
                keywords = result.group("keywords")
                print(keywords)

            # get all of the AltText into 1 searachable string
            #all_text = ""
            #for (altT) in re.findall(regexp_alttext, content_string):
            #    all_text += altT[0] + " "
            
            for (urls) in re.findall(regexp_url, content_string):
                if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                    if title != "": # if the page has a searchable title
                        # Open the pickle file, append a new tuple to the list
                        p = open(pickle_file, "br")
                        data_list = pickle.load(p)
                        p.close()
                        data_list.append((urls, title))
                        p = open(pickle_file, "bw")
                        pickle.dump(data_list, p)
                        p.close()
                        crawler_backlog[urls] = 0
                        visit_url(urls, domain, pickle_file)
            
    except URLError as e:
        print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

#visit_url(seed, "www.newhaven.edu")

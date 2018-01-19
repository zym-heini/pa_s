#coging=utf8
import re,requests
url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1515729563.0 "

header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
"X-CSRFToken":"39df2f5f390cc04620dcf288ddb39e7a",
"Referer":"http://neihanshequ.com/",
}

num = 0
while num < 5:

    response = requests.get(url,headers = header)
    content = response.text
    print content
    joke_list = re.findall(r'"content": "(.*?)"',content)

    f = open("joke1.text","a")

    for joke in joke_list:
        print joke.decode("unicode-escape")
        f.write(joke.decode("unicode-escape").encode("utf-8"))
        f.write("\r\n#########################################################\r\n")
    f.close()

    num +=1
#!/usr/bin/env python3

import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000)


import requests
from apiclient.discovery import build

def main():
    tests = 1
    for test in range(tests):
        # print("Hello World")

        search_engine_id = 'bacf10d320880a82a'
        service_name = 'customsearch'
        service_version = 'v1'
        api_key = 'AIzaSyDe0_tEIiAxvaY9kLAE6YohYdjOZJjg6P0'
        search_string = 'allintext:"Tamanna Verma"'

        resource = build(service_name, service_version, developerKey = api_key).cse()
        firstresult = resource.list(q = search_string, cx = search_engine_id, num = 1).execute()

        print('\n\t{} RESULTS FOUND\n'.format(firstresult["queries"]["request"][0]["totalResults"]))
        try:  
            totalresults = int(firstresult["queries"]["request"][0]["totalResults"])
        except:
            totalresults = 0

        result_set = []
        for i in range(1, min(totalresults, 50), 10):
            result = resource.list(q = search_string, cx = "ba8aefa861c34ab71", start = i).execute()
            result_set += result['items']

        print("{} results found".format(len(result_set)))
        for item in result_set:
            print(item['link'])
if __name__ == '__main__':
    main()


'''
query = "Tamanna Verma"
SEARCH_ENGINE_ID = "ba8aefa861c34ab71"
API_KEY = "AIzaSyBIUdUDNWOfVcSXSY3biu6o4Y0aX1KZx8c"
url = "https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start=1"

# make the API request
data = requests.get(url).json()
print(data)
return
# get the result items
search_items = data.get("items")

# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    try:
        long_description = search_item["pagemap"]["metatags"][0]["og:description"]
    except KeyError:
        long_description = "N/A"
    # get the page title
    title = search_item.get("title")
    # page snippet
    snippet = search_item.get("snippet")
    # alternatively, you can get the HTML snippet (bolded keywords)
    html_snippet = search_item.get("htmlSnippet")
    # extract the page url
    link = search_item.get("link")
    # print the results
    print("="*10, f"Result #{i+start-1}", "="*10)
    print("Title:", title)
    print("Description:", snippet)
    print("Long description:", long_description)
    print("URL:", link, "\n") 
'''

'''
{
   "kind":"customsearch#search",
   "url":{
      "type":"application/json",
      "template":"https://www.googleapis.com/customsearch/v1?q={searchTerms}&num={count?}&start={startIndex?}&lr={language?}&safe={safe?}&cx={cx?}&sort={sort?}&filter={filter?}&gl={gl?}&cr={cr?}&googlehost={googleHost?}&c2coff={disableCnTwTranslation?}&hq={hq?}&hl={hl?}&siteSearch={siteSearch?}&siteSearchFilter={siteSearchFilter?}&exactTerms={exactTerms?}&excludeTerms={excludeTerms?}&linkSite={linkSite?}&orTerms={orTerms?}&relatedSite={relatedSite?}&dateRestrict={dateRestrict?}&lowRange={lowRange?}&highRange={highRange?}&searchType={searchType}&fileType={fileType?}&rights={rights?}&imgSize={imgSize?}&imgType={imgType?}&imgColorType={imgColorType?}&imgDominantColor={imgDominantColor?}&alt=json"
   },
   "queries":{
      "request":[
         {
            "title":"Google Custom Search - Tamanna Verma",
            "totalResults":"55300",
            "searchTerms":"Tamanna Verma",
            "count":2,
            "startIndex":1,
            "inputEncoding":"utf8",
            "outputEncoding":"utf8",
            "safe":"off",
            "cx":"ba8aefa861c34ab71"
         }
      ],
      "nextPage":[
         {
            "title":"Google Custom Search - Tamanna Verma",
            "totalResults":"55300",
            "searchTerms":"Tamanna Verma",
            "count":2,
            "startIndex":3,
            "inputEncoding":"utf8",
            "outputEncoding":"utf8",
            "safe":"off",
            "cx":"ba8aefa861c34ab71"
         }
      ]
   },
   "context":{
      "title":"OSINTsearch"
   },
   "searchInformation":{
      "searchTime":0.14626,
      "formattedSearchTime":"0.15",
      "totalResults":"55300",
      "formattedTotalResults":"55,300"
   },
   "items":[
      {
         "kind":"customsearch#result",
         "title":"tamanna-verma Profiles | Facebook",
         "htmlTitle":"<b>tamanna</b>-<b>verma</b> Profiles | Facebook",
         "link":"https://www.facebook.com/public/Tamanna-Verma",
         "displayLink":"www.facebook.com",
         "snippet":"View the profiles of people named Tamanna Verma. Join Facebook to connect with Tamanna Verma and others you may know. Facebook gives people the power to...",
         "htmlSnippet":"View the profiles of people named <b>Tamanna Verma</b>. Join Facebook to connect with <b>Tamanna Verma</b> and others you may know. Facebook gives people the power to...",
         "cacheId":"ZXsX2JOM1NEJ",
         "formattedUrl":"https://www.facebook.com/public/Tamanna-Verma",
         "htmlFormattedUrl":"https://www.facebook.com/public/<b>Tamanna</b>-<b>Verma</b>",
         "pagemap":{
            "metatags":[
               {
                  "referrer":"origin-when-crossorigin",
                  "theme-color":"#3b5998",
                  "viewport":"user-scalable=no,initial-scale=1,maximum-scale=1"
               }
            ]
         }
      },
      {
         "kind":"customsearch#result",
         "title":"Tamanna Verma (@tamanna.18) • Instagram photos and videos",
         "htmlTitle":"<b>Tamanna Verma</b> (@tamanna.18) • Instagram photos and videos",
         "link":"https://www.instagram.com/tamanna.18/",
         "displayLink":"www.instagram.com",
         "snippet":"207 Followers, 303 Following, 87 Posts - See Instagram photos and videos from Tamanna Verma (@tamanna.18)",
         "htmlSnippet":"207 Followers, 303 Following, 87 Posts - See Instagram photos and videos from <b>Tamanna Verma</b> (@tamanna.18)",
         "formattedUrl":"https://www.instagram.com/tamanna.18/",
         "htmlFormattedUrl":"https://www.instagram.com/<b>tamanna</b>.18/",
         "pagemap":{
            "metatags":[
               {
                  "og:image":"https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/47583432_1207770149376751_5613848660501594112_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=107&_nc_ohc=_WJ82fLCM0cAX83htA9&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT96Tcs73NXWRiu36q9WeGr9vwa467ROD6QCTmp0oXfomw&oe=62AB19F2&_nc_sid=7bff83",
                  "theme-color":"#ffffff",
                  "og:type":"profile",
                  "al:ios:app_name":"Instagram",
                  "og:title":"Tamanna Verma is on Instagram • 87 posts on their profile",
                  "al:android:package":"com.instagram.android",
                  "al:ios:url":"instagram://user?username=tamanna.18",
                  "og:description":"207 Followers, 303 Following, 87 Posts - See Instagram photos and videos from Tamanna Verma (@tamanna.18)",
                  "al:ios:app_store_id":"389801252",
                  "al:android:url":"https://www.instagram.com/_u/tamanna.18/",
                  "apple-mobile-web-app-status-bar-style":"default",
                  "viewport":"width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, viewport-fit=cover",
                  "mobile-web-app-capable":"yes",
                  "og:url":"https://www.instagram.com/tamanna.18/",
                  "al:android:app_name":"Instagram"
               }
            ],
            "cse_image":[
               {
                  "src":"https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/47583432_1207770149376751_5613848660501594112_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=107&_nc_ohc=_WJ82fLCM0cAX83htA9&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT96Tcs73NXWRiu36q9WeGr9vwa467ROD6QCTmp0oXfomw&oe=62AB19F2&_nc_sid=7bff83"
               }
            ]
         }
      }
   ]
}
'''

'''
https://customsearch.googleapis.com/customsearch/v1?q=Tamanna+Verma&cx=ba8aefa861c34ab71&start=101&key=AIzaSyBIUdUDNWOfVcSXSY3biu6o4Y0aX1KZx8c&alt=json
https://www.google.com/search?q=%22Tamanna+Verma%22&sxsrf=ALiCzsYNO9J-zD78lFp-mqMHKw6mQjM8JA%3A1655267483807&ei=m2CpYuvvMLGF4-EPvfyT-Ak&ved=0ahUKEwirqYXzz674AhWxwjg
https://www.google.com/search?q=Tamanna+Verma&sxsrf=ALiCzsbfCkqdpatXSyEeO4KjYqxDIhHU-g%3A1655267488568&ei=oGCpYu6lIu71juMPkrym6Ak&ved=0ahUKEwju9af1z674AhXuumMGHRKeC
https://www.google.com/search?q=intext%3ATamanna+Verma&sxsrf=ALiCzsakvvmavQiJE9hSht58jIugSdmq_Q%3A1655267629169&ei=LWGpYvXrCc3f4-EP---c6AE&ved=0ahUKEwi1tq240K74AhX
'''

'''
https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search
https://www.youtube.com/watch?v=IBhdLRheKyM
https://www.labnol.org/internet/google-web-scraping/28450/
'''

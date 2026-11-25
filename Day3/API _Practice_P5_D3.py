import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10) #send a http get req
    response.raise_for_status() #raises an exception for unsuccessful HTTP status codes
    data = response.json()
    print(data)

except requests.exceptions.Timeout:
    print("Api request Time out")

except requests.exceptions.HTTPError as e:
    print("HTTP Error", e)

except requests.exceptions.RequestException as e:
    print("Request Failed", e)

except ValueError:
    print("Invalid Json Response")    



'''
print (response.status_code)
print(response.text)'''

'''
data = response.json()  # .josn converts the josn into a python objects 

print(data)
print(data["title"])

# Convert API response into Python object

'''

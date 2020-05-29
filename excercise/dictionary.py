user = {"name":"minpyo"}
print(user)
print(type(user))

site = {
    "naver" : "www.naver.com",
    "google" : "www.google.com"
}

print(site["naver"])
print(site["google"])

site["yahoo"] = "www.yahoo.com"

print(site)

del site["yahoo"]

print(site)

#### Get Example

print(site.get("naver"))
print(site.get("daum"))

insert_key = "daum"

if(site.get(insert_key)==None):  ## site[] 로 접근하면 error 발생
    print(insert_key + "에 대한 데이터가 없습니다.")

print(site.keys())
print(site.values())
print(site.items())

for key in site.keys() :
    print(key)

for value in site.values() :
    print(value)

for item in site.items() :
    print(item)
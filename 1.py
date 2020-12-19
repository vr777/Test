import re


def sub_domain_find(url):
    sub_domain = re.findall(
        r"(?:http[s]?:\/\/)?(?:www\.)?([^/\n\r\s]+)?(\b\.\w+\.)", url)
    x = sub_domain[0][0]
    if len(sub_domain) == 0 or x == 'www':
        return 'No Subdomain'
    else:
        return x


url1 = input("Enter url : ")
print('-'*50)
print("Sub-Domain is :",sub_domain_find(url1))
import os

def get_ip_address(url):
    command = "host"+url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address')+12
    ip = results[marker:].splitlines()[0]
    return ip


print get_ip_address('thenewboston.com')

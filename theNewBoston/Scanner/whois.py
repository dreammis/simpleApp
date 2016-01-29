import os

def get_whois(url):
    commands = 'whois '+url
    process = os.popen(commands)
    results = str(process.read())
    return results

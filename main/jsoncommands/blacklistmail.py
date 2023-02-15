import json, re

def JsonMailFilterDeny(fromfile, mail):
  f = open(fromfile)
  check = json.load(f)
  
  for i in range(len(check)):
    checki = check[i]
    if mail == checki["email-url"]:
      return False
      break
    else:
      return True
#!/usr/bin/python3

import argparse, requests, glob, os, sys

welcome_msg="""Welcome to the
______
|  ___|
| |_ _   _ ___________ _ __
|  _| | | |_  /_  / _ \ '__|
| | | |_| |/ / / /  __/ |
\_|  \__,_/___/___\___|_|\n"""

def fuzz(vln, target, query):
  payload = {query : vln}
  r = requests.get(target, params=payload)

  if r.text.find(vln) >= 0:
    print("WARNING: The target is vulnerable to reflected XSS\n")
    print("Goodbye!")
    sys.exit(0)


parser = argparse.ArgumentParser(description='A fuzzer that automatically identifies reflected XSS bugs')
parser.add_argument('-t', dest='target', help='Target URI', default="https://www.cs.tufts.edu/comp/120/hackme.php")
parser.add_argument('-q', dest='query',  help='Query String', default="token")
parser.add_argument('-l', dest='lists', help='Location of external fuzzing lists', default="")
args = parser.parse_args()
print(welcome_msg)
print("Target:  %(t)s\nQuery:   %(q)s" % {"t" : args.target, "q" : args.query})

if not args.lists:
  print("List(s): N/A\n")
  try:
    fuzz(vln="<script>alert(\"XSS_ATTACK_SUCCESSFUL\")</script>", 
              target=args.target, query=args.query)
  except Exception as e:
    print("Sorry, there was an error:\n%(exp)s" % {"exp" : e})
else:
  print("List(s): %(l)s\n" % {"l" : args.lists})
  try:
    os.chdir(args.lists)
    for file in glob.glob("**/*.txt", recursive=True):
        print("Fuzzing using strings from " + file)
        with open(file) as file_in:
          for line in file_in:
            fuzz(vln=line, target=args.target, query=args.query)
  except Exception as e:
    print("Sorry, there was an error:\n%(exp)s" % {"exp" : e})

print("The target is not vulnerable to reflected XSS")
print("Goodbye!")
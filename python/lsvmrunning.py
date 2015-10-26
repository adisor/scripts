#!/usr/bin/python2.7

import XenAPI
import sys
#import smtplib

import argparse
import xmlrpclib

#parser=argparse.ArgumentParser(
#     description='Script for list all the vms running on a Xen Pool')
#parser.add_argument('-s', type=str, default=42, help='server')
#parser.add_argument('-u', type=str, default=42, help='user')
#parser.add_argument('-p', type=str, default=42, help='password')
#args=parser.parse_args()


server=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
sys.stdout = file('vms.txt', 'w')

###Connect to XenApi
session = "https://%s" % XenAPI.Session(server)
session.xenapi.login_with_password(username,password)



print "Session ID: " + session._session

for opaque_ref, vm in session.xenapi.VM.get_all_records().items():
    if not(vm["is_a_template"]) and not(vm["is_control_domain"]) and (vm["power_state"] == "Running"):
	    print vm["name_label"]


session.xenapi.session.logout()
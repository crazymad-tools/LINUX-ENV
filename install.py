#!/usr/bin/python
import os

global system_			# CentOS is True, Ubuntu is False
system_ = True

def setSysName():		# set this system is CentOS or Ubuntu
	# default is CentOS
	while True:
		sysName = raw_input("Input you system name(CentOS or Ubuntu):")
		sysName = sysName.upper()
		if sysName == "CENTOS":
			sysName = raw_input("Your choice is CentOS?(y or n):")
			sysName = sysName.upper()
			if sysName == "Y":
				system_ = True
				break
			else:
				continue
		elif sysName == "UBUNTU":
			sysName = raw_input("Your choice is Ubuntu?(y or n):")
			sysName = sysName.upper()
			if sysName == "Y":
				system_ = False
				break
			else:
				continue
		elif sysName != "":						# default is CentOS
			continue
		else:
			system_ = True
			break


def bash(comm):	# execute the bash comment
	os.system(comm)

def install():	# install some comm soft
	if system_:
		print "is CentOS"
	comm = "yum install " if system_ else "apt-get install "
	print comm
	bash(comm + 'vim')
	bash(comm + 'git')
	bash(comm + 'gcc')
	bash(comm + 'gcc-c++')

def vim_conf(): # confiure the vim
	bash('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim')
	bash('cp ./vim/bashrc ~/.vimrc')	# copy .vimrc to root directory
	bash('vim -c PluginInstall')		# install plugin

def main():
	setSysName()
	install()
	vim_conf()

main()

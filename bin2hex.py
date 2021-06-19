#!/usr/bin/env python
#coding=utf8
import binascii
import argparse
import sys
  

def b2a(filename):
	with open(filename,'rb') as f:
		hexstr=binascii.b2a_hex(f.read())
		return hexstr
def a2b(filename,outfile):
	with open(filename) as f:
		# bsstr=bin(int(f.read(),16))[2:]
		bsstr=binascii.a2b_hex(f.read().strip())
		with open(outfile,'wb') as ff:
			ff.write(bsstr)
		return bsstr


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="convert to binary or strings.")
	# 位置参数
	parser.add_argument('filename',help="the file convert to binary or strings.")
	#添加互斥选项
	#参数不能以数字开头
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-b",action='store_true',dest='b',help="convert to binary,default is bin 2 hex")
	group.add_argument('-s',dest='outfile',help="convert to hex string,save in the outfile, default is a.out")
	# args = parser.parse_args()
	#remaining为不认识的参数
	args, remaining = parser.parse_known_args()
	# print args
	# print help(args['2b'])
	if args.outfile:
		print a2b(args.filename,args.outfile)
	else:
		print b2a(args.filename)


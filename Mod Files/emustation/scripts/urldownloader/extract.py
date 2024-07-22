import os
import shutil
import time
import zipfile

def all(_in, _out, rename_emus, dp=None):
	if dp:
		return allWithProgress(_in, _out, rename_emus, dp)

	return allNoProgress(_in, _out)


def allNoProgress(_in, _out):
	try:
		zin = zipfile.ZipFile(_in, 'r')
		root = zin.namelist()[0]		
		zin.extractall(_out)

	except Exception, e:
		print str(e)
		return False

	return True


def allWithProgress(_in, _out, rename_emus, dp):

	zin = zipfile.ZipFile(_in, 'r')
	root = zin.namelist()[0]
	
	if rename_emus:
		# Check if the original folder already exists
		if os.path.exists(os.path.join(_out, root)) and not os.path.exists(os.path.join(_out, rename_emus)):
			# If it does, rename the original folder
			os.rename(os.path.join(_out, root), os.path.join(_out, rename_emus))

	nFiles = float(len(zin.infolist()))
	count  = 0

	try:
		for item in zin.infolist():
			count += 1
			update = count / nFiles * 100
			dp.update(int(update))
			if rename_emus:
				# Change the directory structure on-the-fly
				if rename_emus and item.filename.startswith(root):
					new_filename = rename_emus + '/' + item.filename[len(root):]
				else:
					new_filename = item.filename
				# Create directories as needed
				if not os.path.isdir(os.path.join(_out, os.path.dirname(new_filename))):
					os.makedirs(os.path.join(_out, os.path.dirname(new_filename)))
				# Extract file
				if not item.filename.endswith('/'):  # Check if the item is a file
					with zin.open(item) as src, open(os.path.join(_out, new_filename), 'wb') as dst:
						shutil.copyfileobj(src, dst)
			else:
				zin.extract(item, _out)	

	except Exception, e:
		print str(e)
		return False

	return True
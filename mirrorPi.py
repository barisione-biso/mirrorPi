import os
import json 
import datetime
import os.path

with open ('mirrorPi.json') as json_data:
	conf = json.load(json_data)

print ('MirrorPi started >>')

#backup old log file
logfile_name='outputmirror'
logfile_name_ext='log'
now=datetime.datetime.now()
#python 2 specific.
if os.path.exists('%s.%s' % (logfile_name, logfile_name_ext)):
	os.rename('%s.%s' % (logfile_name,logfile_name_ext), '%s_%s.%s' % (logfile_name,now,logfile_name_ext))
for m in conf["mirror"]:
	#per each line to rsync
	if m["active"]=="true" and len(m["from"]) > 0 and os.path.isdir(m["to"]) is True:
		print ('Row active: '+str(m["from"])+', processing it')
		command='rsync '+m["options"]+' \"'+m["from"]+'\" \"'+m["to"] +'\" >> ' + logfile_name + '.' + logfile_name_ext
		print ('>> ' + command)
		#command='rsync '+m["options"]+' "'+m["from"]+'" "'+m["to"] +'" >> ' + logfile_name + '.' + logfile_name_ext
		os.system(command)
	else:
		print ('Row inactive: '+str(m["from"])+', skipping it')
print ('check mirrorPi.out for details of rsync process ')

print ('MirrorPi finished <<')

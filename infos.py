from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<20):
			if porcent >= index_make * 5: make_text+= 'β'
			else: make_text+= 'β'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = 'π₯π³π΄ππ²π°ππΆπ°π½π³πΎπ‘... \n\n'
    msg+= 'β’ Nombre: ' + str(filename)+'\n'
    msg+= 'β’ TamaΓ±o total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'β’ Descargado: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'β’ Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'β’ Tiempo restante: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = 'π₯π³π΄ππ²π°ππΆπ°π½π³πΎ π°ππ²π·πΈππΎπ‘...\n\n'
    msg += 'β’ Archivo: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'β’ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += 'β’ TamaΓ±o total: '+sizeof_fmt(totalBits)+'\n\n'
    msg += 'β’ Descargado: '+sizeof_fmt(currentBits)+'\n\n'
    msg += 'β’ Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
    msg += 'β’ Tiempo restante: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = 'π€πππ±πΈπ΄π½π³πΎ π° π»π° π½ππ±π΄βοΈ... \n\n'
    msg+= 'β’ Archivo: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'β’ Subiendo: ' + str(filename)+'\n'
    msg+= 'β’ TamaΓ±o total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'β’ Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'β’ Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'β’ Tiempo restante: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = 'π€πππ±πΈπ΄π½π³πΎ π° π»π° π½ππ±π΄βοΈ...\n\n'
    msg += 'β’ Nombre: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'β’ Parte: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'β’ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += 'β’ TamaΓ±o total: '+sizeof_fmt(totalBits)+'\n\n'
    msg += 'β’ Subido: '+sizeof_fmt(currentBits)+'\n\n'
    msg += 'β’ Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
    msg += 'β’ Tiempo restante: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = 'ποΈπ²πΎπΌπΏππΈπΌπΈπ΄π½π³πΎποΈ... \n\n'
    msg+= 'β’ Nombre: ' + str(filename)+'\n'
    msg+= 'β’ TamaΓ±o Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'β’ TamaΓ±o de Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= 'β’ Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'

    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = 'ππΏππΎπ²π΄ππΎ π΅πΈπ½π°π»πΈππ°π³πΎπ\n\n'
    msg+= 'β’ Nombre: ' + str(filename)+'\n'
    msg+= 'β’ TamaΓ±o Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'β’ TamaΓ±o de Partes: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= 'β’ Partes Subidas: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= 'ποΈπ΄π»πΈπΌπΈπ½π°π π°ππ²π·πΈππΎποΈ: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>ππ΄π½π»π°π²π΄ππ</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">π' + f['name'] + 'π</a>'
            msg+= "<a href='"+url+"'>π"+f['name']+'π</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = 'ππ°ππ²π·πΈππΎπ ('+str(len(evfiles))+')π\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin,quote=""):
    from pyobigram.utils import sizeof_fmt
    msg = 'βοΈπ²πΎπ½π΅πΈπΆπππ°π²πΈπΎπ½ π³π΄ ππππ°ππΈπΎβοΈ\n\n'
    msg+= 'β’ Nombre: ΰΌΊ@' + str(username)+'ΰΌ»\n'
    msg+= 'β’ Usuario: ' + str(userdata['moodle_user'])+'\n'
    msg+= 'β’ ContraseΓ±a: ' + str(userdata['moodle_password'])+'\n'
    msg+= 'β’ Url de nube: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= 'β’ Repo ID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= 'β’ Tipo de nube: ' + str(userdata['cloudtype'])+'\n'
    msg+= 'β’ Tipo de Subida: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= 'β’ Directorio: /' + str(userdata['dir'])+'\n'
    msg+= 'β’ TamaΓ±o de zips: ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'

    if quote!="":
        msg+= 'β’ Nube: ' + quote + '\n'

    msgAdmin = 'NO'
    if isadmin:
        msgAdmin = 'SI'
    msg+= 'β’ Admin : ' + msgAdmin + '\n'
    proxy = 'NO'
    if userdata['proxy'] !='':
       proxy = 'SI'
    tokenize = 'NO'
    if userdata['tokenize']!=0:
       tokenize = 'SI'
    msg+= 'β’ Proxy: ' + proxy + '\n'
    msg+= 'β’ Encriptar: ' + tokenize + '\n\n'
    msg+= 'βοΈπ²πΎπ½π΅πΈπΆπππ°π π²ππ΄π³π΄π½π²πΈπ°π»π΄πβοΈ\n Ejemplo: /acc usuario,contraseΓ±a'
    return msg
    

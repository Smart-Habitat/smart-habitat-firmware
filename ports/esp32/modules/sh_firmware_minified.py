#### COPYRIGHT SMART HABITAT ####
## LICENSED UNDER AGPL-3.0 ##
#### COPYRIGHT SMART HABITAT ####

By="Couldn't connect to the WiFi!"
Bx='/shadow/name/'
Bw='$aws/things/'
Bv='Registered under: '
Bu='old_ip'
Bt='OPTIONS, GET'
Bs='/update'
Br='generate'
Bq='DEVICE REBOOTING IN 10 SECONDS!'
Bp='def_key.der'
Bo='def_cert.der'
Bn='Creating new salt'
Bm='sensors'
Bl='run_finder'
Bk='alerts.json'
Bj='dhcp_hostname'
Bi='ESP32_S3_N8R2'
Bh=RuntimeError
BQ='text/plain'
BP='Access-Control-Allow-Origin'
BO='base64_DER_key'
BN='base64_DER_cert'
BM='ambient_limit'
BL='cust_id'
BK='serial'
BJ='wifi'
BI='name'
BH='anonymous_data_collection'
BG='\x00'
Ax='Starting services'
Aw=None
Av='wb'
Au='firmware_version'
At='customer.json'
As='no_telemetry'
Ar='smart-habitat-'
Aq='username'
Ap='device_id'
Ao='api_key'
An=dict
Am=bytearray
AX='key.der'
AW='cert.der'
AV='POST'
AU='OPTIONS, POST'
AT='desired'
AS='null_desire'
AR='friendly_name'
AQ='drain_check'
AP='powered'
AO='light_override'
AN='off'
AM='on'
AH='close cmd'
AG='note'
AF='no_auto_update'
AE='auto_update'
A9='application/json'
A8='override'
A7=bool
A6=len
A0='Unauthorized'
z='Allow'
y=type
v='admin'
u='runtime'
s=Exception
o='Content-Type'
n='interval'
m='salt'
l='debug'
f='OPTIONS'
a='x-api-key'
U='\n'
T='r'
S=range
P='reported'
O='w'
N='light'
M=False
K='state'
J='pump'
I=str
H=True
F=print
E=open
C=int
import network as Q,gc as L,os as b
from httpclient import HttpClient
from machine import WDT
from ubinascii import hexlify
from time import sleep,localtime as Ay,time as p,gmtime
from sht3x import SHT3x_Sensor as Bz
from ota_updater import OTAUpdater as B_
from ujson import loads as i,dumps as e
from ds3231_port import DS3231
import machine as Az,sys,esp32 as A_,uasyncio as A
from ntptime import settime as B0
from microdot import Microdot as C0,Response as q
from microdot.websocket import with_websocket as BR
from microdot.cors import CORS
from mqtt_as import MQTTClient as BS,config as r
import uhashlib as C1,random,string as BT
from httpclient import HttpClient
import ssl
from binascii import a2b_base64 as AA
X='v0.22.3'
if X.split('.')[0]=='v0':D=H
else:
	try:
		with E(l):D=H
	except:D=M
AY=A_.NVS('nvs')
B=M
AZ=M
try:
	with E(Ao,T)as C2:G=C2.readline().strip()
except:
	try:G=Am(32);AY.get_blob(b'api_key',G);G=G.decode();L.collect()
	except:sys.exit()
try:
	with E('platform')as C3:A1=C3.read().strip()
	B=H
except:
	try:A1=Am(25);AY.get_blob(b'platform',A1);A1=A1.decode().split(BG)[0]
	except:A1=Bi
if Bi in A1:from vars_ESP32_GENERIC_S3 import amb_scl as BU,amb_sda as BV,analog_water_sensor as BW,water_power as B1,hard_reset_button,network_reset_button,pump as j,light as Z,err_light as V,dat_light as B2,i2c_r
else:F('Unsupported board!!');sys.exit()
try:
	with E(Ap)as C4:k=C4.read()
	B=H
except:
	try:k=Am(64);AY.get_blob(b'device_id',k);k=k.decode().split(BG)[0]
	except:k='nodeviceidset_'+I(p());AZ=H
try:
	with E(Aq)as AI:w=A6(AI.readlines())
	with E(Aq)as AI:
		if w==1:d=t=AI.read().strip()
		elif w==2:d=AI.readline().strip();t=AI.readline().strip()
		else:raise s
	B=H
except:
	try:d=Am(25);AY.get_blob(b'serial',d);d=d.decode().split(BG)[0];t=M
	except:d='noserialset_'+I(p());AZ=H
if D or B:F('Loaded device identifiers!')
g=WDT(timeout=60000)
def BX(ssid,password):
	global d,B
	if B:
		try:
			global t
			if t:Q.hostname(Ar+t.lower())
			else:raise s
		except:Q.hostname(Ar+d.lower())
	else:Q.hostname(Ar+d.lower())
	A=Q.WLAN(Q.STA_IF)
	if Q.WLAN(Q.AP_IF).active():Q.WLAN(Q.AP_IF).active(M)
	A.active(H)
	if D or B:F('Connecting to: '+ssid)
	A.connect(ssid,password)
	for C in S(15):
		sleep(1)
		if A.isconnected():break
		elif C==14:A.active(M);raise OSError
def B3():
	global G,d;A=Q.WLAN(Q.AP_IF)
	if Q.WLAN(Q.STA_IF).active():Q.WLAN(Q.STA_IF).active(M)
	A.active(H);A.config(essid=Ar+d.lower(),authmode=Q.AUTH_WPA_WPA2_PSK,password=G)
def CP(file_object,chunk_size=1024):
	while H:
		A=file_object.read(chunk_size)
		if not A:break
		yield A
def B4(n=16):
	A=''
	for B in S(0,n):A=A+random.choice(BT.ascii_lowercase+BT.digits)
	return A
def C5(old,new):
	F=old;C=new;D={}
	for A in C:
		if y(C[A])is An:
			for B in C[A]:
				if y(C[A][B])is An:
					for E in C[A][B]:
						if C[A][B][E]!=F[A][B][E]:
							try:D[A][B][E]=C[A][B][E]
							except:
								try:D[A][B]={};D[A][B][E]=C[A][B][E]
								except:D[A]={};D[A][B]={};D[A][B][E]=C[A][B][E]
				elif C[A][B]!=F[A][B]:
					try:D[A][B]=C[A][B]
					except:D[A]={};D[A][B]=C[A][B]
		elif C[A]!=F[A]:D[A]=C[A]
	return D
def BY():
	if gmtime(0)[0]==2000:A=p()+946684800
	else:A=p()
	return A
async def BZ():
	global BU,BV
	try:D=Bz(freq=100000,sclpin=BU,sdapin=BV)
	except:return-9999,-9999
	try:B=D.read_temp_humd()
	except:
		A.sleep(1)
		try:B=D.read_temp_humd()
		except:
			A.sleep(1)
			try:B=D.read_temp_humd()
			except:return-9999,-9999
	if C(B[0])==-45 and C(B[1])==0:return-9999,-9999
	return B[0],B[1]
async def Ba():
	global B1,BW;B1.value(1);A.sleep(.1);B=BW.read();B=B/4500*100;B1.value(0)
	if B<15:B=-9999
	return B
async def R():global B2;B2.value(1);A.sleep(.05);B2.value(0)
async def Aa():global V;V.value(1);A.sleep(.1);V.value(0)
async def AB(unit_state={},query_state={}):
	a=query_state;G=unit_state;global j,Z;c=M
	with E(N,T)as d:P=d.readline().strip();Q=d.readline().strip()
	L.collect()
	with E(J,T)as K:
		try:V=A7(C(K.readline().strip()));W=C(K.readline().strip());X=C(K.readline().strip())
		except:V=A7(K.readline());W=C(K.readline().strip());X=C(K.readline().strip())
	L.collect()
	if G:
		if D or B:F(G)
		if N in G:
			try:
				if C(G[N][AM])in S(0,2400):
					if C(G[N][AM][:2])in S(0,24)and C(G[N][AM][2:])in S(0,60):P=G[N][AM]
			except:pass
			try:
				if C(G[N][AN])in S(0,2400):
					if C(G[N][AN][:2])in S(0,24)and C(G[N][AN][2:])in S(0,60):Q=G[N][AN]
			except:pass
			with E(N,O)as d:d.write(P+U+Q+U)
			try:
				if G[N][A8]=='1'or G[N][A8]=='0'or G[N][A8]==M:
					if G[N][A8]!=M:
						Z.value(C(G[N][A8]))
						with E(AO,O)as g:g.write(G[N][A8])
					else:
						try:b.remove(AO)
						except:pass
			except:
				try:Y=x.get_time(set_rtc=M)
				except:Y=Ay()
				e=I(Y[3])+(I(Y[4])if A6(I(Y[4]))==2 else'0'+I(Y[4]))
				if Q==P:Z.value(0)
				elif C(P)<C(Q):
					if C(e)in S(C(P),C(Q)):Z.value(1)
					else:Z.value(0)
				elif C(P)>C(Q):
					if C(e)in S(C(P),2400)or C(e)in S(0,C(Q)):Z.value(1)
					else:Z.value(0)
				del e,Y;L.collect()
		if J in G:
			try:
				if G[J][AP]==M or G[J][AP]==H:
					with E(J,O)as K:K.write(I(C(G[J][AP]))+U+I(W)+U+I(X)+U)
					V=G[J][AP]
				if not V:j.value(0)
				L.collect()
			except:pass
			try:
				if y(G[J][n])is C and G[J][n]in S(600,86401):
					with E(J,O)as K:K.write(I(C(V))+U+I(G[J][n])+U+I(X)+U)
					W=G[J][n]
				if y(G[J][n])is not C and C(G[J][n])in S(600,86401):K.write(I(C(V))+U+I(C(G[J][n]))+U+I(X)+U);W=C(G[J][n])
				L.collect()
			except:pass
			try:
				if y(G[J][u])is C and G[J][u]in S(60,86401):
					with E(J,O)as K:K.write(I(C(V))+U+I(W)+U+I(G[J][u])+U)
					X=G[J][u]
				if y(G[J][u])is not C and C(G[J][u])in S(60,86401):K.write(I(C(V))+U+I(W)+U+I(C(G[J][u])+U));X=C(G[J][u])
				L.collect()
			except:pass
			try:
				if G[J]['drain']:
					with E(AQ,O)as h:h.write('1')
					j.value(1)
				else:
					try:b.remove(AQ)
					except:pass
					j.value(0)
			except:pass
		if AE in G:
			i=G[AE]
			if i:
				try:b.remove(AF)
				except:pass
			else:
				with E(AF)as k:k.write('1')
		if BH in G:
			l=G[BH]
			if l:
				try:b.remove(As)
				except:pass
			else:
				with E(As)as m:m.write('1')
		if AR in G:
			with E(BI,O)as o:o.write(I(G[AR]))
	if a:
		if D or B:F(a)
		try:
			if a['restart']:
				for f in S(3):await R()
				A.create_task(A4());c=H
		except:pass
		try:
			if a['network-reset']:
				for f in S(3):await R()
				try:b.remove(BJ)
				except:pass
				A.create_task(A4());c=H
		except:pass
		try:
			if a['factory-reset']:
				for f in b.listdir('/'):
					try:b.remove(f)
					except:pass
				for f in S(3):await R()
				A.create_task(A4());c=H
		except:pass
	if c:return H
	return M
async def C6(setup_dic):
	B=setup_dic;global A2,A3,AZ;C=M
	if AR in B:
		with E(BI,O)as F:F.write(I(B[AR]))
	if A2:
		try:
			with E(BJ,O)as G:G.write(I(B['ssid'])+U+I(B['password']))
			C=H;await R()
		except:pass
	if A3:
		try:
			with E('cust_id_token',O)as J:J.write(B['id_token'])
			C=H;await R()
		except:pass
	if AZ:
		try:
			with E(Aq,O)as K:D=B[Aq];L=D+I(p());K.write(D+U+L)
			C=H;await R()
		except:pass
		try:
			with E(Ap,T)as N:N.write(B[Ap])
			C=H;await R()
		except:pass
	if C:A.create_task(A4());return H
	return M
async def AJ():
	e='status';global j,Z,k,d,B,G,A3;f={Ao:G};O=Q.WLAN(Q.STA_IF)
	if O.active():D=O.ifconfig()[0]
	else:D='192.168.4.1'
	with E(J,T)as F:g=A7(C(F.readline().strip()));h=C(F.readline().strip());l=C(F.readline().strip())
	m=A7(j.value())
	with E(N,T)as P:R=P.readline().strip();S=P.readline().strip()
	o=A7(Z.value())
	try:p=E(AQ,T);U=H;p.close()
	except:U=M
	try:
		with E(AO,T)as q:V=q.read()
	except:V=M
	try:
		with E(AF)as z:W=M
	except:W=H
	try:
		with E(As)as A0:Y=M
	except:Y=H
	L.collect();A={Ap:k,BK:d,N:{e:o,AM:R,AN:S,A8:V},J:{AP:g,n:h,u:l,e:m,'drain':U},'internal_ip':D,AE:W,BH:Y};del D,R,S;L.collect();A.update(f)
	try:
		with E(At)as r:I=i(r.read())
		s=I[BL];K=I['cert_exp'];a=BY()
		if a>float(K):b.remove(At);Az.reset()
		elif a>=float(K)-2592000:A3=1;c=H
		else:c=M
		del I;L.collect();A.update({'customer_id':s,'device_certificate':{'expiration:':K,'renewal_period_active':c}})
	except:pass
	try:
		with E(BI)as v:w=v.read()
		A.update({AR:w})
	except:pass
	if B:
		try:global t;A.update({Bj:t})
		except:pass
	A.update({Au:X})
	with E(Bk,T)as x:y=i(x.read())
	A.update(y);return A
async def Y(unit_state=Bl):
	A=unit_state;C,D=await BZ();E=await Ba();B={Bm:{'environment':{'temperature':C,'humidity':D},'water_level':E}}
	if A:
		if A==Bl:B.update(await AJ())
		else:B.update(A)
	del C,D,E;L.collect();return B
async def B5(payload):
	A=payload;D={};F=BY()
	if A:
		A=A[K][P]
		for B in A:
			if B in[N,J,Au]:
				if y(A[B])is An:
					for C in A[B]:D[B+'_'+C]=A[B][C]
				else:D[B]=A[B]
			if B==Bm:
				for C in A[B]:
					if y(A[B][C])is An:
						for E in A[B][C]:
							if not A[B][C][E]==-9999:D[C+'_'+E]=A[B][C][E]
					elif not A[B][C]==-9999:D[C]=A[B][C]
	D.update({'iso':F});return D
async def A4():
	if D or B:F('Restarting device in 10 seconds!')
	await A.sleep(10);Az.reset()
async def Ab():0
async def Ac():0
async def Ad():
	global j;await A.sleep(600)
	while H:
		try:
			with E(AQ,T)as I:j.value(1)
		except:
			with E(J,T)as B:
				try:D=A7(C(B.readline().strip()));F=C(B.readline().strip());G=C(B.readline().strip())
				except:D=A7(B.readline().strip());F=C(B.readline().strip());G=C(B.readline().strip())
			L.collect()
			if D:j.value(1);await A.sleep(G);j.value(0)
			else:j.value(0)
		await A.sleep(F)
async def Ae():
	global Z
	try:global x;B=x.get_time(set_rtc=M)
	except:B=Ay()
	while H:
		try:
			with E(AO,T)as K:
				O=C(K.readline().strip())
				if O:Z.value(1)
				else:Z.value(0)
		except:
			with E(N,T)as J:D=J.readline().strip();F=J.readline().strip()
			L.collect();G=I(B[3])+(I(B[4])if A6(I(B[4]))==2 else'0'+I(B[4]))
			if F==D:Z.value(0)
			elif C(D)<C(F):
				if C(G)in S(C(D),C(F)):Z.value(1)
				else:Z.value(0)
			elif C(D)>C(F):
				if C(G)in S(C(D),2400)or C(G)in S(0,C(F)):Z.value(1)
				else:Z.value(0)
		await A.sleep(30)
async def Af():
	S='High';N='Low';K='Sensor Error'
	while H:
		if not j.value():
			P=await Ba()
			if P==-9999:G=K
			elif P<25:G=N
			else:G=M
			with E(BM)as B:T=C(B.readline().strip());U=C(B.readline().strip());V=C(B.readline().strip());W=C(B.readline().strip())
			I,J=await BZ()
			if I>T:D=S
			elif I==-9999:D=K
			elif I<U:D=N
			else:D=M
			if J>V:F=S
			elif J==-9999:F=K
			elif J<W:F=N
			else:F=M
			Q={'alerts':{'water_level_alert':G,'temperature_alert':D,'humidity_alert':F}}
			with E(Bk,O)as R:R.write(e(Q))
			del Q,R;L.collect()
		g.feed();await A.sleep(10)
async def C7():
	global V
	while H:V.value(1);await A.sleep(.5);V.value(0);await A.sleep(1)
async def C8():
	global V
	while H:V.value(1);await A.sleep(.1);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.1);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.1);V.value(0);await A.sleep(1)
async def C9():
	global V
	while H:V.value(1);await A.sleep(.1);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.25);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.1);V.value(0);await A.sleep(1)
async def Bb():
	while H:
		try:B0()
		except:
			await A.sleep(120)
			try:B0()
			except:
				await A.sleep(120)
				try:B0()
				except:pass
		try:global x;x.save_time()
		except:pass
		await A.sleep(86400)
async def Ag():
	global A2,B6
	while H:
		B=Q.WLAN(Q.STA_IF)
		if not B.active():
			try:
				BX(BA,BB)
				if B6:Az.reset()
			except:A2=1;B3()
		del B;L.collect();await A.sleep(600)
async def Bc():
	try:global x
	except:pass
	G=0
	while H:
		try:
			with E(AF)as V:0
			P=900
		except:
			try:L=x.get_time(set_rtc=M)
			except:L=Ay()
			Q=I(L[3])+(I(L[4])if A6(I(L[4]))==2 else'0'+I(L[4]))
			with E(N,T)as R:J=R.readline().strip();K=R.readline().strip()
			P=900
			if K==J:
				for U in S(0,48):
					await A.sleep(900)
					if not K==J:break
					if U==47:
						G=G+1
						if G==6:await A4()
						F=await c.update(X,debug=D or B)
						if not F:
							await A.sleep(15);F=await c.update(X,debug=D or B)
							if not F:
								await A.sleep(15);F=await c.update(X,debug=D or B)
								if not F:await A.sleep(15);F=await c.update(X,debug=D or B)
			elif C(K)<C(J):
				O=I(C((C(K)+C(J))/2))[:-2]
				if C(O+'00')<C(Q)<C(O+'20'):
					G=G+1
					if G==6:await A4()
					F=await c.update(X,debug=D or B)
					if not F:
						await A.sleep(15);F=await c.update(X,debug=D or B)
						if not F:
							await A.sleep(15);F=await c.update(X,debug=D or B)
							if not F:await A.sleep(15);F=await c.update(X,debug=D or B)
			elif C(K)>C(J):
				O=I(C((C(K)-C(J))/2))[:-2]
				if C(O+'00')<C(Q)<C(O+'20'):
					G=G+1
					if G==6:await A4()
					F=await c.update(X,debug=D or B)
					if not F:
						await A.sleep(15);F=await c.update(X,debug=D or B)
						if not F:
							await A.sleep(15);F=await c.update(X,debug=D or B)
							if not F:await A.sleep(15);F=await c.update(X,debug=D or B)
		await A.sleep(P)
async def CA():
	await A.sleep(65)
	if D or B:F('All services started successfully!')
	CC.mark_app_valid_cancel_rollback()
	if D or B:F('Since no errors were found, marked boot partition as valid!')
try:
	with E(J,T)as AK:w=A6(AK.readlines())
	if not w==3:raise s
except:
	with E(J,O)as CB:CB.write('0\n600\n60\n')
try:
	with E(N,T)as AK:w=A6(AK.readlines())
	if not w==2:raise s
except:
	with E(N,O)as B7:B7.write('0000\n0000\n')
try:
	with E(BM,T)as AK:w=A6(AK.readlines())
	if not w==4:raise s
except:
	with E(BM,O)as B7:B7.write('40\n10\n90\n10\n')
try:
	with E(m)as AL:W=AL.read()
	if D or B:F('Found existing salt')
except:
	if D or B:F(Bn)
	W=B4()
	with E(m,O)as AL:AL.write(W)
try:x=DS3231(i2c_r);x.get_time(set_rtc=H)
except:pass
CC=A_.Partition(A_.Partition.RUNNING)
c=B_(url='https://raw.githubusercontent.com/Smart-Habitat/smart-habitat-firmware/refs/heads/master/ota/',watchdog=g,light_activities={'good_light':R,'error_light':Aa},platform=A1)
if D or B:F('Loaded global variables!')
g.feed()
try:b.remove(AQ)
except:pass
try:b.remove(AO)
except:pass
try:b.remove(AS)
except:pass
from default_api_cert import base64_cert_and_key as B8
with E(Bo,Av)as CD:CD.write(AA(B8[BN]))
with E(Bp,Av)as CE:CE.write(AA(B8[BO]))
del B8
L.collect()
h=C0()
CORS(h,allowed_origins='*',allow_credentials=H,max_age=20,expose_headers=[z,o,a,BP,'Access-Control-Allow-Methods','Access-Control-Allow-Headers','Access-Control-Request-Method','Access-Control-Expose-Headers','Access-Control-Allow-Credentials'])
@h.route('/control',methods=[AV,f])
async def CQ(request):
	C=request;global W;global G;E=C.headers
	if not E or a not in E or E[a]!=G:return A0,401
	A=C.json
	if A:
		try:F=A[K][v]
		except:F={}
		try:A=A[K][AT]
		except:A={}
	else:F={}
	J=await AB(unit_state=A,query_state=F)
	if J:H={K:{AG:Bq,v:{m:W,l:D or B},P:await Y()}}
	else:H={K:{v:{m:W,l:D or B},P:await Y()}}
	I=q(body=H,status_code=200,headers={o:A9})
	if C.method==f:I.headers[z]=AU
	await R();return I
@h.route('/setup',methods=[AV,f])
async def CR(request):
	A=request;global W;global G;C=A.headers
	if not C or a not in C or C[a]!=G:return A0,401
	E=M;F=A.json
	if F:E=await C6(F)
	if E:H={K:{AG:Bq,v:{m:W,l:D or B},P:await Y()}}
	else:H={K:{v:{m:W,l:D or B},P:await Y()}}
	I=q(body=H,status_code=200,headers={o:A9})
	if A.method==f:I.headers[z]=AU
	return I
@h.route('/salt',methods=[AV,f])
async def CS(request):
	A=request;global W;global G;C=A.headers
	if not C or a not in C or C[a]!=G:return A0,401
	I=A.json
	if I[Br]:
		if D or B:F(Bn)
		W=B4()
		with E(m,O)as J:J.write(W)
	else:raise Bh
	L={K:{AG:'New salt generated!'}};H=q(body=L,status_code=200,headers={o:A9})
	if A.method==f:H.headers[z]=AU
	return H
@h.route('/api_key',methods=[AV,f])
async def CT(request):
	B=request;global G;C=B.headers
	if not C or a not in C or C[a]!=G:return A0,401
	H=B.json
	if H[Br]:
		D=B4(32)
		with E(Ao,O)as I:I.write(D)
		A={Ao:D};A={K:{'new':A}}
	else:A={K:{AG:'New API key not generated!'}}
	F=q(body=A,status_code=200,headers={o:A9})
	try:G=D
	except:pass
	if B.method==f:F.headers[z]=AU
	return F
@h.route(Bs)
@BR
async def CU(request,ws):
	Y='Rebooting';W='No update necessary';V='Update end UTC';U='ERROR!!';S='Update has not yet run after boot!';P='Retrying in 15 seconds!';N='update_log';C=ws;global G;K=i(await C.receive())
	if not K or a not in K or K[a]!=G:await C.send(AH);return A0,401
	try:
		with E(N,T)as I:
			await C.send('Previous run -----------')
			try:
				for F in I:await C.send(F)
			except:pass
			await C.send('End previous run -------')
	except:await C.send(S)
	L=i(await C.receive())
	try:
		if L['auto']:
			try:b.remove(AF);await C.send('Automatic update enabled!')
			except:await C.send('Automatic update was already enabled!')
		else:
			with E(AF,O)as I:I.write('1')
			await C.send('Automatic update disabled!')
	except:pass
	try:
		if L['tail']:
			try:
				with E(N)as I:
					for F in I:await C.send(F)
					if U in F or V in F or W in F or Y in F:await C.send(AH);return M
			except:await C.send(S);await C.send(AH);return M
			Q='';R=0
			while H:
				try:
					with E(N)as I:
						for F in I:0
						if Q==F.encode():R+=1
						Q=F.encode();await C.send(F)
						if R>7 or U in F or V in F or W in F or Y in F:await C.send(AH);return M
				except:break
				await A.sleep(5)
	except:pass
	try:
		if L['start']:
			J=await c.update(X,C,debug=D or B)
			if not J:
				await C.send(P);await A.sleep(15);J=await c.update(X,C,debug=D or B)
				if not J:
					await C.send(P);await A.sleep(15);J=await c.update(X,C,debug=D or B)
					if not J:await C.send(P);await A.sleep(15);J=await c.update(X,C,debug=D or B)
	except:await C.send(AH);return M
@h.route('/debug',methods=[AV,f])
async def CV(request):
	A=request;global D;global G;B=A.headers
	if not B or a not in B or B[a]!=G:return A0,401
	I=A.json
	if I[l]:
		with E(l,O)as J:J.write('1')
		C={K:{AG:'Debugging enabled, please connect the device to a computer to start!'}};F=q(body=C,status_code=200,headers={o:A9});D=H
	else:
		try:b.remove(l)
		except:pass
		C={K:{AG:'Debugging disabled!'}};F=q(body=C,status_code=200,headers={o:A9});D=M
	if A.method==f:F.headers[z]=AU
	return F
@h.route('/poll',methods=['GET',f])
async def CW(request):
	C=request;global W,D,B;global G;A=C.headers
	if not A or a not in A or A[a]!=G:return A0,401
	F={K:{v:{m:W,l:D or B},P:await Y()}};E=q(body=F,status_code=200,headers={o:A9});await R()
	if C.method==f:E.headers[z]=Bt
	return E
@h.route('/metrics')
@BR
async def CX(request,ws):
	O='Sent data through WebSocket';E=ws;global W,D,B;global G;I=i(await E.receive())
	if not I or a not in I or I[a]!=G:await E.send(AH);return A0,401
	J=0;C=e({K:{v:{m:W,l:D or B},P:await Y()}});await E.send(C);await R()
	if D or B:F(O)
	del C;L.collect();M=await AJ()
	while H:
		N=await AJ()
		if M!=N:
			C=e({K:{v:{m:W,l:D or B},P:await Y(N)}});M=N;L.collect();await E.send(C);await R()
			if D or B:F(O)
			L.collect()
		if J<30:J+=1
		else:
			J=0;L.collect();C=e({K:{v:{m:W,l:D or B},P:await Y(M)}});await E.send(C);await R()
			if D or B:F(O)
		await A.sleep(2)
@h.route('/local',methods=['GET',f])
async def CY(request):
	A=q(body='OK',status_code=200,headers={o:BQ});await R()
	if request.method==f:A.headers[z]=Bt
	return A
@h.errorhandler(404)
async def CZ(request):A=q(body='No such endpoint!',status_code=404,headers={o:BQ,BP:'*'});await Aa();return A
@h.errorhandler(Bh)
async def Ca(request,exception):
	A=exception
	if not(D or B):A='Runtime error! Restarting the device is advisable!'
	C=q(body=A,status_code=500,headers={o:BQ,BP:'*'});await Aa();return C
async def Ah():
	global B;A.create_task(CA());C=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
	try:
		with E(AW,'rb'):0
		with E(AX,'rb'):0
		C.load_cert_chain(AW,AX)
		if D or B:F('Using IP specific API certificate')
	except:
		C.load_cert_chain(Bo,Bp)
		if D or B:F('Using default API certificate')
	await h.start_server(port=443,debug=D or B,ssl=C)
def CF(topic,msg,retained):
	H=msg;A.create_task(R())
	try:
		H=H.decode()
		if D or B:F('MQTT message received: '+H)
		C=i(H)
		if K in C:
			try:C=C[K][AT]
			except:
				C=C[K]
				if J not in C and N not in C and AE not in C:C={}
		elif AT in C:C=C[AT]
		if J not in C and N not in C and AE not in C:C={}
		if C:
			for I in C:
				if I==AE:
					with E(AS,'a')as G:G.write(e({I:Aw}));G.write(U)
				else:
					for M in C[I]:
						with E(AS,'a')as G:G.write(e({I:{M:Aw}}));G.write(U)
			L.collect()
		A.create_task(AB(unit_state=C))
	except s as O:
		if D or B:F(O)
		pass
async def CG(client):global Bd;await client.subscribe(Bd,1)
async def CH(client,anon_hash=Aw):
	h='Collected anonymized data';c='anon_hash';a='Sent state to MQTT broker';Z='last_mqtt_update';X=anon_hash;U=client;global AC,Ai;d=0;Q=0;G={K:{P:await Y()}};G=e(G);await U.publish(AC,G,qos=1);await R()
	if D or B:F(a)
	with E(Z,O)as S:S.write(I(p()))
	G=i(G)
	if N in G[K][P]or J in G[K][P]or Au in G[K][P]:
		if X:
			M=await B5(G);M.update({c:X});M=e(M);await U.publish(Ai,M,qos=1);await R();del M
			if D or B:F(h)
			L.collect()
	del G;L.collect();G={K:{P:await Y()}};G=e(G);await U.publish(AC,G,qos=1);await R()
	if D or B:F(a)
	with E(Z,O)as S:S.write(I(p()))
	del G;V=await AJ()
	while H:
		W=await AJ()
		if V!=W:
			f=C5(V,W);Q+=1
			if V[J][n]<=1200:
				if Q<=6:G={K:{P:await Y(f)}}
				else:Q=0;G={K:{P:await Y(W)}}
			elif Q<=4:G={K:{P:await Y(f)}}
			else:Q=0;G={K:{P:await Y(W)}}
			V=W;del W;L.collect();G=e(G);await U.publish(AC,G,qos=1);await R()
			if D or B:F('Sent new state to MQTT broker')
			with E(Z,O)as S:S.write(I(p()))
			try:
				with E(AS,T)as j:
					for g in j:
						k=e({K:{AT:i(g)}});await U.publish(AC,k,qos=1)
						if D or B:F('Deleted desired values from MQTT broker: '+g)
						await A.sleep(1)
				try:b.remove(AS)
				except:pass
			except:pass
			G=i(G)
			if N in G[K][P]or J in G[K][P]or Au in G[K][P]:
				if X:M=await B5(G);M.update({c:X});M=e(M);await U.publish(Ai,M,qos=1);await R();del M;L.collect()
			del G;L.collect()
		with E(Z)as S:l=C(S.read())
		if p()-l>900:
			del W;L.collect()
			if V[J][n]<=1200:
				if Q<=6:G={K:{P:await Y({})}}
				else:Q=0;G={K:{P:await Y(V)}}
			elif Q<=3:G={K:{P:await Y({})}}
			else:Q=0;G={K:{P:await Y(V)}}
			G=e(G);await U.publish(AC,G,qos=1);await R()
			if D or B:F(a)
			with E(Z,O)as S:S.write(I(p()))
			if X:
				M=await B5(i(G));M.update({c:X});M=e(M);await U.publish(Ai,M,qos=1);await R();del M;L.collect()
				if D or B:F(h)
			del G;L.collect()
		if d<2160:d+=1
		else:raise s
		await A.sleep(5)
async def Be(anon_hash=Aw):
	global Aj
	while H:
		try:await A.wait_for(Aj.connect(),50);await CH(Aj,anon_hash)
		except s as C:
			await Aa()
			if D or B:F(C)
			try:Aj.close()
			except:pass
			if D or B:F('MQTT connection closed, reconnecting...')
			await A.sleep(10)
		L.collect()
g.feed()
B9=M
B6=M
try:
	with E(BJ,T)as Bf:BA=Bf.readline().strip();BB=Bf.readline().strip()
	B9=H
	if D or B:F('WiFi file available')
	BX(BA,BB)
	if D or B:F('WiFi connected')
	CI=HttpClient();CJ=Q.WLAN(Q.STA_IF);Ak=CJ.ifconfig()[0]
	try:
		with E(Bu)as BC:CK=BC.read()
		if Ak!=CK:raise s
		with E(AW):0
		with E(AX):0
	except:
		try:
			try:
				if t:Bg={'ip':Ak,BK:d,Bj:t}
				else:raise s
			except:Bg={'ip':Ak,BK:d}
			BD=CI.post('https://httpscert.amastech.cloud/',json=Bg)
			if BD:
				if D or B:F('Got API certificates')
				Al=BD.json()
				if D or B:F(Al)
				with E(AW,Av)as CL:CL.write(AA(Al[BN]))
				with E(AX,Av)as CM:CM.write(AA(Al[BO]))
				with E(Bu,O)as BC:BC.write(Ak)
				del Al,BD;L.collect()
				if D or B:F('Saved API certificates')
		except:
			try:b.remove(AW)
			except:pass
			try:b.remove(AX)
			except:pass
	try:
		with E(At,T)as BE:A5=i(BE.read())
		if D or B:F('Using saved device certificates')
		AD=A5[BL]
		if D or B:F(Bv+AD)
		CN=AA(A5[BN]);CO=AA(A5[BO]);del A5;A2=0;A3=0;Bd=Bw+AD+Bx+k+'/update/delta';AC=Bw+AD+Bx+k+Bs;Ai='$aws/rules/anonymized_data_collection/device/'+k+'/data';r['server']='iotcore.amastech.cloud';r['port']=8883;r['client_id']=k.encode();r['ssid']=BA;r['wifi_pw']=BB;r['ssl']=H;r['ssl_params']={'cert':CN,'key':CO};r['subs_cb']=CF;r['connect_coro']=CG;BS.DEBUG=B or D;Aj=BS(r);A.create_task(AB());L.collect();g.feed()
		if D or B:F(Ax)
		A.create_task(Bb());A.create_task(Ag());A.create_task(Bc());A.create_task(Ab());A.create_task(Ac());A.create_task(Ae());A.create_task(Ad());A.create_task(Af());g.feed()
		try:
			with E(As)as Cb:
				if D or B:F('No telemtry selected')
			A.create_task(Be())
		except:
			if D or B:F('Anonymous telemetry selected')
			with E(m)as AL:W=AL.read()
			BF=C1.sha256((AD+k+W).encode());BF=hexlify(BF.digest())
			if D or B:F('Got hash, continuing with services')
			A.create_task(Be(BF))
		g.feed();A.run(Ah())
	except:
		A2=0;A3=1;L.collect();A.create_task(AB())
		if D or B:F(Ax)
		g.feed();A.create_task(Bb());A.create_task(Ag());A.create_task(Bc());A.create_task(Ab());A.create_task(Ac());A.create_task(C9());A.create_task(Ae());A.create_task(Ad());A.create_task(Af());g.feed();A.run(Ah())
except:
	B6=H
	try:
		with E(At,T)as BE:A5=i(BE.read())
		AD=A5[BL]
		if D or B:F(Bv+AD)
		del A5;A2=1;A3=0;B3();A.create_task(AB())
		if D or B:F(Ax)
		g.feed()
		if B9:
			if D or B:F(By)
			A.create_task(Ag())
		A.create_task(Ab());A.create_task(Ac());A.create_task(C8());A.create_task(Ae());A.create_task(Ad());A.create_task(Af());g.feed();A.run(Ah())
	except:
		A2=1;A3=1;B3();A.create_task(AB())
		if D or B:F(Ax)
		g.feed()
		if B9:
			if D or B:F(By)
			A.create_task(Ag())
		A.create_task(Ab());A.create_task(Ac());A.create_task(C7());A.create_task(Ae());A.create_task(Ad());A.create_task(Af());g.feed();A.run(Ah())
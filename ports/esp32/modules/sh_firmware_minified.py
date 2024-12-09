#### COPYRIGHT SMART HABITAT ####
## LICENSED UNDER AGPL-3.0 ##
#### COPYRIGHT SMART HABITAT ####

C9="Couldn't connect to the WiFi!"
C8='/shadow/name/'
C7='$aws/things/'
C6='Registered under: '
C5='old_ip'
C4='dev_id'
C3='OPTIONS, GET'
C2='/update'
C1='generate'
C0='DEVICE REBOOTING IN 10 SECONDS!'
B_='def_key.der'
Bz='def_cert.der'
By='Creating new salt'
Bx='sensors'
Bw='run_finder'
Bv='alerts.json'
Bu='dhcp_hostname'
Bt=RuntimeError
Bb='text/plain'
Ba='Access-Control-Allow-Origin'
BZ='base64_DER_key'
BY='base64_DER_cert'
BX='ambient_limit'
BW='cust_id_token'
BV='del_cert'
BU='wifi'
BT='name'
BS='anonymous_data_collection'
BR='\x00'
B6='Starting services'
B5=None
B4='wb'
B3='firmware_version'
B2='device_id'
B1='username'
B0='https://devicecert.smarthabitat.in/'
A_='no_telemetry'
Az='smart-habitat-'
Ay=dict
Ax=bytearray
Ai='key.der'
Ah='cert.der'
Ag='POST'
Af='OPTIONS, POST'
Ae='desired'
Ad='null_desire'
Ac='serial'
Ab='api_key'
Aa='friendly_name'
AZ='drain_check'
AY='powered'
AX='light_override'
AW='off'
AV='on'
AP='close cmd'
AO='note'
AN='stale_cert'
AM='cert_id'
AL='no_auto_update'
AK='auto_update'
AC='application/json'
AB='customer.json'
AA='override'
A9=len
A8=bool
A2='Unauthorized'
A1='Allow'
A0=type
x='admin'
w='cust_id'
v='runtime'
t=Exception
p='Content-Type'
o='interval'
n='salt'
m='debug'
i='OPTIONS'
c='x-api-key'
U='\n'
T=range
Q='reported'
P='r'
O='w'
N='light'
M=False
K='state'
J='pump'
I=str
H=True
F=print
D=int
B=open
import network as R,gc as L,os as W
from httpclient import HttpClient as B7
from machine import WDT
from ubinascii import hexlify
from time import sleep,localtime as B8,time as q,gmtime
from sht3x import SHT3x_Sensor as CA
from ota_updater import OTAUpdater as CB
from ujson import loads as d,dumps as e
from ds3231_port import DS3231
import machine as B9,sys,esp32 as BA,uasyncio as A
from ntptime import settime as BB
from microdot import Microdot as CC,Response as r
from microdot.websocket import with_websocket as Bc
from microdot.cors import CORS
from mqtt_as import MQTTClient as Bd,config as s
import uhashlib as CD,random,string as Be
from httpclient import HttpClient as B7
import ssl
from binascii import a2b_base64 as AD
Y='v0.1.0'
Aj=BA.NVS('nvs')
C=M
Ak=M
if Y.split('.')[0]=='v0':E=H
else:
	try:
		with B(m):E=H
	except:E=M
try:
	with B('platform')as CE:AE=CE.read().strip()
	C=H
except:
	try:AE=Ax(25);Aj.get_blob(b'platform',AE);AE=AE.decode().split(BR)[0]
	except:sys.exit()
if'ESP32_S3_N8R2'in AE:from vars_ESP32_GENERIC_S3 import amb_scl as Bf,amb_sda as Bg,analog_water_sensor as Bh,water_power as BC,hard_reset_button,network_reset_button,pump as k,light as a,err_light as V,dat_light as BD,i2c_r
else:F('Unsupported board!!');sys.exit()
g=WDT(timeout=60000)
F('Thank you for choosing Smart Habitat!')
def Bi(ssid,password):
	global b,C
	if C:
		try:
			global u
			if u:R.hostname(Az+u.lower())
			else:raise t
		except:R.hostname(Az+b.lower())
	else:R.hostname(Az+b.lower())
	A=R.WLAN(R.STA_IF)
	if R.WLAN(R.AP_IF).active():R.WLAN(R.AP_IF).active(M)
	A.active(H)
	if E or C:F('Connecting to: '+ssid)
	A.connect(ssid,password)
	for B in T(15):
		sleep(1)
		if A.isconnected():break
		elif B==14:A.active(M);raise OSError
def BE():
	global G,b;A=R.WLAN(R.AP_IF)
	if R.WLAN(R.STA_IF).active():R.WLAN(R.STA_IF).active(M)
	A.active(H);A.config(essid=Az+b.lower(),authmode=R.AUTH_WPA_WPA2_PSK,password=G)
def Ca(file_object,chunk_size=1024):
	while H:
		A=file_object.read(chunk_size)
		if not A:break
		yield A
def AF(n=16):
	A=''
	for B in T(0,n):A=A+random.choice(Be.ascii_lowercase+Be.digits)
	return A
def CF(old,new):
	F=old;C=new;D={}
	for A in C:
		if A0(C[A])is Ay:
			for B in C[A]:
				if A0(C[A][B])is Ay:
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
def Bj():
	if gmtime(0)[0]==2000:A=q()+946684800
	else:A=q()
	return A
async def Bk():
	global Bf,Bg
	try:C=CA(freq=100000,sclpin=Bf,sdapin=Bg)
	except:return-9999,-9999
	try:B=C.read_temp_humd()
	except:
		A.sleep(1)
		try:B=C.read_temp_humd()
		except:
			A.sleep(1)
			try:B=C.read_temp_humd()
			except:return-9999,-9999
	if D(B[0])==-45 and D(B[1])==0:return-9999,-9999
	return B[0],B[1]
async def Bl():
	global BC,Bh;BC.value(1);A.sleep(.1);B=Bh.read();B=B/4500*100;BC.value(0)
	if B<15:B=-9999
	return B
async def S():global BD;BD.value(1);A.sleep(.05);BD.value(0)
async def Al():global V;V.value(1);A.sleep(.1);V.value(0)
async def AG(unit_state={},query_state={}):
	b=query_state;G=unit_state;global k,a;c=M
	with B(N,P)as f:Q=f.readline().strip();R=f.readline().strip()
	L.collect()
	with B(J,P)as K:
		try:V=A8(D(K.readline().strip()));X=D(K.readline().strip());Y=D(K.readline().strip())
		except:V=A8(K.readline());X=D(K.readline().strip());Y=D(K.readline().strip())
	L.collect()
	if G:
		if E or C:F(G)
		if N in G:
			try:
				if D(G[N][AV])in T(0,2400):
					if D(G[N][AV][:2])in T(0,24)and D(G[N][AV][2:])in T(0,60):Q=G[N][AV]
			except:pass
			try:
				if D(G[N][AW])in T(0,2400):
					if D(G[N][AW][:2])in T(0,24)and D(G[N][AW][2:])in T(0,60):R=G[N][AW]
			except:pass
			with B(N,O)as f:f.write(Q+U+R+U)
			try:
				if G[N][AA]=='1'or G[N][AA]=='0'or G[N][AA]==M:
					if G[N][AA]!=M:
						a.value(D(G[N][AA]))
						with B(AX,O)as n:n.write(G[N][AA])
					else:
						try:W.remove(AX)
						except:pass
			except:
				try:Z=y.get_time(set_rtc=M)
				except:Z=B8()
				g=I(Z[3])+(I(Z[4])if A9(I(Z[4]))==2 else'0'+I(Z[4]))
				if R==Q:a.value(0)
				elif D(Q)<D(R):
					if D(g)in T(D(Q),D(R)):a.value(1)
					else:a.value(0)
				elif D(Q)>D(R):
					if D(g)in T(D(Q),2400)or D(g)in T(0,D(R)):a.value(1)
					else:a.value(0)
				del g,Z;L.collect()
		if J in G:
			try:
				if G[J][AY]==M or G[J][AY]==H:
					with B(J,O)as K:K.write(I(D(G[J][AY]))+U+I(X)+U+I(Y)+U)
					V=G[J][AY]
				if not V:k.value(0)
				L.collect()
			except:pass
			try:
				if A0(G[J][o])is D and G[J][o]in T(600,86401):
					with B(J,O)as K:K.write(I(D(V))+U+I(G[J][o])+U+I(Y)+U)
					X=G[J][o]
				if A0(G[J][o])is not D and D(G[J][o])in T(600,86401):K.write(I(D(V))+U+I(D(G[J][o]))+U+I(Y)+U);X=D(G[J][o])
				L.collect()
			except:pass
			try:
				if A0(G[J][v])is D and G[J][v]in T(60,86401):
					with B(J,O)as K:K.write(I(D(V))+U+I(X)+U+I(G[J][v])+U)
					Y=G[J][v]
				if A0(G[J][v])is not D and D(G[J][v])in T(60,86401):K.write(I(D(V))+U+I(X)+U+I(D(G[J][v])+U));Y=D(G[J][v])
				L.collect()
			except:pass
			try:
				if G[J]['drain']:
					with B(AZ,O)as p:p.write('1')
					k.value(1)
				else:
					try:W.remove(AZ)
					except:pass
					k.value(0)
			except:pass
		if AK in G:
			q=G[AK]
			if q:
				try:W.remove(AL)
				except:pass
			else:
				with B(AL)as r:r.write('1')
		if BS in G:
			s=G[BS]
			if s:
				try:W.remove(A_)
				except:pass
			else:
				with B(A_)as t:t.write('1')
		if Aa in G:
			with B(BT,O)as u:u.write(I(G[Aa]))
	if b:
		if E or C:F(b)
		try:
			if b['restart']:
				for h in T(3):await S()
				A.create_task(A5());c=H
		except:pass
		try:
			if b['network-reset']:
				for h in T(3):await S()
				try:W.remove(BU)
				except:pass
				A.create_task(A5());c=H
		except:pass
		try:
			if b['factory-reset']:
				try:
					with B(AB,P)as x:l=d(x.read())
					i=l[AM];j=l[w]
				except:pass
				for h in T(3):await S()
				for h in W.listdir('/'):
					try:W.remove(h)
					except:pass
				m=B7()
				try:
					try:z=m.post(B0,json={BV:{w:j,AM:i}})
					except:await A.sleep(1);L.collect();z=m.post(B0,json={BV:{w:j,AM:i}})
				except:
					with B(AN,O)as A1:A1.write(e({w:j,AM:i}))
				A.create_task(A5());c=H
		except:pass
	if c:return H
	return M
async def CG(setup_dic):
	C=setup_dic;global A3,A4,Ak;D=M
	if Aa in C:
		with B(BT,O)as F:F.write(I(C[Aa]))
	if A3:
		try:
			with B(BU,O)as G:G.write(I(C['ssid'])+U+I(C['password']))
			D=H;await S()
		except:pass
	if A4:
		try:
			with B(BW,O)as J:J.write(C['id_token'])
			D=H;await S()
		except:pass
	if Ak:
		try:
			with B(B1,O)as K:E=C[B1];L=E+I(q());K.write(E+U+L)
			D=H;await S()
		except:pass
		try:
			with B(B2,P)as N:N.write(C[B2])
			D=H;await S()
		except:pass
	if D:A.create_task(A5());return H
	return M
async def AQ():
	f='status';global k,a,h,b,C,G,A4;g={Ab:G};O=R.WLAN(R.STA_IF)
	if O.active():E=O.ifconfig()[0]
	else:E='192.168.4.1'
	with B(J,P)as F:i=A8(D(F.readline().strip()));j=D(F.readline().strip());l=D(F.readline().strip())
	m=A8(k.value())
	with B(N,P)as Q:S=Q.readline().strip();T=Q.readline().strip()
	n=A8(a.value())
	try:p=B(AZ,P);U=H;p.close()
	except:U=M
	try:
		with B(AX,P)as q:V=q.read()
	except:V=M
	try:
		with B(AL)as A0:X=M
	except:X=H
	try:
		with B(A_)as A1:Z=M
	except:Z=H
	L.collect();A={B2:h,Ac:b,N:{f:n,AV:S,AW:T,AA:V},J:{AY:i,o:j,v:l,f:m,'drain':U},'internal_ip':E,AK:X,BS:Z};del E,S,T;L.collect();A.update(g)
	try:
		with B(AB)as r:I=d(r.read())
		s=I[w];K=I['cert_exp'];c=Bj()
		if c>float(K):W.remove(AB);B9.reset()
		elif c>=float(K)-2592000:A4=1;e=H
		else:e=M
		del I;L.collect();A.update({'customer_id':s,'device_certificate':{'expiration:':K,'renewal_period_active':e}})
	except:pass
	try:
		with B(BT)as t:x=t.read()
		A.update({Aa:x})
	except:pass
	if C:
		try:global u;A.update({Bu:u})
		except:pass
	A.update({B3:Y})
	with B(Bv,P)as y:z=d(y.read())
	A.update(z);return A
async def Z(unit_state=Bw):
	A=unit_state;C,D=await Bk();E=await Bl();B={Bx:{'environment':{'temperature':C,'humidity':D},'water_level':E}}
	if A:
		if A==Bw:B.update(await AQ())
		else:B.update(A)
	del C,D,E;L.collect();return B
async def BF(payload):
	A=payload;D={};F=Bj()
	if A:
		A=A[K][Q]
		for B in A:
			if B in[N,J,B3]:
				if A0(A[B])is Ay:
					for C in A[B]:D[B+'_'+C]=A[B][C]
				else:D[B]=A[B]
			if B==Bx:
				for C in A[B]:
					if A0(A[B][C])is Ay:
						for E in A[B][C]:
							if not A[B][C][E]==-9999:D[C+'_'+E]=A[B][C][E]
					elif not A[B][C]==-9999:D[C]=A[B][C]
	D.update({'iso':F});return D
async def A5():
	if E or C:F('Restarting device in 10 seconds!')
	await A.sleep(10);B9.reset()
async def Am():0
async def An():0
async def Ao():
	global k;await A.sleep(600)
	while H:
		try:
			with B(AZ,P)as I:k.value(1)
		except:
			with B(J,P)as C:
				try:E=A8(D(C.readline().strip()));F=D(C.readline().strip());G=D(C.readline().strip())
				except:E=A8(C.readline().strip());F=D(C.readline().strip());G=D(C.readline().strip())
			L.collect()
			if E:k.value(1);await A.sleep(G);k.value(0)
			else:k.value(0)
		await A.sleep(F)
async def Ap():
	global a
	try:global y;C=y.get_time(set_rtc=M)
	except:C=B8()
	while H:
		try:
			with B(AX,P)as K:
				O=D(K.readline().strip())
				if O:a.value(1)
				else:a.value(0)
		except:
			with B(N,P)as J:E=J.readline().strip();F=J.readline().strip()
			L.collect();G=I(C[3])+(I(C[4])if A9(I(C[4]))==2 else'0'+I(C[4]))
			if F==E:a.value(0)
			elif D(E)<D(F):
				if D(G)in T(D(E),D(F)):a.value(1)
				else:a.value(0)
			elif D(E)>D(F):
				if D(G)in T(D(E),2400)or D(G)in T(0,D(F)):a.value(1)
				else:a.value(0)
		await A.sleep(30)
async def Aq():
	S='High';N='Low';K='Sensor Error'
	while H:
		if not k.value():
			P=await Bl()
			if P==-9999:G=K
			elif P<25:G=N
			else:G=M
			with B(BX)as C:T=D(C.readline().strip());U=D(C.readline().strip());V=D(C.readline().strip());W=D(C.readline().strip())
			I,J=await Bk()
			if I>T:E=S
			elif I==-9999:E=K
			elif I<U:E=N
			else:E=M
			if J>V:F=S
			elif J==-9999:F=K
			elif J<W:F=N
			else:F=M
			Q={'alerts':{'water_level_alert':G,'temperature_alert':E,'humidity_alert':F}}
			with B(Bv,O)as R:R.write(e(Q))
			del Q,R;L.collect()
		g.feed();await A.sleep(10)
async def CH():
	global V
	while H:V.value(1);await A.sleep(.5);V.value(0);await A.sleep(1)
async def CI():
	global V
	while H:V.value(1);await A.sleep(.1);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.1);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.1);V.value(0);await A.sleep(1)
async def CJ():
	global V
	while H:V.value(1);await A.sleep(.1);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.25);V.value(0);await A.sleep(.05);V.value(1);await A.sleep(.1);V.value(0);await A.sleep(1)
async def Bm():
	while H:
		try:BB()
		except:
			await A.sleep(120)
			try:BB()
			except:
				await A.sleep(120)
				try:BB()
				except:pass
		try:global y;y.save_time()
		except:pass
		await A.sleep(86400)
async def Ar():
	global A3,BG
	while H:
		B=R.WLAN(R.STA_IF)
		if not B.active():
			try:
				Bi(BL,BM)
				if BG:B9.reset()
			except:A3=1;BE()
		del B;L.collect();await A.sleep(600)
async def Bn():
	try:global y
	except:pass
	G=0
	while H:
		try:
			with B(AL)as V:0
			Q=900
		except:
			try:L=y.get_time(set_rtc=M)
			except:L=B8()
			R=I(L[3])+(I(L[4])if A9(I(L[4]))==2 else'0'+I(L[4]))
			with B(N,P)as S:J=S.readline().strip();K=S.readline().strip()
			Q=900
			if K==J:
				for U in T(0,48):
					await A.sleep(900)
					if not K==J:break
					if U==47:
						G=G+1
						if G==6:await A5()
						F=await f.update(Y,debug=E or C)
						if not F:
							await A.sleep(15);F=await f.update(Y,debug=E or C)
							if not F:
								await A.sleep(15);F=await f.update(Y,debug=E or C)
								if not F:await A.sleep(15);F=await f.update(Y,debug=E or C)
			elif D(K)<D(J):
				O=I(D((D(K)+D(J))/2))[:-2]
				if D(O+'00')<D(R)<D(O+'20'):
					G=G+1
					if G==6:await A5()
					F=await f.update(Y,debug=E or C)
					if not F:
						await A.sleep(15);F=await f.update(Y,debug=E or C)
						if not F:
							await A.sleep(15);F=await f.update(Y,debug=E or C)
							if not F:await A.sleep(15);F=await f.update(Y,debug=E or C)
			elif D(K)>D(J):
				O=I(D((D(K)-D(J))/2))[:-2]
				if D(O+'00')<D(R)<D(O+'20'):
					G=G+1
					if G==6:await A5()
					F=await f.update(Y,debug=E or C)
					if not F:
						await A.sleep(15);F=await f.update(Y,debug=E or C)
						if not F:
							await A.sleep(15);F=await f.update(Y,debug=E or C)
							if not F:await A.sleep(15);F=await f.update(Y,debug=E or C)
		await A.sleep(Q)
async def CK():
	await A.sleep(65)
	if E or C:F('All services started successfully!')
	CN.mark_app_valid_cancel_rollback()
	if E or C:F('Since no errors were found, marked boot partition as valid!')
try:
	with B(Ab,P)as BH:G=BH.readline().strip();F('Found existing API key:');F(G)
except:
	try:G=Ax(32);Aj.get_blob(b'api_key',G);G=G.decode();L.collect()
	except:
		F('No API keys found, creating new API key...');Bo=AF(32)
		with B(Ab,O)as BH:BH.write(Bo)
		G=Bo;F('NEW API KEY IS:');F(G);F("PLEASE SAVE THIS API KEY, YOU'LL NEED IT TO COMMUNICATE WITH YOUR DEVICE!!")
try:
	with B(B2)as CL:h=CL.read()
	C=H
except:
	try:h=Ax(64);Aj.get_blob(b'device_id',h);h=h.decode().split(BR)[0]
	except:h='nodeviceidset_'+I(q())+'_'+AF(5);Ak=H
try:
	with B(B1)as AR:z=A9(AR.readlines())
	with B(B1)as AR:
		if z==1:b=u=AR.read().strip()
		elif z==2:b=AR.readline().strip();u=AR.readline().strip()
		else:raise t
	C=H
except:
	try:b=Ax(25);Aj.get_blob(b'serial',b);b=b.decode().split(BR)[0];u=M
	except:b='noserialset_'+I(q())+'_'+AF(5);Ak=H
if E or C:F('Loaded device identifiers!')
try:
	with B(J,P)as AS:z=A9(AS.readlines())
	if not z==3:raise t
except:
	with B(J,O)as CM:CM.write('0\n600\n60\n')
try:
	with B(N,P)as AS:z=A9(AS.readlines())
	if not z==2:raise t
except:
	with B(N,O)as BI:BI.write('0000\n0000\n')
try:
	with B(BX,P)as AS:z=A9(AS.readlines())
	if not z==4:raise t
except:
	with B(BX,O)as BI:BI.write('40\n10\n90\n10\n')
try:
	with B(n)as AT:X=AT.read()
	if E or C:F('Found existing salt')
except:
	if E or C:F(By)
	X=AF()
	with B(n,O)as AT:AT.write(X)
try:y=DS3231(i2c_r);y.get_time(set_rtc=H)
except:pass
CN=BA.Partition(BA.Partition.RUNNING)
f=CB(url='https://raw.githubusercontent.com/Smart-Habitat/smart-habitat-firmware/refs/heads/master/ota/',watchdog=g,light_activities={'good_light':S,'error_light':Al},platform=AE)
if E or C:F('Loaded global variables!')
g.feed()
try:W.remove(AZ)
except:pass
try:W.remove(AX)
except:pass
try:W.remove(Ad)
except:pass
from default_api_cert import base64_cert_and_key as BJ
with B(Bz,B4)as CO:CO.write(AD(BJ[BY]))
with B(B_,B4)as CP:CP.write(AD(BJ[BZ]))
del BJ
L.collect()
j=CC()
CORS(j,allowed_origins='*',allow_credentials=H,max_age=20,expose_headers=[A1,p,c,Ba,'Access-Control-Allow-Methods','Access-Control-Allow-Headers','Access-Control-Request-Method','Access-Control-Expose-Headers','Access-Control-Allow-Credentials'])
@j.route('/control',methods=[Ag,i])
async def Cb(request):
	B=request;global X;global G;D=B.headers
	if not D or c not in D or D[c]!=G:return A2,401
	A=B.json
	if A:
		try:F=A[K][x]
		except:F={}
		try:A=A[K][Ae]
		except:A={}
	else:F={}
	J=await AG(unit_state=A,query_state=F)
	if J:H={K:{AO:C0,x:{n:X,m:E or C},Q:await Z()}}
	else:H={K:{x:{n:X,m:E or C},Q:await Z()}}
	I=r(body=H,status_code=200,headers={p:AC})
	if B.method==i:I.headers[A1]=Af
	await S();return I
@j.route('/setup',methods=[Ag,i])
async def Cc(request):
	A=request;global X;global G;B=A.headers
	if not B or c not in B or B[c]!=G:return A2,401
	D=M;F=A.json
	if F:D=await CG(F)
	if D:H={K:{AO:C0,x:{n:X,m:E or C},Q:await Z()}}
	else:H={K:{x:{n:X,m:E or C},Q:await Z()}}
	I=r(body=H,status_code=200,headers={p:AC})
	if A.method==i:I.headers[A1]=Af
	return I
@j.route('/salt',methods=[Ag,i])
async def Cd(request):
	A=request;global X;global G;D=A.headers
	if not D or c not in D or D[c]!=G:return A2,401
	I=A.json
	if I[C1]:
		if E or C:F(By)
		X=AF()
		with B(n,O)as J:J.write(X)
	else:raise Bt
	L={K:{AO:'New salt generated!'}};H=r(body=L,status_code=200,headers={p:AC})
	if A.method==i:H.headers[A1]=Af
	return H
@j.route('/api_key',methods=[Ag,i])
async def Ce(request):
	C=request;global G;D=C.headers
	if not D or c not in D or D[c]!=G:return A2,401
	H=C.json
	if H[C1]:
		E=AF(32)
		with B(Ab,O)as I:I.write(E)
		A={Ab:E};A={K:{'new':A}}
	else:A={K:{AO:'New API key not generated!'}}
	F=r(body=A,status_code=200,headers={p:AC})
	try:G=E
	except:pass
	if C.method==i:F.headers[A1]=Af
	return F
@j.route(C2)
@Bc
async def Cf(request,ws):
	Z='Rebooting';X='No update necessary';V='Update end UTC';U='ERROR!!';T='Update has not yet run after boot!';Q='Retrying in 15 seconds!';N='update_log';D=ws;global G;K=d(await D.receive())
	if not K or c not in K or K[c]!=G:await D.send(AP);return A2,401
	try:
		with B(N,P)as I:
			await D.send('Previous run -----------')
			try:
				for F in I:await D.send(F)
			except:pass
			await D.send('End previous run -------')
	except:await D.send(T)
	L=d(await D.receive())
	try:
		if L['auto']:
			try:W.remove(AL);await D.send('Automatic update enabled!')
			except:await D.send('Automatic update was already enabled!')
		else:
			with B(AL,O)as I:I.write('1')
			await D.send('Automatic update disabled!')
	except:pass
	try:
		if L['tail']:
			try:
				with B(N)as I:
					for F in I:await D.send(F)
					if U in F or V in F or X in F or Z in F:await D.send(AP);return M
			except:await D.send(T);await D.send(AP);return M
			R='';S=0
			while H:
				try:
					with B(N)as I:
						for F in I:0
						if R==F.encode():S+=1
						R=F.encode();await D.send(F)
						if S>7 or U in F or V in F or X in F or Z in F:await D.send(AP);return M
				except:break
				await A.sleep(5)
	except:pass
	try:
		if L['start']:
			J=await f.update(Y,D,debug=E or C)
			if not J:
				await D.send(Q);await A.sleep(15);J=await f.update(Y,D,debug=E or C)
				if not J:
					await D.send(Q);await A.sleep(15);J=await f.update(Y,D,debug=E or C)
					if not J:await D.send(Q);await A.sleep(15);J=await f.update(Y,D,debug=E or C)
	except:await D.send(AP);return M
@j.route('/debug',methods=[Ag,i])
async def Cg(request):
	A=request;global E;global G;C=A.headers
	if not C or c not in C or C[c]!=G:return A2,401
	I=A.json
	if I[m]:
		with B(m,O)as J:J.write('1')
		D={K:{AO:'Debugging enabled, please connect the device to a computer to start!'}};F=r(body=D,status_code=200,headers={p:AC});E=H
	else:
		try:W.remove(m)
		except:pass
		D={K:{AO:'Debugging disabled!'}};F=r(body=D,status_code=200,headers={p:AC});E=M
	if A.method==i:F.headers[A1]=Af
	return F
@j.route('/poll',methods=['GET',i])
async def Ch(request):
	B=request;global X,E,C;global G;A=B.headers
	if not A or c not in A or A[c]!=G:return A2,401
	F={K:{x:{n:X,m:E or C},Q:await Z()}};D=r(body=F,status_code=200,headers={p:AC});await S()
	if B.method==i:D.headers[A1]=C3
	return D
@j.route('/metrics')
@Bc
async def Ci(request,ws):
	O='Sent data through WebSocket';D=ws;global X,E,C;global G;I=d(await D.receive())
	if not I or c not in I or I[c]!=G:await D.send(AP);return A2,401
	J=0;B=e({K:{x:{n:X,m:E or C},Q:await Z()}});await D.send(B);await S()
	if E or C:F(O)
	del B;L.collect();M=await AQ()
	while H:
		N=await AQ()
		if M!=N:
			B=e({K:{x:{n:X,m:E or C},Q:await Z(N)}});M=N;L.collect();await D.send(B);await S()
			if E or C:F(O)
			L.collect()
		if J<30:J+=1
		else:
			J=0;L.collect();B=e({K:{x:{n:X,m:E or C},Q:await Z(M)}});await D.send(B);await S()
			if E or C:F(O)
		await A.sleep(2)
@j.route('/local',methods=['GET',i])
async def Cj(request):
	A=r(body='OK',status_code=200,headers={p:Bb});await S()
	if request.method==i:A.headers[A1]=C3
	return A
@j.errorhandler(404)
async def Ck(request):A=r(body='No such endpoint!',status_code=404,headers={p:Bb,Ba:'*'});await Al();return A
@j.errorhandler(Bt)
async def Cl(request,exception):
	A=exception
	if not(E or C):A='Runtime error! Restarting the device is advisable!'
	B=r(body=A,status_code=500,headers={p:Bb,Ba:'*'});await Al();return B
async def As():
	global C;A.create_task(CK());D=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
	try:
		with B(Ah,'rb'):0
		with B(Ai,'rb'):0
		D.load_cert_chain(Ah,Ai)
		if E or C:F('Using IP specific API certificate')
	except:
		D.load_cert_chain(Bz,B_)
		if E or C:F('Using default API certificate')
	await j.start_server(port=443,debug=E or C,ssl=D)
def CQ(topic,msg,retained):
	H=msg;A.create_task(S())
	try:
		H=H.decode()
		if E or C:F('MQTT message received: '+H)
		D=d(H)
		if K in D:
			try:D=D[K][Ae]
			except:
				D=D[K]
				if J not in D and N not in D and AK not in D:D={}
		elif Ae in D:D=D[Ae]
		if J not in D and N not in D and AK not in D:D={}
		if D:
			for I in D:
				if I==AK:
					with B(Ad,'a')as G:G.write(e({I:B5}));G.write(U)
				else:
					for M in D[I]:
						with B(Ad,'a')as G:G.write(e({I:{M:B5}}));G.write(U)
			L.collect()
		A.create_task(AG(unit_state=D))
	except t as O:
		if E or C:F(O)
		pass
async def CR(client):global Bp;await client.subscribe(Bp,1)
async def CS(client,anon_hash=B5):
	i='Collected anonymized data';c='anon_hash';b='Sent state to MQTT broker';a='last_mqtt_update';Y=anon_hash;U=client;global AH,At;f=0;R=0;G={K:{Q:await Z()}};G=e(G);await U.publish(AH,G,qos=1);await S()
	if E or C:F(b)
	with B(a,O)as T:T.write(I(q()))
	G=d(G)
	if N in G[K][Q]or J in G[K][Q]or B3 in G[K][Q]:
		if Y:
			M=await BF(G);M.update({c:Y});M=e(M);await U.publish(At,M,qos=1);await S();del M
			if E or C:F(i)
			L.collect()
	del G;L.collect();G={K:{Q:await Z()}};G=e(G);await U.publish(AH,G,qos=1);await S()
	if E or C:F(b)
	with B(a,O)as T:T.write(I(q()))
	del G;V=await AQ()
	while H:
		X=await AQ()
		if V!=X:
			g=CF(V,X);R+=1
			if V[J][o]<=1200:
				if R<=6:G={K:{Q:await Z(g)}}
				else:R=0;G={K:{Q:await Z(X)}}
			elif R<=4:G={K:{Q:await Z(g)}}
			else:R=0;G={K:{Q:await Z(X)}}
			V=X;del X;L.collect();G=e(G);await U.publish(AH,G,qos=1);await S()
			if E or C:F('Sent new state to MQTT broker')
			with B(a,O)as T:T.write(I(q()))
			try:
				with B(Ad,P)as j:
					for h in j:
						k=e({K:{Ae:d(h)}});await U.publish(AH,k,qos=1)
						if E or C:F('Deleted desired values from MQTT broker: '+h)
						await A.sleep(1)
				try:W.remove(Ad)
				except:pass
			except:pass
			G=d(G)
			if N in G[K][Q]or J in G[K][Q]or B3 in G[K][Q]:
				if Y:M=await BF(G);M.update({c:Y});M=e(M);await U.publish(At,M,qos=1);await S();del M;L.collect()
			del G;L.collect()
		with B(a)as T:l=D(T.read())
		if q()-l>900:
			del X;L.collect()
			if V[J][o]<=1200:
				if R<=6:G={K:{Q:await Z({})}}
				else:R=0;G={K:{Q:await Z(V)}}
			elif R<=3:G={K:{Q:await Z({})}}
			else:R=0;G={K:{Q:await Z(V)}}
			G=e(G);await U.publish(AH,G,qos=1);await S()
			if E or C:F(b)
			with B(a,O)as T:T.write(I(q()))
			if Y:
				M=await BF(d(G));M.update({c:Y});M=e(M);await U.publish(At,M,qos=1);await S();del M;L.collect()
				if E or C:F(i)
			del G;L.collect()
		if f<2160:f+=1
		else:raise t
		await A.sleep(5)
async def Bq(anon_hash=B5):
	global Au
	while H:
		try:await A.wait_for(Au.connect(),50);await CS(Au,anon_hash)
		except t as B:
			await Al()
			if E or C:F(B)
			try:Au.close()
			except:pass
			if E or C:F('MQTT connection closed, reconnecting...')
			await A.sleep(10)
		L.collect()
g.feed()
BK=M
BG=M
try:
	with B(BU,P)as Br:BL=Br.readline().strip();BM=Br.readline().strip()
	BK=H
	if E or C:F('WiFi file available')
	Bi(BL,BM)
	if E or C:F('WiFi connected')
	BN=B7()
	try:
		with B(AN)as BO:AI=d(BO.read());W.remove(AN)
		A6=BN.post(B0,json={BV:AI})
	except:pass
	try:
		with B(BW,P)as CT:Bs=CT.read()
		if E or C:F('Customer id_token found, requesting certificates')
		g.feed()
		try:
			with B(AB,P)as A7:l=d(A7.read())
			AI={w:l[w],AM:l[AM]}
		except:
			try:
				with B(AN)as BO:AI=d(BO.read())
				W.remove(AN)
			except:AI=M
		if AI:AU={'token':Bs,C4:h,Ac:b,AN:AI}
		else:AU={'token':Bs,C4:h,Ac:b}
		A6=BN.post(B0,json=AU)
		if A6:
			l=A6.json()
			if E or C:F('Got user certificates')
			with B(AB,O)as A7:A7.write(e(l))
			W.remove(BW)
	except:pass
	CU=R.WLAN(R.STA_IF);Av=CU.ifconfig()[0]
	try:
		with B(C5)as BP:CV=BP.read()
		if Av!=CV:raise t
		with B(Ah):0
		with B(Ai):0
	except:
		try:
			try:
				if u:AU={'ip':Av,Ac:b,Bu:u}
				else:raise t
			except:AU={'ip':Av,Ac:b}
			A6=BN.post('https://httpscert.smarthabitat.in/',json=AU)
			if A6:
				if E or C:F('Got API certificates')
				Aw=A6.json()
				if E or C:F(Aw)
				with B(Ah,B4)as CW:CW.write(AD(Aw[BY]))
				with B(Ai,B4)as CX:CX.write(AD(Aw[BZ]))
				with B(C5,O)as BP:BP.write(Av)
				del Aw,A6;L.collect()
				if E or C:F('Saved API certificates')
		except:
			try:W.remove(Ah)
			except:pass
			try:W.remove(Ai)
			except:pass
	try:
		with B(AB,P)as A7:l=d(A7.read())
		if E or C:F('Using saved device certificates')
		AJ=l[w]
		if E or C:F(C6+AJ)
		CY=AD(l[BY]);CZ=AD(l[BZ]);del l;A3=0;A4=0;Bp=C7+AJ+C8+h+'/update/delta';AH=C7+AJ+C8+h+C2;At='$aws/rules/anonymized_data_collection/device/'+h+'/data';s['server']='iotcore.smarthabitat.in';s['port']=8883;s['client_id']=h.encode();s['ssid']=BL;s['wifi_pw']=BM;s['ssl']=H;s['ssl_params']={'cert':CY,'key':CZ};s['subs_cb']=CQ;s['connect_coro']=CR;Bd.DEBUG=C or E;Au=Bd(s);A.create_task(AG());L.collect();g.feed()
		if E or C:F(B6)
		A.create_task(Bm());A.create_task(Ar());A.create_task(Bn());A.create_task(Am());A.create_task(An());A.create_task(Ap());A.create_task(Ao());A.create_task(Aq());g.feed()
		try:
			with B(A_)as Cm:
				if E or C:F('No telemtry selected')
			A.create_task(Bq())
		except:
			if E or C:F('Anonymous telemetry selected')
			with B(n)as AT:X=AT.read()
			BQ=CD.sha256((AJ+h+X).encode());BQ=hexlify(BQ.digest())
			if E or C:F('Got hash, continuing with services')
			A.create_task(Bq(BQ))
		g.feed();A.run(As())
	except:
		A3=0;A4=1;L.collect();A.create_task(AG())
		if E or C:F(B6)
		g.feed();A.create_task(Bm());A.create_task(Ar());A.create_task(Bn());A.create_task(Am());A.create_task(An());A.create_task(CJ());A.create_task(Ap());A.create_task(Ao());A.create_task(Aq());g.feed();A.run(As())
except:
	BG=H
	try:
		with B(AB,P)as A7:l=d(A7.read())
		AJ=l[w]
		if E or C:F(C6+AJ)
		del l;A3=1;A4=0;BE();A.create_task(AG())
		if E or C:F(B6)
		g.feed()
		if BK:
			if E or C:F(C9)
			A.create_task(Ar())
		A.create_task(Am());A.create_task(An());A.create_task(CI());A.create_task(Ap());A.create_task(Ao());A.create_task(Aq());g.feed();A.run(As())
	except:
		A3=1;A4=1;BE();A.create_task(AG())
		if E or C:F(B6)
		g.feed()
		if BK:
			if E or C:F(C9)
			A.create_task(Ar())
		A.create_task(Am());A.create_task(An());A.create_task(CH());A.create_task(Ap());A.create_task(Ao());A.create_task(Aq());g.feed();A.run(As())
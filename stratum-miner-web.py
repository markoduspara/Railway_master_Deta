from fastapi import FastAPI, Request, BackgroundTasks

import socket
import select
import binascii

import struct
import json
import sys
import os
import time
import requests

import aiohttp
import asyncio

import ssl
import certifi


from multiprocessing.pool import ThreadPool
 

app = FastAPI()

pool_host = 'xmr.2miners.com'
pool_port = 2222
pool_pass = 'x'
wallet_address = ''
nicehash = False
adrese=[]
duration=60
adresa_provjere=''
rigid=''
middleapikey=''
p_hash="0"
p_nonce="0"
#start_time = time.time()

urls=[
    "https://1ranx-1-v1741127.deta.app",
    "https://2randomx-1-e3775184.deta.app",
    "https://3randomx-1-u4339968.deta.app",
    "https://4randomx-1-q3158453.deta.app",
    "https://5randomx-1-x5660814.deta.app",
    "https://6randomx-1-x6371192.deta.app",
    "https://7randomx-1-z3769433.deta.app",
    "https://8randomx-1-y4974775.deta.app",
    "https://9randomx-1-r7058359.deta.app",
    "https://10randomx-1-g6878805.deta.app",
    "https://11rx-1-e3023455.deta.app",
    "https://12rx-1-d9745425.deta.app",
    "https://13rx-1-l2473886.deta.app",
    "https://14rx-1-e3430487.deta.app",
    "https://15rx-1-u8506449.deta.app",
    "https://16rx-1-g2605045.deta.app",
    "https://17rx-1-w5750850.deta.app",
    "https://18rx-1-k9316494.deta.app",
    "https://19rx-1-t0810669.deta.app",
    "https://20rx-1-e4725871.deta.app",
    "https://21rx-1-z1988041.deta.app",
    "https://22rx-1-e4554503.deta.app",
    "https://23rx-1-t1361503.deta.app",
    "https://24rx-1-s8397176.deta.app",
    "https://25rx-1-r8249842.deta.app",
    "https://26rx-1-g1115882.deta.app",
    "https://27rx-1-d6237872.deta.app",
    "https://28rx-1-e0890020.deta.app",
    "https://29rx-1-r5142642.deta.app",
    "https://30rx-1-f2028009.deta.app",
    "https://31rx-1-h4520150.deta.app",
    "https://32rx-1-a3588367.deta.app",
    "https://33rx-1-q5967340.deta.app",
    "https://34rx-1-b4605552.deta.app",
    "https://35rx-1-h2207756.deta.app",
    "https://36rx-1-x1194048.deta.app",
    "https://37rx-1-a3206239.deta.app",
    "https://38rx-1-h1529693.deta.app",
    "https://39rx-1-y9090869.deta.app",
    "https://40rx-1-p2907333.deta.app",
    "https://41rx-1-g7300522.deta.app",
    "https://42rx-1-f3789962.deta.app",
    "https://43rx-1-e5607285.deta.app",
    "https://44rx-1-a7889643.deta.app",
    "https://45rx-1-f9847661.deta.app",
    "https://46rx-1-x3473683.deta.app",
    "https://47rx-1-h1895798.deta.app",
    "https://48rx-1-p0634831.deta.app",
    "https://49rx-1-n7938069.deta.app",
    "https://50rx-1-y7416487.deta.app",
    "https://51rx-1-a4414564.deta.app",
    "https://52rx-1-b6236695.deta.app",
    "https://53rx-1-s9520983.deta.app",
    "https://54rx-1-o1789226.deta.app",
    "https://55rx-1-k9089454.deta.app",
    "https://56rx-1-j8928459.deta.app",
    "https://57rx-1-t7881677.deta.app",
    "https://58rx-1-q8475232.deta.app",
    "https://59rx-1-p0691924.deta.app",
    "https://60rx-1-j7472564.deta.app",
    "https://61rx-1-f3752329.deta.app",
    "https://62rx-1-k5396790.deta.app",
    "https://63rx-1-g2060526.deta.app",
    "https://64rx-1-t1095535.deta.app",
    "https://65rx-1-o0943887.deta.app",
    "https://66rx-1-j6988726.deta.app",
    "https://67rx-1-w6144310.deta.app",
    "https://68rx-1-h6953776.deta.app",
    "https://69rx-1-r0781588.deta.app",
    "https://70rx-1-d6349536.deta.app",
    "https://71rx-1-s6506592.deta.app",
    "https://72rx-1-r4005969.deta.app",
    "https://73rx-1-l5372427.deta.app",
    "https://74rx-1-l6762030.deta.app",
    "https://75rx-1-v3234712.deta.app",
    "https://76rx-1-x1357458.deta.app",
    "https://77rx-1-r9273074.deta.app",
    "https://78rx-1-a3308917.deta.app",
    "https://79rx-1-f4859402.deta.app",
    "https://80rx-1-j2612498.deta.app",
    "https://81rx-1-a8943997.deta.app",
    "https://82rx-1-m1614526.deta.app",
    "https://83rx-1-w0605850.deta.app",
    "https://84rx-1-w1282128.deta.app",
    "https://85rx-1-b8265841.deta.app",
    "https://86rx-1-s9225054.deta.app",
    "https://87rx-1-d8517894.deta.app",
    "https://88rx-1-p2667936.deta.app",
    "https://89rx-1-v6826692.deta.app",
    "https://90rx-1-z7774801.deta.app",
    "https://91rx-1-j4618626.deta.app",
    "https://92rx-1-j2729195.deta.app",
    "https://93rx-1-s9274525.deta.app",
    "https://94rx-1-d6725513.deta.app",
    "https://95rx-1-d6042938.deta.app",
    "https://96rx-1-q4156611.deta.app",
    "https://97rx-1-k0420623.deta.app",
    "https://98rx-1-b5219605.deta.app",
    "https://99rx-1-a5647966.deta.app"
]
databases=[]
db_headers=[]



for url in urls:
    response = requests.get(url)
    t = response.text
    j= json.loads(t)
    #print(type(j))
    st=j["DETA_PROJECT_KEY"]
    a=st.split("_")
    databases.append("https://database.deta.sh/v1/{}/db_rx/items".format(a[0]))
    db_headers.append({'X-API-Key': st})
    print(a[0])

async def put_params(session,url,p_json,p_headers):
    async with session.put(url,json=p_json,headers=p_headers) as resp:
        rez= await resp.text()
        return rez

async def main_put(p_blob,p_target,p_height,p_job_id,p_seed_hash):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context,limit=0)
    #print(p_blob)
    async with aiohttp.ClientSession(connector=conn,trust_env=True) as session:

        tasks = []
        for db in range(len(databases)):
            p_json={
                "items":[
                    {
                        "key": "blob",
                        "value": p_blob
                    },
                    {
                        "key": "target",
                        "value": p_target
                    },
                    {
                        "key": "job_id",
                        "value": p_job_id
                    },
                    {
                        "key": "seed_hash",
                        "value": p_seed_hash
                    },
                    {
                        "key": "height",
                        "value": p_height
                    },
                    {
                        "key": "n",
                        "value": 1
                    }
                    ,
                    {
                        "key": "start",
                        "value": db+1
                    },
                    {
                        "key": "step",
                        "value": len(databases)
                    },
                    {
                        "key": "duration",
                        "value": 60
                    },
                    {
                        "key": "status",
                        "value": "start"
                    },
                    {
                        "key": "hash",
                        "value": "0"
                    }
                    ,
                    {
                        "key": "blobstop",
                        "value": "0"
                    }
                    ,
                    {
                        "key": "nonce",
                        "value": "0"
                    }
                    ]
                    }
            url = databases[db]
            header= db_headers[db]
            tasks.append(asyncio.ensure_future(put_params(session, url,p_json,header)))

        original_pokemon = await asyncio.gather(*tasks)
        #for pokemon in original_pokemon:
        #    print(pokemon)

async def get_pokemon(session, url):
    try:
        async with session.get(url) as resp:
            pokemon = await resp.text()
            if resp.status != 200:
                print(url + " " + str(resp.status))
            return pokemon
    except Exception as e:
                print(url + " " +str(e))

async def main_get():

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context,limit=150)

    async with aiohttp.ClientSession(connector=conn,trust_env=True) as session:

        tasks = []
        for p_url in urls:#for number in range(1, 2):
            url = p_url + "/pokreni"
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            try:
                r= json.loads(pokemon)
                if r.get("hash")!= "0":
                    global p_hash,p_nonce
                    p_hash,p_nonce = r.get("hash"),r.get("nonce")
                    #p_nonce= 
                    print(pokemon)
            except Exception as e:
                print(str(e))
            #print(pokemon)

def glavni(p_blob,p_target,p_height,p_job_id,p_seed_hash):
    #print(p_blob)
    #print(p_target)
    #print(p_height)
    #print(p_job_id)
    #print(p_seed_hash)
    asyncio.run(main_put(p_blob,p_target,p_height,p_job_id,p_seed_hash))
    global p_hash,p_nonce
    p_hash, p_nonce="0","0"
    i=0
    while 1:
        i+=1
        print("working {}".format(i))
        if p_hash=="0":
            asyncio.run(main_get())
        if p_hash!="0":
            break    
        if i>5:
            break         
    return [{"result": p_hash, "nonce": p_nonce, "job_id": p_job_id}]    


def zaustavi_asyc_minere(adresa,hash,nonce):
    ###za sve async minere osim ovog upisi hash u env
    j = {'hash': hash, 'nonce': nonce}
    for a in adrese:
        if ((a[0] != adresa) and (a[1]=='async')):
            arr_adrese = a[0].split('/RandomX')
            adresa_stop = arr_adrese[0] + '/RandomXstop'
            headers_rx={"X-API-Key": a[2],
                        "Content-Type": "application/json"}
            response = requests.post(adresa_stop, headers=headers_rx,json = j)

def f_mineri(adresa,job,adresa_method,adresa_api):


##napraviti def za asnc i sync servere
    if adresa_method == 'sync':
        response = requests.post(adresa, json = job)
        #print(response.text)
        if response.status_code == 200:
            rezultat=response.json()
            p_nonce=rezultat[0].get('nonce')
            p_hash=rezultat[0].get('result')
            if p_nonce != '0':
                ad = adresa.split('/RandomX')[0] + '/RandomX'
                zaustavi_asyc_minere(ad,p_hash,p_nonce)
            return rezultat
        else:
            print('Greska: ' + adresa + '\n' + response.text)
            list1=[]
            dict1= {'nonce': '0', 'result': '0','job_id': '0'}
            list1.append(dict1)
            return list1
    elif adresa_method == 'async':
        headers_rx={"X-API-Key": adresa_api,
                        "Content-Type": "application/json"}
        response = requests.post(adresa, headers=headers_rx,json = job)
        if response.status_code == 200:
            arr_adrese = adresa.split('/RandomX')
            #adresa_provjere = arr_adrese[0] + '/RandomXprovjeri'
 
            
                

            while 1:
                if 1==1:#adresa.split('/RandomX')[0] == adrese[0][0].split('/RandomX')[0]:
                    #adresa_provjere = 'https://aduspara-middlerandomx.hf.space/provjeri'
                    time.sleep(1)
                    headers_middle={"X-API-Key": middleapikey,
                    "Content-Type": "application/json"}
                    response_async = requests.post(adresa_provjere, headers=headers_middle,json = {'broj_servera': len(adrese)})
                    if response_async.status_code == 200:
                        provjera_json = response_async.text#response_async.json()
                        #print(provjera_json)
                        r = json.loads(provjera_json)
                        r_status = r.get('status')
                        if r_status == 'end':
                            r_nonce = r.get('nonce')
                            r_result = r.get('result')
                            r_job_id = r.get('job_id')
                            p_server = r.get('server')
                            p_hashrate = r.get('hashrate')
                            list1=[]
                            dict1= {'nonce': r_nonce, 'result': r_result,'job_id': r_job_id, 'server': p_server, 'hashrate': p_hashrate}
                            list1.append(dict1)
                            #if r_nonce != '0':
                            #    ad = adresa.split('/RandomX')[0] + '/RandomX'
                            #    zaustavi_asyc_minere(ad,r_result,r_nonce)
                            return list1
                            break
                    else:
                        print('Greska: ' + adresa_provjere + '\n' + response_async.text)
                        list1=[]
                        dict1= {'nonce': '0', 'result': '0','job_id': '0'}
                        list1.append(dict1)
                        return list1
                        break
                    if os.environ["status"] == 'stop':
                        list1=[]
                        dict1= {'nonce': '0', 'result': '0','job_id': '0'}
                        list1.append(dict1)
                        return list1
                        break
                else:
                    list1=[]
                    dict1= {'nonce': '0', 'result': '0','job_id': '0'}
                    list1.append(dict1)
                    return list1
                    break
        else:
            print('Greska: ' + adresa + '\n' + response.text + str(response.status_code))
            list1=[]
            dict1= {'nonce': '0', 'result': '0','job_id': '0'}
            list1.append(dict1)
            return list1
                    

    else:
        list1=[]
        dict1= {'nonce': '0', 'result': '0','job_id': '0'}
        list1.append(dict1)
        return list1

def main():

    try:
        while os.environ["status"] == 'start':
            pool_ip = socket.gethostbyname(pool_host)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((pool_ip, pool_port))

            login = {
                'method': 'login',
                'params': {
                    'login': wallet_address,
                    'pass': pool_pass,
                    'rigid': rigid,
                    'agent': 'stratum-miner-py/0.1'
                },
                'id':1
            }
            print('Logging into pool: {}:{}'.format(pool_host, pool_port))
            #print('Using NiceHash mode: {}'.format(nicehash))
            s.sendall(str(json.dumps(login)+'\n').encode('utf-8'))
            #pool = Pool(processes=4)
            line = s.makefile().readline()
            if line == None or line == '':
                print('I got a null or empty string value for line in a file')
                print(line)
            else:
                
                print(time.ctime(time.time()))
                #print(line)
                        
                r = json.loads(line)
                error = r.get('error')
                result = r.get('result')
                method = r.get('method')
                params = r.get('params')
                if error:
                    print('Error: {}'.format(error))
                    continue
                if result and result.get('status'):
                    print('Status: {}'.format(result.get('status')))
                if result and result.get('job'):
                    #print('job')
                    login_id = result.get('id')
                    job = result.get('job')
                    job['login_id'] = login_id
                    job_id = job.get('job_id')
                    adrese_final=[]
                    #for x in range(0,len(adrese)):
                        #adrese_final.append((adrese[x] + '?n=1&start={}&step={}&duration={}'.format(x+1,len(adrese),duration),job,s))
                    #    adrese_final.append(job)
                        #results = pool.apply(worker, args=(job,adrese[x] + '?n=1&start={}&step={}&duration=200'.format(x+1,len(adrese)), s))
                    p_nonce='0'
                    p_result='0'
                    p_job_id='0'
                    adrese_final.append(job)
                    #with ThreadPool(processes=len(adrese)+1) as pool:
                    #print(job)
                    result1 =worker(job)
                        
                    p_nonce=result1[0].get('nonce')
                    p_result=result1[0].get('result')
                    p_job_id=result1[0].get('job_id')
                    if p_nonce != '0':
                        print(time.ctime(time.time()))
                        print(f'Got result: {result1}', flush=True)
                        submit = {
                            'method':'submit',
                            'params': {
                                'id': login_id,
                                'job_id': p_job_id,
                                'nonce': p_nonce,
                                'result': p_result
                            },
                            'id':1
                        }
                        #print(submit)
                        s.sendall(str(json.dumps(submit)+'\n').encode('utf-8'))
                        select.select([s], [], [], 3)
                        #break
                        #pool.terminate()
                        #pool.close() 
                                            
                elif method and method == 'job' and len(login_id):
                    #print('method')
                    job_id = job.get('job_id')
                    adrese_final=[]
                    ##for x in range(0,len(adrese)):
                    #    adrese_final.append(params)

                        #results = pool.apply(worker, args=(job,adrese[x] + '?n=1&start={}&step={}&duration=200'.format(x+1,len(adrese)), s))
                    p_nonce='0'
                    p_result='0'
                    p_job_id='0'
                    adrese_final.append(params)
                    #with ThreadPool(processes=len(adrese)+1) as pool:
                    result1 =worker(params)
                        
                    p_nonce=result1[0].get('nonce')
                    p_result=result1[0].get('result')
                    p_job_id=result1[0].get('job_id')
                    if p_nonce != '0':
                        print(time.ctime(time.time()))
                        print(f'Got result: {result1}', flush=True)
                        submit = {
                            'method':'submit',
                            'params': {
                                'id': login_id,
                                'job_id': p_job_id,
                                'nonce': p_nonce,
                                'result': p_result
                            },
                            'id':1
                        }
                        #print(submit)
                        s.sendall(str(json.dumps(submit)+'\n').encode('utf-8'))
                        select.select([s], [], [], 3)
                        #break
                        #pool.terminate()
                        #pool.close()            
            s.close()
            if os.environ["status"] == 'stop':
                print('Mining je stopiran.')
                break
    except KeyboardInterrupt:
        print('{}Exiting'.format(os.linesep))
        pool.close()
        s.close()
        sys.exit(0)




def worker(q):
    
    started = time.time()
    hash_count = 0
    #s=q[2]
    #a=q[0]
    #adresa_method=q[3]
    #adresa_api=q[4]
    #print(a)
    #while 1:
    job = q
    #print(job)
    if job.get('login_id'):
        login_id = job.get('login_id')
        #print('Login ID: {}'.format(login_id))
    blob = job.get('blob')
    target = job.get('target')
    job_id = job.get('job_id')
    height = job.get('height')
    block_major = int(blob[:2], 16)
    cnv = 0
    if block_major >= 7:
        cnv = block_major - 6
    if cnv > 5:
        seed_hash = binascii.unhexlify(job.get('seed_hash'))
        return glavni(blob,target,height,job_id,job.get('seed_hash'))
        #return f_mineri(a,job,adresa_method,adresa_api)
        
    else:
        print('New job with target: {}, CNv{}, height: {}'.format(target, cnv, height))

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/start")
async def proc_post(request : Request,background_tasks: BackgroundTasks):         
    req_json = await request.json()
    p_pool_host = req_json['pool_host']
    p_pool_port = int(req_json['pool_port'])
    p_pool_pass = req_json['pool_pass']
    p_wallet_address = req_json['wallet_address']
    p_adresa_provjere = req_json['adresa_provjere']
    p_rigid = req_json['rigid']
    p_duration = int(req_json['duration'])
    p_adrese = req_json['adrese']
    global pool_host,pool_port,pool_pass,wallet_address,duration, adrese,adresa_provjere,rigid,middleapikey
    pool_host =p_pool_host
    pool_port =p_pool_port
    pool_pass =p_pool_pass
    wallet_address =p_wallet_address
    duration =p_duration
    adresa_provjere=p_adresa_provjere
    middleapikey=req_json['middleapikey']
    rigid=p_rigid
    adrese=[]
 
    for d in req_json["adrese"]:
        adrese.append([d.get('url'),d.get('method'),d.get('apikey')])
    os.environ["status"] = 'start'
    print('Mining je pokrenut.')
    background_tasks.add_task(main)
    return adrese

@app.post("/stop")
async def proc_post(request : Request,background_tasks: BackgroundTasks):         
    req_json = await request.json()
    p_pool_host = req_json['pool_host']
    p_pool_port = int(req_json['pool_port'])
    p_pool_pass = req_json['pool_pass']
    p_wallet_address = req_json['wallet_address']
    p_duration = int(req_json['duration'])
    p_adrese = req_json['adrese']
    os.environ["status"] = 'stop'
    j = {'hash': '0', 'nonce': '0'}
    for a in adrese:
        
        arr_adrese = a[0].split('/RandomX')
        headers_rx={"X-API-Key": a[2],
                    "Content-Type": "application/json"}
        adresa_stop = arr_adrese[0] + '/RandomXstop'
        response = requests.post(adresa_stop, headers=headers_rx,json = j)
    return 'stoped'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)

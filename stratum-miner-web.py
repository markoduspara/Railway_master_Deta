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
global_hash='0'
global_nonce='0'
global_job_id='0'
global_server='0'
global_hashrate='0'
global_status='0'



def zaustavi_asyc_minere(adresa,hash,nonce):
    ###za sve async minere osim ovog upisi hash u env
    j = {'hash': hash, 'nonce': nonce}
    for a in adrese:
        if ((a[0] != adresa) and (a[1]=='async')):
            arr_adrese = a[0].split('/RandomX')
            adresa_stop = arr_adrese[0] + '/RandomXstop'
            response = requests.post(adresa_stop, json = j)

def f_mineri(adresa,job,adresa_method):


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
        response = requests.post(adresa, json = job)
        if response.status_code == 200:
            arr_adrese = adresa.split('/RandomX')
            #adresa_provjere = arr_adrese[0] + '/RandomXprovjeri'
 
            
                
            started = time.time()
            while 1:

                if adresa.split('/RandomX')[0] == adrese[0][0].split('/RandomX')[0]:
                    #adresa_provjere = 'https://aduspara-middlerandomx.hf.space/provjeri'
                    

                    ####novi dio upisivanje######
                    global global_hash, global_nonce,global_job_id,global_server,global_hashrate,global_status
                    if global_status=='end':
                        list1=[]
                        dict1= {'nonce': global_nonce, 'result': global_hash,'job_id': global_job_id,'server': global_server, 'hashrate': global_hashrate}
                        list1.append(dict1)
                        
                        global_hash, global_nonce,global_job_id,global_server,global_hashrate,global_status='0','0','0','0','0','0'
                        return list1
                    else:
                        elapsed = time.time() - started
                        if elapsed > 120:
                            #global global_status
                            global_status='end'
                    time.sleep(0.1)
                    #######################

                    '''
                    response_async = requests.post(adresa_provjere, json = {'broj_servera': len(adrese)})
                    if response_async.status_code == 200:
                        provjera_json = response_async.text#response_async.json()
                        #print(provjera_json)
                        r = json.loads(provjera_json)
                        r_status = r.get('status')
                        if r_status == 'end':
                            r_nonce = r.get('nonce')
                            r_result = r.get('result')dc 
                            r_job_id = r.get('job_id')
                            p_server = r.get('server')
                            p_hashrate = r.get('hashrate')
                            list1=[]
                            return list1
                            break
                    else:
                        print('Greska: ' + adresa_provjere + '\n' + response.text)
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
                    '''
                else:
                    list1=[]
                    dict1= {'nonce': '0', 'result': '0','job_id': '0'}
                    list1.append(dict1)
                    return list1
                    break
        else:
            print('Greska: ' + adresa + '\n' + response.text)
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
                    for x in range(0,len(adrese)):
                        #adrese_final.append((adrese[x] + '?n=1&start={}&step={}&duration={}'.format(x+1,len(adrese),duration),job,s))
                        adrese_final.append((adrese[x][0] + '?n=1&start={}&step={}&duration={}'.format(x+1,len(adrese),duration),job,s,adrese[x][1]))
                        #results = pool.apply(worker, args=(job,adrese[x] + '?n=1&start={}&step={}&duration=200'.format(x+1,len(adrese)), s))
                    p_nonce='0'
                    p_result='0'
                    p_job_id='0'
                    with ThreadPool(processes=len(adrese)+1) as pool:
                        for result1 in pool.imap_unordered(worker, adrese_final):
                            
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
                                break
                        pool.terminate()
                        pool.close()
                                            
                elif method and method == 'job' and len(login_id):
                    #print('method')
                    job_id = job.get('job_id')
                    adrese_final=[]
                    for x in range(0,len(adrese)):
                        adrese_final.append((adrese[x][0] + '?n=1&start={}&step={}&duration={}'.format(x+1,len(adrese),duration),params,s,adrese[x][1]))

                        #results = pool.apply(worker, args=(job,adrese[x] + '?n=1&start={}&step={}&duration=200'.format(x+1,len(adrese)), s))
                    p_nonce='0'
                    p_result='0'
                    p_job_id='0'
                    with ThreadPool(processes=len(adrese)+1) as pool:
                        for result1 in pool.imap_unordered(worker, adrese_final):
                            
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
                                break
                        pool.terminate()
                        pool.close()            
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
    s=q[2]
    a=q[0]
    adresa_method=q[3]
    #print(a)
    #while 1:
    job = q[1]#q.get()
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
        
        return f_mineri(a,job,adresa_method)
        
    else:
        print('New job with target: {}, CNv{}, height: {}'.format(target, cnv, height))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upisi")
async def proc_post(request : Request):    
    req_json = await request.json()
    if req_json['hash']!='0':
        global global_hash, global_nonce,global_job_id,global_server,global_hashrate,global_status
        global_hash, global_nonce,global_job_id,global_server,global_hashrate,global_status = req_json['result'],req_json['nonce'], req_json['job_id'], req_json['server'], req_json['hashrate'], req_json['status']


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
    global pool_host,pool_port,pool_pass,wallet_address,duration, adrese,adresa_provjere,rigid
    pool_host =p_pool_host
    pool_port =p_pool_port
    pool_pass =p_pool_pass
    wallet_address =p_wallet_address
    duration =p_duration
    adresa_provjere=p_adresa_provjere
    rigid=p_rigid
    adrese=[]
 
    for d in req_json["adrese"]:
        adrese.append([d.get('url'),d.get('method')])
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
        adresa_stop = arr_adrese[0] + '/RandomXstop'
        response = requests.post(adresa_stop, json = j)
    return 'stoped'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)

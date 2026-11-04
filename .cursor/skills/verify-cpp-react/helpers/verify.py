#!/usr/bin/env python3
import argparse,json,os,pathlib,re,selectors,shutil,socket,subprocess,tempfile,time,urllib.request,urllib.error,http.server,threading,functools
root=pathlib.Path(__file__).resolve().parents[4];skill=pathlib.Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument('mode',choices=['doctor','drive']);p.add_argument('--openssl-root',default=os.environ.get('OPENSSL_ROOT','/usr'));p.add_argument('--out',default='.verification-evidence/cpp-react');a=p.parse_args();out=pathlib.Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True);r={'mode':a.mode,'ok':False,'checks':[]};child=None;server=None;thread=None
try:
 ssl=pathlib.Path(a.openssl_root).resolve();assert (ssl/'include/openssl/ssl.h').is_file(),'OpenSSLheaders missing';assert all(shutil.which(x) for x in ['g++','make','node','npm']),'Tool missing';assert (root/'react-ui/node_modules/react-scripts').is_dir(),'Run npmci --prefix react-ui';assert (skill/'node_modules/puppeteer-core').is_dir(),'Run npmci --prefix skill';r['checks'].append({'doctor':'source/tool/OpenSSL/React/browserdeps present'})
 if a.mode=='drive':
  before=subprocess.run(['git','status','--porcelain'],cwd=root,text=True,capture_output=True,check=True).stdout
  with tempfile.TemporaryDirectory(prefix='cpp-react-verify-') as td:
   td=pathlib.Path(td);flags='-I'+str(ssl/'include')+' -I'+str(ssl/'include/x86_64-linux-gnu')+' -L'+str(ssl/'lib/x86_64-linux-gnu');q=subprocess.run(['make','-B','-f',str(root/'Makefile'),'main','CXXFLAGS='+flags,'SRCS='+str(root/'main.cpp'),'HEADERS='],cwd=td,capture_output=True,text=True,timeout=60);(out/'backend-build.log').write_text(q.stdout+q.stderr);assert q.returncode==0,'C++buildfailed';binary=str(td/'main')
   for args in [['-1'],['65536'],['abc'],['1','2']]:
    q=subprocess.run([binary]+args,capture_output=True,text=True,timeout=5);assert q.returncode==1 and 'Server error:' in q.stderr,'Invalidargs';r['checks'].append({'invalidargs':args,'exit':q.returncode})
   with socket.socket() as held:
    held.bind(('127.0.0.1',0));held.listen();q=subprocess.run([binary,str(held.getsockname()[1])],capture_output=True,text=True,timeout=5);assert q.returncode==1 and 'Cannot bind' in q.stderr,'Busyport';r['checks'].append({'ownedbusyport':'bindfailureexit1'})
   child=subprocess.Popen([binary,'0'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);sel=selectors.DefaultSelector();sel.register(child.stdout,selectors.EVENT_READ);assert sel.select(5),'Startupmissing';line=child.stdout.readline();sel.close();m=re.fullmatch(r'Server started on port (\d+)\.\.\.\n',line);assert m,'Wrongstartup';port=int(m[1]);api='http://127.0.0.1:'+str(port)
   for i in range(50):
    try:response=urllib.request.urlopen(api+'/api/greet',timeout=.2);break
    except (OSError,urllib.error.URLError):time.sleep(.1)
   data=json.load(response);assert data=={'message':'Hello from C++ backend!'} and response.headers['Access-Control-Allow-Origin']=='*','GET/CORS';r['checks'].append({'GET':data})
   response=urllib.request.urlopen(urllib.request.Request(api+'/api/greet',method='OPTIONS'));assert response.status==204 and response.headers['Access-Control-Allow-Origin']=='*','OPTIONS';r['checks'].append({'OPTIONS':204})
   try:urllib.request.urlopen(api+'/missing');raise AssertionError('Missingpathnot404')
   except urllib.error.HTTPError as e:assert e.code==404;r['checks'].append({'missing':404})
   env=os.environ.copy();env.update(REACT_APP_API_BASE_URL=api,BUILD_PATH=str(td/'ui'),CI='true');q=subprocess.run(['npm','run','build','--prefix',str(root/'react-ui')],env=env,capture_output=True,text=True,timeout=90);(out/'frontend-build.log').write_text(q.stdout+q.stderr);assert q.returncode==0,'Reactbuildfailed'
   class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
   server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(td/'ui')));thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();url='http://127.0.0.1:'+str(server.server_port)
   q=subprocess.run(['node',str(skill/'helpers/browser.mjs'),url,str(out/'success'),'success'],timeout=45);assert q.returncode==0,'RealUI successfailed';r['checks'].append({'realUI':'390/1365actualHTTPsuccess'})
   child.terminate();stdout,stderr=child.communicate(timeout=5);assert stderr=='','Backenderror';(out/'backend.log').write_text(line+stdout);child=None
   q=subprocess.run(['node',str(skill/'helpers/browser.mjs'),url,str(out/'failure'),'failure'],timeout=45);assert q.returncode==0,'RealUI stoppedbackendfailurefailed';r['checks'].append({'realUI':'390/1365actualstoppedbackendfailure'})
   server.shutdown();server.server_close();thread.join();server=None
  after=subprocess.run(['git','status','--porcelain'],cwd=root,text=True,capture_output=True,check=True).stdout;assert before==after,'Sourcestatechanged';r['checks'].append({'cleanup':'ownedserver/browser/tempbuildremoved;sourceunchanged'})
 r['ok']=True
except Exception as e:r['failure']=str(e)
finally:
 if child and child.poll() is None:child.terminate();child.communicate(timeout=5)
 if server:server.shutdown();server.server_close();thread.join()
(out/(a.mode+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));raise SystemExit(0 if r['ok'] else 1)

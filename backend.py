#! /usr/bin/python3



import cgi
import subprocess
import time

print("content-type:text/html")
print()

#time.sleep(10)

f = cgi.FieldStorage()
cmd = f.getvalue("x")
t=cmd.split()
if t[0] == "2":
    deploy_name = t[2]
    image_name = t[1]
    cmd1 = "kubectl create deployment " +(deploy_name)+ " --image=" + (image_name)
    print(cmd1)
    o = subprocess.getoutput("sudo " + cmd1 + " --kubeconfig admin.conf" )
    print("image name given:",image_name,end=" @@" )
    print("name of deployment:", deploy_name)
    print(o)
    u = "kubectl get deployments "
    q = subprocess.getoutput("sudo " + u + " --kubeconfig admin.conf" )
    print(q)
elif t[0] == "1":
    pod_name = t[2]
    image_name = t[1]
    cmd1 = "kubectl run " +(pod_name)+ " --image=" + (image_name)
    o = subprocess.getoutput("sudo " + cmd1 + " --kubeconfig admin.conf" )
    print("image name given:",image_name,end=" @@" )
    print("name of pod :", pod_name)
    print(o)
    u = "kubectl get pods "
    q = subprocess.getoutput("sudo " + u + " --kubeconfig admin.conf" )
    print(q)

elif t[0] == "3":
    pod_name = t[1]
    port_no = t[2]
    cmd1 = "kubectl expose deployments " +(pod_name)+ " --port=" + (port_no) + " --type=NodePort"
    o = subprocess.getoutput("sudo " + cmd1 + " --kubeconfig admin.conf" )
    print("pod name given:",pod_name,end=" @@" )
    print("name of pod :", port_no)
    print(o)

elif t[0] == "4":
    deploy_name = t[1]
    replica = t[2]
    cmd1 = "kubectl scale deployment " +(deploy_name)+ " --replicas=" + (replica)
    o = subprocess.getoutput("sudo " + cmd1 + " --kubeconfig admin.conf" )
    print("deploy name given:",deploy_name,end=" @@" )
    print("name of replicas :", replica)
    print(o)
    u = "kubectl get deployments "
    q = subprocess.getoutput("sudo " + u + " --kubeconfig admin.conf" )
    print(q)

elif t[0] == "5":
    cmd1 = "kubectl delete all --all"
    o = subprocess.getoutput("sudo " + cmd1 + " --kubeconfig admin.conf" )
    print("full environment deleted")
    print(o)
elif t[0] == "6":
    pod_name = t[1]
    cmd1 = "kubectl delete pod " +(pod_name)
    o = subprocess.getoutput("sudo " + cmd1 + " --kubeconfig admin.conf" )
    print("name of pod :", pod_name)
    print("deleted successfully")
    print(o)
    u = "kubectl get pods "
    q = subprocess.getoutput("sudo " + u + " --kubeconfig admin.conf" )
    print(q)

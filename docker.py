#!/usr/bin/python
import commands

print "enter no. of datanodes and tasktrackers"
x=raw_input()
print "wait for sme time"
#to stop and remove existing containers
commands.getstatusoutput("docker stop $(docker ps -a)")
commands.getstatusoutput("docker rm $(docker ps -a)")


#for namenode
print commands.getstatusoutput("docker run -itd --name prakharnamenode docker2")[1]
print commands.getstatusoutput("docker exec prakharnamenode hostname -i")


print commands.getstatusoutput("docker cp /root/Desktop/nn/hdfs-site.xml prakharnamenode:/etc/hadoop/")[1]


print commands.getstatusoutput("docker exec prakharnamenode service sshd start")[1]
print commands.getstatusoutput("docker exec prakharnamenode hadoop namenode -format")
print commands.getstatusoutput("docker exec prakharnamenode hadoop-daemon.sh start namenode")[1]
#for jobtracker
print commands.getstatusoutput("docker run -itd --name prakharjobtracker docker2")[1]
print commands.getstatusoutput("docker exec prakharjobtracker hostname -i")
print commands.getstatusoutput("docker exec prakharjobtracker service sshd start")[1]
print commands.getstatusoutput("docker exec prakharjobtracker hadoop-daemon.sh start jobtracker")[1]

y=int(x)
i=0
#for datanode and tasktracker
while i<y:
	f=i+1
	
	print f
	print commands.getstatusoutput("docker run -itd --name dn_tt"+(str(f))+" docker2")[1]
	print commands.getstatusoutput("docker cp /root/Desktop/dn/hdfs-site.xml dn_tt"+(str(f))+":/etc/hadoop/")[1]
	print commands.getstatusoutput("docker exec dn_tt"+(str(f))+" hadoop-daemon.sh start datanode")[1]
	print commands.getstatusoutput("docker exec dn_tt"+(str(f))+" hadoop-daemon.sh start tasktracker")[1]
	print commands.getstatusoutput(" docker exec dn_tt"+(str(f))+" /usr/java/jdk1.7.0_79/bin/jps")
	i=i+1

print commands.getstatusoutput(" docker exec prakharnamenode /usr/java/jdk1.7.0_79/bin/jps")
print "namenode is started at ip 172.17.0.2"
print commands.getstatusoutput(" docker exec prakharjobtracker /usr/java/jdk1.7.0_79/bin/jps")
print "jobtracker is started at ip 172.17.0.3"
print commands.getstatusoutput("docker exec prakharnamenode hadoop dfsadmin -report")


	

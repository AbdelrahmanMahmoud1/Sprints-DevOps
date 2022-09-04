#1 /bin/bash 
echo -n "Hello, please enter the port number: " 
read number 

if [[ ! $number =~ ^[0-9]+$ ]];then 
	echo "Not Valid number"
 	exit 
fi

echo $number 

if [[ "$number -gt 1024 ] && [ "$number" -lt 32767 ] 
then 
	echo "in range" 
	/etc/ssh/sshd_config: 
		PermitRootLogin no #disabled 
else 
	echo "out of range" 
fi 
	getent group wheel 
	exit
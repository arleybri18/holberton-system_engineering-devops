# modify limit open files
exec {'modify file hard':
command =>  "sed -i 's/holberton hard nofile 5/holberton hard nofile 4000/g' /etc/security/limits.conf",
path    => '/bin/',
}
-> exec {'modify file soft':
command =>  "sed -i 's/holberton soft nofile 4/holberton soft nofile 4000/g' /etc/security/limits.conf",
path    =>  '/bin/',
}

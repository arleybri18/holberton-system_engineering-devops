# modify limit open files
exec {'modify file':
command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g'  /etc/default/nginx",
path    => '/bin/',
}
-> exec {'restart service':
command => 'sudo service nginx restart',
path    => '/usr/bin/',
}

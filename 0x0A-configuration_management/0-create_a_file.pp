# create a new file in /tmp dir and set properties
file { 'holberton':
ensure  => 'present',
path    => '/tmp/holberton',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
}

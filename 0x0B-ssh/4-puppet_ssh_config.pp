# modify ssh config with puppet
$_path = '/etc/ssh/ssh_config'
file { '$_path':
  ensure => present,
}
file_line { 'change auth type':
  ensure => present,
  path   => '$_path',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}
file_line { 'set identity file':
  ensure => present,
  path   => '$_path',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile',
}

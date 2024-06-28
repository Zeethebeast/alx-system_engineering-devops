##this file is basically a puppet file that creates file in temp
file { 'school':
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}


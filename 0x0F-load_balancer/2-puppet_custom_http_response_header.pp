#Install Nginx web server

exec { 'Install Nginx':
  command => 'sudo apt -y install nginx',
  path    => ['/usr/bin/', '/bin'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'listen 80 default_server;',
  line     => 'rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

file_line { 'Custom header':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'listen 80 default_server;',
  line     => 'add_header X-Served-By $hostname;',
  multiple => true
}

file_line { 'init script':
  ensure   => present,
  path     => '/etc/default/haproxy',
  line     => 'ENABLED=1',
  multiple => true
}

exec { 'Restart':
  require => Exec['Install Nginx'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}

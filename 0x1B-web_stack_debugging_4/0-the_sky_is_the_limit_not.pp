# Increase the maximum number of open files
exec { 'increase-open-files-limit':
  command => 'ulimit -n 10000',
  path    => '/bin:/usr/bin',
}

# Configure Nginx to use more worker processes
file { '/etc/nginx/nginx.conf':
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Define the Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

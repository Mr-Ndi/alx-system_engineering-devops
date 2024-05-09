exec { 'fix-wordpress':
  command => 'chmod 644 /var/www/html/wp-config.php',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'test $(stat -c "%a" /var/www/html/wp-config.php) -ne 644',
}

service { 'apache2':
  ensure => running,
  enable => true,
}

# 0-strace_is_your_friend.pp

# Make sure Apache service is running
service { 'apache2':
  ensure => 'running',
}

# Use strace to find the issue and fix it
#
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

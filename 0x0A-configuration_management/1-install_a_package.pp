# Puppet manifest to install Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => '/usr/local/bin', # Specify the path where pip3 is located
  require => Package['python3-pip'], # Ensure python3-pip is installed first
}

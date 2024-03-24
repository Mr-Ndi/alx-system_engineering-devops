#!/usr/bin/env bash 
#Client configuration file
file { '/etc/ssh/ssh_config':
  ensure  => present'
  }

file_line { 'turn of password authantication':
	path  => '/etc/ssh/ssh_config',
	line  => 'PasswordAuthentication no',
	match => '^#PasswordAuthentication no',
}

file_line{ 'declaring an identity file':
	path  => '/etc/ssh/ssh_config',
	line  => 'IdentityFile ~/.ssh/school',
	match => '^IdentityFile',

}

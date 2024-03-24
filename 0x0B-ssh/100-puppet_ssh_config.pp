#!/usr/bin/env bash 
#Client configuration file
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => "
    Host 162762-web-01
      HostName 162762-web-01
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
}

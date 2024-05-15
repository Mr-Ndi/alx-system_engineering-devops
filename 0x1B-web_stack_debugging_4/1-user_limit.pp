# Increase the open file limit for the 'holberton' user
exec { 'increase-open-files-limit-for-holberton':
  command => 'ulimit -n 4096 && su - holberton',
  path    => '/bin:/usr/bin',
  user    => 'root',
}


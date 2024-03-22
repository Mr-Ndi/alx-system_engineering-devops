# Using Puppet, create a manifest that kills a process
exec {'proc_killer':
command     => 'pkill killmenow',
path        => '/usr/bin:/sbin',
refreshonly => true'
}

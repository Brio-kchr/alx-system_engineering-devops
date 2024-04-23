# executing a command (to kill a process)

exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}

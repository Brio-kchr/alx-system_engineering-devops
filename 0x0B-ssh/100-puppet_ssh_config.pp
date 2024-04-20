# creating a file in /tmp

file { '/etc/ssh/ssh_config':
  content => '#!/usr/bin/env bash\n# SSH client configuration file\n\nHost *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

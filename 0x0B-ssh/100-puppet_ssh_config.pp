# Puppet manifest to configure SSH client

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  match   => '^#PasswordAuthentication yes',
}

# Declare identity file
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentityFile ~/.ssh/id_rsa',
}

# Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
# Your SSH client configuration must be configured to refuse to authenticate using a password

file_line { 'no password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line { 'identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton'
}

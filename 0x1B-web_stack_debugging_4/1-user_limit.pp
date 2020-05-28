#....
exec {'name_file_fixed':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/4/1000/g' /etc/security/limits.conf && sed -i 's/5/1000/g' /etc/security/limits.conf"
}

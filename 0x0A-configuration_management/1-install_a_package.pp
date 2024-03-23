# Installs puppet-lint

package { 'python3-pip':
  ensure => 'installed',
}

package { 'libpq-dev':
  ensure => 'installed',
}

package { 'build-essential':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/usr/bin'],
  require => Package['python3-pip', 'libpq-dev', 'build-essential'],
}

# Installs puppet-lint

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure Werkzeug is installed with a compatible version
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

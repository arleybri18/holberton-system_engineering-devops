# install puppet-lint gem on this machine
package { 'puppet-lint':
ensure   => 'installed',
provider => 'gem',
}

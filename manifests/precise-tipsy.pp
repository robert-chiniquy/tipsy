exec { "apt-update":
  command => "/usr/bin/apt-get update"
}

# Ensure apt-get update has been run before installing any packages
Exec["apt-update"] -> Package <| |>

package {
    "build-essential":
        ensure => installed,
        provider => apt;
    "python":
        ensure => installed,
        provider => apt;
    "python-dev":
        ensure => installed,
        provider => apt;
    "python-setuptools":
        ensure => installed,
        provider => apt;
    "python-software-properties":
        ensure => installed,
        provider => apt;
}


package { "python-pip": 
  ensure => latest,
}

package { "sqlite3": 
  ensure => latest,
}

package { "pysqlite": 
  ensure => latest,
  provider => pip,
  require => Package['python-pip'],
}

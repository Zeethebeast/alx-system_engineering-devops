##A puppet file  that installs flask, pyhton and werkzueg
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}


# edit_nginx.pp
node default {
  # Ensure the necessary package and service management resources
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/sites-available/default'],
  }

  # Create or overwrite index.html with "Hello World!"
  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  # Create custom 404 error page
  file { '/var/www/html/404.html':
    ensure  => file,
    content => "Ceci n'est pas une page",
    require => Package['nginx'],
  }

  # Add redirect rule to Nginx default server block
  file_line { 'add_redirect_rule':
    path  => '/etc/nginx/sites-available/default',
    line  => '    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    after => 'listen 80 default_server;',
    require => Package['nginx'],
  }

  # Add custom 404 error page to Nginx default server block
  file_line { 'add_custom_404_page':
    path  => '/etc/nginx/sites-available/default',
    line  => '    error_page 404 /404.html;',
    after => 'listen 80 default_server;',
    require => Package['nginx'],
  }

  # Add custom header to Nginx configuration
  $hostname = $facts['networking']['hostname']
  file_line { 'add_custom_header':
    path  => '/etc/nginx/nginx.conf',
    line  => "    add_header X-Served-By ${hostname};",
    after => 'http {',
    require => Package['nginx'],
  }
}

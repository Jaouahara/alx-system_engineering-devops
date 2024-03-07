# try  to replace the fix the extension error

$file_path = '/var/www/html/wp-settings.php'

file { $file_path:
  ensure  => file,
  source  => $file_path,
  replace => false,
}

$replacement_command = 'sed -i "s/\.phpp/\.php/g"'

exec { 'fix_wp_settings':
  command => "${replacement_command} ${file_path}",
  path    => ['/usr/bin', '/bin'],
}

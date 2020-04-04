#documentation

exec { 'configure HTTP':
  command  => "apt-get update && apt-get -y install nginx && echo -e 'Holberton School' > /var/www/html/index.html && sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=EgBJmlPo8Xw permanent;' /etc/nginx/sites-available/default && sed -i '22i add_header X-Served-By $hostname;' /etc/nginx/nginx.conf && service nginx start",
  provider => 'shell',
}

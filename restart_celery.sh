gel2mdt=/home/genseqservadmin/WL_GEL2MDT/wl_instance
docker=/usr/local/bin
$docker/docker-compose -p wl_g2m -f $gel2mdt/docker-compose-prod.yml restart celery
$docker/docker-compose -p wl_g2m -f $gel2mdt/docker-compose-prod.yml restart celery-beat
echo completed: `date`

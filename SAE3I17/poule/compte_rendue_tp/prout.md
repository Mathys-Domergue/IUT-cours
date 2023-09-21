La création d'un nouveau service, il faut dans un premier temps éditer le fichier qui dans notre cas est le ttn-collector.service.

``` bash
[Service]
User=root
WorkingDirectory= /root/aksel/ttn_collector
ExecStart= python3 ttn.py
Restart=always

[Install]
WantedBy=multi-user.target
```


Puis redémarer, le deamon systemctl avec la commande suivante :

``` bash
systemctl deamon-reload
```


Ensuite, il faut enable le service, ce qui permet d'auto  démarer le service lorsqu'il est éteint, avec la commande suivante:

``` bash
systemctl enable ttn-colector
```
Et pour finir démarer, ce qui permet de faire son premier lancement, le service avec la commande suivante :

``` bash
systemctl start ttn-colector
```
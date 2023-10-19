# TD1

## <center>Automatisation de la récupération des prix d’AWS

## 1.1 Installation d’un container de prix

1) 
```    
curl -H 'accept: json' 'https://ec2.shop?region=us-east-1&filter=m5,m6' >> tiny.json
curl -H 'accept: json' 'https://ec2.shop?region=eu-west-1&filter=m5,m6' >> tiny.json
```

2) 
```
curl -H 'accept: json' 'https://ec2.shop?region=eu-west-1&filter=t1,t2.micro' >> medium.json
```

3) Les données sont les sorties du shop d'amazon sur plusieurs région dans le monde

4) 


```

curl -H 'accept: json' 'https://ec2.shop?region=eu-west-1&filter=m6a.48xlarge'

{"Prices":[{"InstanceType":"m6a.48xlarge","Memory":"768 GiB","VCPUS":192,"Storage":"EBS only","Network":"50000 Megabit","Cost":9.2448,"MonthlyPrice":6748.704,"SpotPrice":"NA"}]}



curl -H 'accept: json' 'https://ec2.shop?region=eu-west-1&filter=t1.micro'


{"Prices":[{"InstanceType":"t1.micro","Memory":"0.613 GiB","VCPUS":1,"Storage":"EBS only","Network":"Very Low","Cost":0.02,"MonthlyPrice":14.6,"SpotPrice":"NA"}]}


```


## 2 Transformation des fichiers json en csv


1) Le '-r' permet de sortir les résultat du filtre au format JSON, sans formatge de jq

2) 
```
jq -r '.["Prices"]' tiny.json

```

3) 
```

jq -r '.["Prices"]|keys|@csv' tiny.json

0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107

```


4) 

```
jq -r '.["Prices"]|keys|@csv' tiny.json | head -n 1

0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107

```
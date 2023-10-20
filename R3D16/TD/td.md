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


1) Le '-r' permet de sortir les résultats du filtre au format JSON, sans formatge de jq

2) 
```
jq -r '.["Prices"]' tiny.json
```

3) 
```

jq -r '.Prices[] | keys | @csv' tiny.json

"Cost","InstanceType","Memory","MonthlyPrice","Network","SpotPrice","Storage","VCPUS"  x 216

```


4) 

```

jq -r '.Prices[] | keys | @csv' tiny.json | head -n 1 

"Cost","InstanceType","Memory","MonthlyPrice","Network","SpotPrice","Storage","VCPUS"

```


5) 
```

jq -r '.[][] | join(",")' tiny.json >> ligne.csv
jq -r '.[][] | join(",")' medium.json >> ligne.csv

```

6) 
```

jq -r '.Prices[] | keys | @csv' tiny.json | head -n 1 > header.csv
jq -r '.Prices[] | [.InstanceType, .Memory, .VCPUS, .Storage, .Network, .Cost, .MonthlyPrice, .SpotPrice] | @csv' tiny.json >> ligne.csv
jq -r '.Prices[] | [.InstanceType, .Memory, .VCPUS, .Storage, .Network, .Cost, .MonthlyPrice, .SpotPrice] | @csv' medium.json >> ligne.csv
cat header.csv ligne.csv > medium.csv

```


7) 
```
jq -r '.Prices[] | [.InstanceType, .Memory, .VCPUS, .Storage, .Network, .Cost, .MonthlyPrice, .SpotPrice] | @csv' tiny.json
jq -r '.Prices[] | [.InstanceType, .Memory, .VCPUS, .Storage, .Network, .Cost, .MonthlyPrice, .SpotPrice] | @csv' medium.json

```
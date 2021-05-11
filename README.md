# aws-lambda-container-python
AWS lambda container python

## コンテナをビルドする

```
docker build -t aws-lambda-python:0.1.0 .
```

## コンテナを起動する

```
docker run -p 9000:8080 aws-lambda-python:0.1.0
```

## curlでたたく。

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}' .
```

## ECRへpush

- [コンテナイメージで Python Lambda 関数をデプロイする \- AWS Lambda](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/python-image.html)
- [Lambda コンテナイメージの作成 \- AWS Lambda](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/images-create.html#images-create-1.title)

```
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```


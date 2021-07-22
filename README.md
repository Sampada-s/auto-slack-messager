# auto-slack-messager
A Slack bot script that can be deployed to AWS Lambda. Automatically sends a pre configured message with mentions in a slack channel


#### Deployment -
Using aws cli

1) Download this package as zip
2) install aws cli and run -

aws lambda create-function --function-name slack-messager \
--zip-file fileb://function.zip --handler slackBot.lambda_handler --runtime python3.6 \
--role arn:aws:iam::123456789012:role/lambda-ex

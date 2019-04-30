# Lambda Layers Demo
The Demo was presented at the Israel AWS User Group meetup - Deep dive into new AWS services - Lambda Layers & Firecracker Container.

In this demo we will deploy two Lambda function:
- Lambda with my_lambda_utils deployed with the function, the "old way" - no layers.
- Lambda deployed with my_lambda_utils as a Lambda Layers. 

## Instructions

We will use the serverless framework in this example.
For more details: https://serverless.com/

### Install serverless
```
npm install -g serverless
```

### Clone git repository
```
git clone https://github.com/eitansela/lmabda-layers-demo.git
```

### ZIP the Python files into a Lambda package
For hello-world-no-layers Lambda Function
```
cd hello_world_no_layers
zip lambda_code *.py
```

### Deploy hello-world-no-layers serverless stack
```
serverless deploy
```


### ZIP the Python files into a Lambda package
For hello-world-with-layers Lambda Function
```
cd ../hello_world_with_layers/
zip lambda_code *.py
```

### Deploy hello-world-with-layers serverless stack
```
serverless deploy
```

### Testing on AWS Console
- In the AWS Management Console choose Services then select Lambda under Compute.
- Choose Functions on the left pane.
- You will see the list of Lambda Functions.

### Resource termination
```
serverless remove
cd ../hello_world_no_layers/
serverless remove
```
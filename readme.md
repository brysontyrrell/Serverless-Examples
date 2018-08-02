Serverless Examples
===================

This repository contains small serverless application examples to demonstrate different types of integrations, workflows, and design patterns.

API Gateway Integrated SQS Queue
--------------------------------

This application provides an HTTP interface to an SQS queue. A Lambda function is attached to the queue and will automatically poll for messages using the SQS Event.

By making the interface generic like this it is easier to integrate queued systems with other applications and services as you no longer are required to use AWS SDKs for interaction. Send a HTTP POST with a JSON body to the API Gateway and it will be added to the queue.

S3 Events Integrated SQS Queue
------------------------------

Instead of allowing S3 to spawn as many Lambdas as it needs for an influx of files to your bucket, you can send S3 events directly to an SQS queue and have those processed by Lambda. Consider this approach in situations where you expect high throughput, or you must control the rate of execution for the processing.

S3 File Processing
------------------

A basic application that will process file uploads to an S3 bucket. This app leverages the `Filter` option for S3 Events to only process uploaded JSON files and will ignore any other file type. Use filters to process different files using different dedicated Lambda functions.


MacAdmins 2018 Links
--------------------

These are links shown during my presentation "Dive into Lambda: An Intro to Serverless for Admins" from the Penn State MacAdmins 2018 conference. They server as excellent resources for anyone beginning to develop applications using serverless resources.

[AWS SAM (Serverless Application Model)]( https://github.com/awslabs/serverless-application-model/)

[CloudFormation Psuedo Parameters ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html)

[Lambda Event Examples]( https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html)

[X-Ray for Python ](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html)


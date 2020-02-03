2. Deploy the code to AWS Lambda
    * Note: Initial deploy should use (create).
        ~~~
        $ ask-amy-cli create_lambda --deploy-json-file cli_config.json
      ~~~
    * Note: Subsequent deploys should use (deploy).
        ~~~
        $ ask-amy-cli deploy_lambda --deploy-json-file cli_config.json
        ~~~
3. Check the logs with
    * Note: Subsequent deploys should use (deploy).
    ~~~
    $ ask-amy-cli logs --log-group-name /aws/lambda/device_address_skill
    ~~~

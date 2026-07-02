from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_nodejs20_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/hello"
    should_test_lint = False

class BuildInvoke_nodejs20_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/step-func"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/scratch"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/cw-event"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/s3"
    should_test_lint = False

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/sns"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/sqs"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_response_streaming(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/response-streaming"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/web"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_full_stack(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/full-stack"
    should_test_lint = False


class BuildInvoke_image_nodejs20_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    runtime = "nodejs20.x"
    directory = "nodejs/hello-img"
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_aws_sam_gql_quick_start(BuildInvokeBase.BuildInvokeBase):
    runtime = "nodejs20.x"
    directory = "nodejs/hello-gql"
    should_test_lint = False

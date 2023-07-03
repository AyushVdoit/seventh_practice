import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class SeventhPracticeStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "seventh_Pipeline",
                        pipeline_name="My_seventh_Pipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("AyushKjaiswal/seventh_practice", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )

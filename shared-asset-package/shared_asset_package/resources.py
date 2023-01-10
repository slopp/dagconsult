from dagster import resource

class MyResource():
    def __init__(self, configuration):
        self._configuration = configuration

    def hello(self):
        print(f"hello with {self._configuration}")

@resource(
    config_schema={
        "configuration": str
    }
)
def my_shared_configurable_resource(context):
    return MyResource(context.resource_config["configuration"])
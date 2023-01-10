from dagster import asset

@asset(
    required_resource_keys={"my_configurable_shared_resource"}
)
def my_shared_asset(context):
    context.resources.my_configurable_shared_resource.hello()
    return

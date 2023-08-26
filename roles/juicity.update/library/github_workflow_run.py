#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from github import Github


class Module:
    def __init__(self, repo_owner: str, repo_name: str) -> None:
        self.github = Github()
        self.repo = self.github.get_repo(f"{repo_owner}/{repo_name}")

    def get_latest_workflow_run_id(self, build_type: str) -> int:
        workflow = self.repo.get_workflow(f"{build_type}.yml")
        # Runs are returned in descending order.
        return workflow.get_runs()[0].id


def main():
    module_args = dict(
        owner=dict(type="str", required=True),
        repo=dict(type="str", required=True),
        build_type=dict(type="str", required=True),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    result = dict(changed=True, run_id=0)

    m = Module(module.params["owner"], module.params["repo"])
    latest_run_id = m.get_latest_workflow_run_id(module.params["build_type"])
    result["run_id"] = latest_run_id

    module.exit_json(**result)


if __name__ == "__main__":
    main()

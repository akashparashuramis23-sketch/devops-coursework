# Execution Evidence Log

**Environment:** Linux container, Python 3.13.5, Git 2.47.3, pytest available. Docker, Terraform, Ansible, kubectl, and Jenkins were not installed in this environment. These results are limited to the commands listed below; they do not prove the exercises match the lecturer's prescribed lab list.

| Exercise | Command(s) run | Actual result / output | Issue and fix (if any) | Verified? |
|---|---|---|---|---|
| 01 Git workflow | `git --version` | `git version 2.47.3` | Remote push not performed: no GitHub repository/account authorization was available in this environment. | Partially — Git installed; remote push not verified |
| 02 Bash automation | `bash -n 02-bash-automation/system_report.sh`; `bash 02-bash-automation/system_report.sh` | Syntax check exit code 0; script exit code 0. Printed date, host, user, uptime, and filesystem report. | None observed. | Yes — local script run passed |
| 03 Docker Python app | `python3 -m py_compile 03-docker-python-app/app.py` | Python syntax compilation exit code 0. | Docker is not installed, so image build/container run was not performed. | Partially — syntax only |
| 04 Docker Compose | `python3 -m py_compile 04-docker-compose/app.py`; parse `04-docker-compose/compose.yaml` with PyYAML | Python syntax compilation passed; YAML parsed successfully. | Docker/Compose is not installed, so services were not started. | Partially — syntax/config parse only |
| 05 GitHub Actions | Parse `.github/workflows/python-ci.yml` with PyYAML; `pytest -q 05-github-actions/tests` | YAML parsed successfully; `2 passed in 0.05s`. | Workflow was not run on GitHub Actions; local tests do not prove hosted workflow execution. | Partially — local tests and YAML parse passed |
| 06 Jenkins pipeline | Review `Jenkinsfile` | File is present. | Jenkins is not installed; pipeline syntax/build was not executed. | No — requires Jenkins validation |
| 07 Ansible | Parse `07-ansible/site.yml` with PyYAML | YAML parsed successfully. | `ansible-playbook` is not installed; playbook was not executed. | Partially — YAML parse only |
| 08 Terraform + Docker | Review `08-terraform-docker/main.tf` | File is present. | Terraform and Docker are not installed; `terraform init/validate/apply` was not run. | No — requires Terraform/Docker |
| 09 Kubernetes | Parse `deployment.yaml` and `service.yaml` with PyYAML | Both YAML files parsed successfully. | `kubectl` is not installed; manifest validation and cluster deployment were not performed. | Partially — YAML parse only |
| 10 Monitoring | Parse `compose.yaml` and `prometheus.yml` with PyYAML | Both YAML files parsed successfully. | Docker/Compose is not installed; Prometheus/Grafana services and scrape targets were not tested. | Partially — YAML parse only |

## Commands to complete verification on a suitable machine

- Docker exercises: `docker compose config`, then `docker compose up --build` and inspect service logs.
- GitHub Actions: push to GitHub and confirm the workflow run succeeds in the Actions tab.
- Jenkins: run the pipeline in a Jenkins instance with the required agent/tools.
- Ansible: run `ansible-playbook --syntax-check -i 07-ansible/inventory.ini 07-ansible/site.yml`, then execute only against an appropriate test host.
- Terraform: run `terraform init`, `terraform validate`, and review `terraform plan` before any apply.
- Kubernetes: run `kubectl apply --dry-run=client -f 09-kubernetes/` and deploy to a test cluster if available.
- Monitoring: start the Compose stack, then verify Prometheus targets and Grafana access.

Do not change a row to fully verified until the corresponding integration has actually been run. Add terminal output or screenshots if required by the instructor.

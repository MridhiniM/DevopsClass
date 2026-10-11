Exercise 7: Jenkins CI Automation

Objective

Understand Continuous Integration (CI), its benefits, and how Jenkins automates software development workflows.

1. What is Continuous Integration?

Continuous Integration is a software development practice in which developers frequently integrate code changes into a shared repository. Automated builds and tests help detect errors early and improve software quality.

Key Features

* Frequent code integration
* Automated builds
* Automated testing
* Immediate feedback

Benefits

* Early detection of bugs
* Improved team collaboration
* Faster development cycles
* Better code quality

2. How CI Works

1. A developer changes the application code.
2. The changes are pushed to a Git repository.
3. The CI server detects the changes or receives a build trigger.
4. Automated build and test steps run.
5. Jenkins reports whether the build succeeded or failed.

3. Introduction to Jenkins

Jenkins is an open-source automation server used to build, test, and deploy software.

Why Jenkins?

* Automates repetitive development tasks
* Supports Continuous Integration and Continuous Delivery
* Provides plugins for integration with development tools
* Supports distributed builds using agents

Key Concepts

* Job: A task configured in Jenkins.
* Build: One execution of a job.
* Pipeline: A sequence of automated steps.
* Plugins: Extensions that add functionality.
* Nodes/Agents: Machines that execute Jenkins jobs.

4. Jenkins Setup and Verification

Jenkins was run using Docker Desktop and accessed at:

http://localhost:8080

The Jenkins installation and initial configuration were completed during Exercise 6.

A pipeline named ZAPPTTO-Delivery-Monitoring was created and executed successfully.

The pipeline demonstrated:

* Checking the Jenkins execution environment
* Running shell commands
* Executing multiple pipeline stages
* Reporting build success or failure

5. Example CI Workflow

1. Commit code to Git.
2. Push the changes to GitHub.
3. Trigger a Jenkins build.
4. Run automated validation and tests.
5. Review the build result in Jenkins.

Conclusion

This exercise introduced Continuous Integration, its benefits, common CI tools, and Jenkins fundamentals. Jenkins was installed and accessed through Docker, and a pipeline was executed successfully.

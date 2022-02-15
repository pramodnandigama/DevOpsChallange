# DevOps Challenge

**Description:**
Our users are science teachers who are comfortable using the command line, a ReST API, or a browser. In their “Unit Conversion” science unit, they want to assign students unit-conversion problems on paper worksheets. After students turn in their completed worksheet, the teachers want to be able to enter the questions and student responses into a computer to be graded. Students will convert:

-   _temperatures_ between **Kelvin, Celsius**, **Fahrenheit**, and **Rankine**

## **Setup:**

 - Install Python 3.8
 - FastAPI
 - Pydantic
 - install pip
 - install git
 - docker

Aws Setup:
 - Create an aws account
 - copy account Id
 - and use replace accountId in .gitlab-ci.yml ( refer: <account_id>.dkr.ecr.ap-south-1.amazonaws.com )

## Server Side Setup

 - Create a gitlab account and 

```
	cd DevOpsChallenge
	git init --initial-branch=main
	git remote add origin https://gitlab.com/<UserName>/<repoName>.git
	git add .
	git commit -m "Initial commit"
	git push -u origin main

	git checkout -b feature
	git push -u origin feature
```
- Create lambda with name `dev-lambda`
- use container type not generic one
- provide ECR URI which you'll get from pipeline


## Running on local:

-	Run `python startup.py`
-	Use this to get doc: `http://127.0.0.1:8000/docs`
-	upload `sample.csv` using swagger
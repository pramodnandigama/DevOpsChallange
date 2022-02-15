FROM public.ecr.aws/lambda/python:3.8

ARG FUNCTION_DIR="/var/task"
RUN mkdir -p ${FUNCTION_DIR} && cd ${FUNCTION_DIR}


RUN rm -f ./.env

COPY . ${FUNCTION_DIR}

RUN  pip install --no-cache-dir -r requirements.txt

WORKDIR ${FUNCTION_DIR}

CMD ["startup.handler"]
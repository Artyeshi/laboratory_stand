FROM alpine
RUN apk add --update --no-cache curl wget bash python3 \
    py3-pip python3-dev g++ gcc libxslt-dev && \
    pip3 install requests beautifulsoup4 lxml
ADD *.py /scripts/
WORKDIR /scripts/
CMD tail -f /dev/null